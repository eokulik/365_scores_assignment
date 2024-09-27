from typing import Dict

from endpoints.base_api import BaseApi


class CreatePost(BaseApi):
    _endpoint = '/posts'

    def create_post(self, payload: Dict) -> None:
        self._post(self._url, payload)
