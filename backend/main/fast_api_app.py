from fastapi import FastAPI

from main.middlewares import middlewares
from main.routes import routers

app: FastAPI = FastAPI()

# Add middlewares in reverse order because the first middleware added in FastAPI is the innermost
for middleware in middlewares[::-1]:
    options = middleware[1] if len(middleware) > 1 else {}
    app.add_middleware(middleware[0], **options)

for router in routers:
    app.include_router(router[0], tags=router[1])
