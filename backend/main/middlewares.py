from typing import List, Tuple, Any

from starlette.middleware.sessions import SessionMiddleware

from users.sessions import SessionDataMiddleware, SESSION_MIDDLEWARE_CONFIG

"""
All middlewares must be added here in the order of execution of the "before" phase (and rever order of "after" phase)
Format: (middleware_class, {options})
"""
middlewares: List[Tuple[Any, dict]] = [
    (SessionMiddleware, SESSION_MIDDLEWARE_CONFIG),
    (SessionDataMiddleware,)
]
