import reserve
import time

a = reserve.Reserve('01021843577')
a.login('01021843577', 'sphv8401', 3)
url = a.get_reserve_url('동탄', '부산', '20190301', 1, 0, 8)
a.driver.get(url)
time.sleep(1)
while(True):
    a.find_dpTime_click(8, 20)
    time.sleep(1)
    if (a.complete()==1):
        break

