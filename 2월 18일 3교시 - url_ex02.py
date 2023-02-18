# urllib 모듈 사용
# 인터넷 사이트 정보 가져오기
# 1. 인터넷 주소를 제공
# 2. 제공된 주소에 접속(url open)
# 3. 사이트 주소에서 제공하는 HTML 문서를 읽기
# 위의 모든 기능 웹브라우저가 제공한다.
# 인터넷에 있는 이미지 저장하기(다운로드)

from urllib import request

# 원하는 인터넷 주소를 요청
target = request.urlopen("http://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png")
output = target.read()
print(output)

# 디스크 저장(파일로 저장)
# 저장할 파일명을 설정, 저장할 폴더
file = open("daumlogo_img.png", "wb")
file.write(output)