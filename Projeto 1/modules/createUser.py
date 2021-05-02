import json
from modules.page import sendPage
from random import randint as rd


def create_user_page(filename="db/Server.json"):

    with open(filename) as json_file:
        data = json.load(json_file)
        index = len(data['users']) 
        print(index)
        urn = rd(0, 9999)
        new_file = f'pages/users/{urn}.html'
        with open(new_file, 'w', encoding="utf-8") as new:
            new.write(sendPage(urn))
    json_file.close()
    new.close()

    return f'{index}', f'/{urn}'



