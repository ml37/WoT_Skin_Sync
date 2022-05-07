@echo off

chcp 65001
set StartPosition=%cd%
set dragfiledirectory=%~1%
set dragfilename=%~n1%

cd /d c:
mkdir SyncTank
set InfLocation=%cd%
cd /d %StartPosition%

::C:\에 폴더 만들어서 inf 저장하기
mkdir %InfLocation%SyncTank\Zipmaker
cd /d %InfLocation%SyncTank\Zipmaker
if not exist ServerLocation.inf (
    echo.>ServerLocation.inf W:\WoTskin
    notepad ServerLocation.inf
)
for /f "usebackq" %%a in (ServerLocation.inf) do set ServerLocation=%%a

::
cd /d %StartPosition%
echo.> walalaru.txt %~n1%
notepad walalaru.txt
del walalaru.txt
notepad %ServerLocation%\Skinlist.inf
mkdir DInput
cd DInput
xcopy %~1%
echo.>wa.txt %dragfilename%
for /f "tokens=1 delims=_ usebackq" %%a in (wa.txt) do set FileName=%%a
del wa.txt
cd ..

:Install
mkdir %FileName%\vehicles\%country%\%dragfilename%
mkdir %FileName%\vehicles\%country%\%dragfilename%\PSD
xcopy DInput\*.dds %FileName%\vehicles\%country%\%dragfilename% /e
xcopy DInput\*.psd %FileName%\vehicles\%country%\%dragfilename%\PSD /e
cd DOutput
tar -cvzf %FileName%.zip %FileName%
rmdir /s /q %FileName%
move %FileName%.zip %StartPosition%
cd %StartPosition%
rd /s /q DInput
rd /s /q DOutput
copy %FileName%.zip %ServerLocation%\Skin
explorer %ServerLocation%\Skin
pause