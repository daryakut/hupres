from fastapi.responses import HTMLResponse
from sqlalchemy import func

from database.transaction import transaction
from main.fast_api_app import app


@app.get("/")
async def home():
    with transaction() as session:
        current_timestamp = session.query(func.now()).scalar()
        return HTMLResponse(f"Hello world! {current_timestamp}")


@app.get("/404")
async def missing():
    return HTMLResponse("That's gonna be a 'no' from me.", status_code=404)
