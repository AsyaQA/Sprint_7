import pytest
import data
import helpers


class TestCreateCourier:

    def test_create_courier(self, courier):
        response = courier.create_courier(helpers.return_main_registr_params())
        assert response == (201, {'ok': True})

    def test_create_same_couriers(self, courier):
        response = courier.create_courier(data.static_courier)
        assert response == (409, {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'})

    @pytest.mark.parametrize(
        'data',
        [
            data.courier_no_login,
            data.courier_no_password,
        ]
    )
    def test_create_courier_without_one_some_params(self, courier, data):
        response = courier.create_courier(data)
        assert response == (400, {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'})

    def test_create_courier_with_same_login(self, courier):
        response = courier.create_courier(data.static_same_login_courier)
        assert response == (409, {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'})
