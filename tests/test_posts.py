def test_user_posts(user_id, get_posts_endpoint):
    user_posts = get_posts_endpoint.get_user_posts(user_id)
    get_posts_endpoint.check_post_ids_in_range(user_posts, 1, 100)


def test_create_valid_post(user_id, create_post_endpoint):
    payload = {
        'title': 'Correct title',
        'body': 'Correct body',
        'userId': user_id,
    }
    create_post_endpoint.create_post(payload)
    create_post_endpoint.check_response_status_is_(201)

