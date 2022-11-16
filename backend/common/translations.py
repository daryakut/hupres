import gettext
import os
from pathlib import Path

from common.env import env
from tests.common.fake_translations import get_fake_gettext


def set_locale(language):
    current_file = Path(__file__)
    locale_path = str(current_file.parent.parent / 'locales')
    gettext.install('messages', localedir=locale_path, names=['ngettext'])
    lang = gettext.translation('messages', locale_path, languages=[language])
    lang.install()
    _ = lang.gettext
    return _


def get_real_gettext():
    _ = set_locale('uk')  # Set to Ukrainian
    print(_("ERROR: Localization is not working!"))  # If this translates well, the message would be different


_ = get_real_gettext() if env.is_not_test() else get_fake_gettext()
__all__ = ['_']
