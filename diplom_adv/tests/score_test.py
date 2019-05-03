# import unittest
from unittest import TestCase
from vk_user import VkUserToCompare


class MockedMainUser():
    def __init__(self):
        self.user_data = {}

    def __getitem__(self, key):
        return self.user_data[key]


class MockedUser(VkUserToCompare):
    def __init__(self, main_user):
        self.user_data = {}
        self.main_user = main_user


class TestScore(TestCase):
    def test_score_by_age(self):
        test_main_user = MockedMainUser()
        test_user = MockedUser(test_main_user)
        test_main_user.user_data['age'] = 25
        test_user.user_data['age'] = None
        self.assertEqual(test_user.score_by_age(), 0)
        test_user.user_data['age'] = 25
        self.assertIsInstance(test_user.score_by_age(), int)
        self.assertGreaterEqual(test_user.score_by_age(), 0)
        self.assertEqual(test_user.score_by_age(), 7)
        test_user.user_data['age'] = 31
        self.assertEqual(test_user.score_by_age(), 3)
        test_user.user_data['age'] = 50
        self.assertEqual(test_user.score_by_age(), 0)

    def test_score_by_groups(self):
        test_main_user = MockedMainUser()
        test_user = MockedUser(test_main_user)
        test_main_user.user_data['groups'] = list(range(1, 11))
        test_user.user_data['groups'] = []
        self.assertEqual(test_user.score_by_groups(), 0)
        test_user.user_data['groups'] = [1, 2]
        self.assertEqual(test_user.score_by_groups(), 15)
        # 40 elements, 1 common
        test_user.user_data['groups'] = [1] + list(range(100, 139))
        self.assertEqual(test_user.score_by_groups(), 8)
        test_user.user_data['groups'] = [20]
        self.assertEqual(test_user.score_by_groups(), 0)

    def test_score_by_personal(self):
        test_main_user = MockedMainUser()
        test_user = MockedUser(test_main_user)
        test_main_user.user_data['personal'] = {'political': 9,
                                                'people_main': 1,
                                                'life_main': 1}
        test_user.user_data['personal'] = {}
        self.assertEqual(test_user.score_by_personal(), 0)
        test_user.user_data['personal']['political'] = 9
        self.assertEqual(test_user.score_by_personal(), 2)
        test_user.user_data['personal']['people_main'] = 2
        self.assertEqual(test_user.score_by_personal(), 2)
        test_user.user_data['personal']['smoking'] = 1
        self.assertEqual(test_user.score_by_personal(), 2)
        test_user.user_data['personal']['life_main'] = 1
        self.assertEqual(test_user.score_by_personal(), 4)

    def test_score_by_city(self):
        test_main_user = MockedMainUser()
        test_user = MockedUser(test_main_user)
        self.assertEqual(test_user.score_by_city(), 0)
        test_user.user_data['city'] = {'id': 1, 'title': 'Москва'}
        self.assertEqual(test_user.score_by_city(), 0)
        test_main_user.user_data['city'] = {'id': 1, 'title': 'Москва'}
        self.assertEqual(test_user.score_by_city(), 10)

    def test_score_by_friends(self):
        test_main_user = MockedMainUser()
        test_user = MockedUser(test_main_user)
        test_main_user.user_data['friends'] = []
        test_user.user_data['friends'] = []
        self.assertEqual(test_user.score_by_friends(), 0)
        test_main_user.user_data['friends'] = list(range(1, 11))
        self.assertEqual(test_user.score_by_friends(), 0)
        test_user.user_data['friends'] = [1]
        self.assertEqual(test_user.score_by_friends(), 2)
        test_user.user_data['friends'] = [1, 2, 3]
        self.assertEqual(test_user.score_by_friends(), 6)
        test_user.user_data['friends'] = list(range(1, 11))
        self.assertEqual(test_user.score_by_friends(), 16)
