Run Vim inside Terminator on Windows!
Direct editing of files by drag and drop!


Shell launch script for Windows

Requires WSL (Bash) to be installed in Windows

I've packed an exe for convenience

https://docs.microsoft.com/en-us/windows/wsl/install-win10

Requires Terminator & Vim to be installed in WSL 
Requires an X server (either Xming or Vcxsrv) to be installed on Windows
https://sourceforge.net/projects/xming/
https://sourceforge.net/projects/vcxsrv/
If the program is run wihout parameters, start a terminator shell
Else append the filename to edit in Vim (drag and drop works too!) 

If you have any keyboard mappings issues, look at /usr/share/X11/locale/en_US.UTF-8/Compose

![Alt text](https://raw.githubusercontent.com/eatsoup/ViToW/master/ViToW.png)
