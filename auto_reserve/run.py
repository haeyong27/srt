import reserve

# a = reserve.Reserve('01021843577')
# a.login('01021843577', 'sphv8401', 3)
# url = a.get_reserve_url('동탄', '부산', '20190301', 1, 0, 8)
# a.driver.get(url)
# time.sleep(1)
# while(True):
#     a.find_dpTime_click(8, 20) #몇시 부터 몇시 사이의 표를 예매할건지
#     time.sleep(1)
#     if (a.complete()==1): #예매 완료되면 종료
#         break

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
            if self.res.complete == 1:
                break

if __name__=='__main__':
    a = Run('01021843577', '01021843577', 'sphv8401', '동탄', '부산', '20190306', 2, 1, '09:59', '14:10')
    a.run()