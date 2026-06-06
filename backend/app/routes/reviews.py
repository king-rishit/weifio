from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.review import Review
from app.models.agent import Agent
from app.schemas import ReviewCreate, ReviewResponse
from typing import List
import statistics

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.get("/agent/{agent_id}", response_model=List[ReviewResponse])
def get_agent_reviews(agent_id: int, db: Session = Depends(get_db)):
    """Get all reviews for an agent"""
    reviews = db.query(Review).filter(Review.agent_id == agent_id).all()
    return reviews


@router.post("/{agent_id}", response_model=ReviewResponse)
def create_review(agent_id: int, review: ReviewCreate, user_id: int, db: Session = Depends(get_db)):
    """Create a new review for an agent"""
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    # Check if user already reviewed this agent
    existing = db.query(Review).filter(
        Review.agent_id == agent_id,
        Review.user_id == user_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="You already reviewed this agent")
    
    db_review = Review(
        agent_id=agent_id,
        user_id=user_id,
        **review.dict()
    )
    db.add(db_review)
    
    # Update agent rating
    agent.total_reviews += 1
    all_reviews = db.query(Review).filter(Review.agent_id == agent_id).all()
    ratings = [r.rating for r in all_reviews] + [review.rating]
    agent.rating = statistics.mean(ratings)
    
    db.commit()
    db.refresh(db_review)
    return db_review
