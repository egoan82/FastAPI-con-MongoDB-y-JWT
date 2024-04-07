from fastapi import FastAPI
from routes.auth_route import auth_routes
from routes.user_route import user_routes
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_routes, prefix="/auth", tags=["auth"])
app.include_router(user_routes, prefix="/user", tags=["user"])


@app.get("/")
def read_root():
    return {"Service": "FastAPI - MongoDB JWT"}