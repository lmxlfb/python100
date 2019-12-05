'''
反转整数
'''
num = int(input('请输入一个整数，num= '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10+(num % 10)
    num //= 10
print(reversed_num)
