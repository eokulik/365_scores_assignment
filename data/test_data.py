import os


data_path = os.path.dirname(__file__)
POSTS_DATA_FILE = os.path.join(data_path, 'posts_data.csv')


VALID_POST = {
    'title': 'Correct title',
    'body': 'Correct body',
    'userId': 1,
}
