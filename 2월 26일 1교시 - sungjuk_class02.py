class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        sum = self.korean + self.math + self.english + self.science
        return sum

    def get_avg(self):
        return self.get_sum() / 4
    
    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인터턴스만 비교가능")
        return self.get_sum() == value.get_sum()
    
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.english > value.english

    def to_print(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )
    
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
    Student("김미화", 82, 86, 98, 88),
    Student("김연화", 88, 74, 78, 92),
    Student("박아현", 97, 92, 88, 95),
    Student("서준서", 45, 52, 72, 78)
]
# 학생 10명에 대해서 1명씩 가져와서 총점과 평균을 구한다
# 총점은 모든 과목을 합한다
# 평균은 총점을 과목수로 나눈다

# 항목명 출력
print("이름", "총점", "평균", sep="\t")

for student in students:
    # 점수의 총합과 평균을 구함
    # sum = get_sum(student)
    # avg = get_avg(sum)
    # 성적 출력
    # print(student["name"], sum, avg, sep="\t")
    # print(student.to_print())
    print(str(student)) # 객체가 갖고 있는 속성(값)을 출력하는 용도

kim = Student("김영철", 90, 90, 80, 67)
yun = Student("윤인성", 90, 90, 78, 69)

if kim == 100:
    print("성적 우수")

if kim > yun:
    print(kim.name + "의 영어 성적이 더 좋다")

if kim == yun:
    print(kim.name + "과 " + yun.name + "의 총점은 같다")
else:
    print(kim.name + "과 " + yun.name + "의 총점은 같지 않다")