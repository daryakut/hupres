from typing import Tuple, List

from fastapi import APIRouter

import quizzes.quizzes_api
import users.users_api

"""
All routers must be added here
We don't prefix routers with their respective tags because it makes it easier to search full paths in the code
Format: (router, [tags])
"""
routers: List[Tuple[APIRouter, list[str]]] = [
    (users.users_api.router, ["users"]),
    (quizzes.quizzes_api.router, ["quizzes"]),
]
