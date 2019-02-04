import requests
import math
from bs4 import BeautifulSoup

class ReserveButton:

    def __init__(self, request):
        response = requests.get(request)
        html = response.text
        self.soup = BeautifulSoup(html, 'html.parser')
    

    def search_dpTime(self):
        i = 0
        timeList = []
        for tag in self.soup.select('.time'):
            if i%2 == 0: 
                a, b = tag.text.split(':')
                timeList.append(int(a)+math.ceil(int(b)/60.))
            i += 1
        return timeList
