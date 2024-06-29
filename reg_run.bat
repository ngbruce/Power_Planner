chcp 65001
@echo off
set "WINPYDIR=%~dp0\..\chatRecorder_Env"
set "PATH=%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%PATH%;"
set "PYTHON=%WINPYDIR%\python.exe "
PYTHON regedit.py
echo ======================
echo -程序结束，按任意键-
pause
exit