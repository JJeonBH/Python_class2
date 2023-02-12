# 난수를 이용하여 로또번호 추출
# 로또 번호 섞기
import random

lotto = []

# 로또 번호 초기화
for i in range(1, 46):
    lotto.append(i)

print(lotto)

for i in range(100):
    a = random.randint(0, 44)
    b = random.randint(0, 44)
    # 교환 작업
    c = lotto[a]
    lotto[a] = lotto[b]
    lotto[b] = c

print(lotto[:6])

# 교환
    # a = 10
    # b = 20
    # c = 0
    # print(a, b)
    # c = a
    # a = b
    # b = c
    # print(a, b)
