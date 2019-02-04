import time
from selenium import webdriver
import urlGenerator, dpTime

class Reserve():
    def __init__(self):
        #창 열기
        self.driver = webdriver.Chrome('./chromedriver')
        url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
        self.driver.get(url)
        

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
        return a.generate()

    def find_dpTime(self, url, start=5, end=10):
        time_list = dpTime.ReserveButton(url).search_dpTime()
        selected_time = []
        for a, time in enumerate(time_list):
            if (time>=start and time<=end):
                selected_time.append(a)

        return selected_time


    def button_click(self, i):
        #특정 조건 만족하는 버튼 클릭하기
        a = self.driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, {}, \'1\', \'1101\', true, false); return false;"]'.format(i))
        a[0].click()

