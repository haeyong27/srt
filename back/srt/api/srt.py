import time
import os
from selenium import webdriver
from fake_useragent import UserAgent
import urllib.request
import re
from bs4 import BeautifulSoup
import requests
import json

from slacker import Slacker
from base64 import b64encode


class URLGenerator():

    def __init__(self, startStn, endStn, date, numAdult, numKid, time_start):
        self.startStn = startStn
        self.endStn = endStn
        self.date = date
        self.numAdult = numAdult
        self.numKid = numKid
        self.time_start = time_start
        self.time_start_int = time_start

        url_sample = 'https://etk.srail.co.kr/hpg/hra/01/selectMapInfo.do?isAll=Y&other=&target=dpt&pageId=TK0101010000'
        response = requests.get(url_sample)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        p = re.compile('\d+')
        station_num = {}

        for tag in soup.select('.map a'):
            station_num[tag.text] = p.findall(tag['onclick'])[0]

        self.station_num = station_num

    def urlGenerate(self):

        url_base = 'https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000'
        url_params = 'stlbTrnClsfCd=05&trnGpCd=109&psgNum=1&seatAttCd=015&isRequest=Y&dptRsStnCd=0015&arvRsStnCd=0552&dptDt=20190205&dptTm=100000&psgInfoPerPrnb1=1&psgInfoPerPrnb5=0&trnGpCd=300'
        
        #parse params
        params = {}
        for i in url_params.split('&'):
            key, value = i.split('=')
            params[key] = value

        params['dptRsStnCd'] = self.station_num[self.startStn]
        params['arvRsStnCd'] = self.station_num[self.endStn]
        params['dptDt'] = self.date
        params['psgInfoPerPrnb1'] = self.numAdult
        params['psgInfoPerPrnb5'] = self.numKid
        params['trnGpCd'] = 300
        
        if (int(self.time_start_int) < 10):
            params['dptTm'] = '0' + str(self.time_start_int) + '0000'
        else:
            params['dptTm'] = str(self.time_start_int) + '0000'

        url = url_base
        for i in params:
            url += '&' + i + '=' + str(params[i])
        
        return url

class Reserve():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.url = 'https://etk.srail.co.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000' 
        self.driver.get(self.url)
        self.selected_time = []

    def login_and_geturl(self, srt_id, srt_pw, login_type, url):
        tag_category = self.driver.find_element_by_id('srchDvCd{}'.format(login_type))
        tag_category.click()
        tag_id = self.driver.find_element_by_id('srchDvNm0{}'.format(login_type))
        tag_id.send_keys(str(srt_id))
        tag_pw = self.driver.find_element_by_id('hmpgPwdCphd0{}'.format(login_type))
        tag_pw.send_keys(str(srt_pw))
        tag_pw.submit()
        self.driver.get(url)
        
    def time_list(self, click_list):
        for i in click_list:
            self.driver.find_elements_by_xpath('//a[@onclick="requestReservationInfo(this, {}, \'1\', \'1101\', true, false); return false;"]'.format(i))[0].click()
            



