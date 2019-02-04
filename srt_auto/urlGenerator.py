import stationNum

class UrlGen():
    def __init__(self, start='부산', end='동탄', date='20190205', adult=1, kid=0, dp_time = 0):
        c = stationNum.StationNum()
        self.station_dic = c.station_num()
        self.url_base = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
        self.url = 'stlbTrnClsfCd=05&trnGpCd=109&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCd=0015&arvRsStnCd=0552&dptDt=20190205&dptTm=100000&psgInfoPerPrnb1=1&psgInfoPerPrnb5=0'
        self.date = date #날짜
        self.adult = adult #인원
        self.kid = kid
        self.dp_time = dp_time #어느 시간 이후로 예약할지
        self.start_stn_num = self.station_dic[start] #역 번호
        self.end_stn_num = self.station_dic[end] #역 번호


    def parse_url(self):
        dic = {}
        for i in self.url.split('&'):
            key, value = i.split('=')
            dic[key] = value
        return dic

        
    def generate(self):
        params = self.parse_url()
        params['dptRsStnCd'] = self.start_stn_num
        params['arvRsStnCd'] = self.end_stn_num
        params['dptDt'] = self.date
        params['psgInfoPerPrnb1'] = self.adult
        params['psgInfoPerPrnb5'] = self.kid
        if (int(self.dp_time) < 10):
            params['dptTm'] = '0' + str(self.dp_time) + '0000'
        else:
            params['dptTm'] = str(self.dp_time) + '0000'

        url = self.url_base
        for i in params:
            url += '&' + i + '=' + str(params[i])
        
        return url