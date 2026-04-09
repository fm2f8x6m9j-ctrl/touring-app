from sqlalchemy import Column, String ,Date,DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base
class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    name = Column(String(50),nullable=False)

class Routes(Base):
    __tablename__ = "routes"

    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    name = Column(String(100),nullable=False)
    start_point =  Column(String(100),nullable=False)
    end_point =  Column(String(100),nullable=False)
    date = Column(Date)
    memo = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
class Spots(Base):
    __tablename__ = "spots"
    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    route_id = Column(UUID(as_uuid=True), ForeignKey("routes.id"))
    classategorytegory_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))
    name = Column(String(100),nullable=False)
    memo = Column(Text)
    created_at = Column(DateTime)
