#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 Agent Marketplace - Setup Script${NC}\n"

# Backend setup
echo -e "${BLUE}Setting up Backend...${NC}"
cd backend

# Copy .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env from .env.example"
fi

# Create venv if not exists
if [ ! -d venv ]; then
    python -m venv venv
    echo "✓ Created Python virtual environment"
fi

# Activate venv and install dependencies
source venv/bin/activate
pip install -q -r requirements.txt
echo -e "${GREEN}✓ Backend dependencies installed${NC}\n"

cd ..

# Frontend setup
echo -e "${BLUE}Setting up Frontend...${NC}"
cd frontend

# Copy .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env from .env.example"
fi

# Install dependencies
npm install -q
echo -e "${GREEN}✓ Frontend dependencies installed${NC}\n"

cd ..

echo -e "${GREEN}✅ Setup Complete!${NC}\n"
echo -e "${BLUE}Next Steps:${NC}"
echo "1. Backend: cd backend && source venv/bin/activate && python main.py"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "Backend will be available at: http://localhost:8000"
echo "Frontend will be available at: http://localhost:5173"
