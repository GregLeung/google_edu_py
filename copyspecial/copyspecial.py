#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# /Users/FrankLeung/Documents/Project/google_edu_py/copyspecial

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  filenames = os.listdir(dir)
  result = []
  for filename in filenames:
    match = re.search(r'.+__\w+__.+', filename)
    if match:
      result.append(filename)
  return result

def copy_to(paths, dir):
  if not os.path.exists(paths):
    os.mkdir(paths)
  for filename in get_special_paths(dir):
    shutil.copy(os.path.join(os.path.abspath(dir), filename), paths)

def zip_to(dir, zippath):
  cmd = 'zip -j ' + zippath + ' '
  for filename in get_special_paths(dir):
    cmd += os.path.join(os.path.abspath(dir), filename) + ' '
  try:
    output = commands.getoutput(cmd)
    print(output)
  except:
    sys.stderr('cannot find path: ' + zippath)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    fromdir = args[2]
    del args[0:2]
    copy_to(todir, fromdir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    fromdir = args[2]
    del args[0:2]
    zip_to(fromdir, tozip)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  if not todir and not tozip:
    for filename in get_special_paths(args[0]):
      print(filename)

if __name__ == "__main__":
  main()
