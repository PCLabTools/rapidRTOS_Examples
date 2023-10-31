###########################################################################
# UPLOAD                                                                  #
# Do not run this script in isolation.                                    #
# This script is ran after the project build process to allow actions     #
# before uploading to the target                                          #
###########################################################################

try:
  Import("env") # type: ignore
  current_env = env["PIOENV"] # type: ignore
  project_path = env["PROJECT_DIR"] #type: ignore
  error = '\033[0;31m'
  warning = '\033[0;33m'
  report = '\033[0;32m'
  info = '\033[0;30m'

  def before_upload(source, target, env):
    print(report + 'running \'pre_upload.py\'...')


    print(report + 'pre-upload script complete')

  env.AddPreAction("upload", before_upload) # type: ignore

except:
  error = '[error] '
  warning = '[warning] '
  report = ''
  info = '[info] '
  print(error + 'cannot run a \'upload script\' in isolation!')