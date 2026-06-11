from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class AgentCreate(BaseModel):
    name: str
    description: str
    price: float = 0.0
    image_url: Optional[str] = None
    model_type: str = "ollama"
    model_name: str
    guardrails_enabled: bool = False
    guardrails_config: Optional[str] = None


class AgentUpdate(BaseModel):
    description: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    guardrails_enabled: Optional[bool] = None
    guardrails_config: Optional[str] = None


class AgentResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: Optional[str]
    rating: float
    total_reviews: int
    model_type: str
    model_name: str
    guardrails_enabled: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PurchaseResponse(BaseModel):
    id: int
    user_id: int
    agent_id: int
    api_key: str
    price_paid: float
    is_active: bool
    created_at: datetime
    expires_at: Optional[datetime]

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    rating: float
    comment: Optional[str] = None


class ReviewResponse(BaseModel):
    id: int
    agent_id: int
    user_id: int
    rating: float
    comment: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
