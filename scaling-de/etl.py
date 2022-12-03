import json
import requests

country_list = [0,1,2]
base_url = 'http://127.0.0.1:5000'
users_endpoint = f'{base_url}/users'
movements_endpoint = f'{base_url}/movements'

def etl():
    for country in country_list:
        print(f'Getting users for country {country}')
        r = requests.get(f'{users_endpoint}/{country}')
        user_list = r.json()['users']
        for user in user_list:
            print(f'Getting movements for user {user}')
            r = requests.get(f'{movements_endpoint}/{user}')
            moves_list = r.json()['movements']
            print(moves_list)

if __name__ == '__main__':
    etl()