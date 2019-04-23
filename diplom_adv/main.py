from vk_user import VkUser, fields, vk_authorize
from vk_user import vk_user_db
from search import create_users_from_search
from settings import APP_ID


if __name__ == '__main__':
    vk_api_instanse = vk_authorize(APP_ID)
    vk_user_db.users.drop()
    test_user = VkUser(6349860, fields, vk_api_instanse)
    test_user.write_to_db()
    create_users_from_search(test_user, 30)
    for user in vk_user_db.users.find({'score': {'$gt': 0}}):
        print(user['id'], user['first_name'],
              user['last_name'], user['age'])
        try:
            print(user['score'])
        except KeyError:
            print('Main user')
