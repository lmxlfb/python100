def fibonacci_num(num):
    if num == 1 or num ==2:
        return 1
    else:
        return fibonacci_num(num-1)+fibonacci_num(num-2)

num1 = int(input('input something:'))
for i in range(1,num1+1):
    print('%d'%fibonacci_num(i))



