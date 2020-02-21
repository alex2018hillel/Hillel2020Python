import random
import requests

RCODE = [200, 300, 403, 404, 500]
URL = 'http://httpbin.org/status/{st}'

def retry(try_count):
    def create_retry(func):
        def wrapper(*args):
            counter_200 = 0
            counter = 0
            while counter != try_count:
                counter += 1
                response = (func(*args))
                if response == 200:
                    print('{} - Success'.format(response))
                    counter_200 += 1
                elif response == 300:
                    print('{} - Redirection'.format(response))
                elif response == 403 or 404:
                    print('{} - Client Errors'.format(response))
                elif response == 500:
                    print('{} - Server Errors'.format(response))
            print(counter_200)

            if counter_200 == counter:
                return 'Ok'
            else:
                return "ERROR"
        return  wrapper
    return create_retry

@retry(5)
def get_request():
    code = random.choice(RCODE)
    resp = requests.get(URL.format(st=code))
    return resp.status_code

print(get_request())

exit()






       #     return resp.status