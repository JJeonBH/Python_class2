
class Student:

    # 클래스 멤버(변수) 영역
    count = 0
    students = []

    # 클래스 메서드
    @classmethod
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-----------------------")

    # 객체 생성자(객체의 필요한 값을 설정)
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        # 클래스 변수를 이용하여 시리얼번호 생성
        # 클래스명.변수명
        Student.count += 1
        Student.students.append(self)

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

# 학생 10명에 대해서 1명씩 가져와서 총점과 평균을 구한다
# 총점은 모든 과목을 합한다
# 평균은 총점을 과목수로 나눈다

# 항목명 출력
# print("이름", "총점", "평균", sep="\t")

Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)

# 전체 학생 성적을 출력

Student.print()

# 윤인성의 정보를 출력
윤인성 = Student("윤인성", 87, 98, 88, 95)
print(윤인성.name)
print(str(윤인성))
print(윤인성)

std = Student.students[0]
std1 = Student.students[0]
print(std)

# 객체 고유의 번호를 출력(self)
print(id(std))
print(id(std1))

# 클래스 변수로 속성 접근
print(Student.students[0].name)
print(Student.students[0].get_sum())
print(Student.students[0].get_avg())
print("-----------------------")

# 객체로 속성 접근
print(std.name)
print(std.get_sum())
print(std.get_avg())