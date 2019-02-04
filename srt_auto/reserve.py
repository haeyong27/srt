import time
from selenium import webdriver
import url_generator, dpTime, sendingMail

class Reserve():
    def __init__(self, phone = 0):
        #창 열기
        self.phone = phone
        self.driver = webdriver.Chrome('./chromedriver')
        self.url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
        self.driver.get(self.url)
        
        

    def login(self, srt_id, pw, n):

        tag_category = self.driver.find_element_by_id('srchDvCd{}'.format(n))
        tag_category.click()

        tag_id = self.driver.find_element_by_id('srchDvNm0{}'.format(n))
        tag_id.send_keys(str(srt_id))

        tag_pw = self.driver.find_element_by_id('hmpgPwdCphd0{}'.format(n))
        tag_pw.send_keys(str(pw))

        tag_pw.submit()
        
        
    def get_reserve_url(self, start_stn, end_stn, date, adult, kid, dp_time):
        #원하는 조건 만족하는 예약 창 열기
        c = url_generator.UrlGen(start_stn, end_stn, date, adult, kid, dp_time)
        self.url = c.generate()
        return self.url
        

    def find_dpTime_click(self, start, end):
        time_list = dpTime.ReserveButton(self.url).search_dpTime()
        selected_time = []
        for a, t in enumerate(time_list):
            if (t>=start and t<=end):
                selected_time.append(a)
        for i in selected_time:
            b = self.driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, {}, \'1\', \'1101\', true, false); return false;"]'.format(i))
            if (len(b) > 0):
                b[0].click()
        self.driver.refresh()
                

    def complete(self):
        try:
            self.driver.find_element_by_class_name('alert_box')
            sendingMail.Mail(self.phone)
            return 1
        except:
            return 0


def llast(phone, idd, pw, n, start, end, date, ts, te, adult, kid):

    a = Reserve(phone)
    a.login(idd, pw, n)
    url = a.get_reserve_url(start, end, date, adult, kid, ts)
    a.driver.get(url)
    time.sleep(1)
    while(True):
        a.find_dpTime_click(ts, te)
        if (a.complete()==1):
            break

a = Reserve()
llast('1022969002','1785043400',  'kimdo82!!',1,'부산','천안아산','20190205',12,15,2,0)
# a.last('1080810724','1582373708', 'dltmdrl87!',1,'광주송정','수서','20190205',18, 18, 1,0)
# a.last('1089739468','1592364224', 'qwert1234',1,'부산','수서','20190205',13,16,2,0)
# a.last('1023803559','1580376558', '7135',1,'광주송정','동탄','20190205',14,23,2,1)
# a.last('1033131806','happygiki', 'kcb1231',1,'나주','동탄','20190205',18, 18,3,0)
							