import random
import requests

RCODE = [200, 300, 403, 404, 500]
URL = 'http://httpbin.org/status/{st}'

def create_retry(try_count):
    def retry(func):
        def wrapper(*args):
            func(*args)
            while args != 0:
                args -=1

            print(try_count)
            #5 popytok(reduce)
        return  wrapper
    return create_retry()

@create_retry(5)
def get_request():
    code = random.choice(RCODE)
    print(code)
    resp = requests.get(URL.format(st=code))
    print(resp.status_code)
    return resp.status_code

print(get_request)

exit()






       #     return resp.status