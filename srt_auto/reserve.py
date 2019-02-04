import time
from selenium import webdriver
import url_generator, dpTime, sendingMail

class Reserve():
    def __init__(self, phone):
        #창 열기
        self.phone = phone
        self.driver = webdriver.Chrome('./chromedriver')
        self.url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
        self.driver.get(self.url)
        
        

    def login(self, srt_id, pw, n):

        
        time.sleep(1)
        tag_category = self.driver.find_element_by_id('srchDvCd{}'.format(n))
        tag_category.click()
        time.sleep(1)
        tag_id = self.driver.find_element_by_id('srchDvNm0{}'.format(n))
        tag_id.send_keys(str(srt_id))
        time.sleep(1)
        tag_pw = self.driver.find_element_by_id('hmpgPwdCphd0{}'.format(n))
        tag_pw.send_keys(str(pw))
        time.sleep(1)
        tag_pw.submit()
        
        

    def get_reserve_url(self, start_stn, end_stn, date, adult, kid, dp_time):
        #원하는 조건 만족하는 예약 창 열기
        c = url_generator.UrlGen(start_stn, end_stn, date, adult, kid, dp_time)
        return c.generate()
        

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
                

    def refresh(self):
        self.driver.refresh()
        time.sleep(1)

    def complete(self):
        try:
            self.driver.find_element_by_class_name('alert_box')
            # self.driver.get('https://www.naver.com/')
            #네이버 접속 대신 메일 보내면 완성
            sendingMail.Mail(self.phone)

            return 1
        except:
            return 0


a = Reserve('01022969002')
a.login('1785043400', 'kimdo82!!',1)
a.driver.get(a.get_reserve_url('부산', '천안아산', 20190205, 2, 0, 12))
# a.driver.get(a.get_reserve_url('광주송정', '동탄', 20190205, 2, 1, 14))
time.sleep(2)
while(True):
    a.find_dpTime_click(12, 15)
    a.refresh()
    if (a.complete()==1):
        break