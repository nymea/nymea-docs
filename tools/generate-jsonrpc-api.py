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

def extract_refs(entry):
  ret = []
  if isinstance(entry, str):
    if entry.startswith("$ref:"):
      ret.append(re.sub(r'\$ref:', '', entry))
  elif isinstance(entry, list):
    for child in entry:
      ret.extend(extract_refs(child))
  elif isinstance(entry, dict):
    for key in entry.keys():
      value = entry[key]
      ret.extend(extract_refs(value))
  return ret

def generate_markdown(version, api):
  ret = "";

  ret += "## Nymea client API\n\n"
  ret += "The current version of the API is %s.\n\n" % version
  ret += "### Enums\n"
  for enum in api["enums"].keys():
    ret += "#### %s\n\n" % enum
    ret += Utils.build_codeblock(json.dumps(api["enums"][enum], indent=2), "json")
    ret += "\n"

  ret += "### Flags\n"
  for flag in api["flags"].keys():
    ret += "#### %s\n\n" % flag
    ret += Utils.build_codeblock(json.dumps(api["flags"][flag], indent=2), "json")
    ret += "\n"

  ret += "### Methods\n"
  for method in api["methods"].keys():
    ret += "#### %s\n\n" % method
    method_dict = api["methods"][method]
    description = method_dict["description"]
    description = re.sub(r'\)', '\\)', description)
    description = re.sub(r'\n', '\n\n', description)
    ret += description
    ret += "\n\n"
    if "deprecated" in method_dict:
      deprecation_warning = method_dict["deprecated"]
      ret += "> Note: This method is deprecated. %s\n\n" % deprecation_warning
    method_dict.pop("description", None)
    method_dict.pop("deprecated", None)
    ret += Utils.build_codeblock(json.dumps(method_dict, indent=2), "json")
    refs = extract_refs(method_dict)
    if len(refs) > 0:
      ret += "\n\nSee also: "
      reflist = []
      for ref in refs:
        reflist.append("[%s](#%s)" % (ref, ref))
      ret += ", ".join(reflist)
    ret += "\n\n"
  for notification in api["notifications"].keys():
    ret += "#### %s\n\n" % notification
    method_dict = api["notifications"][notification]
    description = method_dict["description"]
    description = re.sub(r'\)', '\\)', description)
    description = re.sub(r'\n', '\n\n', description)
    ret += description
    ret += "\n\n"
    if "deprecated" in method_dict:
      deprecation_warning = method_dict["deprecated"]
      ret += "> Note: This notification is deprecated. %s\n\n" % deprecation_warning
    method_dict.pop("description", None)
    method_dict.pop("deprecated", None)
    ret += Utils.build_codeblock(json.dumps(method_dict, indent=2), "json")
    refs = extract_refs(method_dict)
    # if len(refs) > 0:
    #   ret += "\n\nSee also: "
    #   reflist = []
    #   for ref in refs:
    #     reflist.append("[%s](#%s)" % (ref, ref))
    #   ret += ", ".join(reflist)
    ret += "\n\n"

  return ret


def generate_markdown_list(list):
  ret = "\n"
  for entry in list:
    ret += "* %s\n" % entry
  ret += "\n"
  return ret

config = Utils.read_json("jsonrpc-api-config.json")
Utils.clone_repo(config["srcdir"])
targets = Utils.find_targets(config["keyword"], config["outputdir"])
targets.extend(Utils.find_targets(config["inputtypes_keyword"], config["outputdir"]))
targets.extend(Utils.find_targets(config["units_keyword"], config["outputdir"]))
print("Files to modify: %s" % targets)
version, api = load_api(os.path.join(config["srcdir"], "nymea"))
markdown_api = generate_markdown(version, api)

inputtypes = api["enums"]["InputType"]
markdown_inputtypes = generate_markdown_list(inputtypes)

units = api["enums"]["Unit"]
markdown_units = generate_markdown_list(units)


replacements = {}
replacements[config["keyword"]] = markdown_api
replacements[config["inputtypes_keyword"]] = markdown_inputtypes
replacements[config["units_keyword"]] = markdown_units

Utils.generate_output_md(targets, replacements)
