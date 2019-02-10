import requests

API_KEY = 'trnsl.1.1.20190210T064739Z.bb56526e07131ddc.1d469aae976873e44c3dac6181031b24583ad196'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(file_to_translate, file_result, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """
    with open(file_to_translate, encoding='utf8') as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}',
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    result_text = ''.join(json_['text'])
    with open(file_result, 'w', encoding='utf8') as result:
        result.write(result_text)
    return result_text


file_path = 'Homework_3_2\{}\{}.txt'
langs = ['DE', 'ES', 'FR' ]

for lang in langs:
    file_to_translate = file_path.format('files_to_translate', lang)
    file_result = file_path.format('files_result', lang + '_result')
    translated_text = translate_it(file_to_translate, file_result, lang.lower())
    print(translated_text)



