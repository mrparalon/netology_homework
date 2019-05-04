from vk_user import VkUserMain, fields
from vk_api_handler import vk_authorize
from search import vk_search, create_users_from_ids
from db_handler import write_users_to_db, get_top_10_match, vk_user_db
from settings import APP_ID
import json


if __name__ == '__main__':
    vk_user_db.users.drop()
    vk_user_db.offset.drop()
    token = vk_user_db.token.find_one()
    if token:
        token = token['token']
    vk_api_instanse = vk_authorize(APP_ID, token)
    test_user = VkUserMain(fields, vk_api_instanse)
    # test_user.write_to_db()
    found_ids = vk_search(test_user, 20, vk_user_db)
    found_data = create_users_from_ids(found_ids, test_user)
    users_added_to_db = write_users_to_db(found_data, vk_user_db)
    top_10 = get_top_10_match(vk_user_db)
    with open('result.json', 'w', encoding='utf8') as result_file:
        json.dump(top_10, result_file, indent=1, ensure_ascii=False)
