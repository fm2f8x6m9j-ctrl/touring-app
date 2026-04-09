from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, Category, Routes, Spots
from schemas import CategoryCreate, CategoryResponse, RouteCreate, RouteResponse, SpotCreate, SpotResponse
from uuid import UUID

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "ツーリングアプリAPI起動中"}

@app.post("/categories",response_model = CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(name = category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@app.get("/categories",response_model = list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@app.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category(category_id: UUID, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category

@app.delete("/categories/{category_id}")
def delete_category(category_id: UUID, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    db.delete(db_category)
    db.commit()
    return {"message": "削除しました"}

@app.post("/routes", response_model= RouteResponse)
def create_route(route: RouteCreate, db: Session = Depends(get_db)):
    new_route = Routes(
        name=route.name,
        start_point=route.start_point,
        end_point=route.end_point,
        date=route.date,
        memo=route.memo
    )
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route

@app.get("/routes", response_model=list[RouteResponse])
def get_routes(db: Session = Depends(get_db)):
    return db.query(Routes).all()

@app.put("/routes/{route_id}", response_model=RouteResponse)
def update_route(route_id: UUID, route: RouteCreate, db: Session = Depends(get_db)):
    db_route = db.query(Routes).filter(Routes.id == route_id).first()
    db_route.name = route.name
    db_route.start_point = route.start_point
    db_route.end_point = route.end_point
    db_route.date = route.date
    db_route.memo = route.memo
    db.commit()
    db.refresh(db_route)
    return db_route

@app.delete("/routes/{route_id}")
def delete_route(route_id: UUID, db: Session = Depends(get_db)):
    db_route = db.query(Routes).filter(Routes.id == route_id).first()
    db.delete(db_route)
    db.commit()
    return {"message": "削除しました"}

@app.post("/spots", response_model=SpotResponse)
def create_spot(spot: SpotCreate, db: Session = Depends(get_db)):
    new_spot = Spots(
        route_id=spot.route_id,
        category_id=spot.category_id,
        name=spot.name,
        memo=spot.memo
    )
    db.add(new_spot)
    db.commit()
    db.refresh(new_spot)
    return new_spot

@app.get("/spots", response_model=list[SpotResponse])
def get_spots(db: Session = Depends(get_db)):
    return db.query(Spots).all()

@app.put("/spots/{spot_id}", response_model=SpotResponse)
def update_spot(spot_id: UUID, spot: SpotCreate, db: Session =
    Depends(get_db)):
        db_spot = db.query(Spots).filter(Spots.id == spot_id).first()
        db_spot.route_id = spot.route_id
        db_spot.category_id = spot.category_id
        db_spot.name = spot.name
        db_spot.memo = spot.memo
        db.commit()
        db.refresh(db_spot)
        return db_spot

@app.delete("/spots/{spot_id}")
def delete_spot(spot_id: UUID, db: Session = Depends(get_db)):
    db_spot = db.query(Spots).filter(Spots.id == spot_id).first()
    db.delete(db_spot)
    db.commit()
    return {"message": "削除しました"}
