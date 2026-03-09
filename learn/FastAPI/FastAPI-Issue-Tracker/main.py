from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.middleware("http")(timing_middleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(issues_router)


#Each decorator is an extension of the app object, and the path is the URL path that will trigger the function below it.
#Creation of a GET endpoint at the path "/health". When a client sends a GET request to this path, the function below will be executed.
@app.get("/health")
def health_check():
    return {"status": "ok"}
