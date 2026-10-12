@echo off
title Radiant Optimizer - ADMIN MODE
color 0C

echo ========================================
echo   RADIANT OPTIMIZER [ADMIN MODE]
echo   Gaming Performance Booster
echo ========================================
echo.
echo Running with Administrator privileges...
echo This enables ALL optimizations!
echo.

REM Check if running as admin
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Not running as Administrator!
    echo Requesting admin rights...
    echo.
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo [SUCCESS] Running as Administrator
echo.

REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed!
    echo Please install Python 3.7+ from python.org
    pause
    exit /b 1
)

REM Install dependencies
pip install psutil >nul 2>&1

echo [INFO] Launching Radiant Optimizer with full privileges...
echo.

REM Run the optimizer
python radiant_optimizer.py

pause
