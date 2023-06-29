@echo off
set "WINPYDIR=%~dp0\..\chatRecorder_Env"
set "PATH=%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%PATH%;"
set "PYTHON=%WINPYDIR%\python.exe "
PYTHON main.py
echo ======================
pause
call set_git.bat
exit