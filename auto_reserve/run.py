import reserve

class Run():
    def __init__(self, phone, id1, pw, dptStn, arrStn, date1, numAdult, numChild, fromTime, toTime):
        self.phone = phone
        self.id1 = id1
        self.pw = pw
        self.dptStn = dptStn
        self.arrStn = arrStn
        self.date1 = date1
        self.numAdult = numAdult
        self.numChild = numChild
        self.fromTime = fromTime
        self.toTime = toTime
        self.res = reserve.Reserve(self.phone, self.fromTime, self.toTime)

    def run(self):
        #로그인 유형 아직 어떻게할지 못정함
        self.res.login(self.id1, self.pw, 3)
        # time.sleep(1)
        self.res.get_reserve_url(self.dptStn, self.arrStn, self.date1, self.numAdult, self.numChild)
        self.res.find_dptime()
        #예약화면으로 넘어갈 때 까지 클릭 반복하기, 아래 코드는 한번만 실행
        while(True):
            self.res.click_dptime()
            if self.res.complete() == 1:
                break
        
        self.res.driver.quit()

if __name__=='__main__':
    a = Run('11', '01021843577', 'sphv8401', '수서', '부산', '20190306', 1, 0, '09:59', '14:10')
    a.run()
