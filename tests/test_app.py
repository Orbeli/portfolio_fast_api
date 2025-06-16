from http import HTTPStatus

from fastapi.testclient import TestClient

from portfolio_rest_api.app import app


def test_root_deve_retornar_ok_e_mensagem_fixa():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "root read"}
