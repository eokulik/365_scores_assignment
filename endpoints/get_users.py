import logging
from typing import List

import allure

from endpoints.base_api import BaseApi
from endpoints.models.user import User
from data import constants

logging.getLogger(__name__)


class GetUsers(BaseApi):
    _endpoint = constants.USERS_ENDPOINT

    @allure.step('Get list of users')
    def get_all_users(self) -> None:
        self._get(self._url)
        logging.info('Fetched all users')

    def data(self) -> List[User]:
        users = list(map(lambda user: User(**user), self.response_json))
        return users
