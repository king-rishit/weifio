# Agent Marketplace

A modern marketplace platform for buying and using AI agents with comprehensive guardrails integration.

## Features

- ✅ Agent Marketplace with browsable agent cards
- ✅ Agent ratings and reviews system
- ✅ Purchase system with API key generation
- ✅ Guardrails integration (Ollama compatible)
- ✅ User authentication (API key-based)
- ✅ Admin dashboard for agent management

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── models/       # SQLAlchemy models
│   │   ├── routes/       # FastAPI routes
│   │   ├── database/     # Database configuration
│   │   └── schemas.py    # Pydantic schemas
│   ├── main.py          # FastAPI app entry point
│   └── requirements.txt  # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/   # Vue components
    │   ├── pages/        # Page components
    │   ├── services/     # API services
    │   └── stores/       # Pinia state
    ├── package.json      # Node.js dependencies
    └── vite.config.js    # Vite configuration
```

## Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL (or SQLite for development)
- Ollama (for guardrails support)

## Backend Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your database URL and settings
   ```

3. **Run the server:**
   ```bash
   python main.py
   ```

   The API will be available at `http://localhost:8000`

4. **Access API Documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## Frontend Setup

1. **Install Node.js dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Update API URL if needed
   ```

3. **Run development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

4. **Build for production:**
   ```bash
   npm run build
   ```

## API Endpoints

### Agents
- `GET /agents` - List all agents
- `GET /agents/{id}` - Get agent details
- `POST /agents` - Create new agent (admin)
- `PUT /agents/{id}` - Update agent (admin)
- `DELETE /agents/{id}` - Delete agent (admin)

### Purchases
- `POST /purchases/{agent_id}` - Purchase agent
- `GET /purchases/my-purchases` - Get user's purchases
- `GET /purchases/verify-key/{api_key}` - Verify API key

### Reviews
- `GET /reviews/agent/{agent_id}` - Get agent reviews
- `POST /reviews/{agent_id}` - Submit review

## Guardrails Configuration

Agents can be configured with guardrails through the `guardrails_config` field. Example:

```json
{
  "name": "Safe Agent",
  "guardrails_enabled": true,
  "guardrails_config": {
    "enabled_validators": ["pii", "hate_speech", "toxicity"],
    "ollama_model": "neural-chat",
    "max_tokens": 1024
  }
}
```

## Using Agent API Key

Once purchased, authenticate with the agent using your API key:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  http://localhost:8000/purchases/verify-key/YOUR_API_KEY
```

## Development

### Mock Data

To populate the database with sample agents:

```python
# In backend/main.py or a separate script
from app.database.db import SessionLocal
from app.models.agent import Agent

db = SessionLocal()
sample_agents = [
    Agent(
        name="GPT-4 Lite",
        description="Fast and efficient language model",
        price=9.99,
        model_type="ollama",
        model_name="gpt-4",
        guardrails_enabled=True
    ),
    # Add more agents...
]
db.add_all(sample_agents)
db.commit()
```

## Troubleshooting

### Database Connection Error
- Ensure PostgreSQL is running
- Check DATABASE_URL in .env
- Run migrations if needed

### Frontend cannot connect to API
- Verify backend is running on port 8000
- Check VITE_API_URL in frontend/.env
- Check CORS configuration in main.py

### Guardrails not working
- Ensure Ollama is running locally
- Check OLLAMA_API_URL setting
- Verify model exists: `ollama list`

## Production Deployment

### Backend (with Gunicorn)
```bash
pip install gunicorn
gunicorn main:app -w 4 -b 0.0.0.0:8000
```

### Frontend (with Nginx)
```bash
npm run build
# Serve dist/ folder with Nginx
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT
