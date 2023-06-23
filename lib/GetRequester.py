import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content.decode('utf-8')  # Decode response content to string

    def load_json(self):
        response_body = self.get_response_body()
        json_data = json.loads(response_body)
        return json_data
url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
requester = GetRequester(url)
response_body = requester.get_response_body()
json_data = requester.load_json()
print(json_data)

