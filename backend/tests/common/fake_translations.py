def get_fake_gettext():
    def fake_gettext(message):
        return message

    return fake_gettext
