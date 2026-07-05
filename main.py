from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"]
)
# Create tables
database_models.Base.metadata.create_all(bind=engine)

# Initial data for seeding
products = [
    Product(
        id=1,
        name="phone",
        description="budget phone",
        price=99,
        quantity=8,
    ),
    Product(
        id=2,
        name="laptop",
        description="budget laptop",
        price=999,
        quantity=1,
    ),
    Product(
        id=3,
        name="mic",
        description="budget mic",
        price=599,
        quantity=5,
    ),
    Product(
        id=4,
        name="speaker",
        description="budget speaker",
        price=1999,
        quantity=12,
    ),
]


# Database Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# Seed database if empty
def init_db():
    db = session()

    try:
        count = db.query(database_models.Product).count()

        if count == 0:
            for product in products:
                db.add(
                    database_models.Product(
                        **product.model_dump()
                    )
                )

            db.commit()

    finally:
        db.close()


init_db()


@app.get("/")
def greet():
    return "Welcome to our own hosting env"


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


@app.get("/products/{id}")
def get_product_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )

    if not db_product:
        return {"message": "Product not found"}

    return db_product


@app.post("/products")
def add_product(product: Product,db: Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@app.put("/products/{id}")
def update_product(
    id: int,
    product: Product,
    db: Session = Depends(get_db)
):
    db_product = (db.query(database_models.Product).filter(database_models.Product.id == id).first())
    if not db_product:
        return {"message": "Product not found"}

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)

    return db_product


@app.delete("/products/{id}")
def delete_product(id: int,db: Session = Depends(get_db)):
    db_product = (db.query(database_models.Product).filter(database_models.Product.id == id).first())
    if not db_product:
        return {"message": "Product not found"}

    db.delete(db_product)
    db.commit()

    return {"message": "Product deleted successfully"}