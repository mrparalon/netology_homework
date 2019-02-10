import requests
from urllib.parse import urlencode
from pprint import pprint
from time import sleep


class VkUser:
    
    def __init__(self, id, token, v='5.92'):
        self.URL = 'https://api.vk.com/method/'
        self.id = id
        self.params = {
                        'v': v,
                        'access_token': token,
                        'user_id': id
                    }
        self.user_info = requests.get(self.URL+'users.get', self.params)
        self.user_info = self.user_info.json()['response'][0]

    def __repr__(self):
        return f'https://vk.com/id{self.user_info["id"]}'

    def __and__(self, other):
        self_friends = self.get_friends_list()
        other_friends = other.get_friends_list()
        common_friends_set = set(self_friends) & set(other_friends)
        common_friends_list = []
        for friend_id in common_friends_set:
            common_friends_list.append(VkUser(friend_id, token=self.params['access_token']))
            print(f'Пользователь {friend_id} добавлен в лист общих друзей')
            sleep(0.35) # 3 requests per minute limit
        return common_friends_list

    def get_friends_list(self):
        friends = requests.get(self.URL+'friends.get', self.params)
        self.friends_list = friends.json()['response']['items']
        return self.friends_list

def test_vkuser_class():
    TOKEN = 'PASTE YOUR TOKEN HERE'
    URL = 'https://api.vk.com/method/'
    mr_paralon = VkUser('15745994', TOKEN)
    katrin_mamontova = VkUser('18936907', TOKEN)
    mr_paralon_info = mr_paralon.user_info
    common_friends = mr_paralon & katrin_mamontova
    print(mr_paralon, katrin_mamontova)
    for friend in common_friends:
        print(friend)

test_vkuser_class()