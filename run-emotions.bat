@echo off
powershell -ExecutionPolicy Bypass -File "%~dp0organize-emotions.ps1"
cd /d "%~dp0"
git add .
git commit -m "add emotion images"
git push origin master
echo Done.
pause
