import vk_api
from db_handler import vk_user_db


def create_vk_session(app_id, token):
    vk_session = vk_api.VkApi(app_id=app_id, token=token)
    vk_api_instanse = vk_session.get_api()
    return vk_api_instanse


def vk_authorize(app_id, token):
    if token:
        try:
            vk = create_vk_session(app_id, token)
            user = vk.users.get()[0]
            print(f"С возвращением, {user['first_name']} {user['last_name']}")
            return vk
        except vk_api.VkApiError:
            vk_user_db.token.remove({})
            vk_authorize(app_id, token)
            # with open('vk_user_token.py', 'w') as token_file:
            #     token_file.write('TOKEN = None')
            #     vk_authorize(app_id, token)
    else:
        print('<3<3<3<3<3<3<3<3<3<3')
        print('Перейдите по ссылке, чтобы получить доступ к своему будущему счастью')
        print('<3<3<3<3<3<3<3<3<3<3'+'\n')
        print('https://oauth.vk.com/authorize?client_id=6854512&scope=friends,groups&display=page&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.95'+'\n')
        token = input('Вставьте значение токена из адресной строки:\n')
        vk_user_db.token.insert_one({'token': token})
        return create_vk_session(app_id, token)
