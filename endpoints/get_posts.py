import logging
from typing import List

import allure

from endpoints.base_api import BaseApi
from endpoints.models.post import Post
from data import constants

logging.getLogger(__name__)


class GetPosts(BaseApi):
    _endpoint = constants.POSTS_ENDPOINT

    @allure.step('Get all user\'s posts')
    def get_user_posts(self, user_id: int) -> List:
        self._get(self._url)
        user_posts = list(filter(lambda post: post.userId == user_id, self.data()))
        if user_posts:
            logging.info('User\'s posts fetched: %s', user_posts)
        else:
            logging.warning('There are no posts created by the user with id %s', user_id)
        return user_posts

    @staticmethod
    def check_post_ids_in_range(posts: List, range_from: int, range_to: int):
        posts_ids = list(map(lambda post: post.id, posts))
        try:
            assert posts_ids and all(map(lambda post_id: post_id in range(range_from, range_to + 1), posts_ids)), \
                f'not all the post IDs are in range {range_from} - {range_to}, posts: {posts_ids}'
            logging.info('All post IDs are in range %s - %s', range_from, range_to)
        except AssertionError as err:
            logging.exception(
                'not all the post IDs are in range %s - %s, post IDs: %s',
                range_from, range_to, posts_ids
            )
            raise err

    def data(self) -> List[object]:
        posts = list(map(lambda post: Post(**post), self.response_json))
        return posts
