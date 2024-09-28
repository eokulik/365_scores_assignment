import logging

import allure

from endpoints.base_api import BaseApi
from data import constants

logging.getLogger(__name__)


class GetUsers(BaseApi):
    _endpoint = constants.USERS_ENDPOINT

    @allure.step('Get list of users')
    def get_all_users(self) -> None:
        self._get(self._url)
        logging.info('Fetched all users')
