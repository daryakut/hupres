import os
from typing import List, Tuple, Any

from starlette.middleware.sessions import SessionMiddleware

from users.sessions import SessionDataMiddleware

"""
All middlewares must be added here in the order of execution of the "before" phase (and rever order of "after" phase)
Format: (middleware_class, {options})
"""
middlewares: List[Tuple[Any, dict]] = [
    (
        SessionMiddleware,
        {
            'secret_key': os.environ['HUPRES_SECRET_SESSION_KEY'],
            'session_cookie': 'hupres_session',
            'same_site': 'none',
        }
    ),
    (SessionDataMiddleware,)
]
