::&cls&::

@echo off
setlocal enabledelayedexpansion

call :setESC

title Installer PE

echo Change coding on W1251 for correct output russian text.

chcp 1251

echo ��������� ��������� �� Windows 1251 ��� ����������� ������ �������� ������.

set count=0
for /f "usebackq tokens=1,* delims==" %%a in ("config.ini") do (
    if "%%a"=="category" (
        set /a count+=1
        set "category[!count!]=%%b"
    )
    if "%%a"=="name" (
        set "program[!count!]=%%b"
    )
    if "%%a"=="url" (
        set "url[!count!]=%%b"
    )
    if "%%a"=="silentArgs" (
        set "silentArgs[!count!]=%%b"
    )
)
set back_count=0
set /a back_count=%count%+1

:first_loading
cls
echo %ESC%[42m======================= ���������� ������������ ��� ������� ��������-����������...=======================%ESC%[0m
start /wait "" curl -o file.lua "https://raw.githubusercontent.com/alfantasy/AdminTool/main/ATEvents.lua"
timeout /t 3 >nul
echo %ESC%[92m������. ��������� ��������� ����������...%ESC%[0m
timeout /t 3 >nul
cls
echo %ESC%[100mLoading.%ESC%[0m
timeout /t 1 >nul
cls
echo %ESC%[100mLoading..%ESC%[0m
timeout /t 1 >nul
cls
echo %ESC%[100mLoading...%ESC%[0m
timeout /t 1 >nul
cls
echo %ESC%[100mLoading.%ESC%[0m
timeout /t 1 >nul
cls
echo %ESC%[100mLoading..%ESC%[0m
timeout /t 1 >nul
cls
echo %ESC%[100mLoading...%ESC%[0m
timeout /t 1 >nul
cls
echo %ESC%[100mLoading complete.%ESC%[0m
timeout /t 1 >nul
goto menu

:menu
:: ������� ���� ������ ���������
cls
echo %ESC%[34m======================= Installer Program PE by InfoSecurity =======================%ESC%[0m
echo �������� ����������� ��������:
echo 1: ���������� � ��������� ����������� ��������.
echo 2: ��������� ��������� �� ������ PE IFS.
echo 3: �������
echo.
echo.
echo 0. �����
echo %ESC%[34m======================= Installer Program PE by InfoSecurity =======================%ESC%[0m

:: �������� ���� ������������
set /p choice="������� ����������� ��������... "

if "%choice%"=="1" goto download_and_install_programs
if "%choice%"=="2" goto install_program_ifs
if "%choice%"=="3" goto echo_help
if %choice%==0 goto exit 
if not "%choice%"=="1" if not "%choice%"=="2" if not "%choice%"=="0" (
    echo �������� �����. ����������, �������� �����.
    goto menu
)
goto :eof

:echo_help
cls
echo %ESC%[34m======================= Installer Program PE by InfoSecurity =======================%ESC%[0m
echo %ESC%[36m========================= Help. ������� � ������������� ������� =========================%ESC%[0m
echo ������ �������� � ��������� ���� "���������� � ��������� ����������� ��������":
echo    ��������� �� ��������� ������� ������������ ��������� � �������������. 
echo    ��� ������ � ��������� ��������� ��� ���������.
echo ������ �������� � ��������� ���� "��������� ��������� �� ������ PE IFS"
echo    ������������, ��� ������ ����� �������� PE (PostInstallation Environment) �� InfoSecurity. ��� ��������� � ���� ���� ��������� � ������������.
echo    ������� ����� �� ������ ����.
echo.
echo.
echo %ESC%[36m========================= Help. ������� � ������������� ������� =========================%ESC%[0m
echo %ESC%[34m======================= Installer Program PE by InfoSecurity =======================%ESC%[0m

set /p choice_help="������� 0 ��� ������..."

if %choice_help%==0 goto menu
goto :eof

:download_and_install_programs
cls
echo %ESC%[34m======================= Installer Program PE by InfoSecurity - Online =======================%ESC%[0m
echo �������� ��������� ������������ ������������ �����������.
echo 1: ��������
echo 2: ����������
echo 3: ��������� ��������� � IDE
echo 4: �����������
echo.
echo.
echo 0: �����
echo %ESC%[34m======================= Installer Program PE by InfoSecurity - Online =======================%ESC%[0m


set /p choice_category="����..." 

if %choice_category% geq 1 if %choice_category% leq %count% (
    call :select_category %choice_category%
) else if %choice_category% == 0 (
    echo ������������ � ������� ����...
    goto menu
) else (
    echo �������� �����. ����������, �������� �����.
    goto download_and_install_programs
)
if %choice_category% == 0 (
    echo ������������ � ������� ����...
    goto menu
)
goto :eof

:select_category
cls
echo %ESC%[34m======================= Installer Program PE by InfoSecurity - Online =======================%ESC%[0m
echo �������� ����������� ��� ���������. ��������� ����������� �� ������������, �� ��������� ��������.
for /l %%i in (1,1,%count%) do (
    if "%choice_category%"=="1" (
        if !category[%%i]! == Browser (
            echo %%i: !program[%%i]!
        )
    )
    if "%choice_category%"=="2" (
        if !category[%%i]! == Archiver (
            echo %%i: !program[%%i]!
        )
    )    
    if "%choice_category%"=="3" (
        if "!category[%%i]!" == "Text Editor" (
            echo %%i: !program[%%i]!
        )
    )      
    if "%choice_category%"=="4" (
        if "!category[%%i]!" == "Media Player" (
            echo %%i: !program[%%i]!
        )
    )        
)
echo.
echo.
echo 0. �����
echo %ESC%[34m======================= Installer Program PE by InfoSecurity - Online =======================%ESC%[0m

set /p choice_program="����..."

if %choice_program% geq 1 if %choice_program% leq %count% (
    call :install_program %choice_program%
) else if "%choice_program%"=="0" (
    echo ������������ �����...
    goto download_and_install_programs
) else (
    echo �������� �����. ����������, �������� �����
    call :select_category %choice_category%
)
if %choice_program%==0 (
    echo ������������ �����...
    goto download_and_install_programs
)
goto :eof

:install_program_ifs
cls
echo %ESC%[34m======================= Installer Program PE by InfoSecurity - Offline =======================%ESC%[0m
echo ��������! ��������� Offline �������� ������������ ������� ������ �� IFS. ���� ��� ���, �������� ������ ����. 
echo ���� �� ����������, �� �������� ������ ������ ��� ����������.
echo.
echo �������� ����������� �������...
echo 1: program A
echo 2: program B
echo 3: program C 
echo.
echo.
echo 0. �����
echo %ESC%[34m======================= Installer Program PE by InfoSecurity - Online =======================%ESC%[0m

set /p choice_program_ifs="����..."

if %choice_program_ifs%==0 (
    echo ����������� � ������� ����...
    goto menu
)
if not "%choice_program_ifs%"=="1" if not "%choice_program_ifs%"=="2" if not "%choice_program_ifs%"=="3" if not "%choice_program_ifs%"=="4" (
    echo �������� �����. ����������, �������� �����.
    goto install_program_ifs
)
goto :eof

:install_program
set program=!program[%1]!
set url=!url[%1]!
set silentArgs=!silentArgs[%1]!
cls
if not "%program%" == "None" (
    :: ��������� ������������ ����
    echo �������� ������� ���������� � ��������� ��������� %program%...
    echo ������������� URL: %url%
    timeout /t 3 >nul
    echo ����������� %program%...
    powershell -Command "try {Invoke-WebRequest -Uri '%url%' -OutFile \"$env:TEMP\installer.exe\"} catch {Write-Host '������ PowerShell: ' $_.Exception.Message; exit 1}"


    :: ������������� ��������� � ������� ������
    echo ��������������� %program%...
    if not exist "%TEMP%\installer.exe" (
        echo ������. �� ������� ��������� ������������ ���� ��� %program%. ��������, �� �����������.
    )

    if exist "%TEMP%\installer.exe" (
        if "%silentArgs%" == "/None" (
            start /wait "" "%TEMP%\installer.exe"
        ) else (
            start /wait "" "%TEMP%\installer.exe" %silentArgs%
        )
    )

    :: ������� ������������ ���� ����� ���������
    if not exist "%TEMP%\installer.exe" (
        echo %program% ���� ����������� �����������. ��������� ������������ �������.
    )
    if exist "%TEMP%\installer.exe" (
        del "%TEMP%\installer.exe"
        echo %program% ������� �����������.
    )
    set program="None"
    set url="None"
    set silentArgs="None"
    set choice="None"
    set choice_category="None"
    set choice_program_ifs="None"
)
pause
goto download_and_install_programs

endlocal

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0