from . import reserve

a = reserve.Reserve()
# a.login('01021843577', 'sphv8401')
a.driver.get(a.get_reserve_url())

time_list = a.find_dpTime()
for i in time_list:
    a.button_click(i)
