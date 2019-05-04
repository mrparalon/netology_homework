from db_handler import get_all_user_ids,\
                       write_users_to_db,\
                       get_top_10_match,\
                       client
from unittest import TestCase


test_vk_user_db = client.test_vk_user_db


def create_fake_data():
    users_data = []
    for user_id, score in enumerate(range(20, 41)):
        users_data.append({'id': user_id,
                           'photos': f'{user_id}.jpg',
                           'score': score})
    return users_data


class TestDbHandler(TestCase):
    def test_write_users_to_db(self):
        test_vk_user_db.users.drop()
        users_data = create_fake_data()
        returned_ids = write_users_to_db(users_data, test_vk_user_db)
        self.assertIsInstance(returned_ids, list)
        db_data = list(test_vk_user_db.users.find({}, {'id': 1,
                                                       'photos': 1,
                                                       'score': 1}))
        self.assertEqual(users_data, db_data)

    def test_get_all_user_ids(self):
        test_vk_user_db.users.drop()
        users_data = create_fake_data()
        write_users_to_db(users_data, test_vk_user_db)
        user_ids = list(map(lambda x: x['id'], users_data))
        user_ids_from_db = get_all_user_ids(test_vk_user_db)
        self.assertEqual(user_ids, user_ids_from_db)
        for user_id in user_ids_from_db:
            self.assertIsInstance(user_id, int)

    def test_get_top_10_match(self):
        test_vk_user_db.users.drop()
        users_data = create_fake_data()
        write_users_to_db(users_data, test_vk_user_db)
        top_10 = get_top_10_match(test_vk_user_db)
        # write_users_to_db почему-то записывает id из базы в словарь
        top_10_from_users_data = sorted(users_data,
                                        key=lambda x: x['score'],
                                        reverse=True)[:10]
        for user in top_10_from_users_data:
            user.pop('_id')
            user.pop('score')
        self.assertEqual(top_10, top_10_from_users_data)