import bs4
import time
import requests
import logging
import collections
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')

ParseEsult = collections.namedtuple(
    'Parseresult',
    (
        'name',
        'url'
    ),
)
# class Bot:
#     def __init__(self):
#         self.driver = webdriver.Firefox(executable_path=r'C:\Intel\geckodriver.exe')
#         self.navigate()
#
#     def navigate(self):
#         self.driver.get('https://www.pinterest.com/pin/735986764087357271/')

class Client:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Intel\geckodriver.exe')
        #####  !!!!!!!!!!!!!  self.navigate()
        # self.session = requests.Session()
        # self.session.headers = {
        #     'user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.17 Safari/537.36 OPR/68.0.3609.0 (Edition developer)'
        # }
        # self.result = []
        self.text = self.driver.page_source
        #self.images = self.driver.find_element_by_xpath("//div[@id='__PWS_ROOT__']//div[@class='gridCentered']//img").get_attribute()
        #self.images = self.driver.find_element_by_xpath("//div[@id='__PWS_ROOT__']").find_element_by_xpath("//div[@class='gridCentered']").find_element_by_tag_name('img').text


    def navigate(self):
        self.driver.get('https://www.pinterest.com/pin/735986764087357271/')
        time.sleep(5)
        return self.driver.title

    # def load_page(self, page: int = None):
    #         url = 'https://www.pinterest.com/pin/735986764087357271/'
    #
    #         res = self.session.get(url=url,cookies =
    #         {'_pinterest_sess':'TWc9PSZHeG85OUxhbFd5bzFNU0NRS3BmMEY2U1dyNWFoUHBEMTh5eFZQdnJZeEwwWlIxUHRMbU9kVDZ2ak1ZTDhQVkZ0UjIycTRFNUsvUEhyQjV5UCtNZ3M0Zi9SUjBJWHZyS1A3ejlBK01oQS9iVkNPNlRmTitRMVNEMkNnRjVqRk4vU05OdUE1SUp0cnB6cEkyY0tUV0cvbkZ0Q2ZsRHRBWW1ZeGlOOFRNS2lNNndqQjdXRDJQME1SZzk2VGgzb0Z2Rjl5azVLK0cxYlduWlZkdHd5R1dyZGtVN2hRRjBYZG1QM05uejNuTVduVmZ3WmY4N20wR2ZWQlZiaVVKSkZRWVdTNk0zQUhqMFBtb0FKRDA3c2xoZVlXWHlKa1dEQUZ0ckFnQ2FodU9tSTRBQnh0Wmk0dkNVR3IwMit2UlM1U1JtZGdFckFBWk5neXB6L3NzcFVjK1p6OUYwNlhoc3NSdG5NbGlFbjVvQkp1ZWhTSXVjUnlQbWorM3RpZ1drYmYrUTNLZVllMGVPQkxPa3BWdk1HV010bGRWa2hCNnF2Nm9uZFRxVDJyU1NvWlJST3JPSWVzSVpncnJvNmM2eXB2SU1wTy9DZGtIRVJ3aXFNNWRvZDBDamJ5Szc4eFBHakowdkNndmxvaTVsNUhQZ0p4SnBQNlBwVGR3UnBNa24wZFdJZ3ppWXhZZW9rczhLc3BiZmpGWG9rMlE0bE5rT0Y1UHA4U0wxeEdWanZsQTBMRHNIZnRlQTI5WjM1QURhUzBqSUt6eS9VR1VDM3pCYitzQ1JoUjhIS2lLYWIrcmVqRTF2TmozeVR0VThlNUpGV1FaZFdNWXhkaTNGV1BqTXd1ZW0rWk1oN2d0SUpsbXYrODNCNDJxZGl3Zks0ZWZLR3VNd0NqUDFYVGtFclJRQzBXSm4vZW9jTkpmb3dOWExYNHR3cWpMY0I1VFcxMHVZb3FHOElnTFN5KzI1cW1sNWM2bGVseXR5SG5iajNvY2RKZklhNWtJUVZGcENWRXk2dWNlclE4aGl6N1NuVGdxYkkvOTExTTdqSHpoaFRKMW8rZUNIMzhJc0hvQzNzMTQ5VjdJUTk0bWVaRXVPMEZxUkZiZUgrJnA1T1l1bE41V0FoZW1zNkhCbXBJNytENjFVQT0='})
    #         print(res.status_code)
    #         res.raise_for_status()
    #         return res.text

    def parse_page(self, text: str):
        print('============parse_page========')
        #soup = bs4.BeautifulSoup(text, 'lxml')
        soup = bs4.BeautifulSoup(self.text, 'html.parser')
        container = soup.select('div.__PWS_ROOT__')
        print(container)
        #container = soup.select("//div[@id='__PWS_ROOT__']//div[@class='gridCentered']//img")
        # for i in self.images:
        #     print(i)
        # for each_div in soup.findAll('div',{'class':'Grid__Container'}):
        #     print(each_div)



        #soup.('a') # [<a ..>, ..]
        # d = soup.find_all('div', class='XiG zI7 iyn Hsu')

        # for link in soup.find_all('img'):
        #     print(link.get('href'))
        # soup.find_all(href=re.compile("elsie"), id='link1')
        # container = soup.find_all('div', {'class': ['Yl-', 'MIw','Hb7']})
        # print(container)
        # for block in container:
        #     self.parse_block(block=block)

    def parse_block(self,block):
        # logger.info(block)
        # logger.info('='*100)

        #url_block = block.select_one()
        url_block = block.select_one('img.hCL kVc L4E MIw')
        if not url_block:
            logger.error('no url_block')
            return

        url = url_block.get('href')
        if not url:
            logger.error('no href')
            return

        logger.info('%s', url)

    def run(self):
        head = self.navigate()
        #text = self.load_page()
        print(head)
        self.parse_page(text=self.text)

    def quit(self):
        time.sleep(50)
        self.driver.quit()


if __name__ == '__main__':
    #b = Bot()
    parser = Client()
    parser.run() #https://ru.traveltables.com/img/flags_gifs/
    parser.quit()

