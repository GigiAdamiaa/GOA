# 1)

num = 0
i = 0
while i <= 10:
    num = i + num
    i = i + 2
    print(i)

print(num)

# 2)

i = 0
while i <= 20:
    if (i % 3==0
        and i % 5 ==0):
        print(i)
    i = i + 1

# 3)

for i in range(1,100 + 1):
    if i % 5 ==0:
        print(i)

# 4)

for i in range(1,20 + 1):
    if i % 6 ==0 :
        print(i)
