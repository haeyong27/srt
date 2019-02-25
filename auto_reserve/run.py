import reserve
import time

a = reserve.Reserve('01021843577')
a.login('01021843577', 'sphv8401', 3)
url = a.get_reserve_url('동탄', '부산', '20190301', 1, 0, 8)
a.driver.get(url)
time.sleep(1)
while(True):
    a.find_dpTime_click(8, 20) #몇시 부터 몇시 사이의 표를 예매할건지
    time.sleep(1)
    if (a.complete()==1): #예매 완료되면 종료
        break