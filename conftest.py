import random
import datetime

import pytest

from endpoints.get_users import GetUsers
from endpoints.get_posts import GetPosts
from endpoints.create_post import CreatePost


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


@pytest.fixture()
def get_posts_endpoint():
    return GetPosts()


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


def pytest_configure(config):
    if not config.option.log_file:
        timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = f'logs/api_tests_{timestamp}.log'
