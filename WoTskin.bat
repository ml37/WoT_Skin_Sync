@echo off
chcp 65001


for /f "delims=" %%a in (WoTskinList.inf) do set list=%%a

for /f "delims=" %%b in (WoTskinLocation.inf) do set loc=%%b

echo Skin list : %list%
echo Gamefile Location : %loc%

pause