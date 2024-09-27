from typing import List

import allure

from endpoints.base_api import BaseApi


class GetPosts(BaseApi):
    _endpoint = '/posts'

    @allure.step('Get all user\'s posts')
    def get_user_posts(self, user_id: int) -> List:
        self._get(self._url)
        user_posts = filter(lambda post: post['userId'] == user_id, self.response_json)
        return user_posts

    @staticmethod
    def check_post_ids_in_range(posts: List, range_from: int, range_to: int):
        posts_ids = map(lambda post: post['id'], posts)
        assert all(map(lambda post_id: post_id in range(range_from, range_to + 1), posts_ids))
