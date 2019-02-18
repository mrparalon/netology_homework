#! python
import requests
from time import sleep
import sys
from pprint import pprint
import json
from vk_api_exceprions import BannedDeletedUser, PermissionDenied
import settings

"""
Run using comand line, pass user ID as argument
"""


URL_METHOD = 'https://api.vk.com/method/'
TOKEN = settings.token

def vk_api_get_request(url, request_method, params):
    response = requests.get(url + request_method, params=params)
    sys.stdout.write('\u2588')
    sys.stdout.flush()
    if 'error' in response.json():
        if response.json()['error']['error_code'] == 6:
            response = vk_api_get_request(url, request_method, params=params)
        elif response.json()['error']['error_code'] == 7:
            raise PermissionDenied('Permission to perform this action is denied')
        elif response.json()['error']['error_code'] == 18:
            raise BannedDeletedUser('User was deleted or banned')
    sleep(0.35)
    return response


class VkUser:
    def __init__(self, id):
        self. params = {
            'v': '5.52',
            'access_token': TOKEN,
            'user_ids': str(id),
        }
        self.id = str(id)
        resp_user = vk_api_get_request(URL_METHOD, 'users.get', self.params)
        self.user_info = resp_user.json()['response'][0]
        self.params['user_id'] = self.user_info['id']
        self.groups = self.get_groups_id_list()

    def __repr__(self):
        first_name = self.user_info["first_name"]
        last_name = self.user_info["last_name"]
        return f'{first_name} {last_name}, id {self.id}'

    def get_groups_id_list(self):
        try:
            resp_groups = vk_api_get_request(URL_METHOD, 'groups.get', self.params)
            groups_int_list = resp_groups.json()['response']['items']
            groups = list(map(str, groups_int_list))
            return groups
        except (PermissionDenied, BannedDeletedUser):
            pass
        

    def get_all_groups_info(self):
        params = self.params
        params['group_ids'] = ','.join(self.groups)
        params['fields'] = 'members_count'
        resp_groups_info = vk_api_get_request(URL_METHOD, 'groups.getById', self.params)
        user_groups_info = resp_groups_info.json()['response']
        return user_groups_info

    def get_friends_list(self):
        try:
            resp_friends = vk_api_get_request(URL_METHOD, 'friends.get', self.params)
            friends_id_list = resp_friends.json()['response']['items']
            return friends_id_list
        except BannedDeletedUser:
            pass

    def get_unique_groups(self):
        self.friends_list = self.get_friends_list()
        groups_set = set(self.groups)
        print(groups_set)
        for friend in self.friends_list:
            friend_obj = VkUser(friend)
            if friend_obj.groups:
                groups_set = groups_set - set(friend_obj.groups)
        return groups_set



class VkGroup:
    """
    Handle basic information about VK group.
    Initialize by group ID or dict with group info. 
    """
    def __init__(self, group_generation_info):
        self. params = {
            'v': '5.52',
            'access_token': TOKEN,
        }
        if isinstance(group_generation_info, str) or isinstance(group_generation_info, int):
            params = self.params
            params['group_id'] = str(group_generation_info)
            params['fields'] = 'members_count'
            resp_groups_info = vk_api_get_request(URL_METHOD, 'groups.getById', self.params)
            self.group_info = resp_groups_info.json()['response'][0]
        elif isinstance(group_generation_info, dict):
            self.group_info = group_generation_info

        self.short_group_info = {}
        self.short_group_info['gid'] = self.group_info['id']
        self.short_group_info['name'] = self.group_info['name']
        self.short_group_info['members_count'] = self.group_info['members_count']

    def __repr__(self):
        return str(self.short_group_info)




if __name__ == '__main__':
    id = sys.argv[1]
    user = VkUser(id)
    user.get_groups_id_list()
    unique_groups = user.get_unique_groups()
    print(unique_groups)
    print(f'Hello, {user}!')

