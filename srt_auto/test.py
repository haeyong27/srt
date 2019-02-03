from . import reserve


class Test:
    def __init__(self, id, pw, dpst, endst, date, startTime, endTime):
        a = reserve.Reserve()
        a.login(id, pw)
        a.driver.get(a.get_reserve_url())
        time_list = a.find_dpTime()
        for i in time_list:
            a.button_click(i)
