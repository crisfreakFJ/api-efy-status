import requests
import json
from dependencies.settings import Settings

settings = Settings()

class ResultsService:

    def get_results_from_survey(self, id):
        endpoint = f"http://api.surveymonkey.com/v3/surveys/{id}/rollups"
        headers = {
            'Accept': "application/json",
            'Authorization': f"Bearer {settings.api_key}"
        }
        response_api = requests.get(url=endpoint, headers=headers)
        text_response = response_api.text
        dict_response = json.loads(text_response)
        count = dict_response['data'][22]['summary'][0]['answered']
        return count