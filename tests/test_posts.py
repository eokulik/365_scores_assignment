from data import test_data


def test_user_posts(user_id, get_posts_endpoint):
    user_posts = get_posts_endpoint.get_user_posts(user_id)
    get_posts_endpoint.check_post_ids_in_range(user_posts, 1, 100)


def test_create_valid_post(user_id, create_post_endpoint, clean_up, request):
    payload = test_data.VALID_POST
    payload['userId'] = user_id
    create_post_endpoint.create_post(payload)
    request.function.post_id = create_post_endpoint.data().id
    create_post_endpoint.check_response_status_is_(201)
    create_post_endpoint.check_post_content(payload['title'], payload['body'], user_id)
