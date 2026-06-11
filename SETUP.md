# Setup Instructions

## Quick Start

### Option 1: Run Everything Locally

#### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend runs on: `http://localhost:8000`

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend runs on: `http://localhost:5173`

### Option 2: Using Docker

```bash
# Build images
docker-compose build

# Start services
docker-compose up
```

## Initial Setup

1. **Backend Database**
   - Create `.env` from `.env.example`
   - Update DATABASE_URL
   - Models auto-create on first run

2. **Frontend**
   - Create `.env` from `.env.example`
   - Update VITE_API_URL if needed
   - Install dependencies: `npm install`

3. **Sample Data**
   - Use the API documentation at `/docs` to create agents
   - Or use the provided seed script

## Testing the Marketplace

1. Open `http://localhost:5173` in browser
2. Browse agents on marketplace page
3. Click "Buy" on any agent
4. Receive API key for that agent
5. Go to "My Purchases" to see your API keys
6. Read Documentation for API usage

## API Key Usage

```bash
# Verify your API key
curl http://localhost:8000/purchases/verify-key/YOUR_API_KEY

# Use in requests
curl -H "Authorization: Bearer YOUR_API_KEY" \
  http://localhost:8000/your-endpoint
```

## Guardrails Integration

Agents with guardrails validate outputs before returning them. Configuration example:

```json
{
  "guardrails_enabled": true,
  "guardrails_config": "{\"validators\": [\"pii\", \"toxicity\"]}"
}
```

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost/agent_marketplace
SECRET_KEY=your-secret-key
ALGORITHM=HS256
OLLAMA_API_URL=http://localhost:11434
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000
```

## Troubleshooting

**"Cannot connect to backend"**
→ Ensure backend is running on port 8000

**"Database error"**
→ Check DATABASE_URL and PostgreSQL is running

**"No agents showing"**
→ Create agents via API: `POST /agents`

**"Guardrails not working"**
→ Ensure Ollama is installed and running
