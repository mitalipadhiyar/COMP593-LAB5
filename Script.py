from pastebin_api import post_new_paste
from poke_api import get_poke_name
import sys

def main():
    name=get_pokemon_name()
    info=get_poke_name(name)
    

def get_pokemon_name():
    num_params=len(sys.argv)-1
    if num_params>0:
        return sys.argv[1]
    else:
        print("Error: Missing pokemon name.")
def poke_paste(info):
    return 




if __name__ == '__main__':
    main()