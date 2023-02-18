# 시계
# 1. 시간을 1초 주기로 얻어온다
# 2. 그 시간을 화면에 출력한다.

import datetime
import time

for i in range(10):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    print(hour, ":", minute, ":", second)
    time.sleep(1)