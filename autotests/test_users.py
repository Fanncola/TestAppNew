import requests
from framework.asserts import Asserts
from framework.fake import Fake
from settings import Settings
url = Settings.get_url()
asserts = Asserts
fake = Fake


class TestUsers:
    def test_get_users(self):
        response = requests.get(
            url + 'users',
            headers={'api-key': 'fbe04d08-a7a1-441f-8673-dd2a7aad0eef'}
        )
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 200)

    def test_get_users_wrond_auth(self):
        response = requests.get(
            url + 'users',
            headers={'api-key': 'fbe04d08-a7a1-441f-8673-dd2a7aad0ee'}
        )
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 401)

    def test_get_users_without_header(self):
        response = requests.get(url + 'users')
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 401)

    def test_get_all_users(self):
        response = requests.get(
            url + 'users?' + 'limit=10',
            headers={'api-key': 'fbe04d08-a7a1-441f-8673-dd2a7aad0eef'}
        )
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 200)

    def test_get_all_users_without_header(self):
        response = requests.get(
            url + 'users?' + 'limit=10'
        )
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 401)

    def test_get_all_users_wrong_auth(self):
        response = requests.get(
            url + 'users?' + 'limit=10',
            headers={'api-key': 'fbe04d08-a7a1-441f-8673-dd2a7aad0e'}
        )
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 401)

    def test_post_user(self):
        data = fake.fake_user()
        response = requests.post(
            url + 'user',
            headers={'api-key': 'fbe04d08-a7a1-441f-8673-dd2a7aad0eef'},
            json=data
        )
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 200)
        asserts.check_id(response, "Don't id")
        asserts.json_has_key(response, 'gender')
        asserts.json_has_key(response, 'firstname')
        asserts.json_has_key(response, 'lastname')
        asserts.json_has_key(response, 'id')
        asserts.json_has_no_key(response, 'password')

    def test_not_unique_email(self):
        data = {
            'firstname': 'Jon',
            'lastname': 'Snow',
            'gender': 'M',
            'email': 'winter@is.coming',
            'password': 'king of the night'
        }
        response = requests.post(
            url + 'user',
            headers={'api-key': 'fbe04d08-a7a1-441f-8673-dd2a7aad0eef'},
            json=data
        )
        asserts.elapsed_time(response, 1)
        asserts.status_code(response, 400)



