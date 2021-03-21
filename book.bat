@echo off

set fn=%1
set flag=%2
set unlim=%*
cd /d %~dp0

if NOT "%1"=="" (
    python createDir.py %unlim%
    ) else (
        echo "error"
    )
)