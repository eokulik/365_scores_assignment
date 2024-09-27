from typing import Dict, List

import allure
import requests
from requests import Response

DEFAULT_HEADERS = {'Content-type': 'application/json'}


class BaseApi:
    __base_url = 'https://jsonplaceholder.typicode.com/'
    _endpoint: str
    _response: Response

    def __init__(self):
        self._url = self.__base_url + self._endpoint

    def __run_request(self, method: str, *args, **kwargs) -> None:
        self._response = requests.request(method, *args, **kwargs)

    def _get(self, *args, **kwargs) -> None:
        self.__run_request('GET', *args, **kwargs)

    def _post(self, payload: Dict, headers: Dict = None, *args, **kwargs):
        headers = headers if headers else DEFAULT_HEADERS
        self.__run_request('POST', *args, json=payload, headers=headers, **kwargs)

    @allure.step('Check response status')
    def check_response_status_is_(self, code: int) -> None:
        assert self._response.status_code == code

    @property
    def response_json(self) -> List | Dict:
        return self._response.json()
