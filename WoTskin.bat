@echo off
chcp 65001


for /f "delims=" %%a in (WoTskinList.inf) do set list=%%a

for /f "delims=" %%b in (WoTskinLocation.inf) do set loc=%%b

echo 리스트 : %list%
echo 위치 : %loc%

pause