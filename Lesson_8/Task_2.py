import os
from tld import get_tld

TXT_FOLDER = []
for top, dirs, files in os.walk("lesson6"):
    for nm in files:
        TXT_FOLDER.append(os.path.join(top, nm))

SORTING_TXT_FOLDER = sorted(TXT_FOLDER)
count = 0
all_list = []

for i in range(0,len(SORTING_TXT_FOLDER)):
    path = SORTING_TXT_FOLDER[count]
    count += 1
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')
            l = line.split('\t')
            a, *b = l[3], l[4], l[7]
            all_list.append([a, b])

def data_preparation(city):
    body = []
    for i in all_list:
        if i[0] == city:
            value = i[1]
            try:
                url = value[1].split('/')[2]
                try:
                    name = get_tld(url)
                except:
                    name = url
                body.append([name,value[0]])
            except:
                pass
    return body

def record_to_file(body):

    list_requests = []
    for l in body:
        list_requests.append(l[0])

    list_id = []
    for site_name in set(list_requests):
        for l in body:
            if l[0] == site_name:
                list_id.append(l[1])
        number = len(set(list_id))
        line = '{}{}{}'.format(site_name, '\t', str(number))
        try:
            myfile.write(line+'\n')
        except:
            chunk = line.encode('utf-16')
            myfile.write(chunk.decode('cp1251', 'replace')+'\n')

all_city = []
for i in all_list:
    all_city.append(i[0])

for city in set(all_city):
    file_name = city + ".tsv"
    print(file_name)
    myfile = open(file_name, 'w')

    record_to_file(data_preparation(city))
