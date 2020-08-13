import os

def scores():
    dic = {}
    message = ''
    while message !='quit':

        name=input("姓名：")
        chinese=int(input("语文成绩:"))
        math=int(input("数学成绩："))
        english=int(input("英语成绩："))
        scores=chinese+math+english
        avg=scores/3
        dic[name]=avg
        message=input("如果想要退出，请输入quit:")

    return dic

def find(dic):
    for name, avg in dic.items():
        print(name + "的平均分为" + str(avg))
        if avg>80:
            f = open("score.txt", "a")
            f.write(name+"的平均分"+str(avg))
            f.close()

dic=scores()

find(dic)