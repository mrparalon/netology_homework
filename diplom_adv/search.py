from vk_user import VkUserToCompare, vk_user_db
from db_handler import get_all_user_ids, vk_user_db
from pprint import pprint


fields = ','.join(['bdate', 'city', 'country', 'interests',
                    'books', 'games', 'movies', 'music',
                    'personal', 'relation', 'sex', 'tv'])


def vk_search(vk_user, count):
    """
    Принимает объет VkUser того пользователя, 
    для которого нужно найти пару. Возращает список id найденных
    пользователей.
    """
    offset = vk_user_db.offset.find_one()
    if offset:
        offset = offset['offset']
    else:
        offset = 0
    sex = 1 if vk_user['sex'] == 2 else 2
    result = vk_user.vk.users.search(count=count, sex=sex,
                                     status=1, offset=offset)['items']
    result = list(map(lambda x: int(x['id']), result))
    offset += count
    if offset > 1000:
        offset = 1000
    vk_user_db.offset.remove({})
    vk_user_db.offset.insert_one({'offset': offset})
    print(offset)
    return result


def delete_duplicate_users(user_ids_list):
    db_user_ids = set(get_all_user_ids())
    user_ids = set(user_ids_list)
    return user_ids - db_user_ids


def create_users_from_ids(user_ids_list, vk_user_main):
    """
    Создает список расширенных данных
    пользователей, считает счет совпадения с главным пользователем.
    """
    user_ids_list = delete_duplicate_users(user_ids_list)
    users_data_extended_list = []
    if user_ids_list:
        for user_id in user_ids_list:
            user_object = VkUserToCompare(user_id,
                                          vk_user_main.fields,
                                          vk_user_main.vk,
                                          vk_user_main)
            print(f'User {user_object["id"]} created')
            # if not user_object.is_exists_in_db():
            users_data_extended_list.append(user_object.user_data)
    return users_data_extended_list
