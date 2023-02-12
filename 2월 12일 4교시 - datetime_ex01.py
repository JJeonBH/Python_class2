# 날짜와 시간 관리
import datetime

# 현재 시간을 알고 싶다
now = datetime.datetime.now()

print("현재 시간 :", now)

print("년 :", now.year)
print("월 :", now.month)
print("일 :", now.day)
print("시 :", now.hour)
print("분 :", now.minute)
print("초 :", now.second)
