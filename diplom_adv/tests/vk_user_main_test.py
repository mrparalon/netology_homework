from unittest import TestCase
from unittest.mock import patch
from vk_user import VkUserMain


class MockedMainUser(VkUserMain):
    def __init__(self):
        self.user_data = {}

    def __getitem__(self, key):
        return self.user_data[key]


class TestVkUserMain(TestCase):
    @patch('vk_user.VkUserMain._get_input', return_value='26')
    def test_get_age_from_user(self, input):
        test_user = MockedMainUser()
        self.assertEqual(test_user._get_age_from_user(), 26)

    @patch('vk_user.VkUserMain._get_input', return_value='1')
    def test_get_age_from_user(self, input):
        test_user = MockedMainUser()
        self.assertEqual(test_user._get_city_from_user(), '1')