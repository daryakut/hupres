def require_not_none(nullable_variable, message):
    if nullable_variable is None:
        raise ValueError(message)


def require(predicate, message):
    if predicate():
        raise ValueError(message)


def TODO():
    raise NotImplementedError("TODO")
