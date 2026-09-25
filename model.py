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
    before: str | None
    head: str | None
    push_id: int | None
    ref: str
    ref_type: str | None
    repository_id: int | None


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
