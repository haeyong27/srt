import time
from selenium import webdriver
from .. import url_generator

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
        a = url_generator.URL_gen()
        return a.generate()

a = Reserve()
time.sleep(2)
a.login('01021843577', 'sphv8401')
a.driver.get(a.get_reserve_url())



# url = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000&dptRsStnCd=0020&arvRsStnCd=0552&stlbTrnClsfCd=05&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCdNm=부산&arvRsStnCdNm=동탄&dptDt=20190205&dptTm=000000&chtnDvCd=1&psgInfoPerPrnb1=1&psgInfoPerPrnb5=0&psgInfoPerPrnb4=0&psgInfoPerPrnb2=0&psgInfoPerPrnb3=0&locSeatAttCd1=000&rqSeatAttCd1=015&trnGpCd=109'
# driver.get(url)
# a = driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, 0, \'2\', \'1101\', true, false); return false;"]')
# a[0].click()

