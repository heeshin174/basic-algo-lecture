@echo off
rem VS 2022 MSVC 환경 설정 스크립트 호출 (x64 Native Tools)
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\VsDevCmd.bat" -arch=amd64

rem Windsurf 실행
start "" "%LOCALAPPDATA%\Programs\Windsurf\Windsurf.exe"