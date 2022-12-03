import json
import requests
import click

country_list = [0,1,2]
base_url = 'http://127.0.0.1:5000'
users_endpoint = f'{base_url}/users'
movements_endpoint = f'{base_url}/movements'

def etl(country):
    print(f'Getting users for country {country}')
    r = requests.get(f'{users_endpoint}/{country}')
    user_list = r.json()['users']
    for user in user_list:
        print(f'Getting movements for user {user}')
        r = requests.get(f'{movements_endpoint}/{user}')
        moves_list = r.json()['movements']
        print(moves_list)

@click.command()
@click.option('--country', required= True,help='country to query')
def main(country):
    etl(country)

if __name__ == '__main__':
    main()