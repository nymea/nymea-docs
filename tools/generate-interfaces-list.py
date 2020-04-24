#!/usr/bin/python3

import re
import sys
import os
import json
import git

def read_json(file):
  with open(file) as configFile:
    data = json.load(configFile)
    return data

def read_text(file):
  with open(file) as input:
    data = input.read()
    return data

def write_text(file, content):
  with open(file, "w") as output:
    print("writing to: %s" % file)
    output.write(content)

def clone_repo(target):
  repo = "https://github.com/nymea/nymea"
  repo_name = "nymea"
  try:
    g = git.Repo("%s/%s" % (target, repo_name))
    g.remotes.origin.pull()
    print("Pulled repo: %s" % repo_name)
  except:
    print("Cloning repo: %s" % repo_name)
    g = git.Repo.clone_from(repo, "%s/%s" % (target, repo_name))
  g.git.checkout('master')

def list_subdirs(path):
  subdirs = [ f.name for f in os.scandir(path) if f.is_dir() ]
  return subdirs

def list_files(path, filter):
  files = [ f.name for f in os.scandir(path) if f.is_file() and f.name.endswith(filter) ]
  return files

def find_targets(keyword, dir):
  fileNames = list_files(dir, ".md.in")
  targets = []
  for fileName in fileNames:
    file = open(os.path.join(dir, fileName), "r")
    for line in file:
      if re.search(keyword, line):
        targets.append(os.path.join(dir, fileName))
        break;
  subdirs = list_subdirs(dir)
  for subdir in subdirs:
    subtargets = find_targets(keyword, os.path.join(dir, subdir))
    for subtarget in subtargets:
      targets.append(subtarget)
  return targets

def load_interfaces(sourcedir):
  interfaces = {}
  files = list_files(sourcedir, ".json")
  for file in files:
    ifaceName = file.split(".")[0]
    interface = read_json(os.path.join(sourcedir, file))
    interfaces[ifaceName] = interface
  return interfaces

def build_codeblock(text):
  ret = ""
  for line in text.split("\n"):
    ret += "    %s\n" % line
  return ret

def build_links(interface):
  ret = ""
  if "extends" in interface:
    extends = interface["extends"]
    if type(extends) is not list:
      extends = [extends]
    for extend in extends:
      if ret != "":
        ret += ", "
      ret += "[%s](#%s)" % (extend, extend)
  return ret

def build_markdown(interfaces):
  ret = ""
  for ifaceName in sorted(interfaces):
    interface = interfaces[ifaceName]
    ret += "## %s\n\n" % ifaceName
    if "description" in interface:
      ret += "%s\n\n" % interface["description"]
      del interface["description"]
    ret += build_codeblock(json.dumps(interface, indent=4))
    ret += "\n\n"
    links = build_links(interface)
    if links != "":
      ret += "See also: %s\n\n" % links
  return ret

def generate_output(targets, keyword, mardown):
  for target in targets:
    fileName = os.path.basename(target)
    fileName = re.sub(r"^_", "", fileName)
    fileName = re.sub(".in$", "", fileName)
    input = read_text(target)
    output = re.sub(keyword, markdown, input)
    write_text(os.path.join(os.path.dirname(target), fileName), output)

### Main

config = read_json("interfaces-config.json")
clone_repo(config["srcdir"])
targets = find_targets(config["keyword"], config["outputdir"])
print("Files to replace: %s" % targets)
interfaces = load_interfaces(os.path.join(config["srcdir"], "nymea/libnymea/interfaces"))
markdown = build_markdown(interfaces)
generate_output(targets, config["keyword"], markdown)
