class ArgumentExtractError(ValueError):
    ...


class InternetError(Exception):
    ...


class HttpError(InternetError):
    ...


class UrlError(InternetError):
    ...


class EventParserError(Exception):
    ...


class EventKeyError(EventParserError):
    ...


class PayloadKeyError(EventParserError):
    ...



class ActorKeyError(EventParserError):
    ...


class RepoKeyError(EventParserError):
    ...


class EventValueError(EventParserError):
    ...


class PayloadValueError(EventParserError):
    ...


class ActorValueError(EventParserError):
    ...


class RepoValueError(EventParserError):
    ...
