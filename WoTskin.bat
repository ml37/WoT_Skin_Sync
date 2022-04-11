@echo off
chcp 65001
color 8f

set ListNumber = 1
set ServerAddress=mashiro37.i234.me

curl -OL# http://%ServerAddress%/WoTskin/Skinlist.inf
curl -OL# http://%ServerAddress%/WoTskin/Version.inf 

for /f "delims=" %%a in (ClientLocation.inf) do set ClientLocation=%%a
for /f "delims=" %%b in (Version.inf) do set ClientVersion=%%b

cls

title "World Of Tank Skin Sync %ClientLocation% | %ClientVersion%"
echo -----------Select------------
setlocal enabledelayedexpansion
for /f "tokens=*" %%s in (Skinlist.inf) do (
    set /a ListNumber = !ListNumber! + 1
    echo No.!ListNumber! - %%s
)

rem 번호 입력 코드 탱크 이름 예시) A134_M24E2_SuperChaffee, It12_Prototipo_Standard_B
echo -----------------------------
for /f "delims=_ usebackq" %%c in (Skinlist.inf) do (echo %%c) 
echo -----------Select------------
setlocal
set /p "Ask= Walalaru : "
curl -OL# http://%ServerAddress%/WoTskin/Skin/%Ask%.zip
mkdir %ClientLocation%\SkinTemp\file
mkdir %ClientLocation%\SkinTemp\list
echo.> %ClientLocation%\SkinTemp\list\%Ask%.inf
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



rem ClientLocation.inf에서 위치 가져오고 res_mods 폴더로 이동
for /f "delims=\ usebackq" %%b in (ClientLocation.inf) do set DriveName=%%b
cd /d %DriveName%

cd %ClientLocation%\SkinTemp\file\

xcopy %Ask% %ClientLocation%\res_mods\%ClientVersion%\ /e




:: 국가 선택 한 다음에 가능한 번호 쫙 띄워서 보여주는쪽이 직관적일듯 골때리는게 코드(A134)랑 스킨이름(A134_M24E2_SuperChaffee) 매칭이 짜증날듯 이거는 wotmod형식으로 묶어서 A134.wotmod 해놓고 안에 res/1.16.0/america/A134_M24E2_SuperChaffee 이런식으로 포장하는게 좋을거같은데 아니면 서버 저장공간에서 A134 폴더 이런식으로 따로 묶어놔도 될거고


pause