#!/usr/bin/python3

import re
import sys
import os
import json
import git

import docutils as Utils

def load_interfaces(sourcedir):
  interfaces = {}
  files = Utils.list_files(sourcedir, ".json")
  for file in files:
    ifaceName = file.split(".")[0]
    interface = Utils.read_json(os.path.join(sourcedir, file))
    interfaces[ifaceName] = interface
  return interfaces

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
    ret += Utils.build_codeblock(json.dumps(interface, indent=2), "json")
    ret += "\n\n"
    links = build_links(interface)
    if links != "":
      ret += "See also: %s\n\n" % links
  return ret

### Main

config = Utils.read_json("interfaces-config.json")
Utils.clone_repo(config["srcdir"])
targets = Utils.find_targets(config["keyword"], config["outputdir"])
print("Files to replace: %s" % targets)
interfaces = load_interfaces(os.path.join(config["srcdir"], "nymea/libnymea/interfaces"))
markdown = build_markdown(interfaces)
replacements = {}
replacements[config["keyword"]] = markdown
Utils.generate_output_md(targets, replacements)
