@echo off
echo === moving images ===
powershell -ExecutionPolicy Bypass -File "%~dp0move-mg-images.ps1"
echo.
echo === git push ===
cd /d "%~dp0"
git add images\mg\*.jpg
git add index.html
git commit -m "add puzzles 10-14 to mr-gamish"
git push origin master
echo.
echo Done!
pause
