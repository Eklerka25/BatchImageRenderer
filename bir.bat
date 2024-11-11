@echo off
setlocal enableDelayedExpansion

title Batch Image Renderer by Eklerka25

cls
MODE CON:cols=340 lines=116
set /p "file=File to render >> "
echo.
echo Please set your font size to lowest posible and 
echo use regular CMD instead of windows terminalfor the best results
echo.
echo Press any key if you did that...
pause > nul
echo.
cls

MODE CON:cols=340 lines=116

set /a "int=0"
set "var="

for /f %%L in (!file!) do (
    set /a "int+= 1"
    set var=!var![48;2;%%Lm [0m

    if "!int!" == "340" (
        set /a int=0
        echo !var!
        set "var="
    )
)

pause > nul
exit

:err
echo.
echo [91m ERROR [0m: File '%1' not found 
pause > nul
exit