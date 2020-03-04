import json
import os
import requests
from pathlib import Path
# path = Path('test.json')
# data = json.loads(path.read_text(encoding='utf-8'))
# print(data)
# data['level2'].update({'timestamp':0.015,'movement':'type_2'})
# path.write_text(json.dumps(data), encoding='utf-8')
# data = json.loads(path.read_text(encoding='utf-8'))
# print(data)
def request(i):
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    print(r.content)
    return (r.content)

for i in range(3):
    data = json.loads(request(i))
    path = Path("test" + str(i) + ".json")
    path.write_text(json.dumps(data), encoding='utf-8')
#--------------------------------------------------------------------#

templates = {}
for i in range(3):
    with open("test" + str(i) + ".json") as f:
        file_content = f.read()
        templates.update(json.loads(file_content))
        print(templates)
path = Path("1/test.json")
path.write_text(json.dumps(templates), encoding='utf-8')
#--------------------------------------------------------------------#

dir_path = os.getcwd()
print(dir_path)
split_dir_path = list(dir_path.split('\, /'))
abspath = str(os.path.abspath (r'1/test.json'))
print(abspath)
split_abspath = list(abspath.split('/'))
print(list(split_abspath))
print(split_abspath - split_dir_path)
#for item in split_abspath:


#     list_id = []
# for l in body:
#     if l[0] == site_name:
#         list_id.append(l[1])
# number = len(set(list_id))


# list_id = set([l[1] for l in body if l[0] == site_name]




# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))


# def find_str(d):
#     result = []
#     for section, commands in d.items():
#         print(section)
#     # print('\n'.join(commands))
#     return result



    # print(find_str(json.loads(request(i))))

# data.update({'timestamp':0.015,'movement':'type_2'})
