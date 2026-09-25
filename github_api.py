from urllib import request, error
from exceptions import (
    HttpError, 
    UrlError
)

class GitHubApi:

    BASE_URL = "https://api.github.com"

    def get_user_events(self, username: str):
        url = f"{self.BASE_URL}/users/{username}/events"

        try:
            request_data = request.Request(url)
            return request.urlopen(request_data)
        
        except error.HTTPError as api_error:
            raise HttpError(
                f"Error: GitHub API returned HTTP {api_error.code}"
            ) from api_error
         
        except error.URLError as connection_error:
            raise UrlError(
                f"Error: Unable to connect to GitHub"
            ) from connection_error