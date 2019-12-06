import time
import math
upNum = input('请输入一个大于0的整数：')
begintime = time.process_time()

if upNum.isdigit():
    upNum = int(upNum)
    arr_list = [1]
    for x in range(1,upNum+1):
        print("第%s次执行！"%x)
       # print(math.sqrt(x)+1)
        su = 0
        for a in range(1,x):
            if x % a == 0:
                su += a
        if x == su:
            arr_list.append(x)
    print('%s以内的完美数有%s个，分别是：%s'%(upNum,len(arr_list),arr_list))
else:
    print('你输入的数字不正确')

endtime = time.process_time()
runtime = endtime - begintime

print('程序执行的时间为:',runtime)

begin=time.process_time()
upnum = int(upNum)
for num in range(1,upnum+1):
    result = 0
    # print(math.sqrt(num))
    for factor in range(1,int(math.sqrt(num))+1):
        if num % factor ==0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
end = time.process_time()
print('runtime=',end-begin)


