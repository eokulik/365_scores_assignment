import logging
from typing import Dict

from endpoints.base_api import BaseApi
from data import constants

logging.getLogger(__name__)


class CreatePost(BaseApi):
    _endpoint = constants.POSTS_ENDPOINT

    def create_post(self, payload: Dict) -> None:
        self._post(self._url, payload)
        logging.info('Post created with payload %s', payload)

