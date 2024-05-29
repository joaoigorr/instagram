import requests
import json

def get_data_instagram(account):
    url = "https://ig-public-info.p.rapidapi.com/1vk79zjt34dums9m8ce924x7mfbs8fg9"

    querystring = {"account":account}

    headers = {
	"x-rapidapi-key": "3ddb9a9c0emsh1f6885b791607eap167752jsn77c1e460cb88",
	"x-rapidapi-host": "ig-public-info.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    text = response.text
    texto = text.replace('\n', '')
    json_data = json.loads(texto)
    return json_data