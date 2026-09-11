from dataclasses import dataclass

@dataclass
class Actor:
    avatar_url: str
    display_login: str
    gravatar_id: str
    id: int
    login: str
    url: str


@dataclass
class Payload:
    before: str
    head: str
    push_id: int
    ref: str
    repository_id: int


@dataclass
class Repo:
    id: int
    name: str
    url: str


@dataclass
class Event:
    actor: Actor
    created_at: str
    id: int
    payload: Payload
    public: bool
    repo: Repo
    event_type: str
