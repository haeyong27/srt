import re
import requests
from bs4 import BeautifulSoup

class URLGenerator():

    def __init__(self, startStn, endStn, date, numAdult, numKid, time_start, time_end):
        self.startStn = startStn
        self.endStn = endStn
        self.date = date
        self.numAdult = numAdult
        self.numKid = numKid
        self.time_start = time_start
        self.time_end = time_end

        #extract station num
        # ex) '수서': '0551', '동탄': '0552', 
        url_sample = 'https://etk.srail.co.kr/hpg/hra/01/selectMapInfo.do?isAll=Y&other=&target=dpt&pageId=TK0101010000'
        response = requests.get(url_sample)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        p = re.compile('\d+')
        station_num = {}

        for tag in soup.select('.map a'):
            station_num[tag.text] = p.findall(tag['onclick'])[0]

        self.station_num = station_num


    def urlGenerate(self):

        url_base = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
        url_params = 'stlbTrnClsfCd=05&trnGpCd=109&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCd=0015&arvRsStnCd=0552&dptDt=20190205&dptTm=100000&psgInfoPerPrnb1=1&psgInfoPerPrnb5=0'
        
        #parse params
        params = {}
        for i in url_params.split('&'):
            key, value = i.split('=')
            params[key] = value

        params['dptRsStnCd'] = self.station_num[self.startStn]
        params['arvRsStnCd'] = self.station_num[self.endStn]
        params['dptDt'] = self.date
        params['psgInfoPerPrnb1'] = self.numAdult
        params['psgInfoPerPrnb5'] = self.numKid
        
        if (int(self.time_start) < 10):
            params['dptTm'] = '0' + str(self.time_start) + '0000'
        else:
            params['dptTm'] = str(self.time_start) + '0000'

        url = url_base
        for i in params:
            url += '&' + i + '=' + str(params[i])
        
        return url

if __name__ == '__main__':
    url = URLGenerator('동탄', '부산', '20190306', 2, 1, 9, 15)
    print(url.urlGenerate())