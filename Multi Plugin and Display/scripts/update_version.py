###########################################################################
# UPDATE VERSION                                                          #
# Run this script increment the current build version number and update   #
# the current build time, author and git commit information               #
###########################################################################

try:
  Import("env") # type: ignore
  current_env = env["PIOENV"] # type: ignore
  project_path = env["PROJECT_DIR"] #type: ignore
  error = '\033[0;31m'
  warning = '\033[0;33m'
  report = '\033[0;32m'
  info = '\033[0;30m'
except:
  error = '[error] '
  warning = '[warning] '
  report = ''
  info = '[info] '

print(report + 'running \'update_version.py\'...')

import os
import datetime
import re
import linecache
import subprocess

FILEPATH_VERSION_H = 'include/version.h'

version_major = 1
version_minor = 0
version_fix = 0
version_build = 0
author = os.getlogin()
git_commit = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip('\r\n')
git_branch = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip('\r\n')
date_time = datetime.datetime.now()

try:
  
  with open(FILEPATH_VERSION_H) as f:
    version_major_string = re.split(" ", linecache.getline(r"include/version.h", 8))
    version_major = int(version_major_string[len(version_major_string) - 1])
    version_minor_string = re.split(" ", linecache.getline(r"include/version.h", 11))
    version_minor = int(version_minor_string[len(version_minor_string) - 1])
    version_fix_string = re.split(" ", linecache.getline(r"include/version.h", 14))
    version_fix = int(version_fix_string[len(version_fix_string) - 1])
    version_build_string = re.split(" ", linecache.getline(r"include/version.h", 17))
    version_build = int(version_build_string[len(version_build_string) - 1]) + 1

  print(info + 'Build number: {}.{}.{}.{}'.format(version_major, version_minor, version_fix, version_build))
  
  header_contents = '''/**
 * @file version.h
 * @brief Project Version. DO NOT EDIT THIS FILE DIRECTLY (Edited in "scripts/update_version.py")
 * 
 */

#ifndef SOFTWARE_VERSION_MAJOR
  #define SOFTWARE_VERSION_MAJOR {}
#endif
#ifndef SOFTWARE_VERSION_MINOR
  #define SOFTWARE_VERSION_MINOR {}
#endif
#ifndef SOFTWARE_VERSION_FIX
  #define SOFTWARE_VERSION_FIX {}
#endif
#ifndef SOFTWARE_VERSION_BUILD
  #define SOFTWARE_VERSION_BUILD {}
#endif
#ifndef SOFTWARE_BUILD_TIME
  #define SOFTWARE_BUILD_TIME "{}"
#endif
#ifndef SOFTWARE_AUTHOR
  #define SOFTWARE_AUTHOR "{}"
#endif
#ifndef SOFTWARE_GIT_COMMIT
  #define SOFTWARE_GIT_COMMIT "{}->{}"
#endif
'''.format(version_major, version_minor, version_fix, version_build, date_time, author, git_branch, git_commit)

  with open(FILEPATH_VERSION_H, 'w+') as f:
    f.write(header_contents)

  print(report + 'version updated')

except:
  print(error + '\'version.h\' could not be parsed -> check if \'version.h\' has not been manually modified (reset version using \'reset_version.py\')')