import requests
import translator

YD_API_KEY = 'OAuth AgAAAABCm-vHAADLW1fx4HWva0ODvej6T2eYXQE'
YD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


def get_href(file):
    headers = {'Authorization': YD_API_KEY}
    params = {'path': file,
              'overwrite': 'true'
              }
    response = requests.get(YD_URL, headers=headers, params=params).json()
    return response['href']


def yd_upload(up_link, file):
    URL = up_link
    headers = {'Authorization': YD_API_KEY}
    params = {'path': file}
    with open(file, encoding='utf-8') as up_file:
        content = up_file.read().encode('utf-8')
        requests.put(URL, data=content, headers=headers, params=params)


if __name__ == '__main__':
    def main(file):
        yd_upload(get_href(file),
                  translator.translate_it('DE.txt', file, 'de'))


    main('translated text.txt')
