@echo off
set BASE=C:\Users\Yairn\Desktop\roy-games
set DL=C:\Users\Yairn\Downloads

echo === Step 1: Copy source images from Downloads ===
mkdir "%BASE%\images\emotions-src" 2>nul
for %%F in (boy-happy boy-sad boy-angry boy-surprised boy-scared girl-happy girl-sad girl-angry girl-surprised girl-scared) do (
    powershell -NoProfile -Command ^
    "$f=Get-ChildItem '%DL%' -Filter '%%F*.jpg'|Sort-Object LastWriteTime -Desc|Select-Object -First 1;if($f){Copy-Item $f.FullName '%BASE%\images\emotions-src\%%F.jpg' -Force;Write-Host 'OK: %%F ('+$f.Length+' bytes)'}else{Write-Host 'MISSING: %%F'}"
)

echo.
echo === Step 2: Install Pillow ===
python -m pip install Pillow -q 2>nul
if errorlevel 1 python -m pip install Pillow --break-system-packages -q

echo.
echo === Step 3: Generate 50 emotion images ===
python "%BASE%\make-emotions.py"
if errorlevel 1 (
    echo ERROR in Python script!
    pause
    exit /b 1
)

echo.
echo === Step 4: Git push ===
cd /d "%BASE%"
if exist .git\index.lock del /f .git\index.lock
git add images\emotions\
git commit -m "emotions: AI cartoon illustration style (50 images, boy+girl)"
git push origin master

echo.
echo === DONE ===
pause
