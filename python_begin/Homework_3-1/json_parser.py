import json
from pprint import pprint
import xml.etree.ElementTree as ET

def json_news_parser(filename):
    """
    Counts words in news title and description
    """
    with open(filename, encoding='utf8') as news_json:
        news = json.load(news_json)
        word_dict = {}
        for item in news['rss']['channel']['items']:
            title_word_list = item['title'].split()
            description_word_list = item['description'].split()
            word_dict = count_words_in_list(title_word_list, word_dict)
            word_dict = count_words_in_list(description_word_list, word_dict)
        return word_dict


def xml_news_parser(filename):
    """
    Counts words in news title and description
    """
    word_dict = {}
    with open(filename, encoding='utf8') as news_xml:
        tree = ET.parse(filename)
        root = tree.getroot()
        titles = root.findall('channel/item/title')
        descriptions = root.findall('channel/item/description')
        for title in titles:
            title_word_list = title.text.split()
            word_dict = count_words_in_list(title_word_list, word_dict)
        for description in descriptions:
            description_word_list = description.text.split()
            word_dict = count_words_in_list(description_word_list, word_dict)
        return word_dict



def count_words_in_list(word_list, word_dict={}, letters=6):
    for word in word_list:
        if len(word) > letters:
            try:
                if word not in word_dict.keys():
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
            except AttributeError:
                pass
    return word_dict

def find_top_10_words(word_dict):
    top_10_words_list = []
    for word in sorted(word_dict, key=word_dict.get, reverse=True):
        top_10_words_list.append((word, word_dict[word]))
        if len(top_10_words_list) >= 10:
            break
    return top_10_words_list



afr_news_word_dict_json = json_news_parser('Homework_3-1\\files\\newsafr.json')
afr_news_word_dict_xml = xml_news_parser('Homework_3-1\\files\\newsafr.xml')
print(find_top_10_words(afr_news_word_dict_json))
print(find_top_10_words(afr_news_word_dict_xml))