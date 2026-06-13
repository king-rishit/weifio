# Agent Marketplace - Quick Start Guide

## 🚀 Getting Started (5 minutes)

### Option 1: Windows Quick Start

```bash
# Run setup script
setup.bat

# Then in two different terminals:

# Terminal 1 - Backend
cd backend
venv\Scripts\activate.bat
python main.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### Option 2: Linux/Mac Quick Start

```bash
# Run setup script
bash setup.sh

# Then in two different terminals:

# Terminal 1 - Backend
cd backend
source venv/bin/activate
python main.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### Option 3: Docker

```bash
docker-compose up
```

---

## 📝 What You Get

### ✨ Features Included

1. **Marketplace Frontend**
   - Browse agents with search & filters
   - View agent details and reviews
   - See ratings and pricing
   - Responsive design

2. **Backend API**
   - FastAPI with automatic documentation
   - Agent CRUD operations
   - Purchase system with API keys
   - Review management
   - Guardrails configuration

3. **Database**
   - Agent profiles with metadata
   - User purchases and API keys
   - Review system with ratings
   - Guardrails configuration storage

4. **Integration**
   - Ollama guardrails support
   - API key verification
   - Mock payment system
   - PostgreSQL support

---

## 🔑 API Key Workflow

1. **Browse Marketplace**
   - Open http://localhost:5173
   - See available agents

2. **Purchase Agent**
   - Click "Buy" on any agent
   - Get instant API key

3. **View API Key**
   - Go to "My Purchases"
   - Copy your API key

4. **Use Agent**
   - Include key in requests
   - Access agent features

---

## 📚 API Documentation

Auto-generated docs available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🎯 Next Steps

1. **Seed Sample Data**
   ```bash
   python seed.py
   ```

2. **Visit Frontend**
   - http://localhost:5173

3. **Try API**
   - GET /agents - List all agents
   - POST /purchases/{id} - Buy agent

4. **Read Docs in App**
   - Click "Documentation" tab in frontend

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Backend won't start | Install deps: `pip install -r requirements.txt` |
| Frontend won't start | Install deps: `npm install` |
| Can't connect to API | Check backend on port 8000 |
| Database error | Update DATABASE_URL in .env |
| No agents showing | Run `python seed.py` |

---

## 📁 File Structure

```
agent aloo/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── models/         # Database models
│   │   ├── routes/         # API endpoints
│   │   ├── database/       # DB config
│   │   └── schemas.py      # Data schemas
│   ├── main.py             # Entry point
│   └── requirements.txt    # Dependencies
│
├── frontend/               # Vue.js frontend
│   ├── src/
│   │   ├── components/     # Vue components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API client
│   │   └── stores/         # Pinia state
│   ├── vite.config.js      # Build config
│   └── package.json        # NPM deps
│
├── docker-compose.yml      # Docker setup
├── seed.py                 # Sample data
├── README.md               # Full docs
└── SETUP.md                # Setup guide
```

---

## 💡 Pro Tips

1. **Development**
   - Both frontend and backend support hot reload
   - API auto-reloads when you edit routes
   - Frontend recompiles when you change components

2. **Database**
   - First run auto-creates tables
   - Use `seed.py` to populate sample agents
   - SQLite works for development, PostgreSQL for production

3. **Guardrails**
   - Set `guardrails_enabled: true` when creating agents
   - Add validator config in `guardrails_config` field
   - Integrate with Ollama for actual validation

4. **API Keys**
   - Unique per purchase
   - Can be used immediately after purchase
   - Include in Authorization header when using agent

---

## 🎨 Customization

### Add New Agent Field
1. Add column to `Agent` model in `backend/app/models/agent.py`
2. Update schema in `backend/app/schemas.py`
3. Update API routes in `backend/app/routes/agents.py`
4. Update frontend API call in `frontend/src/services/api.js`

### Change Pricing Model
- Currently uses fixed price in database
- Add `discount` or `subscription_tier` fields to customize
- Update purchase logic in `backend/app/routes/purchases.py`

### Add Payment Integration
- Currently uses mock purchase system
- Integrate Stripe, PayPal, or other payment provider
- Store payment transaction ID with purchase record

---

## 📞 Support

### For API Issues
- Check `/docs` endpoint for interactive API docs
- Check `main.py` for route definitions
- Use browser DevTools to debug API calls

### For Frontend Issues
- Check browser console for errors
- Verify API is running on port 8000
- Check `.env` file has correct API URL

### For Database Issues
- Verify PostgreSQL is running
- Check `DATABASE_URL` in `.env`
- Try with SQLite for quick testing

---

## 🎓 Learning Resources

- FastAPI docs: https://fastapi.tiangolo.com/
- Vue.js docs: https://vuejs.org/
- Pinia (state management): https://pinia.vuejs.org/
- SQLAlchemy (ORM): https://www.sqlalchemy.org/

---

Happy coding! 🚀
