@echo off
echo ============================================================
echo  BAMBANG SPLIT-FLAP CLOCK - Remove Startup Shortcut
echo ============================================================
echo.

set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

if exist "%STARTUP_FOLDER%\BambangClock.lnk" (
    del "%STARTUP_FOLDER%\BambangClock.lnk"
    echo [SUCCESS] Startup shortcut removed!
    echo The clock will no longer start automatically.
) else (
    echo [INFO] No startup shortcut found.
)

echo.
pause
