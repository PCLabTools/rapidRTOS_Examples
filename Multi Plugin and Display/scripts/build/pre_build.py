###########################################################################
# PRE BUILD                                                               #
# Do not run this script in isolation.                                    #
# This script is ran during the project build process to prepare and      #
# update files necessary for compilation                                  #
###########################################################################

try:
  Import("env") # type: ignore
  current_env = env["PIOENV"] # type: ignore
  project_path = env["PROJECT_DIR"] #type: ignore
  error = '\033[0;31m'
  warning = '\033[0;33m'
  report = '\033[0;32m'
  info = '\033[0;30m'

  print(report + 'running \'pre_build.py\'...')

  exec(open('scripts/generate_docs.py').read())
  exec(open('scripts/update_version.py').read())

  print(report + 'pre-build script complete')

except:
  error = '[error] '
  warning = '[warning] '
  report = ''
  info = '[info] '
  print(error + 'cannot run a \'build script\' in isolation!')
