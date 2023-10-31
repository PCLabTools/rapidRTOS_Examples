###########################################################################
# PREPARE RELEASE                                                         #
# Run this script to prepare the project for an official release.         #
# This script will place the prepared files into the 'release/' folder    #
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

print(report + 'running \'prepare_git.py\'...')

import subprocess

git_commit = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip('\r\n')
git_branch = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip('\r\n')

print(info + 'Git Info: {}->{}'.format(git_branch, git_commit))