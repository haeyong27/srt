import time
import datetime
from selenium import webdriver
import url_gen, dpt_time, sendingMail

class Reserve():

    def __init__(self, phone, dp_time_start, dp_time_end):
        #로그인화면 창 열기

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.phone = phone
        self.driver = webdriver.Chrome('./driver/chromedriver', chrome_options=options)
        self.url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000' 
        self.driver.get(self.url)
        self.dp_time_start = dp_time_start
        self.dp_time_end = dp_time_end
        self.selected_time = []

    def login(self, srt_id, srt_pw, n):
        tag_category = self.driver.find_element_by_id('srchDvCd{}'.format(n))
        tag_category.click()
        tag_id = self.driver.find_element_by_id('srchDvNm0{}'.format(n))
        tag_id.send_keys(str(srt_id))
        tag_pw = self.driver.find_element_by_id('hmpgPwdCphd0{}'.format(n))
        tag_pw.send_keys(str(srt_pw))
        tag_pw.submit()
        
        
    def get_reserve_url(self, start_stn, end_stn, date, adult, kid):
        #원하는 조건 만족하는 예약 창 열기
        c = url_gen.URLGenerator(start_stn, end_stn, date, adult, kid, self.dp_time_start, self.dp_time_end)
        self.url = c.urlGenerate()
        self.driver.get(self.url)
        time.sleep(1)

        
    def find_dptime(self):
        time_dic = dpt_time.ReserveButton(self.url).search_dpTime()

        for k, v in time_dic.items():
            tempTime = datetime.datetime.strptime(v, "%H:%M")
            fromTime = datetime.datetime.strptime(self.dp_time_start, "%H:%M")
            toTime = datetime.datetime.strptime(self.dp_time_end, "%H:%M")
            if fromTime.time() <= tempTime.time() <= toTime.time():
                self.selected_time.append(k)

    def click_dptime(self):
        self.driver.refresh()
        for i in self.selected_time:
            b = self.driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, {}, \'1\', \'1101\', true, false); return false;"]'.format(i))
            if (len(b) > 0):
                b[0].click()
        time.sleep(1)

    def complete(self):
        try:
            self.driver.find_element_by_class_name('btn_station_switch')
            content = f'phone : {self.phone}, 예약됐어요 '
            sendingMail.Mail(content)
            return 0
        except:
            return 1


if __name__ == '__main__':

    r = Reserve('01021843577', '09:59', '14:10')
    # time.sleep(1)
    r.login('01021843577', 'sphv8401', 3)
    # time.sleep(1)
    r.get_reserve_url('동탄', '부산', '20190306', 2, 1)
    r.find_dptime()
    #예약화면으로 넘어갈 때 까지 클릭 반복하기, 아래 코드는 한번만 실행
    r.click_dptime()
