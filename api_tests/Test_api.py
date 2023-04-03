import pytest
from api import *
import requests

class Test_api:
    #The test checks if the status code is successful when searching for the word 'ignore'
    def test_status_the_word_ignore(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/ignore'
        response = requests.get(url)

        assert 200 <= response.status_code < 400

    # The test checks if the status code is successful when searching for the word 'yauza' (the word 'yauoza' doesn't exist in website)
    def test_status_the_word_yauza_N(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/yauza'
        response = requests.get(url)


        assert response.status_code==404