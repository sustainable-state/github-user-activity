from functools import wraps
from typing import Callable


def handle_parse_errors(
    key_exception: type[Exception],
    value_exception: type[Exception],
    model_class: type,
):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except KeyError as error:
                missing_key = error.args[0]

                raise key_exception(
                    f"{model_class.__name__}: "
                    f"missing required field {missing_key!r}"
                ) from error

            except ValueError as error:
                raise value_exception(
                    f"{model_class.__name__}: "
                    f"invalid value: {error}"
                ) from error

        return wrapper
    return decorator