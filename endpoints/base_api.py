import os
import logging
from typing import Dict, List
from abc import abstractmethod

import allure
import requests
import dotenv
from requests import Response
from requests.exceptions import ConnectionError, JSONDecodeError

from data import constants

logging.getLogger(__name__)
dotenv.load_dotenv(override=True)


class BaseApi:
    __base_url = os.getenv('BASE_URL')
    _endpoint: str
    _response: Response

    def __init__(self):
        self._url = self.__base_url + self._endpoint

    def __run_request(self, method: str, url: str,  *args, **kwargs) -> None:
        try:
            self._response = requests.request(method, url, *args, **kwargs)
            logging.info(
                'Request run: url %s, method %s, %s, %s, response status: %s',
                url, method, args, kwargs, self._response.status_code
            )
        except ConnectionError as err:
            logging.exception(
                'Failed to execute request: url %s, method %s, %s, %s ', url, method, args, kwargs
            )
            raise err

    def _get(self, url: str, *args, **kwargs) -> None:
        self.__run_request('GET', url, *args, **kwargs)

    def _post(self, url: str, payload: Dict, headers: Dict = None, *args, **kwargs):
        headers = headers if headers else constants.DEFAULT_HEADERS
        self.__run_request('POST', url, *args, json=payload, headers=headers, **kwargs)

    @allure.step('Check response status')
    def check_response_status_is_(self, code: int) -> None:
        try:
            assert self._response.status_code == code, \
                f'Actual status code ({self._response.status_code}) doesn\'t match the expected one ({code})'
            logging.info('Status code %s matches the expected one %s', self._response.status_code, code)
        except AssertionError as err:
            logging.error(
                f'Actual status code (%s) doesn\'t match the expected one (%s)',
                self._response.status_code, code
            )
            raise err

    @property
    def response_json(self) -> List | Dict:
        try:
            data = self._response.json()
            logging.info('Received data: %s', data)
            return data
        except JSONDecodeError as err:
            logging.exception('Failed to decode JSON from the response: %s', self._response.text)
            raise err

    @abstractmethod
    def data(self) -> object | List[object]:
        pass
