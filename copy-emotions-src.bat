@echo off
set SRC=C:\Users\Yairn\Downloads
set DST=C:\Users\Yairn\Desktop\roy-games\images\emotions-src

if not exist "%DST%" mkdir "%DST%"

for %%F in (boy-happy boy-sad boy-angry boy-surprised boy-scared girl-happy girl-sad girl-angry girl-surprised girl-scared) do (
    powershell -NoProfile -Command ^
    "$f = Get-ChildItem '%SRC%' -Filter '%%F*.jpg' | Sort-Object LastWriteTime -Descending | Select-Object -First 1; if($f){ Copy-Item $f.FullName '%DST%\%%F.jpg' -Force; Write-Host 'OK: %%F (' + $f.Length + ' bytes)' } else { Write-Host 'MISSING: %%F' }"
)

echo.
echo Done! Files in %DST%
pause
