import random
import datetime
import logging

import pytest

from endpoints.get_users import GetUsers
from endpoints.get_posts import GetPosts
from endpoints.create_post import CreatePost

logging.getLogger(__name__)


@pytest.fixture(scope='session')
def user_id():
    get_users_endpoint = GetUsers()
    get_users_endpoint.get_all_users()
    user = random.choice(get_users_endpoint.data())
    print(f"Selected user email is: {user.email}")
    yield user.id


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    test_name = item.nodeid
    logging.info(f"Starting test: {test_name}")
    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item):
    yield
    test_name = item.nodeid
    logging.info(f"Finished test: {test_name}")


@pytest.fixture()
def clean_up(request):
    yield
    print(f'I would delete the post with id {request.function.post_id} if it was not a mock API')
    logging.info('Post with id %s deleted', request.function.post_id)


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
