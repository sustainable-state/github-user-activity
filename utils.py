from exceptions import ArgumentExtractError

def extract_username(args: list[str, str]) -> str:
    try:
        _, username = args
        return username
    except ValueError:
        raise ArgumentExtractError(
            f"Error: {"github-user-activity"!r} requires "
            f"2 arguments, but {len(args)} were provided."
        ) from ValueError