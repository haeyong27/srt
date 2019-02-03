import requests
from bs4 import BeautifulSoup



class ReserveButton:
    def __init__(self, request):
        response = requests.get(request)
        html = response.text
        self.soup = BeautifulSoup(html, 'html.parser')
    
    def search_dpTime(self):
        i = 0
        for tag in self.soup.select('.time'):
            if i%2 == 0: 
                print(tag.text)
            i += 1

if __name__ == '__main__':
    url = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000&dptRsStnCd=0020&arvRsStnCd=0552&stlbTrnClsfCd=05&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCdNm=부산&arvRsStnCdNm=동탄&dptDt=20190205&dptTm=000000&chtnDvCd=1&psgInfoPerPrnb1=1&psgInfoPerPrnb5=0&psgInfoPerPrnb4=0&psgInfoPerPrnb2=0&psgInfoPerPrnb3=0&locSeatAttCd1=000&rqSeatAttCd1=015&trnGpCd=109'
    a = ReserveButton(url)
    a.search_dpTime()