import json

from github_api import GitHubApi
from github_parser import EventParser
from model import Event



class GitHubService:
    def __init__(self, username: str) -> None:
        self.username = username
        self.parser = EventParser()
        self.api = GitHubApi()

    
    def fetch_events(self) -> list[Event]:
        response = self.api.get_user_events(self.username)
        data = json.load(response)
        
        return self.parser.parse_events(data)
