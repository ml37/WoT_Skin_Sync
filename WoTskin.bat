@echo off
chcp 65001
color 8f
title World Of Tank Skin Sync
set ServerAddress=mashiro37.i234.me
rem curl -OL http://%ServerAddress%/WoTskin/walalaru.zip -o mods.zip
for /f


curl -OL# http://%ServerAddress%/WoTskin/Skinlist.inf

for /f "delims=" %%a in (Skinlist.inf) do set list=%%a
for /f "delims=" %%b in (WoTskinLocation.inf) do set loc=%%b

echo Skin list : %list%
echo Gamefile Location : %loc%
cls

for /f "tokens=*" %%s in (Skinlist.inf) do (
  echo %%s
)




pause