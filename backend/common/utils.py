def check_not_none(nullable_variable, message):
    if nullable_variable is None:
        raise ValueError(message)


def check_not_empty(emptyable_variable, message):
    if not emptyable_variable:
        raise ValueError(message)


def check(predicate, message):
    if not predicate():
        raise ValueError(message)


def TODO():
    raise NotImplementedError("TODO")


def first_or_none(collection):
    return next(iter(collection), None)
