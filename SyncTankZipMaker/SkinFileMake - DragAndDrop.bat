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
    echo.> %FileName%.wow %FileName%
    for /f "delims=1 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=2 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=3 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=4 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=5 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=6 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=7 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=8 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=9 usebackq" %%d in (%FileName%.wow) do (echo.> %FileName%.wow %%d)
    for /f "delims=0 usebackq" %%d in (%FileName%.wow) do (set wa=%%d)
    del %FileName%.wow
    if  %wa%==A (
        set country=american
        goto :Install
    )
    if  %wa%==GB (
        set country=british
        goto :Install
    )
    if  %wa%==Ch (
        set country=chinese
        goto :Install
    )
    if  %wa%==Cz (
        set country=czech
        goto :Install
    )
    if  %wa%==F (
        set country=french
        goto :Install
    )
    if  %wa%==G (
        set country=german
        goto :Install
    )
    if  %wa%==It (
        set country=italy
        goto :Install
    )
    if  %wa%==J (
        set country=japan
        goto :Install
    )
    if  %wa%==Pl (
        set country=poland
        goto :Install
    )
    if  %wa%==R (
        set country=russian
        goto :Install
    )
    if  %wa%==S (
        set country=sweden
        goto :Install
    )
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