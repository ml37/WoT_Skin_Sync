@echo on
:aa
::set dragfiledirectory=%~1%
echo %~1% 
pause
goto aa

::결론 : 실행 도중에는 %~1%가 작동하지않음
::Conclude : While Action, %~1% is not working