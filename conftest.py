import random

import pytest

from endpoints.get_users import GetUsers


@pytest.fixture(scope='session')
def user_id():
    get_users_endpoint = GetUsers()
    get_users_endpoint.get_all_users()
    user = random.choice(get_users_endpoint.response_json)
    print(f"Selected user email is: {user['email']}")
    yield user['id']


@pytest.fixture()
def get_users_endpoint():
    return GetUsers()
