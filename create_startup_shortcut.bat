@echo off
echo ============================================================
echo  BAMBANG SPLIT-FLAP CLOCK - Startup Shortcut Creator
echo ============================================================
echo.

:: Get the script directory
set "SCRIPT_DIR=%~dp0"
set "VBS_FILE=%SCRIPT_DIR%run_clock_hidden.vbs"
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

:: Create shortcut using PowerShell
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%STARTUP_FOLDER%\BambangClock.lnk'); $s.TargetPath = '%VBS_FILE%'; $s.WorkingDirectory = '%SCRIPT_DIR%'; $s.Description = 'Bambang Split-Flap Clock'; $s.Save()"

if exist "%STARTUP_FOLDER%\BambangClock.lnk" (
    echo.
    echo [SUCCESS] Startup shortcut created!
    echo Location: %STARTUP_FOLDER%\BambangClock.lnk
    echo.
    echo The clock will now start automatically when Windows boots.
) else (
    echo.
    echo [ERROR] Failed to create shortcut.
    echo Please try running this script as Administrator.
)

echo.
pause
