import requests
from bs4 import BeautifulSoup
import re

class Crawl:

    def __init__(self):
        pass
    
    def button_num(self):
        pass

    def station_num(self):
        url = 'https://etk.srail.co.kr/hpg/hra/01/selectMapInfo.do?isAll=Y&other=&target=dpt&pageId=TK0101010000'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        p = re.compile('\d+')
        station_num = {}

        for tag in soup.select('.map a'):
            station_num[tag.text] = p.findall(tag['onclick'])[0]
            
        return station_num
