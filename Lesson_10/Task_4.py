import json
import os
import requests
from pathlib import Path

def request(i, base_url):
    r = requests.get(base_url+ str(i))
    print(r.content)
    return (r.content)

class JsonRuner:
    BASE_URL = 'http://swapi.co/api/people/'
    OUTPUT = '../3/test.json'
    def __init__(self):
        self.N = 3

    def write_json(self):
        for i in range(self.N):
            data = json.loads(request(i, self.BASE_URL))
            path = Path("test" + str(i) + ".json")
            path.write_text(json.dumps(data), encoding='utf-8')
#--------------------------------------------------------------------#

    def read_json(self):
        templates = {}
        for i in range(self.N):
            with open("test" + str(i) + ".json") as f:
                file_content = f.read()
                templates.update(json.loads(file_content))
                print(templates)
        path = Path(self.OUTPUT)
        path.write_text(json.dumps(templates), encoding='utf-8')
    #--------------------------------------------------------------------#

    def find_abspath(self):
        abspath = str(os.path.abspath (self.OUTPUT))
        print(abspath)
    #-------------------------------------------------------------------#

    def find_relative_path(self):
        relative_path = os.path.relpath(os.path.abspath (self.OUTPUT))
        print(relative_path)
    #-------------------------------------------------------------------#

if __name__ == '__main__':
    JR = JsonRuner()
    JR.write_json()
    JR.read_json()
    JR.find_abspath()
    JR.find_relative_path()





