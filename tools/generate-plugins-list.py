#!/usr/bin/python3

import sys
import os
import json
from urllib.request import urlopen, Request
import git
import shutil
import re

def read_config():
  with open('plugins-config.json') as configFile:
    data = json.load(configFile)
    return data

def parse_repo_url(repository):
  repo_name = repository.split("/")[4]
  return repo_name

def clone_repos(repos, target, branch="master"):
  for repo in repos:
    repo_name = parse_repo_url(repo)
    try:
      g = git.Repo("%s/%s" % (target, repo_name))
      g.remotes.origin.pull()
      print("Pulled repo: %s" % repo_name)
    except:
      print("Cloning repo: %s" % repo_name)
      g = git.Repo.clone_from(repo, "%s/%s" % (target, repo_name))
    print("checking out branch %s" % branch)
    g.git.checkout(branch)

def has_plugin_meta(path):
  found_meta = False
  found_readme = False
  for f in os.listdir(path):
    if f == "meta.json":
      found_meta = True
    if f == "README.md":
      found_readme = True
    if found_meta and found_readme:
      return True
  return False

def extract_plugin_meta(path):
  with open('%s/meta.json' % path) as metaFile:
    try:
        data = json.load(metaFile)
    except Exception as e:
        print("Error parsing meta.json: %s" % e)
        raise e
    return data

def extract_plugin_info(path, name):
  jsonFile = list_files(os.path.join(path, name),  "integrationplugin[a-z0-9\-]*\.json")[0]
  with open(os.path.join(path, name, jsonFile)) as pluginInfo:
    data = json.load(pluginInfo)
    return data

def list_subdirs(path):
  subdirs = [ f.name for f in os.scandir(path) if f.is_dir() ]
  return subdirs

def list_files(path, filter):
  files = [ f.name for f in os.scandir(path) if f.is_file() and re.match(filter, f.name) ]
  return files

def find_plugins(path):
  all_plugins = []
  for dir in list_subdirs(path):
    if has_plugin_meta("%s/%s" % (path, dir)):
      print("Found plugin at %s/%s" % (path, dir))
      plugin = {}
      plugin["name"] = dir
      plugin["path"] = path
      all_plugins.append(plugin)
    else:
      for subdir in list_subdirs("%s/%s" % (path, dir)):
        if has_plugin_meta("%s/%s/%s" % (path, dir, subdir)):
          print("Found plugin at %s/%s/%s" % (path, dir, subdir))
          plugin = {}
          plugin["name"] = subdir
          plugin["path"] = "%s/%s" % (path, dir)
          all_plugins.append(plugin)
  return all_plugins

def compose_meta(plugins, outputpath, iconoutputpath, categories, technologies):
  meta = []

  if not os.path.exists(iconoutputpath):
    os.mkdir(iconoutputpath)

  for plugin in plugins:

    try:
      plugin_meta = extract_plugin_meta("%s/%s" % (plugin["path"], plugin["name"]))
    except:
      print("ERROR: Plugin %s has invalid meta.json" % plugin["name"])
      continue

    try:
      plugin_info = extract_plugin_info(plugin["path"], plugin["name"])
    except:
      print("ERROR: Plugin %s has invalid plugininfo json" % plugin["name"])
      continue

    ok = True
    for category in plugin_meta["categories"]:
      if category not in categories:
        ok = False
    if not ok:
      print("ERROR: Plugin %s has invalid categories: %s. Allowed: %s" % (plugin["name"], plugin_meta["categories"], categories))
      continue

    if len(plugin_meta["categories"]) == 0:
      print("WARNING: Plugin %s is not in any category!" % plugin["name"])

    if "technologies" in plugin_meta:
      for technology in plugin_meta["technologies"]:
        if technology not in technologies:
          ok = False
      if not ok:
        print("ERROR: Plugin %s has invalid technologies: %s. Allowed: %s" % (plugin["name"], plugin_meta["technologies"], technologies))
        continue

    vendors = {}
    for vendor in plugin_info["vendors"]:
      thingClasses = []
      for thingClass in vendor["thingClasses"]:
        thingClasses.append(thingClass["displayName"])
      vendors[vendor["displayName"]] = thingClasses
    plugin_meta["things"] = vendors

    try:
      shutil.copyfile("%s/%s/README.md" % (plugin["path"], plugin["name"]), "%s/%s.md" % (outputpath, plugin["name"]))
      plugin_meta["readme"] = "%s.md" % plugin["name"]
    except:
      print("ERROR: Plugin %s has invalid README.md" % plugin["name"])
      continue

    icon = plugin_meta["icon"]
    try:
      shutil.copyfile("%s/%s/%s" % (plugin["path"], plugin["name"], icon), "%s/%s-%s" % (iconoutputpath, plugin["name"], icon))
      plugin_meta["icon"] = "%s-%s" % (plugin["name"], icon)
    except:
      print("WARNING: Plugin %s has invalid icon: %s" % (plugin["name"], plugin_meta["icon"]))
      #continue

    meta.append(plugin_meta)

  outputtext = "export const meta = "
  outputtext += json.dumps(meta, indent=2)
  with open("%s/_meta.js" % outputpath, "w") as outfile:
    outfile.write(outputtext)


### Main
branch = "master"

if len(sys.argv) > 1:
  branch = sys.argv[1]

config = read_config()
clone_repos(config["plugins"], config["srcdir"], branch)
plugins = find_plugins(config["srcdir"])
compose_meta(plugins, config["outputdir"], config["iconoutputdir"], config["allowed_categories"], config["allowed_technologies"])
