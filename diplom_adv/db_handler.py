from pymongo import MongoClient
from pymongo import DESCENDING


client = MongoClient()
vk_user_db = client.vk_user_db


def get_all_user_ids():
    users_in_db = vk_user_db.users.find({}, {'id': 1})
    ids_users_in_db = list(map(lambda x: int(x['id']), users_in_db))
    return ids_users_in_db


def write_users_to_db(users_data_list):
    if users_data_list:
        inserted_ids = vk_user_db.users.insert_many(users_data_list)
        print('Users added to db')
        return inserted_ids
    else:
        print('All users already in DB')
        return


def get_top_10_match():
    all_users = vk_user_db.users.find({}, {'id': 1,
                                           'first_name': 1,
                                           'last_name': 1,
                                           })
    all_users.sort('score', DESCENDING)
    return all_users