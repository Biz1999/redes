import json

def update_json(updateData, filename="db/Server.json"):
    with open(filename) as json_file:
        data = json.load(json_file)

        for i in range(len(data['users'])):
            if data['users'][i]['id'] == updateData['id']:
                print('to aqui')
                data['users'][i]['nome'] = updateData['nome']
                data['users'][i]['sobrenome'] = updateData['sobrenome']
                data['users'][i]['img'] = updateData['img']
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    json_file.close()
    f.close()
