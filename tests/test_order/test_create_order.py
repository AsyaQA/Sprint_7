import json
import pytest
import data


class TestCreateOrder:

    @pytest.mark.parametrize(
        'data',
        [
            data.grey_order,
            data.black_order,
            data.both_color,
            data.without_color
        ]
    )
    def test_create_order(self, courier, data):
        response = courier.create_order(json.dumps(data))
        assert 'track' in response
