from faker import Faker
fake = Faker()


class Fake:
    @staticmethod
    def fake_user():
        data = {
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'gender': 'F',
            'email': fake.email(),
            'password': fake.password(length=12)
        }
        return data


