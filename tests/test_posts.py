import random

import pytest
import allure

from data import test_data
from utils import csv_test_data


@pytest.mark.flaky(retries=3)
@allure.feature('Users')
def test_user_posts(user_id, get_posts_endpoint):
    user_id = random.choice([user_id, 42, 77])  # This is just to make the test flaky
    user_posts = get_posts_endpoint.get_user_posts(user_id)
    get_posts_endpoint.check_post_ids_in_range(user_posts, 1, 100)


@allure.feature('Posts')
@pytest.mark.parametrize(
    'title,body',
    csv_test_data.read_test_data(test_data.POSTS_DATA_FILE, 'valid')
)
def test_create_valid_post(user_id, create_post_endpoint, clean_up, request, title, body):
    payload = test_data.VALID_POST
    payload['title'] = title
    payload['body'] = body
    payload['userId'] = user_id
    create_post_endpoint.create_post(payload)
    request.function.post_id = create_post_endpoint.data().id
    create_post_endpoint.check_response_status_is_(201)
    create_post_endpoint.check_post_content(payload['title'], payload['body'], user_id)
