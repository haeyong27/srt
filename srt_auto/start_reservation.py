a=10
s = ''
if (int(a) < 10):
    s = '0' + str(a) + '0000'
else:
    s = str(a) + '0000'

print(s)