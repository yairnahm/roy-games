@echo off
echo === Contents of Downloads folder ===
dir "C:\Users\Yairn\Downloads" /O-D /B 2>nul
echo.
echo === If empty, searching other locations ===
dir "%USERPROFILE%\Downloads" /O-D /B 2>nul
echo.
echo USERPROFILE = %USERPROFILE%
echo.
pause
