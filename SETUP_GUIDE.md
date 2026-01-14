# 🕐 Bambang Split-Flap Clock - Windows 10 Auto-Start Setup Guide

## 📁 Project Structure

```
multi_function_clock/
├── main.py                      # Main clock application
├── run_clock.bat                # Run clock (shows console)
├── run_clock_hidden.vbs         # Run clock (hidden console) ⭐
├── create_startup_shortcut.bat  # Add to Windows startup
├── remove_startup_shortcut.bat  # Remove from Windows startup
├── build_exe.bat                # Build standalone .exe file
└── SETUP_GUIDE.md               # This guide
```

---

## 🚀 METHOD 1: Quick Start (Recommended)

### Step 1: Test the Clock
Double-click `run_clock.bat` to make sure the clock works.

### Step 2: Enable Auto-Start
Double-click `create_startup_shortcut.bat`

✅ **Done!** The clock will now start automatically every time Windows boots.

### To Disable Auto-Start
Double-click `remove_startup_shortcut.bat`

---

## 🔧 METHOD 2: Manual Startup Setup

### Step 1: Open Windows Startup Folder
1. Press `Win + R` to open Run dialog
2. Type: `shell:startup`
3. Press Enter

### Step 2: Create Shortcut
1. Right-click in the Startup folder
2. Select **New → Shortcut**
3. Browse to: `C:\Users\marlina trisia\Downloads\CODES\multi_function_clock\run_clock_hidden.vbs`
4. Name it: `Bambang Clock`
5. Click Finish

---

## 📦 METHOD 3: Build Standalone Executable (.exe)

This creates a single `.exe` file that runs without needing Python installed.

### Step 1: Build the Executable
Double-click `build_exe.bat`

Wait for the build process to complete (may take 1-2 minutes).

### Step 2: Find Your Executable
The executable will be in: `dist\BambangClock.exe`

### Step 3: Add to Startup (Optional)
1. Copy `BambangClock.exe` to the Startup folder
2. Open Startup folder: Press `Win + R`, type `shell:startup`, press Enter
3. Paste the `.exe` file there

---

## ⚙️ Windows Task Scheduler (Advanced)

For more control over when and how the app starts:

### Step 1: Open Task Scheduler
1. Press `Win + R`
2. Type: `taskschd.msc`
3. Press Enter

### Step 2: Create Basic Task
1. Click **Create Basic Task**
2. Name: `Bambang Clock`
3. Trigger: **When I log on**
4. Action: **Start a program**
5. Program: `wscript.exe`
6. Arguments: `"C:\Users\marlina trisia\Downloads\CODES\multi_function_clock\run_clock_hidden.vbs"`
7. Finish

---

## 🔍 Troubleshooting

### Clock doesn't start?
- Make sure Python is installed and in your PATH
- Try running `run_clock.bat` first to check for errors

### Black console window appears?
- Use `run_clock_hidden.vbs` instead of `run_clock.bat`

### Want to stop auto-start?
- Run `remove_startup_shortcut.bat`
- Or manually delete the shortcut from the Startup folder

### Need to run without Python installed?
- Use `build_exe.bat` to create a standalone `.exe`

---

## 📋 System Requirements

- Windows 10/11
- Python 3.8+ (not needed if using .exe)
- Tkinter (included with Python)

---

Made with ❤️ - Bambang Split-Flap Clock
