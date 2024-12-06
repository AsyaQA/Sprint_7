class TestGetOrderList:

    def test_get_order_list(self, courier):
        response = courier.get_order_list()
        assert "order", "pageInfo" in response
