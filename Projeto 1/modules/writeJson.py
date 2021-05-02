import json
from modules.createUser import create_user_page

def write_json(newData, filename="db/Server.json"):
    with open(filename) as json_file:
        data = json.load(json_file)
        newData['id'], newData['uri'] = create_user_page()
        data['users'].append(newData)
        data['count'] +=1
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    
    json_file.close()
    f.close()

