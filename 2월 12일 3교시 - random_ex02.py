import random

# 난수 모듈 응용
# 10~100사이의 임의 실수값을 생성

a = 10  # 시작값
b = 100  # 종료값
num = random.random() * (b+1-a)+a
print(num)
