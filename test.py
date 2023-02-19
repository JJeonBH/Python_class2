import test_module as test

# 이 프로그램은 다양한 모듈을 사용하는
# 주 프로그램이다. __main__

if __name__ == "__main__":
    print("프로그램은 이제부터 시작합니다")
    radius = test.number_input()
    print("원의 둘레 :", test.get_circumference(radius))
    print("원의 면적 :", test.get_circle_area(radius))