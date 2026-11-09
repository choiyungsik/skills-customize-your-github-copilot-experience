from fastapi import FastAPI

app = FastAPI(title="Student API")

# Example in-memory data store
items = [
    {"id": 1, "name": "Example Item"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"message": "Item not found"}
