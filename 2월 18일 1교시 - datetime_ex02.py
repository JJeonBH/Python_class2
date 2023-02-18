import datetime

# 현재 시간을 알고 싶다
now = datetime.datetime.now()
year = now.year
print(year, "년")
print(now.month, "월")
print(datetime.datetime.now().day, "일")

print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print(now.microsecond, "1/1,000,000초")

# 시간 출력 방법
output_a = now.strftime("%Y년%m월%d일 %H시%M분%S초")
print(type(output_a))
print(output_a)
output_b = "{}년{}월{}일 {}:{}:{}".format(now.year,\
            now.month, now.day, now.hour, now.minute, now.second)
print(output_b)
