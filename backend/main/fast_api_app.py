from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from main.middlewares import middlewares
from main.routes import routers

app: FastAPI = FastAPI()

# Add middlewares in reverse order because the first middleware added in FastAPI is the innermost
for middleware in middlewares[::-1]:
    options = middleware[1] if len(middleware) > 1 else {}
    app.add_middleware(middleware[0], **options)

for router in routers:
    app.include_router(router[0], tags=router[1])

# Set up CORS middleware options
origins = [
    "https://hupres-web.onrender.com",  # The origin of the frontend application
    "http://localhost:3000",  # The origin of the frontend application
    "http://127.0.0.1:3000",  # Also include this if we're using 127.0.0.1 to access the frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
