from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime
from typing import Optional

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: UUID
    name: str

class RouteCreate(BaseModel):
    name: str
    start_point: str
    end_point: str
    date: Optional[date] = None
    memo: Optional[str] = None

class RouteResponse(BaseModel):
    id: UUID
    name: str
    start_point: str
    end_point: str
    date: Optional[date] = None
    memo: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SpotCreate(BaseModel):
    route_id: UUID
    category_id: UUID
    name: str
    memo: Optional[str] = None

class SpotResponse(BaseModel):
    id: UUID
    route_id: UUID
    category_id: UUID
    name: str
    memo: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

