@echo off

:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Please Run as Administrator..
	pause
	exit /B
)else ( goto gotAdmin )

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
    regsvr32 /u "UnityCaptureFilter32.dll"
    regsvr32 /u "UnityCaptureFilter64.dll"
:--------------------------------------
