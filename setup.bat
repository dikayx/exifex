@echo off
setlocal EnableDelayedExpansion

rem This script is used to help the user setup the entire project

set "banner=--------------------------------
  ______      _  __ ______      
 |  ____|    (_)/ _|  ____|     
 | |__  __  ___| |_| |__  __  __
 |  __| \ \/ / |  _|  __| \ \/ /
 | |____ >  <| | | | |____ >  < 
 |______/_/\_\_|_| |______/_/\_\

--------------------------------"
echo %banner%
echo Welcome to the ExifEx setup script!
echo Press any key to continue...
pause >nul

rem Function to check if the port is valid
:CHECK_PORT
set port=%1
if not defined port set port=8080
if "%port%"=="0" (
    set "isValidPort=false"
) else (
    set "isValidPort=true"
    for /L %%i in (1,1,65535) do (
        if "!port!"=="%%i" set "isValidPort=true"
    )
)
exit /b

rem Check if Docker is running
docker info >nul 2>&1
if %errorlevel% equ 0 (
    echo Docker is installed and running.
    echo Proceeding with Docker setup...
    rem Setup the Docker container
    docker build -t exifex .

    rem Ask the user for the port (default is 8080)
    set /p "port=Please enter the port for the Docker container (default is 8080): "
    if not defined port set port=8080

    rem Validate the port
    call :CHECK_PORT %port%
    if "!isValidPort!"=="false" (
        echo Invalid port. Please enter a port number between 1 and 65535:
        set /p "port="
        call :CHECK_PORT %port%
    )

    echo Starting ExifEx container on port !port!...
    docker run -p !port!:!port! exifex
) else (
    rem Setup a local environment
    echo It appears that Docker is not installed or the Docker daemon is not running.
    echo Would you like to setup a local environment instead? (y/n)
    set /p "yn="
    if /i "!yn!"=="y" (
        echo Setting up local environment...
    ) else (
        echo Exiting...
        exit /b
    )

    rem Ask the user for the host (default is 127.0.0.1)
    set /p "host=Please enter the host for the local environment (default is 127.0.0.1): "
    if not defined host set host=127.0.0.1

    rem Ask the user for the port (default is 8080)
    set /p "port=Please enter the port for the local environment (default is 8080): "
    if not defined port set port=8080

    rem Validate the port
    call :CHECK_PORT %port%
    if "!isValidPort!"=="false" (
        echo Invalid port. Please enter a port number between 1 and 65535:
        set /p "port="
        call :CHECK_PORT %port%
    )

    rem Ask the user if they want to disable limits (default is no)
    echo Would you like to disable limits? (y/n)
    set limit=true
    set /p "yn="
    if /i "!yn!"=="y" (
        set limit=false
    )

    rem Setup python virtual environment
    python -m venv .venv
    call .venv\Scripts\activate

    rem Install dependencies
    pip install -r requirements.txt

    rem Run the app with the user's configuration
    echo Starting ExifEx on !host!:!port! with limits set to !limit!...
    if "!limit!"=="true" (
        python src\app.py -b !host! -p !port!
    ) else (
        python src\app.py -b !host! -p !port! --no-limits
    )
)

endlocal
