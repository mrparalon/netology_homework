from vk_user import VkUser
from unittest import TestCase
from datetime import datetime
import json
import os

user_data_path = os.path.join('tests', 'test_user.json')


class TestVkUser(TestCase):
    class MockedVkUser(VkUser):
        def __init__(self):
            with open(user_data_path, encoding='utf8') as test_user_json:
                self.user_data = json.load(test_user_json)

    def test_select_top_3_photo(self):
        test_user = self.MockedVkUser()
        top_3_photos = test_user.select_top_3_photo()
        self.assertIsInstance(top_3_photos, list)
        self.assertEqual(len(top_3_photos), 3)
        for photo in top_3_photos:
            self.assertIsInstance(photo, str)
            self.assertTrue('http' in photo)

    def test_bdate_to_datetime(self):
        test_user = self.MockedVkUser()
        bdate = test_user.bdate_to_datetime()
        date_to_assert = datetime(year=1986, month=9, day=21)
        self.assertIsInstance(bdate, datetime)
        self.assertEqual(bdate, date_to_assert)
        test_user.user_data['bdate'] = '21.9'
        self.assertIsNone(test_user.bdate_to_datetime())
        # Предыдущий вызов удаляет bdate, создаем заново и удаляем явно
        test_user.user_data['bdate'] = '21.9'
        test_user.user_data.pop('bdate')
        self.assertIsNone(test_user.bdate_to_datetime())

    def test_get_age(self):
        test_user = self.MockedVkUser()
        test_user['bdate'] = test_user.bdate_to_datetime()
        bdate = datetime(year=1986, month=9, day=21)
        real_age = datetime.now().year - bdate.year
        age = test_user.get_age()
        self.assertIsInstance(age, int)
        self.assertEqual(age, real_age)

