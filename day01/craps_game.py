'''
craps美国花旗骰子赌博游戏
第一次：7，11玩家胜
        2，3，12庄家胜
        继续摇
第 n次：==第一次，玩家胜
        ==7，庄家胜
        继续摇
'''
from random import randint
 
# money = int(input('请输入你要换币的金额：'))
money = 1000
while money > 0:
    print('你当前的总资产为：',money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    num = randint(1,6) + randint(1,6)
    print('玩家摇出了%d' % num)
    if num == 7 or num == 11:
        print("玩家胜")
        money += debt 
    elif num == 2 or num == 3 or num == 12:
        print("庄家胜")
        money -= debt
    else:
        needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1,6) + randint(1,6)
            print('玩家摇出了%d' % current)
            if(current == 7):
                print("庄家胜")
                money -= debt
            elif(num == current):
                print("玩家胜")
                money += debt
            else:
                needs_go_on = True
print('你破产了，游戏结束!')
