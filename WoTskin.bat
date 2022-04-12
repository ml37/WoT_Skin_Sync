@echo on
chcp 65001
color 8f
for /f "delims=" %%a in (ClientLocation.inf) do set ClientLocation=%%a
for /f "delims=\ usebackq" %%e in (ClientLocation.inf) do set DriveName=%%e
set ListNumber = 1
set ServerAddress=mashiro37.i234.me
curl -OL# http://%ServerAddress%/WoTskin/Skinlist.inf
curl -OL# http://%ServerAddress%/WoTskin/Version.inf 
for /f "delims=" %%b in (Version.inf) do set ClientVersion=%%b
:Sync

curl -OL# http://%ServerAddress%/WoTskin/Skinlist.inf
curl -OL# http://%ServerAddress%/WoTskin/Version.inf 
for /f "delims=" %%b in (Version.inf) do set ClientVersion=%%b


cls

title "World Of Tank Skin Sync %ClientLocation% | %ClientVersion%"
echo -----------Select------------
setlocal enabledelayedexpansion
for /f "tokens=*" %%c in (Skinlist.inf) do (
    set /a ListNumber = !ListNumber! + 1
    echo No.!ListNumber! - %%c
)
set ListNumber = 1
echo -----------------------------
for /f "delims=_ usebackq" %%d in (Skinlist.inf) do (echo %%d) 
echo -----------Select------------
setlocal
set /p "Ask= Number [ex) It17], If you want to load backup, type [walalaru] : "
if %Ask%==walalaru (goto loadbackup) else (
curl -OL# http://%ServerAddress%/WoTskin/Skin/%Ask%.zip
mkdir %ClientLocation%\SkinTemp\file
mkdir %ClientLocation%\SkinTemp\list
echo.> %ClientLocation%\SkinTemp\list\%Ask%.skin %Ask% \ %time%
mkdir %ClientLocation%\SkinTemp\Zip
tar.exe -xf %Ask%.zip -C %ClientLocation%\SkinTemp\file
move %Ask%.zip %ClientLocation%\SkinTemp\Zip

mkdir %ClientLocation%\res_mods\%ClientVersion%
mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles
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
pause
goto Sync
pause
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

    mkdir %ClientLocation%\res_mods\%ClientVersion%
    mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles
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
pause
goto Sync