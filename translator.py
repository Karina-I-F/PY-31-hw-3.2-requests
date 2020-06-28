import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(input_file, output_file, source_lang, to_lang='ru'):
    """
    Принимает файл с текстом, файл для результата,
    язык с которого перевести,
    язык на который перевести (по-умолчанию русский)
    """
    with open(input_file, encoding='utf-8') as source:
        with open(output_file, 'w', encoding='utf-8') as result:
            text = source.read()
            params = dict(key=API_KEY, text=text, lang=source_lang + '-{}'.format(to_lang))
            response = requests.get(URL, params=params)
            json_ = response.json()
            result.write(''.join(json_['text']))
            return output_file


if __name__ == '__main__':
    translate_it('DE.txt', 'translated text.txt', 'de')
    translate_it('ES.txt', 'translated text2.txt', 'es')
    translate_it('FR.txt', 'translated text3.txt', 'fr')
