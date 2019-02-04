import time
from selenium import webdriver
import urlGenerator, dpTime

class Reserve():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
        self.driver.get(url)
        

    def login(self, id, pw):
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
    

    def get_reserve_url(self):
        a = urlGenerator.UrlGen()
        return a.generate()


    def button_click(self, i):
        a = self.driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, {}, \'1\', \'1101\', true, false); return false;"]'.format(i))
        a[0].click()