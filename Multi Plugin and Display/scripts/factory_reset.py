###########################################################################
# FACTORY RESET                                                           #
# Run this script to factory reset an RP2040 board. Make sure the RP2040  #
# is in UF2 upload mode, to do this hold BOOTSEL button when plugging     #
# in the board to USB.                                                    #
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

print(report + 'running \'factory_reset.py\'...')

import os
import subprocess

user = os.getlogin()
firmwarepath = 'scripts/bin/RP2040_FactoryReset.elf'
toolfolder = os.path.expanduser('~') + '/.arduino15/packages/rp2040/tools/pqt-picotool/'
toolversion = os.listdir(toolfolder)
toolpath = toolfolder + toolversion[0] + '/picotool'

if subprocess.run([toolpath, 'load', firmwarepath, '-F']).returncode == 0:
  print(report + 'firmware flash complete')
else:
  print(error + 'firmware flash failed')