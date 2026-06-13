"""
Sample script to seed the database with sample agents
Usage: python seed.py
"""

import sys
sys.path.insert(0, 'backend')

from app.database.db import SessionLocal, engine, Base
from app.models.agent import Agent
from app.models.review import Review
import json

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Sample agent data
sample_agents = [
    {
        "name": "GPT-4 Lite",
        "description": "Fast and efficient language model based on OpenAI's GPT-4. Perfect for general-purpose tasks.",
        "price": 9.99,
        "image_url": "https://via.placeholder.com/300x200/4F46E5/FFFFFF?text=GPT-4+Lite",
        "rating": 4.8,
        "total_reviews": 24,
        "model_type": "ollama",
        "model_name": "gpt-4",
        "guardrails_enabled": True,
        "guardrails_config": json.dumps({
            "validators": ["pii", "toxicity"],
            "max_tokens": 2048
        })
    },
    {
        "name": "Claude 3 Sonnet",
        "description": "Anthropic's Claude 3 model with advanced reasoning capabilities and cost efficiency.",
        "price": 14.99,
        "image_url": "https://via.placeholder.com/300x200/EC4899/FFFFFF?text=Claude+3",
        "rating": 4.9,
        "total_reviews": 18,
        "model_type": "ollama",
        "model_name": "claude-3-sonnet",
        "guardrails_enabled": True,
        "guardrails_config": json.dumps({
            "validators": ["pii", "toxicity", "hate_speech"],
            "max_tokens": 4096
        })
    },
    {
        "name": "Llama 2 Chat",
        "description": "Meta's open-source Llama 2 model, fine-tuned for conversational use.",
        "price": 4.99,
        "image_url": "https://via.placeholder.com/300x200/F59E0B/FFFFFF?text=Llama+2",
        "rating": 4.3,
        "total_reviews": 42,
        "model_type": "ollama",
        "model_name": "llama2:7b-chat",
        "guardrails_enabled": False,
        "guardrails_config": None
    },
    {
        "name": "Mixtral 8x7B",
        "description": "Mixture of Experts model with superior performance for complex reasoning tasks.",
        "price": 7.99,
        "image_url": "https://via.placeholder.com/300x200/10B981/FFFFFF?text=Mixtral",
        "rating": 4.6,
        "total_reviews": 31,
        "model_type": "ollama",
        "model_name": "mixtral:8x7b",
        "guardrails_enabled": True,
        "guardrails_config": json.dumps({
            "validators": ["pii"],
            "max_tokens": 8192
        })
    },
    {
        "name": "Neural Chat",
        "description": "Specialized model for multi-turn conversations with context awareness.",
        "price": 0.0,  # Free model
        "image_url": "https://via.placeholder.com/300x200/8B5CF6/FFFFFF?text=Neural+Chat",
        "rating": 4.2,
        "total_reviews": 15,
        "model_type": "ollama",
        "model_name": "neural-chat",
        "guardrails_enabled": False,
        "guardrails_config": None
    },
    {
        "name": "Code Llama",
        "description": "Specialized model for code generation and programming tasks.",
        "price": 6.99,
        "image_url": "https://via.placeholder.com/300x200/06B6D4/FFFFFF?text=Code+Llama",
        "rating": 4.7,
        "total_reviews": 28,
        "model_type": "ollama",
        "model_name": "codellama:7b",
        "guardrails_enabled": True,
        "guardrails_config": json.dumps({
            "validators": ["code_injection"],
            "max_tokens": 4096
        })
    }
]

# Clear existing agents
db.query(Agent).delete()
print("Cleared existing agents")

# Add sample agents
for agent_data in sample_agents:
    agent = Agent(**agent_data, is_active=True)
    db.add(agent)
    print(f"Added agent: {agent.name}")

db.commit()
print(f"\n✅ Successfully seeded {len(sample_agents)} agents!")
print("\nSample agents created:")
for agent in db.query(Agent).all():
    print(f"  - {agent.name} (${agent.price})")

db.close()
