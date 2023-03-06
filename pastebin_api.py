import requests 

APIPOST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_APIKEY = 'Oe8f2bAXVwnM9k0Ml3GD4ERzoSnluNbo'
def main():
    paste_url = post_new_paste('New Pastebin', 'Hello World!',)
    pass

def post_new_paste(title, body_text, expiration='1M', listed=True):

    params = {
        'api_dev_key': DEVELOPER_APIKEY,
        'api_option' : 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }

    print("Posting new paste to PasteBin...", end='')
    resp_msg = requests.post(APIPOST_URL, data=params)

    if resp_msg.ok:
        print('success')
        print(f'URL of new paste : {resp_msg.text}')
        return resp_msg.text
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")




    return  
if __name__ == "__main__":
    main()
    