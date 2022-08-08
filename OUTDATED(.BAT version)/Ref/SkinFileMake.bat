@echo on
chcp 65001
rd /s /q Input
rd /s /q Output
cls

set StartPosition=%cd%
mkdir Input
explorer Input
pause

mkdir Output
cd Input
dir /a:d /b > list.txt
for /f  %%a in (list.txt) do set OriginalFileName=%%a
for /f "delims=_ usebackq" %%e in (list.txt) do set FileName=%%e
echo %FileName%
del list.txt

:start
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
        set country=J
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
:Install
cls
echo %country% 
cd ..
mkdir Output\%FileName%
mkdir Output\%FileName%\vehicles\%country%\%OriginalFileName%
cd %cd%
xcopy Input\ Output\%FileName%\vehicles\%country%\ /e
cd Output
tar -cvzf %FileName%.zip %FileName%
rmdir /s /q %FileName%
move %FileName%.zip %StartPosition%
cd ..
rd /s /q Input
rd /s /q Output