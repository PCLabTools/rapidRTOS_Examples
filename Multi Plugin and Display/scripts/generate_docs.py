###########################################################################
# GENERATE DOCS                                                           #
# Run this script to generate the Doxygen output files containing         #
# the documentation for this project.                                     #
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

print(report + 'running \'generate_docs.py\'...')

import subprocess

doxyfile = 'docs/doxyfile'
toolpath = 'doxygen'

if subprocess.run([toolpath, doxyfile]).returncode == 0:
  print(report + 'document generation complete')
else:
  print(error + 'document generation failed')