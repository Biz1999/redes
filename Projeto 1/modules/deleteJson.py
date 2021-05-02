import os
import json

def delete_json(deleteData, filename="db/Server.json"):
    with open(filename) as json_file:
        data = json.load(json_file)

        for i in range(len(data['users'])):
            if data['users'][i]['id'] == deleteData:
                path = data['users'][i]['uri']
                try:
                    os.remove(f'pages/users{path}.html')
                except OSError:
                    print('Arquivo nao existe')
                data['users'].pop(i)
                break

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    json_file.close()
    f.close()
