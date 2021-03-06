import pytest
from ..model_base_test import ModelBaseTest
from tests.sampleresponse.invoice import invoice_response
from xendit.models import Invoice


# fmt: off
class TestCreateInvoice(ModelBaseTest):
    @pytest.fixture
    def default_invoice_data(self):
        tested_class = Invoice
        class_name = "Invoice"
        method_name = "create"
        http_method_name = "post"
        args = ()
        kwargs = {
            "external_id": "invoice-1593677698",
            "amount": 20000,
            "payer_email": "customer@domain.com",
            "description": "Invoice Demo #123",
            "x_idempotency_key": "test-idemp_123",
        }
        params = (args, kwargs)
        url = "/v2/invoices"
        expected_correct_result = invoice_response()
        return (tested_class, class_name, method_name, http_method_name, url, params, expected_correct_result)

    @pytest.fixture
    def api_requestor_request_data(self, default_invoice_data):
        tested_class, class_name, method_name, http_method_name, url, params, _ = default_invoice_data
        headers = {"X-IDEMPOTENCY-KEY": "test-idemp_123"}
        body = {
            "external_id": "invoice-1593677698",
            "amount": 20000,
            "payer_email": "customer@domain.com",
            "description": "Invoice Demo #123",
        }
        return (tested_class, class_name, method_name, http_method_name, url, params, headers, body)

    @pytest.mark.parametrize("mock_correct_response", [invoice_response()], indirect=True)
    def test_return_dana_payment_on_correct_params(
        self, mocker, mock_correct_response, default_invoice_data
    ):
        self.run_success_return_test_on_xendit_instance(mocker, mock_correct_response, default_invoice_data)

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_invoice_data
    ):
        self.run_raises_error_test_on_xendit_instance(mocker, mock_error_request_response, default_invoice_data)

    @pytest.mark.parametrize("mock_correct_response", [invoice_response()], indirect=True)
    def test_return_dana_payment_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_invoice_data
    ):
        self.run_success_return_test_on_global_config(mocker, mock_correct_response, default_invoice_data)

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_invoice_data
    ):
        self.run_raises_error_test_on_global_config(mocker, mock_error_request_response, default_invoice_data)

    @pytest.mark.parametrize("mock_correct_response", [invoice_response()], indirect=True)
    def test_send_correct_request_to_api_requestor(self, mocker, mock_correct_response, api_requestor_request_data):
        self.run_send_correct_request_to_api_requestor(mocker, mock_correct_response, api_requestor_request_data)
# fmt: on
