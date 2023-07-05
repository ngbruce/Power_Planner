@echo off
set "WINPYDIR=%~dp0\..\chatRecorder_Env"
set "PATH=%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%PATH%;"
set "PYTHON=%WINPYDIR%\python.exe "
PYTHON main.py
chcp 65001
echo ======================
echo -程序结束，按任意键进入git工具-
pause
call set_git.bat
exit