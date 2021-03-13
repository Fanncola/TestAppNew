from faker import Faker
from datetime import datetime
fake = Faker()



class Fake:
    @staticmethod
    def fake_user():
        # date = datetime.datetime.now()
        data = {
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'gender': 'F',
            'email': fake.email(),
            'password': fake.password(length=12),
            'createdate': datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
        }
        return data


