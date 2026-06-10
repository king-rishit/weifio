from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.purchase import Purchase
from app.models.agent import Agent
from app.schemas import PurchaseResponse
import uuid
import secrets

router = APIRouter(prefix="/purchases", tags=["purchases"])


def generate_api_key():
    """Generate a unique API key"""
    return f"ak_{secrets.token_hex(16)}"


@router.get("/my-purchases", response_model=list[PurchaseResponse])
def get_user_purchases(user_id: int, db: Session = Depends(get_db)):
    """Get all purchases for the current user"""
    purchases = db.query(Purchase).filter(
        Purchase.user_id == user_id,
        Purchase.is_active == True
    ).all()
    return purchases


@router.post("/{agent_id}", response_model=PurchaseResponse)
def purchase_agent(agent_id: int, user_id: int, db: Session = Depends(get_db)):
    """Purchase an agent and get an API key"""
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    # Check if user already has access
    existing = db.query(Purchase).filter(
        Purchase.user_id == user_id,
        Purchase.agent_id == agent_id,
        Purchase.is_active == True
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="You already own this agent")
    
    # Create purchase with API key
    api_key = generate_api_key()
    purchase = Purchase(
        user_id=user_id,
        agent_id=agent_id,
        api_key=api_key,
        price_paid=agent.price
    )
    db.add(purchase)
    db.commit()
    db.refresh(purchase)
    return purchase


@router.get("/verify-key/{api_key}")
def verify_api_key(api_key: str, db: Session = Depends(get_db)):
    """Verify if an API key is valid and return agent info"""
    purchase = db.query(Purchase).filter(
        Purchase.api_key == api_key,
        Purchase.is_active == True
    ).first()
    
    if not purchase:
        raise HTTPException(status_code=401, detail="Invalid or inactive API key")
    
    agent = db.query(Agent).filter(Agent.id == purchase.agent_id).first()
    return {
        "valid": True,
        "agent_id": agent.id,
        "agent_name": agent.name,
        "model_name": agent.model_name,
        "guardrails_enabled": agent.guardrails_enabled,
        "guardrails_config": agent.guardrails_config
    }
