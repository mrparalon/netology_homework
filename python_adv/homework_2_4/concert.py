import csv
import re
from datetime import datetime

from pymongo import MongoClient, DESCENDING

client = MongoClient()
concert_db = client.concert_db


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    concert_data = []
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        for concert in reader:
            concert_fixed = {}
            concert_fixed['artist'] = concert['Исполнитель']
            concert_fixed['price'] = int(concert['Цена'])
            concert_fixed['place'] = concert['Место']
            date_list = concert['Дата'].split('.')
            date = datetime(year=2019,
                            month=int(date_list[1]),
                            day=int(date_list[0]))
            concert_fixed['date'] = date
            concert_data.append(concert_fixed)
    concert_db.concerts.insert_many(concert_data)


def find_cheapest(db):
    """
    Найти самые дешевые билеты
    Документация: https://docs.mongodb.com/manual/reference/operator/aggregation/sort/
    """
    chipest_concerts = []
    sorted_by_price = db.concerts.find().sort('price', DESCENDING)
    lowest_price = int(sorted_by_price[0]['price'])
    for consert in sorted_by_price:
        if int(consert['price']) == lowest_price:
            chipest_concerts.append(consert)
        else:
            break
    return chipest_concerts


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и выведите их по возрастанию цены
    """
    regex = re.compile(name, re.I)
    result = db.concerts.find({'artist': regex}).sort('price', DESCENDING)
    return result


def find_by_date(start_date, end_date, db):
    res = db.concerts.find({'$and':
                               [{'date': {'$lte': end_date}},
                                 {'date': {'$gte': start_date}}]})
    return res




if __name__ == '__main__':
    # read_data('artists.csv', None)
    print(find_cheapest(concert_db))
    print(list(find_by_name('семен', concert_db)))
    start_date = datetime(year=2019, month=7, day=1)
    end_date = datetime(year=2019, month=7, day=30)
    finded_by_date = find_by_date(start_date, end_date, concert_db)
    print(list(finded_by_date))