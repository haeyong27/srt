import os 
from celery import shared_task
from time import sleep 
from slacker import Slacker
from .srt import URLGenerator, Reserve
from selenium import webdriver
import json 
import time
import requests
from datetime import datetime, timedelta
API_KEY = os.getenv('SLACK_API_KEY')


@shared_task(ignore_result=True)
def srt(params):
    params = json.dumps(params)
    params = json.loads(params)
    slacker = Slacker(API_KEY)
    message = '---- 고객 : ' + params['phone'] + '의 출발지 : '+ params['dpt'] +'에서 ' + params['arr']

    options = webdriver.ChromeOptions()
    options.add_argument('headless')    
    driver = webdriver.Chrome('/Users/hwanghaeyong/Desktop/chromedriver', chrome_options=options)
    # driver = webdriver.Chrome('/Users/hwanghaeyong/Desktop/chromedriver')

    #로그인
    url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000' 
    driver.get(url)
    srt_id = params['srtid']
    srt_pw = params['srtpw']
    login_type = params['logintype']
    
    tag_category = driver.find_element_by_id('srchDvCd{}'.format(login_type))
    tag_category.click()
    tag_id = driver.find_element_by_id('srchDvNm0{}'.format(login_type))
    tag_id.send_keys(str(srt_id))
    tag_pw = driver.find_element_by_id('hmpgPwdCphd0{}'.format(login_type))
    tag_pw.send_keys(str(srt_pw))
    tag_pw.submit()

    #예약 준비하기
    url = URLGenerator(params['dpt'], params['arr'], params['date'].replace('-', ''), params['adult'], params['child'], params['dptime']).urlGenerate()
    driver.get(url)

    minutes = 0
    start = time.time()
    now = datetime.now() + timedelta(hours=9)
    msg_time = now.strftime("%H:%M:%S  %d/%m/%Y")
    slacker.chat.post_message('#start', msg_time + '---시작 ' + message)
    while(1):
        if time.time() - start > 60:
            start = time.time()
            minutes += 1
            now = datetime.now() + timedelta(hours=9)
            msg_time = now.strftime("%H:%M:%S  %d/%m/%Y")
            slacker.chat.post_message('#ing', msg_time + '---' + str(minutes) + '분 지남 ' + message)

        time.sleep(0.5)
        driver.refresh()

        #예약구간
        ticket_count = int(params['ticketnum'])
        for count in range(ticket_count):
            try:
                #예약가능 버튼이 있으면 클릭하고
                count = int(count)
                driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, {}, \'1\', \'1101\', true, false); return false;"]'.format(count))[0].click()
            except:
                #버튼이 없으면 패스
                pass

            page = driver.page_source
            if '10분 내에 결제하지 않으면 예약이 취소됩니다.' in page:
                now = datetime.now() + timedelta(hours=9)
                msg_time = now.strftime("%H:%M:%S  %d/%m/%Y")
                slacker.chat.post_message('#srt', msg_time + '---' + params['phone'] + '님 표 예약 됐습니다.' )
                #is_completed = True
                complete_url = 'http://127.0.0.1:8000/ticket/' + str(params['id']) +'/'
                requests.patch(complete_url, {'is_complete':1})
                driver.quit()
                return

            if '잔여석없음' in page:
                now = datetime.now() + timedelta(hours=9) 
                msg_time = now.strftime("%H:%M:%S   %d/%m/%Y")
                slacker.chat.post_message('#noseat',msg_time + '---잔여석없음' + message)
                driver.get(url)

            if '400 Bad Request' in page:
                slacker.chat.post_message('#etc', '400 bad requests ')
                driver.get(url)

    driver.quit()


    return 'hi'





