@echo off
chcp 65001
title SyncTank
setlocal enabledelayedexpansion
set offlinestatus= 
set ListNumber = 1
set ServerAddress=mashiro37.i234.me

:start
color 70
if not exist ClientLocation.inf (
    echo.> ClientLocation.inf "Text Your Client Location here (ex : D:\Games\World_of_Tanks_ASIA)"
)
for /f "delims=" %%a in (ClientLocation.inf) do set ClientLocation=%%a
if %ClientLocation%=="Text Your Client Location here (ex : D:\Games\World_of_Tanks_ASIA)" (
    cls
    title "Error 1 : ClientLocation.inf has Include Error message"
    color 40
    echo ----------------------------------
    echo .
    echo .
    echo "Error 1 : ClientLocation.inf has Include Error message"
    echo "Client Location Not Found! Please Write Your Client location on ClientLocation.inf!"
    echo .
    echo .
    echo ----------------------------------
    notepad ClientLocation.inf
    goto start
    
)
for /f "delims=\ usebackq" %%e in (ClientLocation.inf) do set DriveName=%%e

    curl -OL# http://%ServerAddress%/WoTskin/Skinlist.inf
    curl -OL# http://%ServerAddress%/WoTskin/Version.inf

if not exist Skinlist.inf (
    color 40
    cls
    title "error 2 : Skinlist.inf Not Exist"
    echo ----------------------------------
    echo .
    echo .
    echo "error 2 : Skinlist.inf Not Exist"
    echo Can`t Download Skin list!
    echo .
    echo .
    echo ----------------------------------
    echo.> Skinlist.inf "Can`t Download Skin list!"
    goto start
)
if not exist Version.inf (
    color 40
    cls
    title "error 3 : Version.inf Not Exist"
    echo ----------------------------------
    echo .
    echo .
    echo "error 3 : Version.inf Not Exist"
    echo Can`t Download Client Version! Check Internet Connection!
    echo .
    echo .
    echo ----------------------------------

    set /p "cvml=Type Client res_mods Version (ex : 1.16.1.0): "
    echo Input : !cvml!
    echo.> Version.inf !cvml!
    goto start
)

for /f "delims=" %%b in (Version.inf) do set ClientVersion=%%b
set StartInstall=%cd%


:Install
cd %StartInstall%
cls
title "SyncTank | Client on %ClientLocation% | WoT Client %ClientVersion% %offlinestatus%"
echo ----------------select------------------
echo .
echo .
setlocal enabledelayedexpansion

for /f "tokens=*" %%c in (Skinlist.inf) do (
    set /a ListNumber = !ListNumber! + 1
    echo No.!ListNumber! - %%c
)
set ListNumber = 1
echo .
echo .
echo ----------------------------------------
echo .
echo .
setlocal
echo Example : It17
set /p "Ask= Type Vehicle Number Code, If you want to load backup, Type [walalaru] : "
echo.>wa.wa %Ask%
for /f "delims=_ usebackq" %%k in (wa.wa) do set FileName=%%k
del wa.wa
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
        goto :Downloadandinstall
    )
    if  %wa%==GB (
        set country=british
        goto :Downloadandinstall
    )
    if  %wa%==Ch (
        set country=chinese
        goto :Downloadandinstall
    )
    if  %wa%==Cz (
        set country=czech
        goto :Downloadandinstall
    )
    if  %wa%==F (
        set country=french
        goto :Downloadandinstall
    )
    if  %wa%==G (
        set country=german
        goto :Downloadandinstall
    )
    if  %wa%==It (
        set country=italy
        goto :Downloadandinstall
    )
    if  %wa%==J (
        set country=Japan
        goto :Downloadandinstall
    )
    if  %wa%==Pl (
        set country=poland
        goto :Downloadandinstall
    )
    if  %wa%==R (
        set country=russian
        goto :Downloadandinstall
    )
    if  %wa%==S (
        set country=sweden
        goto :Downloadandinstall
    )
    goto install
:Downloadandinstall
cls
echo %country%
if %Ask%==walalaru (goto loadbackup) else (
curl -OL# http://%ServerAddress%/WoTskin/Skin/%Ask%.zip
mkdir %ClientLocation%\SkinTemp\file
mkdir %ClientLocation%\SkinTemp\list
echo.> %ClientLocation%\SkinTemp\list\%Ask%.skin %Ask% \ %time%
mkdir %ClientLocation%\SkinTemp\Zip
tar.exe -xf %Ask%.zip -C %ClientLocation%\SkinTemp\file
move %Ask%.zip %ClientLocation%\SkinTemp\Zip
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\american
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\british
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\chinese
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\czech
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\french
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\german
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\japan
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\italy
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\poland
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\russian
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\sweden

for /f "delims=\ usebackq" %%e in (ClientLocation.inf) do set DriveName=%%e
cd /d %DriveName%
cd %ClientLocation%\SkinTemp\file\
xcopy %Ask% %ClientLocation%\res_mods\%ClientVersion%\ /e
goto Install
)

:loadbackup
cls
echo WIP
for %%z in (%ClientLocation%\SkinTemp\list\*.skin) do (
    set loadbackuped=%%~nz
    echo %%~nz
    echo !loadbackuped!
    curl -OL# http://%ServerAddress%/WoTskin/Skin/!loadbackuped!.zip
    mkdir %ClientLocation%\SkinTemp\file
    mkdir %ClientLocation%\SkinTemp\list
    mkdir %ClientLocation%\SkinTemp\Zip
    tar.exe -xf !loadbackuped!.zip -C %ClientLocation%\SkinTemp\file
    move !loadbackuped!.zip %ClientLocation%\SkinTemp\Zip

    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\american
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\british
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\chinese
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\czech
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\french
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\german
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\japan
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\italy
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\poland
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\russian
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\sweden

    cd /d %DriveName%
    cd %ClientLocation%\SkinTemp\file\

    xcopy !loadbackuped! %ClientLocation%\res_mods\%ClientVersion%\ /e
)
goto Install