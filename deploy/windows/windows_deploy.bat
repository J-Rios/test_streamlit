@echo off

REM Constants
set APP_NAME="streamlit_demo"
set DIR_SRC="..\..\src"

REM Run PyInstaller Deploy
pyinstaller --name %APP_NAME% --clean --onefile %DIR_SRC%\run_app.py

REM Check if deploy was success
if %errorlevel% neq 0 (
    echo "Error: PyInstaller deploy fail."
    echo ""
    exit /b %errorlevel%
)

REM Copy .streamlit to release directory
xcopy /E /I /H /Y "..\.streamlit" "dist\.streamlit"

REM Copy source files to release directory
for %%f in (%DIR_SRC%\*.py) do (
    copy "%%f" "dist\"
)

REM Remove build directory & spec file
rmdir /S /Q ".\build"
del %APP_NAME%.spec

REM Rename release directory
ren dist %APP_NAME%

echo ""
