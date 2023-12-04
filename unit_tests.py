import requests
import unittest
from unittest.mock import MagicMock, patch
from health_check import check_health, calculate_availability, print_availability

class TestYourScript(unittest.TestCase):

    def test_check_health_up(self):
        endpoint = {'url': 'https://fetch.com/'}
        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.elapsed.total_seconds.return_value = 0.1
        with patch("requests.request", return_value=response_mock):
            status = check_health(endpoint)
        self.assertEqual(status, 'UP')

    def test_check_health_down(self):
        endpoint = {'url': 'https://fetch.com/'}
        with patch("requests.request", side_effect=requests.exceptions.RequestException) as mock_request:
            status = check_health(endpoint)
            print("Exception captured:", mock_request.side_effect)
        self.assertEqual(status, 'DOWN')

    def test_calculate_availability(self):
        availability_list = ['UP', 'UP', 'DOWN', 'UP', 'DOWN']
        availability_percentage = calculate_availability(availability_list)
        self.assertEqual(availability_percentage, 60)

    def test_calculate_availability_empty_list(self):
        availability_percentage = calculate_availability([])
        self.assertEqual(availability_percentage, 0)

    def test_calculate_availability_all_up(self):
        availability_list = ['UP', 'UP', 'UP']
        availability_percentage = calculate_availability(availability_list)
        self.assertEqual(availability_percentage, 100)

    def test_calculate_availability_all_down(self):
        availability_list = ['DOWN', 'DOWN', 'DOWN']
        availability_percentage = calculate_availability(availability_list)
        self.assertEqual(availability_percentage, 0)

    def test_print_availability(self):
        domain_availability = {'fetch.com/': {'history': ['UP', 'UP', 'DOWN'], 'availability': 66}}
        with patch("builtins.print") as mock_print:
            print_availability(domain_availability)
        mock_print.assert_called_with("fetch.com/ has 66% availability percentage")


if __name__ == '__main__':
    unittest.main(verbosity=2)
