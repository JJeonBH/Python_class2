# 1분 타이머
# 1. time 모듈 준비

import time

minute = 10
second = 60
print(minute, ":", second)

for i in range(600):
    second -= 1
    time.sleep(1)
    print(minute, ":", second)
    if second == 0:
        second = 60
        minute = minute - 1

print("타이머 종료되었습니다.")