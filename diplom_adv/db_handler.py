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
    all_users = vk_user_db.users.find({'showed': {'$exists': False}},
                                      {'id': 1, 'photos': 1})\
                                       .sort('score', DESCENDING)\
                                       .limit(10)
    result = []
    user_db_ids = []
    for user in all_users:
        user_db_id = user.pop('_id')
        user_db_ids.append(user_db_id)
        result.append(user)
    vk_user_db.users.update_many({'_id': {'$in': user_db_ids}},
                                 {'$set': {'showed': True}})
    return result
