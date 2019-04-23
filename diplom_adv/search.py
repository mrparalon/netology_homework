from vk_user import VkUserToCompare, vk_user_db
from pprint import pprint


fields = ','.join(['bdate', 'city', 'country', 'interests',
                    'books', 'games', 'movies', 'music',
                    'personal', 'relation', 'sex', 'tv'])


def vk_search(vk_user, count, offset=0):
    """
    Принимает объет VkUser того пользователя, 
    для которого нужно найти пару.
    """
    sex = 1 if vk_user['sex'] == 2 else 2
    result = vk_user.vk.users.search(count=count, sex=sex, status=1)['items']
    return result


def create_users_from_search(vk_user, count, offset=0):
    """
    Принимает объет VkUser того пользователя,
    для которого нужно найти пару. Создает список расширенных данных
    пользователей и пишет их в базу.
    """
    users_data_list = vk_search(vk_user, count)
    users_data_extended_list = []
    for user in users_data_list:
        if not vk_user_db.users.find_one({'id': user['id']}):
            user_object = VkUserToCompare(user['id'],
                                          vk_user.fields,
                                          vk_user.vk,
                                          vk_user)
            print(f'User {user_object["id"]} created')
            # if not user_object.is_exists_in_db():
            users_data_extended_list.append(user_object.user_data)
    if users_data_extended_list:
        vk_user_db.users.insert_many(users_data_extended_list)
        print('Users added')
        return users_data_extended_list
    else:
        print('All users already in DB')
        return



