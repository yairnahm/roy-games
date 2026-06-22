@echo off
cd /d "C:\Users\Yairn\Desktop\roy-games"
echo Running image processing...
py process_emotions.py
echo.
echo Adding images to git...
git add images/emotions/boy/ images/emotions/girl/
git add index.html
echo Committing...
git commit -m "emparts: update emotion images"
echo Pushing...
git push origin master
echo.
echo Done!
pause
