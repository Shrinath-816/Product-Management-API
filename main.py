
from fastapi import FastAPI , Depends
from models import Product
from database import session,engine
import database_models 
from sqlalchemy.orm import Session
app = FastAPI()

database_models.Base.metadata.create_all(bind=engine) #to create the table automatically in postgresql database
""" Why pydantic - Pydantic is a data validation and settings management library that uses Python type annotations. Just
    say that in product a price cannot be in negative and quantity cannot be negative. So we can use pydantic to validate that data before it is processed further in the application
    . It helps to ensure that the data we are working with is correct and consistent, which can prevent bugs and improve the overall reliability of the application. """
@app.get("/")
def greet():
    return "Hello, World!"
products = [Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
            Product(id=2, name="Smartphone", description="A latest model smartphone", price=499.99, quantity=20)
            ]
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():   # to initialize the database with the products data present in the products list
    db = session()
    count = db.query(database_models.Product).count() # to check if the products table is empty or not

    if count == 0:  # Only add products if the table is empty
        for product in products:
            db.add(database_models.Product(**product.model_dump())) # ** is used to unpack the attributes of the product object and pass them as keyword arguments to the Product constructor. This allows us to create a new Product instance with the same attributes as the original product object, 
            # model_dump() is a method provided by Pydantic that returns a dictionary representation of the model instance. It converts the attributes of the product object into a dictionary format, which can then be unpacked using ** to create a new Product instance in the database.
        db.commit()

init_db() # to initialize the database with the products data

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    #db = session()
    #db.query
    db_products = db.query(database_models.Product).all() # to fetch all the products from the database
    return db_products

@app.get("/products/{product_id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() # to fetch a product by id from the database
    if db_product:
        return db_product
    return {"message": "Product not found"}

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated successfully"
    return {"message": "Product not found"}

@app.delete("/products")
def delete_product(id: int , db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted successfully"
    else:
        return {"message": "Product not found"}
    

