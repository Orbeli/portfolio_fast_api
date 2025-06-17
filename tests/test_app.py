from http import HTTPStatus

from faker import Faker

faker = Faker()


def test_root_deve_retornar_ok_e_mensagem_fixa(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'root read'}


def test_creat_user_and_return_created(client):
    name = faker.word()
    email = faker.email()
    password = faker.password()

    payload = {
        'name': name,
        'password': password,
        'email': email,
    }

    response = client.post('/users', json=payload)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': name,
        'email': email,
    }

    # Will be implemented with database implementation
    # def test_read_users(client):
    #     response = client.get('/users/')

    #     assert response.status_code == HTTPStatus.OK
    #     assert response.json() == {'users': []}

    # def test_update_user_and_return_ok(client):
    ...


def test_update_user_and_return_not_found(client):
    name = faker.word()
    email = faker.email()
    password = faker.password()

    payload = {
        'name': name,
        'password': password,
        'email': email,
    }

    response = client.put(f'/users/{faker.random_int()}', json=payload)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
