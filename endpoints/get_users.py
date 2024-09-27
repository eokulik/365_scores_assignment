import allure

from endpoints.base_api import BaseApi


class GetUsers(BaseApi):
    _endpoint = '/users'

    @allure.step('Get list of users')
    def get_all_users(self) -> None:
        self._get(self._url)
