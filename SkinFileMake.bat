@echo on
chcp 65001
rd /s /q Input
rd /s /q Output
cls
set StartPosition=%cd%
mkdir Input
pause
mkdir Output
cd Input
dir /a:d /b > list.txt
for /f  %%a in (list.txt) do set OriginalFileName=%%a
for /f "delims=_ usebackq" %%e in (list.txt) do set FileName=%%e
del list.txt
cls
echo %FileName%
echo %StartPosition%
cd ..
mkdir Output\%FileName%
mkdir Output\%FileName%\vehicles\italy\%OriginalFileName%
cd %cd%
xcopy Input\ Output\%FileName%\vehicles\italy\ /e
cd Output
tar -cvzf %FileName%.zip %FileName%
rmdir /s /q %FileName%
move %FileName%.zip %StartPosition%
cd ..
rd /s /q Input
rd /s /q Output
pause