import pytest
import data


class TestLoginCourier:

    def test_login_courier(self, courier):
        response = courier.login_courier(data.static_login_courier)
        assert "id" in response

    @pytest.mark.parametrize(
        'data',
        [
            data.wrong_login,
            data.wrong_password,
        ]
    )
    def test_wrong_login_or_password_and_not_created(self, courier, data):
        response = courier.login_courier(data)
        assert response == {"code": 404, "message": "Учетная запись не найдена"}

    @pytest.mark.parametrize(
        'data',
         [
            data.no_login,
            data.no_password
        ]
    )
    def test_no_login_or_no_password(self, courier, data):
        response = courier.login_courier(data)
        assert response == {"code": 400, "message": "Недостаточно данных для входа"}
