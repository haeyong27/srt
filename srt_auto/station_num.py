import re
import requests
from bs4 import BeautifulSoup

class StationNum:

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
