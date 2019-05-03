from db_handler import vk_user_db
from datetime import datetime


fields = ','.join(['bdate', 'city', 'country', 'interests',
                   'books', 'games', 'movies', 'music',
                   'personal', 'relation', 'sex', 'tv'])


class VkUser():
    def __init__(self, fields, vk_api_instanse, user_id=None):
        self.fields = fields
        self.vk = vk_api_instanse
        self.user_id = user_id
        if not self.user_id:
            self.user_id = int(self.vk.users.get()[0]['id'])
        self.entry_user = self.is_exists_in_db()
        if not self.entry_user:
            self.user_data = self.get_user_data(self.user_id,
                                                self.fields)
            self['photos'] = self.select_top_3_photo()
            self['bdate'] = self.bdate_to_datetime()
            self['age'] = self.get_age()
        else:
            self.user_data = vk_user_db.users.find_one(
                                              {'_id': self.entry_user})

    def __getitem__(self, key):
        return self.user_data[key]

    def __setitem__(self, key, value):
        self.user_data[key] = value

    def __str__(self):
        return str(self.user_data)

    def get_user_data(self, user_id, fields):
        code = f'''var user = API.users.get({{"user_ids": "{user_id}",
                                "fields": "{fields}"}})[0];
        var friends = API.friends.get({{"user_id":"{user_id}"}});
        var photos = API.photos.get({{"owner_id":"{user_id}",
                                        "album_id":"profile",
                                        "extended":"1"}});
        var groups = API.groups.get({{"user_id":"{user_id}"}});
        user.friends = friends["items"];
        user.photos = photos["items"];
        user.groups = groups["items"];
        return user;'''
        user_data = self.vk.execute(code=code)
        return user_data

    def select_top_3_photo(self):
        if self.user_data['photos']:
            photos = []
            for photo in self.user_data['photos']:
                full_size_with_likes = {}
                full_size_with_likes['likes'] = photo['likes']
                full_size_with_likes['id'] = photo['id']
                full_size_with_likes['url'] = photo['sizes'][-1]['url']
                photos.append(full_size_with_likes)
            sorted_by_like = sorted(photos, reverse=True,
                                    key=lambda x: x['likes']['count'],)
            top_3_photo = []
            for photo in sorted_by_like[:3]:
                top_3_photo.append(photo.pop('url'))
            return top_3_photo
        return None

    def bdate_to_datetime(self):
        if 'bdate' in self.user_data:
            date = self.user_data['bdate'].split('.')
            date = list(map(int, date))
            if len(date) == 3:
                date = datetime(day=date[0], month=date[1], year=date[2])
                return date
            else:
                self.user_data.pop('bdate')
                return None

    def get_age(self):
        if self['bdate']:
            age = datetime.now().year - self['bdate'].year
            return age
        else:
            return None

    def is_exists_in_db(self):
        is_exists = vk_user_db.users.find_one({'id': self.user_id})
        if is_exists:
            # print(f"User {user_id} already exist!")
            return is_exists['_id']

    def write_to_db(self):
        if not self.is_exists_in_db():
            print(f"id{self['id']} {self['first_name']} {self['last_name']}\
                    added!")
            res = vk_user_db.users.insert_one(self.user_data)
            self.entry_user = res.inserted_id
            return self.entry_user


class VkUserMain(VkUser):
    def __init__(self, fields, vk_api_instanse, user_id=None):
        super().__init__(fields, vk_api_instanse, user_id=user_id)
        self.user_data = self.get_missing_data()

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    def __str__(self):
        return super().__str__()

    def get_missing_data(self):
        user_data = self.user_data
        if not user_data['age']:
            age = int(input('Введите свой возраст: '))
            user_data['age'] = age
        if not user_data['city']:
            city = input('Введите id вашего города: ')
            user_data['city'] = {'id': city}
        if not user_data['books']:
            books = input('Введите любимые книги через запятую:\n')
            user_data['books'] = books
        return user_data


class VkUserToCompare(VkUser):
    def __init__(self, user_id, fields, vk_api_instanse, vk_user):
        super().__init__(fields, vk_api_instanse, user_id=user_id)
        self.main_user = vk_user
        self['score'] = self.get_score()

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    def __str__(self):
        return super().__str__()

    def get_score(self):
        score = 0
        score += self.score_by_age()
        score += self.score_by_groups()
        score += self.score_by_personal()
        score += self.score_by_city()
        return score

    def score_by_age(self):
        score = 0
        if self['age'] and self.main_user['age']:
            age_difference = abs(int(self['age']) - int(self.main_user['age']))
            if self['age'] < 18:
                score = -1000
            elif age_difference <= 5:
                score = 7
            elif 5 < age_difference <= 10:
                score = 3
        return score

    def score_by_groups(self):
        score = 0
        main_user_groups = self.main_user['groups']
        other_user_groups = self['groups']
        if main_user_groups and other_user_groups:
            common_groups_counter = len(set(main_user_groups) &
                                        set(other_user_groups))
            score = common_groups_counter * 400 /\
                    (len(main_user_groups) +
                     len(other_user_groups))
        if score > 15:
            score = 15
        return score

    def score_by_personal(self):
        score = 0
        if ('personal' in self.main_user.user_data) and\
           ('personal' in self.user_data):
            main_personal = self.main_user['personal']
            other_personal = self['personal']
            similar_categories = set(main_personal.keys()) &\
                                 set(other_personal.keys())
            if similar_categories:
                for category in similar_categories:
                    if main_personal[category] == other_personal[category]:
                        score += 2
        return score

    def score_by_city(self):
        score = 0
        if 'city' in self.user_data and 'city' in self.main_user.user_data:
            if self['city']['id'] == self.main_user['city']['id']:
                score += 10
        return score

    def score_by_friends(self):
        score = 0
        if self['friends'] and self.main_user['friends']:
            common_freinds_counter = len(set(self['friends']) &
                                         set(self.main_user['friends']))
            score += common_freinds_counter * 2
            if score > 16:
                score = 16
        return score


# if __name__ == '__main__':
    # fields = ','.join(['bdate', 'city', 'country', 'interests',
    #                    'books', 'games', 'movies', 'music',
    #                    'personal', 'relation', 'sex', 'tv'])
    # # test_user = VkUser(28086193, fields)
    # vk = vk_authorize(6854512)
    # print(vk.users.get(user_ids=None))
