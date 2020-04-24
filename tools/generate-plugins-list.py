#!/usr/bin/python3

import os
import json
from urllib.request import urlopen, Request
from git import Repo
import shutil

def read_config():
  with open('plugins-config.json') as configFile:
    data = json.load(configFile)
    return data["plugins"]

def parse_repo_url(repository):
  repo_name = repository.split("/")[4]
  return repo_name

def clone_repos(repos, target):
  for repo in repos:
    repo_name = parse_repo_url(repo)
    print("Cloning repo: %s" % repo_name)
    Repo.clone_from(repo, "%s/%s" % (target, repo_name), branch="rework-readmes")

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
    data = json.load(metaFile)
    return data

def list_subdirs(path):
  subdirs = [ f.name for f in os.scandir(path) if f.is_dir() ]
  return subdirs

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

def compose_meta(plugins, outputpath):
  meta = []
  for plugin in plugins:

    try:
      plugin_meta = extract_plugin_meta("%s/%s" % (plugin["path"], plugin["name"]))
    except:
      print("WARNING: Plugin %s has invalid meta.json" % plugin["name"])
      continue

    plugin_meta["readme"] = "%s.md" % plugin["name"]
    try:
      shutil.copyfile("%s/%s/README.md" % (plugin["path"], plugin["name"]), "%s/%s.md" % (outputpath, plugin["name"]))
    except:
      print("WARNING: Plugin %s has invalid README.md" % plugin["name"])
      continue

    icon = plugin_meta["icon"]
    try:
      shutil.copyfile("%s/%s/%s" % (plugin["path"], plugin["name"], icon), "%s/%s-%s" % (outputpath, plugin["name"], icon))
    except:
      print("WARNING: Plugin %s has invalid icon: %s" % (plugin["name"], plugin_meta["icon"]))
      continue
    plugin_meta["icon"] = "%s-%s" % (plugin["name"], icon)

    meta.append(plugin_meta)

  outputtext = "export const meta = "
  outputtext += json.dumps(meta, indent=4)
  with open("%s/_meta.js" % outputpath, "w") as outfile:
    outfile.write(outputtext)

builddir = "build/"
outputpath = "../src/routes/overview/documentation/integrations/"
shutil.rmtree(builddir, ignore_errors=True)
repos = read_config()
clone_repos(repos, builddir)
plugins = find_plugins(builddir)
compose_meta(plugins, outputpath)
