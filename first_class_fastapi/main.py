# Commit: Import FastAPI class from fastapi module
from fastapi import FastAPI

# Commit: Initialize FastAPI application
app = FastAPI()

# Commit: Add GET endpoint at root "/"
@app.get("/")
# Commit: Define function to handle GET requests at "/"
def read_root():
    # Commit: Return simple message for GET request
    return {"message": "Hello World"}

# Commit: Add POST endpoint at root "/"
@app.post("/")
# Commit: Define function to handle POST requests at "/"
def post_items():
    # Commit: Return fixed sample item
    return {"item_id": 1, "name": "Sample Item"}

# Commit: Add PUT endpoint at root "/"
@app.put("/")
# Commit: Define function to handle PUT requests at "/"
def update_items():
    # Commit: Return fixed updated item
    return {"item_id": 1, "name": "Updated Item"}

# Commit: Add DELETE endpoint at root "/"
@app.delete("/")
# Commit: Define function to handle DELETE requests at "/"
def delete_items():
    # Commit: Return fixed deletion message
    return {"message": "Item with id 1 has been deleted"}








# # Commit: Add FastAPI import
# from fastapi import FastAPI

# # Commit: Initialize FastAPI app
# app = FastAPI()

# # Commit: Add GET root endpoint decorator
# @app.get("/")
# # Commit: Add GET root function
# def read_root():
# # Commit: Add return statement for GET root
#     return {"Hello": "World"}

# # Commit: Add POST /items/ endpoint decorator
# @app.post("/items/")
# # Commit: Add POST function header
# def create_items(item_id: int, name: str):
# # Commit: Add return statement for POST
#     return {"item_id": item_id, "name": name}

# # Commit: Add PUT /items/{item_id} endpoint decorator
# @app.put("/items/{item_id}")
# # Commit: Add PUT function header
# def update_item(item_id: int, name: str):
# # Commit: Add return statement for PUT
#     return {"item_id": item_id, "name": name}

# # Commit: Add DELETE /items/{item_id} endpoint decorator
# @app.delete("/items/{item_id}")
# # Commit: Add DELETE function header
# def delete_item(item_id: int):
# # Commit: Add return statement for DELETE
#     return {"message": f"Item with id {item_id} has been deleted"}
