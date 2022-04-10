chcp 65001
@echo off
color 8f
	set nowver=3.12
	set minecraftloc=%UserProfile%\appdata\Roaming\.minecraft\
	set downlink=mashiro37.i234.me
	set batloc=%cd%
	title %nowver% %downlink% %cd%
	
:start
	cls
	echo ─────────────Ver.%nowver%──────────────
	echo 1. 모드 관리
	echo 2. mod tool install
	echo 3. 수동설치(Pin)
	echo 4. 업데이트
	echo 5. 게임 설치
	echo 6. .minecraft 폴더 열기
	echo ───────────────────────────────────────
	
	set /p sel="선택 : "
		if %sel%==1 goto modmanage
		if %sel%==2 goto modtoolinstall
		if %sel%==3 goto manualinstall
		if %sel%==4 goto update
		if %sel%==5 goto gameinstall
		if %sel%==6 goto openmcfolder
		if %sel%==7 goto makezip
		if %sel%==8 goto normalmod
		if %sel%==9 goto devmod
		
		
:openmcfolder
	cls
	echo open .minecraft folder...
	explorer %UserProfile%\appdata\Roaming\.minecraft\
	goto start
:devmod
	@echo on
	set downlink=192.168.0.111
	title %nowver% %downlink%
	color 43
	goto start

:normalmod
	@echo off
	set downlink=mashiro37.i234.me
	title %nowver% %downlink%
	color 8f
	goto start
	
:modmanage
	cls
	echo ────────MOD 관리─────────
	echo 1. 마인크래프트 모드 설치
	echo 2. 뒤로가기
	echo ──────────────────────
	set /p selmod="선택 : "
		if %selmod%==1 goto minecraftmodautoinstall
		if %selmod%==2 goto start
		if %selmod%==9 goto makemodzip
		
		:minecraftmodautoinstall
			mkdir %minecraftloc%\mods

			curl -OL http://%downlink%/mad/mcmod/mods.zip -o mods.zip
pause
			tar.exe -xf mods.zip -C %minecraftloc%
pause
			del mods.zip
			
			goto start
			
		:makemodzip
		cls
			md mods
				echo input mod files on mods file
		pause
			tar -cvzf mods.zip mods
		pause
			echo make zip complete
		pause
		goto start
	

:modtoolinstall
	cls
	echo ────────MOD 툴 설치────────
	echo 1. World Of Tank 모드 툴
	echo 2. 뒤로가기
	echo ────────────────────────────────
	set /p seltool="선택 : "
		if %seltool%==1 curl http://%downlink%/mad/wotmod/wotse.zip -o wotse.zip
		if %seltool%==2 goto start
	


:manualinstall
	cls
	echo ────────Manual install────────
	echo 모드나 게임 등을 정해진 핀을 입력해서
	echo 수동 설치할 수 있습니다. Work In Progress
	echo ──────────────────────────────
	set /p selmanualfin="입력 : "
		echo %selmanualfin%
		pause
		curl http://%downlink%/mad/manual/list/%selmanualfin%.txt -o hmm.txt
		pause
		set /p manualfin=<hmm.txt
		echo manualfin %manualfin%
		pause
		echo selmanual %selmanualfin%
		pause
		cls
		if %manualfin%==%selmanualfin% goto manualauth
	goto start
	
	:manualauth
		echo auth complete
		pause
		mkdir manualdownload
		curl http://%downlink%/mad/manual/files/%selmanualfin%.zip -o %selmanualfin%.zip
		pause
		goto start
		
		
:update
	cls
		curl http://%downlink%/mad/madbat/update.txt -o update.txt
		set /p updatever=<update.txt
		del update.txt
		cls
		echo 현재버전 : %nowver%
		echo 최신버전 : %updatever%
		pause
	if %nowver%==%updatever% goto samever
		curl http://%downlink%/mad/madbat/launcher/mad%updatever%.bat -o mad%updatever%.bat
		start mad%updatever%.bat
		exit
	:samever
		echo 현재 버전이 최신 버전입니다
			pause
			goto start

:gameinstall
	cls
		curl http://%downlink%/mad/games/gamelist.txt -o glist.txt
		set /p ablegamelist=<glist.txt
		del glist.txt
		echo %ablegamelist%
		pause
	
:makezip
	cls
		set /p makezipfin="fin : "
			md %makezipfin%
			pause
			cd %makezipfin%
			pause
			echo input %makezipfin% files on mods file
		pause
		echo %cd%
		pause

			tar -cvzf %makezipfin%.zip "*.*"
			pause
		cd ..
		pause
			copy "%cd%\%makezipfin%\%makezipfin%.zip" "%cd%\"
			pause
		cd %makezipfin%
		pause
			del %makezipfin%.zip
			pause
		cd ..
		pause
		cls
		pause
			echo make zip complete
		pause
		goto start
	
	echo wip
	pause
	goto start