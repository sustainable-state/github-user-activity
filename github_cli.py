from utils import extract_username
from github_service import GitHubService
from exceptions import ArgumentExtractError, EventParserError
from pprint import pprint

class CLI:

    def run(self, args: list[str]) -> None:
        try:
            username = extract_username(args)
            service = GitHubService(username)
            data = service.fetch_events()
            pprint(data)

        except ArgumentExtractError as error:
            print(error)
        
        except EventParserError as error:
            print(error)