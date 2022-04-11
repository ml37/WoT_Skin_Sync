@echo on
chcp 65001
color 8f
title World Of Tank Skin Sync

set ListNumber = 1
set ServerAddress=mashiro37.i234.me

rem curl -OL# http://%ServerAddress%/WoTskin/Skinlist.inf rem 서버에서 다운가능한 리스트 받아오기

for /f "delims=" %%a in (ClientLocation.inf) do set ClientLocation=%%a


cls

title World Of Tank Skin Sync %ClientLocation%
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
mkdir %ClientLocation%\SkinTemp
tar.exe -xf %Ask%.zip -C %ClientLocation%\SkinTemp\


rem ClientLocation.inf에서 위치 가져오고 res_mods 폴더로 이동
for /f "delims=\ usebackq" %%b in (ClientLocation.inf) do set DriveName=%%b
cd /d %DriveName%
cd %ClientLocation%\SkinTemp

:: 국가 선택 한 다음에 가능한 번호 쫙 띄워서 보여주는쪽이 직관적일듯 골때리는게 코드(A134)랑 스킨이름(A134_M24E2_SuperChaffee) 매칭이 짜증날듯 이거는 wotmod형식으로 묶어서 A134.wotmod 해놓고 안에 res/1.16.0/america/A134_M24E2_SuperChaffee 이런식으로 포장하는게 좋을거같은데 아니면 서버 저장공간에서 A134 폴더 이런식으로 따로 묶어놔도 될거고


pause