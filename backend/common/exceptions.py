from fastapi.exceptions import HTTPException


class BadRequest(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=400, detail=detail)
