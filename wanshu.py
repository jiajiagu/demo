#num=int(input('请输入一个数字：'))
def wanshu(num):
    list = []
    b = 0
    for i in range(1,num):
        a=num%i
        if a==0:
            list.append(i)

#    print(list)

    for j in range(len(list)):
        b=b+list[j]

    if (num==b):
        print('{}是完数'.format(num))
  #  else:
  #      print('{}不是完数'.format(num))

for num in range(1,10000):
    wanshu(num)