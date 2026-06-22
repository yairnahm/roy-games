@echo off
cd /d "C:\Users\Yairn\Desktop\roy-games"
if exist .git\index.lock del /f .git\index.lock
if exist .git\HEAD.lock del /f .git\HEAD.lock
git add index.html
git commit -m "mgamish: add puzzles 10-14 to mgPuzzles array"
git push origin master
echo.
echo Done!
pause
