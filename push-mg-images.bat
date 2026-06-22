@echo off
echo === commit + push mr-gamish images ===
cd /d "%~dp0"
if exist .git\index.lock del /f .git\index.lock
if exist .git\HEAD.lock del /f .git\HEAD.lock
git add images\mg\*.jpg
git commit -m "add mr-gamish images 10-14 (20 images)"
git push origin master
echo.
echo Done!
pause
