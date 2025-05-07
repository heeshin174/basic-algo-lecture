@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\VsDevCmd.bat" -arch=amd64 -no_logo
start "" "%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"