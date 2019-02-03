from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
driver.get(url)
time.sleep(2)
tag_category = driver.find_element_by_id('srchDvCd3')
tag_category.click()
time.sleep(2)
tag_id = driver.find_element_by_id('srchDvNm03')
tag_id.send_keys('아이디입력')
time.sleep(2)
tag_pw = driver.find_element_by_id('hmpgPwdCphd03')
tag_pw.send_keys('비밀번호입력')
time.sleep(2)
tag_pw.submit()
time.sleep(2)
url = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000&dptRsStnCd=0020&arvRsStnCd=0552&stlbTrnClsfCd=05&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCdNm=부산&arvRsStnCdNm=동탄&dptDt=20190205&dptTm=000000&chtnDvCd=1&psgInfoPerPrnb1=1&psgInfoPerPrnb5=0&psgInfoPerPrnb4=0&psgInfoPerPrnb2=0&psgInfoPerPrnb3=0&locSeatAttCd1=000&rqSeatAttCd1=015&trnGpCd=109'
driver.get(url)
a = driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, 0, \'2\', \'1101\', true, false); return false;"]')
a[0].click()