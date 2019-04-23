from vk_user import VkUser, fields, vk_authorize
from vk_user import vk_user_db
from search import vk_search, create_users_from_ids
from db_handler import write_users_to_db, get_top_10_match
from settings import APP_ID
from vk_user_token import TOKEN
from pprint import pprint


def get_additional_data(vk_user):
    pass


if __name__ == '__main__':
    vk_api_instanse = vk_authorize(APP_ID, TOKEN)
    # vk_user_db.users.drop()
    test_user = VkUser(fields, vk_api_instanse)
    test_user.write_to_db()
    found_ids = vk_search(test_user, 30)
    found_data = create_users_from_ids(found_ids, test_user)
    users_added_to_db = write_users_to_db(found_data)
    top_10 = get_top_10_match()
    for user in top_10:
        print(user)
