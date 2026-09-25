import json

from github_api import GitHubApi
from github_parser import EventParser
from github_presenter import EventFormatter
from model import Event


class GitHubService:

    def __init__(self, username: str) -> None:
        self.username = username
        self.api = GitHubApi()
        self.parser = EventParser()
        self.formatter = EventFormatter()

    def fetch_events(self) -> list[Event]:        
        with self.api.get_user_events(self.username) as response:
            data = json.load(response)

        return self.parser.parse_events(data)

    def format_events(self, events: list[Event]) -> tuple[str, ...]:
        return self.formatter.format_events(events)
