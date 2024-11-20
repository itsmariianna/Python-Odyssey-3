from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Users(BaseModel):
    id : int
    name : str

class Products(BaseModel):
    id : int
    name : str
    price : int

class CreateUser(BaseModel):
    name : str

class CreateProduct(BaseModel):
    name : str
    price : int


users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]


@app.get("/")
def homepage():
    return "Here you can add users and products"

# Users

# Return a list of all users.
@app.get("/users")
def showing_users() -> List[Users]:
    return [Users(**user) for user in users]

# Adding new user
@app.post("/users/add")
def adding_user(user: CreateUser):
    new_user_id = len(users) + 1
    new_user = {"id" : new_user_id, "name" : user.name}
    users.append(new_user)
    return new_user

# Return a single user by their ID.
@app.get("/users/{id}")
def get_user_with_id(id : int) -> List[Users]:
    for user in users:
        if user['id'] == id:
            return [Users(**user)]
    raise HTTPException(status_code=404, detail="Only user with id 2 is available")


# Update an existing user by ID
@app.put("/users/{user_id}")
def updating_user(user_id: int, updated_user: CreateUser):
    user = next((u for u in users if u["id"] == user_id), None)
    user["name"] = updated_user.name
    return user


# Delete a user by ID
@app.delete("/users/{user_id}")
def deleting_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    users.remove(user)
    return {"message": f"User with ID {user_id} deleted"}


# Products

# Return a list of all products.
@app.get("/products")
def showing_products() -> List[Products]:
    return [Products(**product) for product in products]

# Adding new user
@app.post("/products/add")
def adding_products(product : CreateProduct):
    new_id = len(products) + 1
    new_product = {'id' : new_id, 'name' : product.name, 'price' : product.price}
    products.append(new_product)


# Return a single product by their ID.
@app.get("/products/{id}")
def get_product_with_id(id: int) -> List[Products]:
    for product in products:
        if product['id'] == id:
            return [Products(**product)]
    raise HTTPException(status_code=404, detail='Product not found')



# Update an existing priduct by ID
@app.put("/product/{product_id}")
def updating_user(product_id: int, updated_product: CreateProduct):
    product = next((p for p in products if p["id"] == product_id), None)
    product["name"] = updated_product.name
    product['price'] = updated_product.price
    return product


# Delete a product by ID
@app.delete("/product/{product_id}")
def deleting_product(product_id: int):
    product = next((p for p in users if p["id"] == product_id), None)
    products.remove(product)
    return {"message": f"User with ID {product_id} deleted"}
