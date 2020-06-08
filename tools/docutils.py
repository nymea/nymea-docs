import git
import json
import os
import re

def clone_repo(target, branch="master"):
  repo = "https://github.com/nymea/nymea"
  repo_name = "nymea"
  try:
    g = git.Repo("%s/%s" % (target, repo_name))
    g.remotes.origin.pull()
    print("Pulled repo: %s" % repo_name)
  except:
    print("Cloning repo: %s" % repo_name)
    g = git.Repo.clone_from(repo, "%s/%s" % (target, repo_name))
  g.git.checkout(branch)


def read_json(file):
  with open(file) as jsonFile:
    data = json.load(jsonFile)
    return data

def read_text(file):
  with open(file) as input:
    data = input.read()
    return data

def write_text(file, content):
  with open(file, "w") as output:
    print("writing to: %s" % file)
    output.write(content)

def list_files(path, filter):
  files = [ f.name for f in os.scandir(path) if f.is_file() and f.name.endswith(filter) ]
  return files

def list_subdirs(path):
  subdirs = [ f.name for f in os.scandir(path) if f.is_dir() ]
  return subdirs

def find_targets(keyword, dir):
  fileNames = list_files(dir, ".in")
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

def build_codeblock(text, language=""):
  ret = "```%s\n" % language
  for line in text.split("\n"):
    ret += "%s\n" % line
  ret += "```"
  return ret


# replacements is a map of <keyword, content> pairs
def generate_output_file(targets, replacements):
  for target in targets:
    print("working on %s" % target)
    fileName = os.path.basename(target)
    fileName = re.sub(r"^_", "", fileName)
    fileName = re.sub(".in$", "", fileName)
    content = read_text(target)
    for keyword in replacements.keys():
#      print("replacing %s with %s" % (keyword, replacements[keyword]))
      content = re.sub(keyword, replacements[keyword], content)
    write_text(os.path.join(os.path.dirname(target), fileName), content)
