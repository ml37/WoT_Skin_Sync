@echo off
chcp 65001
color 8f
title World Of Tank Skin Sync
set ServerAddress=mashiro37.i234.me

for /f "delims=" %%a in (WoTskinList.inf) do set list=%%a

for /f "delims=" %%b in (WoTskinLocation.inf) do set loc=%%b
for /f "delims=" %%c in (_Aslains_Installer_Options.inf) do set aslain=%%c

echo Skin list : %list%
echo Gamefile Location : %loc%
echo aslain : %aslain%

rem curl -OL http://%ServerAddress%/WoTskin/walalaru.zip -o mods.zip


pause