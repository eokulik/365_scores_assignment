import logging
from typing import Dict, List

from endpoints.base_api import BaseApi
from endpoints.models.post import Post
from data import constants

logging.getLogger(__name__)


class CreatePost(BaseApi):
    _endpoint = constants.POSTS_ENDPOINT

    def create_post(self, payload: Dict) -> None:
        self._post(self._url, payload)
        logging.info('Post created with payload %s', payload)

    def data(self) -> Post:
        return Post(**self.response_json)

    def check_post_content(self, title: str, body: str, user_id: int):
        try:
            assert self.data().title == title, \
                f'Title "{self.data().title}" doesn\'t correspond to the expected one "{title}"'
            logging.info('Title "%s" is correct', title)
        except AssertionError as err:
            logging.exception('Title "%s" doesn\'t correspond to the expected one "%s"', self.data().title, title)
            raise err
        try:
            assert self.data().userId == user_id, \
                f'User id {self.data().userId} doest\'t correspond to the expected one {user_id}'
            logging.info('User id %s is correct', user_id)
        except AssertionError as err:
            logging.exception(
                'User id %s doest\'t correspond to the expected one %s', self.data().userId, user_id
            )
            raise err
        try:
            assert self.data().body == body, \
                f'Body "{self.data().body}" doesn\'t correspond to the expected one "{body}"'
            logging.info('Body "%s" is correct', body)
        except AssertionError as err:
            logging.exception(
                'Body "%s" doesn\'t correspond to the expected one "%s"', self.data().body == body, body
            )
