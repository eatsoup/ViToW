# Shell launch script for Windows
# Requires WSL (Bash) to be installed in Windows
# https://docs.microsoft.com/en-us/windows/wsl/install-win10

# Requires Terminator & Vim to be installed in WSL 
# Requires an X server (either Xming or Vcxsrv) to be installed on Windows
# https://sourceforge.net/projects/xming/
# https://sourceforge.net/projects/vcxsrv/
# If the program is run wihout parameters, start a terminator shell
# Else append the filename to edit in Vim (drag and drop works too!) 

# If you have any keyboard mappings issues, look at /usr/share/X11/locale/en_US.UTF-8/Compose


import sys, psutil, os
import subprocess
import platform
import time
xming = 'Xming.exe'
vcxsrv = 'vcxsrv.exe'
xmingpath86 = 'c:\\Program Files (x86)\\Xming\\Xming.exe'
xmingpath64 = 'c:\\Program Files\\Xming\\Xming.exe'
vcxsrvpath86 = 'c:\\Program Files (x86)\\VcXsrv\\vcxsrv.exe'
vcxsrvpath64 = 'c:\\Program Files\\VcXsrv\\vcxsrv.exe'
vcxsrvrunarg = '  :0 -ac -terminate -lesspointer -multiwindow -clipboard -wgl'
xmingrunarg = '   :0 -clipboard -multiwindow'
xrunning = False
CREATE_NO_WINDOW = 0x08000000

# Bug with system32 directory
is32bit = (platform.architecture()[0] == '32bit')
system32 = os.path.join(os.environ['SystemRoot'], 
  'SysNative' if is32bit else 'System32')
bash = os.path.join(system32, 'bash.exe')

# Check for argv[1] else start terminator
if len(sys.argv)<2:
  command = bash + " ~ -c 'DISPLAY=:0 GTK_IM_MODULE=xim nohup terminator -m'"
else:
  convarg = ''.join(sys.argv[1:])
  convarg = convarg.replace('c:\\', '/mnt/c/')
  convarg = convarg.replace('C:\\', '/mnt/c/')
  convarg = convarg.replace('\\', '/')
  convarg = convarg.replace(' ', '\\ ')
  print ('Opening: ' + sys.argv[1] + '(' + convarg + ')' + ' in Vim')
  command = bash + " ~ -c 'DISPLAY=:0 GTK_IM_MODULE=xim nohup terminator -m -x vi " + convarg + "'"
  print(command)

# Check for running X server
def checkxserver():
  for proc in psutil.process_iter():
    if proc.name() == xming:
      return 'xming'
    elif proc.name() == vcxsrv:
      return 'vcxsrv'

# If the server is not running, try to locate and run
def detectxexe():
  if os.path.isfile(xmingpath86):
    subprocess.Popen(xmingpath86 + xmingrunarg, creationflags = CREATE_NO_WINDOW)
    return True
  elif os.path.isfile(xmingpath64):
    subprocess.Popen(xmingpath64 + xmingrunarg, creationflags = CREATE_NO_WINDOW)
    return True
  elif os.path.isfile(vcxsrvpath86):
    subprocess.Popen(vcxsrvpath86 + vcxsrvrunarg, creationflags = CREATE_NO_WINDOW)
    return True
  elif os.path.isfile(vcxsrvpath64):
    subprocess.Popen(vcxsrvpath64 + vcxsrvrunarg, creationflags = CREATE_NO_WINDOW)
    return True
  else:
    return False

# Main 
if checkxserver() == 'xming':
  print('Xming found, launching')
  subprocess.Popen(command, creationflags = CREATE_NO_WINDOW)
elif checkxserver() == 'vcxsrv':
  print('vcxsrv found, launching')  
  subprocess.Popen(command, creationflags = CREATE_NO_WINDOW)
else:
  print('No compatible X server running, trying to detect one')
  if detectxexe() == True:
    subprocess.Popen(command, creationflags = CREATE_NO_WINDOW)
  else:
    print('Cannot detect X server, is Xming or Vcxsrv installed?')
    time.sleep(10)
