@echo off
:start_program
cls
chcp 936
python main.py
chcp 65001
echo ======================
echo -程序结束，按任意键进入git工具-
pause
call set_git.bat
cls
echo ======================
echo -按任意键重新执行程序-
pause
goto start_program
exit