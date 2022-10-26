from fastapi import FastAPI
from routes.auth_route import auth_routes
from routes.user_route import user_routes
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

app.include_router(auth_routes)
app.include_router(user_routes)
