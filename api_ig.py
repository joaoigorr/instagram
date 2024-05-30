import requests
import json
from instascrap import InstaScraper

def get_data_instagram(account):
    url = "https://ig-public-info.p.rapidapi.com/1vk79zjt34dums9m8ce924x7mfbs8fg9"

    querystring = {"account":account}

    headers = {
	"x-rapidapi-key": "796a4a0384msh585e39c01965b88p149ce1jsnf254eb11a77d",
	"x-rapidapi-host": "ig-public-info.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    text = response.text
    print(response)
    print(text)
    texto = text.replace('\n', '')
    json_data = json.loads(texto)
    return json_data

def get_data_instagram_v2(account):

    scraper = InstaScraper()
    input_data = {"usernames": [account]}
    json_data = scraper.Scraper(input_data)
    return json_data
