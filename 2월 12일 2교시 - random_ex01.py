import random

# 0.0 ~ 0.9999999999...(0이상 1미만) 사이의 임의의 값을 출력
x = random.random()
print(x)

# 1이상 11미만 사이의 임의의 값을 출력
y = random.random() * 10 + 1
print(y)

# 1이상 45이하 사이의 임의의 정수값 출력
for i in range(6):
    z = random.randint(1, 45)
    print(z, end=" ")
