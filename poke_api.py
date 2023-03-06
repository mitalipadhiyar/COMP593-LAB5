

import requests


def main():
    url=get_poke_name('MITALI')
    pass 
def get_poke_name(name):

    poke_name=str(name).strip().lower()
    PokeMon_url=f'https://pokeapi.co/api/v2/pokemon/{poke_name}'

    resp_msg=requests.get(PokeMon_url)

    print(f"Getting information for {poke_name}...",end='')

    if resp_msg.ok:
        print('success')
        return resp_msg.json()
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")


    pass


if __name__ == '__main__':
    main()






 