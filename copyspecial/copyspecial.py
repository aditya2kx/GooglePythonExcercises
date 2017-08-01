#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

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
  result = []
  filenames = os.listdir(dir)
  for filename in filenames:
    match = re.search(r'__\w+__', filename)
    if match:
      result.append(os.path.abspath(os.path.join(dir, filename)))
  return result

def copy_to(paths, dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
  for path in paths:
    shutil.copy(path, dir)

def zip_to(paths, zippath):
  pathsString = ' '.join(paths)
  cmd = 'zip -j %s %s' % (zippath, pathsString)
  print "About to execute command %s" % cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    print 'Failed to execute command because %s' % (output)
    sys.exit(status)

  print "Zipped all the files in %s" % zippath

def main():
  # The basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    fromdir = args[2]
    paths = get_special_paths(fromdir)
    copy_to(paths, todir)
    del args[0:2]
    return

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    fromdir = args[2]
    paths = get_special_paths(fromdir)
    zip_to(paths, tozip)
    del args[0:2]
    return

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  for dirName in args:
    filenames = get_special_paths(dirName)
    for filename in filenames:
      print filename


  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
