from fastapi.exceptions import HTTPException


class BadRequest(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=400, detail=detail)


class Unauthorized(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=401, detail=detail)
