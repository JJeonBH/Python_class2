
class Car:
    def __init__(self, modelName, color, maxSpeed, fuel):
        self.modelName = modelName
        self.color = color
        self.maxSpeed = maxSpeed
        self.fuel = fuel
        self.speed = 0 # 현재 속도
        self.distance = 0 # 주행 거리
        self.bootState = False # 시동 상태 시동걸면 True 시동끄면 False
        self.direction = 0 # 우회전 1~90 좌회전 -1~-90
    
    def input(self):
        while True:
            cmdInput = input("실행할 메서드를 입력하세요 : ")
            if cmdInput == "boot":
                self.boot()
            elif cmdInput == "bootStop":
                self.bootStop()
            elif cmdInput == "accel":
                self.accel()
            elif cmdInput == "breakCar":
                self.breakCar()
            elif cmdInput == "handle":
                self.handle()
            elif cmdInput == "fuelFill":
                self.fuelFill()
            elif cmdInput == "dashboard":
                self.dashboard()
            elif cmdInput == "exit":
                break
            else:
                print("제대로 입력해주세요!")
                continue
            

    # 시동 걸기
    def boot(self):
        if self.bootState == True:
            print("이미 시동이 켜있습니다")
            return
        if self.fuel == 0:
            print("연료가 없습니다")
            return
        self.fuel -= 1
        print("현재 연료 :", self.fuel)
        self.bootState = True
        print("시동이 켜졌습니다")

    # 시동 끄기
    def bootStop(self):
        if self.bootState != True:
            print("이미 시동이 꺼져있습니다")
            return
        if self.speed != 0:
            print("달리는 중입니다")
            return
        self.bootState = False
        print("시동이 꺼졌습니다")
    
    # 악셀
    def accel(self):
        if self.bootState == False:
            print("시동이 안걸려있습니다")
            return
        if self.fuel <= self.speed/10 + 1:
            print("현재 연료가 너무 적습니다")
            return
        if self.speed == self.maxSpeed:
            print("최고속도에 도달하였습니다")
            return
        self.fuel -= 1
        print("현재 연료 :", self.fuel)
        self.speed += 10
        print("현재 속도 :", self.speed)
        self.distance += self.speed * 1
        print("주행거리 : ", self.distance)

    # 브레이크
    def breakCar(self):
        if self.bootState == False:
            print("시동이 안걸려있습니다")
            return
        if self.speed == 0:
            print("이미 속도가 0입니다")
            return
        self.fuel -= 1
        print("현재 연료 :", self.fuel)
        self.speed -= 10
        print("현재 속도 :", self.speed)
        self.distance += self.speed * 1
        print("주행거리 : ", self.distance)
        if self.speed == 0:
            print("정지되었습니다")
            return

    # 운전중 핸들 조작
    def handle(self):
        if self.bootState == False:
            print("시동이 안걸려있습니다")
            return
        if self.speed == 0:
            print("자동차가 멈춰있습니다")
            return
        while True:
            try:
                direction = int(input("우회전[1~90], 좌회전[-1~-90] : "))
                if direction > 90 or direction < -90:
                    print("정확히 입력해주세요")
                    continue

                if (self.speed >= 60 and (direction >= 70 or direction <= -70)):
                    print("현재 속도가 너무 빠릅니다. 사고 위험이 있습니다")
                    print("속도를 60km보다 줄이고 회전해주세요")
                    return
                else:
                    self.direction += direction
                    if(self.direction > 360 or self.direction < -360):
                        self.direction = 0
                        self.direction += direction
                    if(1 <= direction <= 90):
                        print("우측으로", direction, "도 만큼 회전했습니다.")
                        print("현재 방향", self.direction)
                        break
                    elif(-90 <= direction <= -1):
                        print("좌측으로", direction, "도 만큼 회전했습니다.")
                        print("현재 방향", self.direction)
                        break
                    elif direction == 0:
                        print("방향을 유지합니다")
                        break
            except:
                print("숫자를 입력해주세요!")


    # 연료 채우기
    def fuelFill(self):
        try:
            fuel = int(input("연료를 넣어주세요 : "))
            self.fuel += fuel
            print("현재 연료 :", self.fuel)
        except:
            print("숫자를 입력해주세요!")
        
    # 자동차 정보 보여주기
    def dashboard(self):
        print("모델명 : " + self.modelName)
        print("색상 : " + self.color)
        print("현재 속도 :", self.speed)
        print("최고 속도 :", self.maxSpeed)
        print("현재 연료 :", self.fuel)
        print("현재 방향 :", self.direction)
        print("주행 거리 :", self.distance)


소나타 = Car("소나타", "흰색", 300, 0)

소나타.input()