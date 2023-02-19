# 모듈 읽어오기
from urllib import request
from bs4 import BeautifulSoup

# urlopen 함수로 기상청의 전국 날씨 읽어오기
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# xml, html 기상청 날씨정보 문서
soup = BeautifulSoup(target, "html.parser")

# location 태그를 찾는다
for location in soup.select("location"):
    # 내부 데이터 가져오기 : 도시명(city), 최저/최고 기온(tmn, tmx), 날씨상태(wf)
    print("도시 :", location.select_one("city").string)
    print("날짜 :", location.select_one("tmEf").string)
    print("날씨 :", location.select_one("wf").string)
    print("최저기온 :", location.select_one("tmn").string)
    print("최고기온 :", location.select_one("tmx").string)
    print() # 한줄 띄어쓰기