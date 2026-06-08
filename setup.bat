@echo off
REM Colors setup (using echo for Windows)
REM Windows batch limited in colors, using basic output

echo.
echo 🤖 Agent Marketplace - Setup Script (Windows)
echo.

REM Backend setup
echo Setting up Backend...
cd backend

REM Copy .env if not exists
if not exist .env (
    copy .env.example .env
    echo + Created .env from .env.example
)

REM Create venv if not exists
if not exist venv (
    python -m venv venv
    echo + Created Python virtual environment
)

REM Activate venv and install dependencies
call venv\Scripts\activate.bat
pip install -q -r requirements.txt
echo + Backend dependencies installed

cd ..

REM Frontend setup
echo.
echo Setting up Frontend...
cd frontend

REM Copy .env if not exists
if not exist .env (
    copy .env.example .env
    echo + Created .env from .env.example
)

REM Install dependencies
call npm install -q
echo + Frontend dependencies installed

cd ..

echo.
echo Setup Complete!
echo.
echo Next Steps:
echo 1. Backend: cd backend ^&^& venv\Scripts\activate.bat ^&^& python main.py
echo 2. Frontend: cd frontend ^&^& npm run dev
echo.
echo Backend will be available at: http://localhost:8000
echo Frontend will be available at: http://localhost:5173
