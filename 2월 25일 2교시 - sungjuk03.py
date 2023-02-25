# 데이터 준비(입력) --> 리스트안에 딕셔너리
def create_student(name, korean, math, english, science):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

def get_sum(student):
    sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    return sum

def get_avg(sum):
    return sum / 4

def to_print(student):
    return "{}\t{}\t{}".format(
        student["name"],
        get_sum(student),
        get_avg(get_sum(student))
    )

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
    create_student("김미화", 82, 86, 98, 88),
    create_student("김연화", 88, 74, 78, 92),
    create_student("박아현", 97, 92, 88, 95),
    create_student("서준서", 45, 52, 72, 78)
]
# 학생 10명에 대해서 1명씩 가져와서 총점과 평균을 구한다
# 총점은 모든 과목을 합한다
# 평균은 총점을 과목수로 나눈다

sum = 0  # 총점
avg = 0.0  # 평균

# 항목명 출력
print("이름", "총점", "평균", sep="\t")

for student in students:
    # 점수의 총합과 평균을 구함
    # sum = get_sum(student)
    # avg = get_avg(sum)
    # 성적 출력
    # print(student["name"], sum, avg, sep="\t")
    print(to_print(student))
