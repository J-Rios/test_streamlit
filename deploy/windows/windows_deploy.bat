@echo off

REM Application Name
set APP_NAME="streamlit_demo"

REM Run PyInstaller Deploy
pyinstaller --clean deploy_setup.spec

REM Check if deploy was success
if %errorlevel% neq 0 (
    echo "Error: PyInstaller deploy fail."
    pause
    exit /b %errorlevel%
)

REM Remove build directory
rmdir /S /Q ".\build"
del /Q ".\dist\%APP_NAME%.exe"

REM Clean and add .streamlit config file to deployed app directory
rmdir /S /Q ".\dist\%APP_NAME%\_internal"
xcopy /E /I /H /Y "..\.streamlit" ".\dist\%APP_NAME%\.streamlit"

echo "Application deploy success."
