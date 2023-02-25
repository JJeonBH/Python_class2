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

    def to_print(self):
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
    print(student.to_print())

kim = Student("김영철", 90, 90, 78, 67)
print(kim.name)
print(kim.math)
kim.name = "김철수"
kim.math = 100
print(kim.name)
print(kim.math)
print(kim.get_sum())
print(kim.get_avg())
print("학생인가?", isinstance(kim, Student))

subin = "박수빈"
print("학생인가?", isinstance(subin, Student))

subin = "Subin Park"
print(subin.lower())
