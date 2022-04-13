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
del list.txt
:start
cls
    echo ───────────────────────────────────────
    echo %FileName%
    echo %StartPosition%
	echo ───────────────────────────────────────
	echo 1. 미국(american) - A
	echo 2. 영국(british) - GB
	echo 3. 중국(chinese) - Ch
	echo 4. 체코(czech) - Cz
	echo 5. 프랑스(french) - F
	echo 6. 독일(german) - G
    echo 7. 이탈리아(italy) - It
    echo 8. 일본(japan) - J
    echo 9. 폴란드(poland) - Pl
    echo 10. 러시아(russian) - R
    echo 11. 스웨덴(sweden) - S
	echo ───────────────────────────────────────
    set /p sel="국가 : "
    echo 
    if %sel%=="" (
        goto start
    ) 
    if  %sel%==A (
        set country=american
        goto :Install
    )
    if  %sel%==GB (
        set country=british
        goto :Install
    )
    if  %sel%==Ch (
        set country=chinese
        goto :Install
    )
    if  %sel%==Cz (
        set country=czech
        goto :Install
    )
    if  %sel%==F (
        set country=french
        goto :Install
    )
    if  %sel%==G (
        set country=german
        goto :Install
    )
    if  %sel%==It (
        set country=italy
        goto :Install
    )
    if  %sel%==J (
        set country=J
        goto :Install
    )
    if  %sel%==Pl (
        set country=poland
        goto :Install
    )
    if  %sel%==R (
        set country=russian
        goto :Install
    )
    if  %sel%==S (
        set country=sweden
        goto :Install
    )
    if  %sel%==a (
        set country=american
        goto :Install
    )
    if  %sel%==gb (
        set country=british
        goto :Install
    )
    if  %sel%==ch (
        set country=chinese
        goto :Install
    )
    if  %sel%==cz (
        set country=czech
        goto :Install
    )
    if  %sel%==f (
        set country=french
        goto :Install
    )
    if  %sel%==g (
        set country=german
        goto :Install
    )
    if  %sel%==it (
        set country=italy
        goto :Install
    )
    if  %sel%==j (
        set country=J
        goto :Install
    )
    if  %sel%==pl (
        set country=poland
        goto :Install
    )
    if  %sel%==r (
        set country=russian
        goto :Install
    )
    if  %sel%==s (
        set country=sweden
        goto :Install
    )
    cls
    echo %country% 
    pause
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
pause