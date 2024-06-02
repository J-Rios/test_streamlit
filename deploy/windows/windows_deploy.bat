@echo off

REM Constants
set APPNAME=streamlit_demo

REM Run PyInstaller Deploy
pyinstaller --name %APPNAME% --clean --onefile ..\..\src\run_app.py

REM Check if deploy was success
if %errorlevel% neq 0 (
    echo PyInstaller fallo.
    exit /b %errorlevel%
)

REM Copy .streamlit to release directory
xcopy /E /I /H /Y "..\.streamlit" "dist\.streamlit"

REM Copy source files to release directory
for %%f in (..\..\src\*.py) do (
    copy "%%f" "dist\"
)

REM Remove build directory & spec file
rmdir /S /Q ".\build"
del %APPNAME%.spec

REM Rename release directory
ren dist %APPNAME%
