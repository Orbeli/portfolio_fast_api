from dataclasses import asdict

from faker import Faker
from sqlalchemy import select

from portfolio_rest_api.models import User

faker = Faker()


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        name = faker.word()
        email = faker.email()
        password = faker.word()

        new_user = User(name=name, email=email, password=password)

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.email == email))

    assert asdict(user) == {
        'id': 1,
        'name': name,
        'email': email,
        'password': password,
        'created_at': time,
        'updated_at': time,
    }
