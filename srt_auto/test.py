import reserve


class Test:
    def __init__(self, id, pw, start_stn, end_stn, date, adult, kid, dp_time, startTime, endTime):
        a = reserve.Reserve()
        a.login(id, pw)
        url = a.get_reserve_url(start_stn, end_stn, date, adult, kid, dp_time)
        a.driver.get(url)
        time_list = a.find_dpTime(url, startTime, endTime)
        for i in time_list:
            a.button_click(i)

a = Test('01021843577', 'sphv8401', '부산', '동탄', 20190205, 2, 4, 12, 12, 14)