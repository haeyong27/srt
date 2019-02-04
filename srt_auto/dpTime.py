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


    def find_dpTime(self, start=5, end=10):
        time_list = self.search_dpTime()
        selected_time = []
        for a, time in enumerate(time_list):
            if (time>=start and time<=end):
                selected_time.append(a)

        return selected_time


# url = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000&stlbTrnClsfCd=05&trnGpCd=109&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCd=0015&arvRsStnCd=0552&dptDt=20190206&dptTm=140000&psgInfoPerPrnb1=3&psgInfoPerPrnb5=2#n'
# a = ReserveButton(url)
# t = a.find_dpTime(17, 19)
# print(t)