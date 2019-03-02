import requests
import math
from bs4 import BeautifulSoup
import url_gen


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
                timeList.append(f'{a}:{b}')
            i += 1

        time_dic = {}
        for i, time in enumerate(timeList):
            time_dic[i] = time

        return time_dic


if __name__ == '__main__':
    url_generator = url_gen.URLGenerator('동탄', '부산', '20190306', 2, 1, 9, 15)
    url = url_generator.urlGenerate()
    print(url)
    button = ReserveButton(url)
    time_dic = button.search_dpTime()
    for k, v in time_dic.items():
        print(k, v)