@echo on
chcp 65001
FOR /R %%a in (It???.zip) do (echo %%~na)
echo Fin
pause