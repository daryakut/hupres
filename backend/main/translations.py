import gettext
import os


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
__all__ = ['_']
