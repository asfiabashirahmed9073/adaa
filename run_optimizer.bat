@echo off
title Radiant Optimizer - Gaming Performance Booster
color 0A

echo ========================================
echo   RADIANT OPTIMIZER
echo   Gaming Performance Booster
echo ========================================
echo.

REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed!
    echo Please install Python 3.7+ from python.org
    echo.
    pause
    exit /b 1
)

echo [INFO] Python found. Installing dependencies...
echo.

REM Install required packages
pip install psutil >nul 2>&1

echo [SUCCESS] Dependencies installed!
echo.
echo [INFO] Launching Radiant Optimizer...
echo.

REM Run the optimizer
python radiant_optimizer.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to run the optimizer!
    echo Make sure all files are in the same directory.
    pause
    exit /b 1
)

pause
