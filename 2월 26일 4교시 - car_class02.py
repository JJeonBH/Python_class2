# 자동차 클래스를 생성(Car)
#   1. 속성
#       기능에 필요한 속성은 추출해서 설정
#   2. 메서드
#       - 시동
#       - 정지
#       - 운행(직진, 좌/우 회전)

class Car:
    # 속성

    def __inti__(self, state, fuel):
        self.state = state
        self.fuel = fuel
        self.speed = 0
        self.direction = 0

    # 메서드
    def 시동(self):
        self.state = True
        self.fuel -= 2

    def 정지(self):
        self.speed = 0

    def 운전(self):
        self.악셀()
        self.핸들조작()

    def 악셀(self):
        self.speed += 2

    def 핸들조작(self, direction):
        self.direction = direction
