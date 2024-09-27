import allure

from endpoints.base_api import BaseApi
from data import constants


class GetUsers(BaseApi):
    _endpoint = constants.USERS_ENDPOINT

    @allure.step('Get list of users')
    def get_all_users(self) -> None:
        self._get(self._url)
