#100~999
print("输出100~1000的水仙花数")
for i in range(100,1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100 % 10
    if i == low ** 3 + mid ** 3 + high ** 3:
        print(i)
