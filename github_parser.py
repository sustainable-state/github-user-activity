from model import Event, Payload, Repo, Actor

class EventParser:

    def parse_events(self, data: list[dict]) -> list[Event]:
        return [self._parse_event(row) for row in data]


    @staticmethod
    def _parse_event(data: dict) -> Event:
        return Event(
            actor=EventParser._parse_actor(data["actor"]),
            created_at=data["created_at"],
            id=int(data["id"]),
            payload=EventParser._parse_payload(data["payload"]),
            public=data["public"],
            repo=EventParser._parse_repo(data["repo"]),
            event_type=data["type"],
        )


    @staticmethod
    def _parse_actor(data: dict) -> Actor:
        return Actor(
            avatar_url=data["avatar_url"],
            display_login=data["display_login"],
            gravatar_id=data["gravatar_id"],
            id=int(data["id"]),
            login=data["login"],
            url=data["url"],
        )


    @staticmethod
    def _parse_payload(data: dict) -> Payload:
        return Payload(
            before=data["before"],
            head=data["head"],
            push_id=int(data["push_id"]),
            ref=data["ref"],
            repository_id=int(data["repository_id"]),
        )


    @staticmethod
    def _parse_repo(data: dict) -> Repo:
        return Repo(
            id=int(data["id"]),
            name=data["name"],
            url=data["url"],
        )



