#!/usr/bin/python3

import re
import sys
import os
import json

import docutils as Utils

def load_api(sourcedir):
  api_txt = Utils.read_text(os.path.join(sourcedir, "tests/auto/api.json"))
  version = api_txt.split("\n")[0]
  api_json = api_txt[api_txt.find("\n"):]
  api = json.loads(api_json)
  return version, api

def generate_markdown(version, api):
  ret = "";

  ret += "### Enums\n"
  for enum in api["enums"].keys():
    ret += "#### %s\n" % enum
    for value in api["enums"][enum]:
      ret += "    %s\n" % value

  ret += "### Flags\n"
  for flag in api["flags"].keys():
    ret += "#### %s\n" % flag
    for value in api["flags"][flag]:
      ret += "    [%s]\n" % value

  ret += "### Methods\n"
  for method in api["methods"].keys():
    ret += "#### %s\n" % method
    ret += "%s\n\n" % api["methods"][method]["description"]
    ret += "Parameters\n\n"
    for param in api["methods"][method]["params"].keys():
      ret += "    %s\n" % param
    ret += "\n"


  return ret

config = Utils.read_json("jsonrpc-api-config.json")
Utils.clone_repo(config["srcdir"])
targets = Utils.find_targets(config["keyword"], config["outputdir"])
print("Files to replacee: %s" % targets)
version, api = load_api(os.path.join(config["srcdir"], "nymea"))
markdown = generate_markdown(version, api)
Utils.generate_output(targets, config["keyword"], markdown)
