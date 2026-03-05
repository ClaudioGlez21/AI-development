from fastapi import FastAPI

app = FastAPI()

items = [
    {"id":1, "name":"Item 1"},
    {"id":2, "name":"Claudio"},
    {"id":3, "name":"Item 3"}
]

#Each decorator is an extension of the app object, and the path is the URL path that will trigger the function below it.
#Creation of a GET endpoint at the path "/health". When a client sends a GET request to this path, the function below will be executed.
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}") #the curly braces with the id represents a path param
def read_item_id(item_id:int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items")
def add_items(item:dict):
    items.append(item)
    return item
