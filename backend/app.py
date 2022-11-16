from main.translations import _
from fastapi.responses import HTMLResponse
from sqlalchemy import func

from common.env import env
from database.transaction import transaction
from main.fast_api_app import app

@app.get("/")
async def home():
    with transaction() as session:
        current_timestamp = session.query(func.now()).scalar()
        message = _("Hello world!")
        return HTMLResponse(f"{message} {current_timestamp} {env.stage}")


@app.get("/404")
async def missing():
    return HTMLResponse(_("That's gonna be a 'no' from me."), status_code=404)
