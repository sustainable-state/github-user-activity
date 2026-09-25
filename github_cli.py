from utils import extract_username
from github_service import GitHubService
from exceptions import (
    ArgumentExtractError, 
    EventParserError, 
    InternetError
)


class CLI:

    def run(self, args: list[str]) -> None:
        try:
            username = extract_username(args)

            service = GitHubService(username)
            events = service.fetch_events()

            if not events:
                print(f"No data about {username!r}")
                return

            formatted_events = service.format_events(events)
            print(*formatted_events, sep="\n")

        except ArgumentExtractError as error:
            print(error)

        except EventParserError as error:
            print(error)

        except InternetError as error:
            print(error)
        