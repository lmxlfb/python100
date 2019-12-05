#cock=5 #公鸡
#hen=3 #母鸡
#chick=1/3 #小鸡
#momey=100 
num=0

for x in range(0,20):
    for y in range(0,33):
        t = 100 - x - y
        if x*5 + y*3 + t/3 == 100:
            print('公鸡：%d,母鸡：%d,小鸡：%d' %(x,y,t))

