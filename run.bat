@echo off
:start
set /a var+=1
if %var% EQU 100 goto end
py app.py %var% %var% '+' >> result.txt
goto start
:end
pause
exit