import os

from starlette.middleware.sessions import SessionMiddleware

from app import SessionDataMiddleware

"""
All middlewares must be added here in the order of execution of the "before" phase (and rever order of "after" phase)
"""
middlewares = [
    (SessionMiddleware, {'secret_key': os.environ['HUPRES_SECRET_SESSION_KEY']}),
    (SessionDataMiddleware,)
]
