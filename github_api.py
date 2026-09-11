from urllib import request
    

class GitHubApi:

    BASE_URL = "https://api.github.com"

    def get_user_events(self, username: str):
        url = f"{self.BASE_URL}/users/{username}/events"
        request_data = request.Request(url)

        return request.urlopen(request_data)