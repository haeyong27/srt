import time
from selenium import webdriver
import urlGenerator, dpTime

class Reserve():
    def __init__(self):
        #창 열기
        self.driver = webdriver.Chrome('./chromedriver')
        self.url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
        self.driver.get(self.url)
        self.url = ''
        

    def login(self, id, pw):
        #로그인
        time.sleep(1)
        tag_category = self.driver.find_element_by_id('srchDvCd3')
        tag_category.click()
        time.sleep(1)
        tag_id = self.driver.find_element_by_id('srchDvNm03')
        tag_id.send_keys(str(id))
        time.sleep(1)
        tag_pw = self.driver.find_element_by_id('hmpgPwdCphd03')
        tag_pw.send_keys(str(pw))
        time.sleep(1)
        tag_pw.submit()
    

    def get_reserve_url(self, start_stn, end_stn, date, adult, kid, dp_time):
        #원하는 조건 만족하는 예약 창 열기
        a = urlGenerator.UrlGen(start_stn, end_stn, date, adult, kid, dp_time)
        self.url = a.generate()
        self.driver.get(self.url)

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
            self.driver.get('https://www.naver.com/')
            return 1
        except:
            return 0