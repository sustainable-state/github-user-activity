from exceptions import ArgumentExtractError

def extract_username(args: list[str]) -> str:
    if len(args) != 2:
        raise ArgumentExtractError(
            f"Error: {'github-user-activity'!r} requires "
            f"2 arguments, but {len(args)} were provided."
        )

    return args[1]