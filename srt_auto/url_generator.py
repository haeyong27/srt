from . import station_num

class URL_gen():
    def __init__(self, start='부산', end='동탄', date='20190205', person = 1, dpTime = 0):
        c = station_num.StationNum()
        self.station_dic = c.station_num()
        self.url_base = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
        self.url = 'dptRsStnCd=0552&arvRsStnCd=0020&stlbTrnClsfCd=05&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCdNm=%EB%8F%99%ED%83%84&arvRsStnCdNm=%EB%B6%80%EC%82%B0&dptDt=20190203&dptTm=105900&chtnDvCd=1&psgInfoPerPrnb1=1&psgInfoPerPrnb5=0&psgInfoPerPrnb4=0&psgInfoPerPrnb2=0&psgInfoPerPrnb3=0&locSeatAttCd1=000&rqSeatAttCd1=015&trnGpCd=109'
        self.start = start
        self.end = end
        self.date = date
        self.person = person
        self.dpTime = dpTime
        self.start_stn_num = self.station_dic[start]
        self.end_stn_num = self.station_dic[end]

    def generate(self):
        params = self.parse_url()
        params['dptRsStnCd'] = self.start_stn_num
        params['arvRsStnCd'] = self.end_stn_num
        params['dptRsStnCdNm'] = self.start
        params['arvRsStnCdNm'] = self.end
        params['dptDt'] = self.date
        params['psgInfoPerPrnb1'] = self.person
        if (self.dpTime < 10):
            params['dptTm'] = '0' + str(self.dpTime) + '0000'
        else:
            params['dptTm'] = str(self.dpTime) + '0000'

        url = self.url_base
        for i in params:
            url += '&' + i + '=' + str(params[i])

        return url


    def parse_url(self):
        d = {}
        for i in self.url.split('&'):
            a, b = i.split('=')
            d[a] = b
        return d

if __name__ == "__main__":
    a = URL_gen('부산', '동탄', '20190205')
    print(a.generate())




    