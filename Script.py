from pastebin_api import post_new_paste
from poke_api import get_poke_name
import sys




def main():
    name=get_pokemon_name()
    info=get_poke_name(name)
    

    if info:
       title, body_text=poke_paste(info)
       paste_url=post_new_paste(title,body_text,'1M')
       print(paste_url)
    return

def get_pokemon_name():
    num_params=len(sys.argv)-1
    if num_params>0:
        return sys.argv[1]
    else:
        print("Error: Missing pokemon name.")
def poke_paste(info):
    name=info['name'].capitalize()
    abilities_name=[ability['ability']['name'] for ability in info['abilities']]
    print (abilities_name)
    abilities_list= '- ' + '\n '.join(abilities_name)
    title= f"{name}'s Abilities"
    body=abilities_list

    return title,body 




if __name__ == '__main__':
    main()