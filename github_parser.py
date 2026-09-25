from model import Event, Payload, Repo, Actor
from decorators import handle_parse_errors

from exceptions import (
    EventKeyError,
    EventValueError,
    PayloadKeyError,
    PayloadValueError,
    ActorKeyError,
    ActorValueError,
    RepoKeyError,
    RepoValueError,
    EventParserError
)


class EventParser:

    def parse_events(self, data: list[dict]) -> list[Event]:
        return [self._parse_event(row) for row in data]

    @handle_parse_errors(
        EventKeyError,
        EventValueError,
        Event,
    )
    def _parse_event(self, data: dict) -> Event:
        event_type = data["type"]

        return Event(
            actor=self._parse_actor(data["actor"]),
            created_at=data["created_at"],
            id=int(data["id"]),
            payload=self._parse_payload(
                data["payload"],
                event_type,
            ),
            public=data["public"],
            repo=self._parse_repo(data["repo"]),
            event_type=event_type,
        )


    @staticmethod
    @handle_parse_errors(
        ActorKeyError,
        ActorValueError,
        Actor,
    )
    def _parse_actor(data: dict) -> Actor:
        return Actor(
            avatar_url=data["avatar_url"],
            display_login=data["display_login"],
            gravatar_id=data["gravatar_id"],
            id=int(data["id"]),
            login=data["login"],
            url=data["url"],
        )

    @handle_parse_errors(
        PayloadKeyError,
        PayloadValueError,
        Payload,
    )
    def _parse_payload(
        self,
        data: dict,
        event_type: str,
    ) -> Payload:

        payload_event_type = {
            "CreateEvent": self._payload_create_event,
            "PushEvent": self._payload_push_event,
        }

        parser = payload_event_type.get(event_type)

        if parser is None:
            raise EventParserError(f"Unsupported event type: {event_type}")

        return parser(data)


    @staticmethod
    def _payload_create_event(data: dict) -> Payload:
        return Payload(
            before=None,
            head=None,
            push_id=None,
            ref=data["ref"],
            ref_type=data["ref_type"],
            repository_id=None,
        )


    @staticmethod
    def _payload_push_event(data: dict) -> Payload:
        return Payload(
            before=data["before"],
            head=data["head"],
            push_id=int(data["push_id"]),
            ref=data["ref"],
            ref_type=None,
            repository_id=int(data["repository_id"]),
        )


    @staticmethod
    @handle_parse_errors(
        RepoKeyError,
        RepoValueError,
        Repo,
    )
    def _parse_repo(data: dict) -> Repo:
        return Repo(
            id=int(data["id"]),
            name=data["name"],
            url=data["url"],
        )