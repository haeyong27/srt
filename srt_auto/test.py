import time
import reserve


class Test:
    def __init__(self, phone, srt_id, pw, start_stn, end_stn, date, adult, kid, dp_time, startTime, endTime):
        
        self.phone = phone
        self.srt_id = srt_id
        self.pw = pw
        self.start_stn = start_stn
        self.end_stn = end_stn
        self.date = date
        self.adult = adult
        self.kid = kid
        self.dp_time = dp_time
        self.startTime = startTime
        self.endTime = endTime
        
        
    def execute_reserve(self):

        a = reserve.Reserve(self.phone)
        a.login(self.srt_id, self.pw)
        time.sleep(2)
        a.get_reserve_url(self.start_stn, self.end_stn, self.date, self.adult, self.kid, self.dp_time)
        time.sleep(2)
        while(True):
            a.find_dpTime_click(self.startTime, self.endTime)
            a.refresh()
            if (a.complete()==1):
                break

a = Test('01021843577', '1785043400', 'kimdo82!!', '부산', '천안아산', 20190205, 2, 0, 12, 12, 15)
a.execute_reserve()
