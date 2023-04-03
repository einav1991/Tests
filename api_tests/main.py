import requests


#Return True if the status of the website passed 200-399 and ERROR if Failed 400-599
def status(request_url):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/ignore'
    response = requests.get(url)

    if 200 <= response.status_code < 400:
        print('success')
    else:
        print('ERROR')


#Return True if the status of the website passed 200-399 and ERROR if Failed 400-599
def false_status(request_url):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/yauoza'
    response = requests.get(url)

    if 200 <= response.status_code < 400:
        print('success')
    else:
        print('ERROR')