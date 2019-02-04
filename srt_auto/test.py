import time
import reserve


class Test:
    def __init__(self, phone, id, pw, start_stn, end_stn, date, adult, kid, dp_time, startTime, endTime):
        
        self.phone = phone
        self.id = id
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
        a.login(self.id, self.pw)
        a.get_reserve_url(self.start_stn, self.end_stn, self.date, self.adult, self.kid, self.dp_time)
        time.sleep(2)
        while(True):
            a.find_dpTime_click(self.startTime, self.endTime)
            a.refresh()
            if (a.complete()==1):
                break

