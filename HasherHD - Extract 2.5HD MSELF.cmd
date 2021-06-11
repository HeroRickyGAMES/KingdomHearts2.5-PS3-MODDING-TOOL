@echo off
if not exist "%~dp0HasherHD.exe" echo.Error: %~nx0 must be in the same folder as HasherHD.exe. & pause & exit/b
if not exist "%~dp0SDATA_DEC.exe" echo.Warning: Files will be saved encrypted. To automatically decrypt files, put & echo.         sdata-tool.exe in the same folder as HasherHD.exe. & pause
if not exist "%~f1" echo.Drag the MSELF file to extract onto this. & pause & exit/b
if not "%~x1"==".mself" echo.Error: %~nx1 is not a MSELF. & pause & exit/b
if not exist "%~dp1index.dat" echo.Error: Corresponding index.dat not found in the same folder as %~nx1. & pause & exit/b

pushd "%~dp1"
"%~dp0HasherHD.exe" --batch --extractmself "%~dp1index.dat" "%~f1"
popd
echo.Done!

pause
