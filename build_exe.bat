@echo off
echo ============================================================
echo  BAMBANG SPLIT-FLAP CLOCK - Build Executable
echo ============================================================
echo.

:: Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing PyInstaller...
    pip install pyinstaller
)

echo.
echo [INFO] Building executable...
echo.

cd /d "%~dp0"
pyinstaller --onefile --windowed --name "BambangClock" --icon=NONE main.py

if exist "dist\BambangClock.exe" (
    echo.
    echo ============================================================
    echo [SUCCESS] Executable created!
    echo.
    echo Location: %~dp0dist\BambangClock.exe
    echo.
    echo You can now:
    echo 1. Run BambangClock.exe directly
    echo 2. Copy it to your Startup folder to auto-run on boot
    echo    Startup folder: %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
    echo ============================================================
) else (
    echo.
    echo [ERROR] Build failed. Check for errors above.
)

echo.
pause
