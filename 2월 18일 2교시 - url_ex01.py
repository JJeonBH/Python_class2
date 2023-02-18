# urllib 모듈 사용
# 인터넷 사이트 정보 가져오기
# 1. 인터넷 주소를 제공
# 2. 제공된 주소에 접속(url open)
# 3. 사이트 주소에서 제공하는 HTML 문서를 읽기
# 위의 모든 기능 웹브라우저가 제공한다.

from urllib import request

# 원하는 인터넷 주소를 요청
target = request.urlopen("http://intpump.com/")
output = target.read()
print(output)