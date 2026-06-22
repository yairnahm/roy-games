@echo off
echo === Recent JPG/PNG files in Downloads ===
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"Get-ChildItem 'C:\Users\Yairn\Downloads' -Filter '*.jpg','*.png' | ^
 Where-Object { $_.Name -match 'top|left|right|success' } | ^
 Sort-Object LastWriteTime -Descending | ^
 Select-Object Name, Length, LastWriteTime | ^
 Format-Table -AutoSize"
echo.
echo === If empty, showing last 20 downloads of any type ===
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"Get-ChildItem 'C:\Users\Yairn\Downloads' | ^
 Sort-Object LastWriteTime -Descending | ^
 Select-Object -First 20 Name, Length, LastWriteTime | ^
 Format-Table -AutoSize"
pause
