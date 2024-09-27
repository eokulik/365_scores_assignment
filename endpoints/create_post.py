from typing import Dict

from endpoints.base_api import BaseApi
from data import constants


class CreatePost(BaseApi):
    _endpoint = constants.POSTS_ENDPOINT

    def create_post(self, payload: Dict) -> None:
        self._post(self._url, payload)
