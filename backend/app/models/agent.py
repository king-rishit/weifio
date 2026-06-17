from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database.db import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    description = Column(Text)
    price = Column(Float, default=0.0)
    image_url = Column(String, nullable=True)
    rating = Column(Float, default=0.0)
    total_reviews = Column(Integer, default=0)
    creator_id = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    model_type = Column(String, default="ollama")  # ollama, huggingface, etc.
    model_name = Column(String)
    guardrails_enabled = Column(Boolean, default=False)
    guardrails_config = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Agent {self.name}>"
