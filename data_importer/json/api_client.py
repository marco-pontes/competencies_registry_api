from logging import info

import requests
from requests.adapters import Retry, HTTPAdapter
import json


class ApiClient:

    def get(self, resource_url):
        info('Requesting URL: {url}'.format(url=resource_url.complete_url))
        session = requests.Session()
        retries = Retry(total=10, backoff_factor=1, status_forcelist=[502, 503, 504, 403])
        session.mount('https://', HTTPAdapter(max_retries=retries))

        api_response = session.get(resource_url.complete_url)
        #api_response = requests.get(resource_url.complete_url)
        resource_data = api_response.text
        data_as_json = json.loads(resource_data)
        info('Finished requesting resource')
        return data_as_json
