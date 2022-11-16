from gettext import gettext as _
import gettext
import os
from fastapi.responses import HTMLResponse
from sqlalchemy import func

from common.env import env
from database.transaction import transaction
from main.fast_api_app import app


def set_locale(language):
    locale_path = os.path.join(os.getcwd(), 'locales')
    gettext.install('messages', localedir=locale_path, names=['ngettext'])
    lang = gettext.translation('messages', locale_path, languages=[language])
    lang.install()
    _ = lang.gettext
    return _


# Example usage
_ = set_locale('uk')  # Set to Ukrainian
print(_("ERROR: Localization is not working!"))  # If this translates well, the message would be different


@app.get("/")
async def home():
    with transaction() as session:
        current_timestamp = session.query(func.now()).scalar()
        message = _("Hello world!")
        return HTMLResponse(f"{message} {current_timestamp} {env.stage}")


@app.get("/404")
async def missing():
    return HTMLResponse(_("That's gonna be a 'no' from me."), status_code=404)
