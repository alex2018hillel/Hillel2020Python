import json
import os
import requests
from pathlib import Path
from os.path import relpath

def request(i, base_url):
    #r = requests.get('http://swapi.co/api/people/'+ str(i))
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
        #path = Path("1/test.json")
        path = Path(self.OUTPUT)
        path.write_text(json.dumps(templates), encoding='utf-8')
    #--------------------------------------------------------------------#

    def find_abspath(self):
        abspath = str(os.path.abspath (self.OUTPUT))
        print(abspath)
    #-------------------------------------------------------------------#

    #relative_path = os.path.realpath(r'1/test.json')
    def find_relative_path(self):
        relative_path = os.path.dirname(os.path.realpath(self.OUTPUT))
        #relative_path = os.path.realpath(self.OUTPUT)
        print(relative_path)
    #-------------------------------------------------------------------#


    # print(os.path.realpath(r'1/test.json'))
    # print(os.path.realpath(r'\Lesson\test.json'))

    # dir_path = str(os.getcwd())
    # split_abspath = abspath.split(dir_path)
    # print(split_abspath[1])

if __name__ == '__main__':
    JR = JsonRuner()
    JR.write_json()
    JR.read_json()
    JR.find_abspath()
    JR.find_relative_path()





