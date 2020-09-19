dic={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
month=eval(input('请输入月份：'))
day=eval(input('请输入日期：'))
result=0
if month not in range(1,13):
    print('error')
elif dic[month] < day:
    print("error")
else:
    for i in range(1,month):
        result+=dic[i]
        print ('这是年度第{}天'.format(result+day))