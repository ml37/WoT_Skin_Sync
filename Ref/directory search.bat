chcp 65001
@echo on
setlocal EnableDelayedExpansion

for /d %%a in (*) do (
    dir /a:d /b /s > list.txt
)
pause