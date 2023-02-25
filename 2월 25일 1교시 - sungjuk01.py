# 데이터 준비(입력) --> 리스트안에 딕셔너리
students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92},
    {"name": "김미화", "korean": 82, "math": 86, "english": 98, "science": 88},
    {"name": "김연화", "korean": 88, "math": 74, "english": 78, "science": 92},
    {"name": "박아현", "korean": 97, "math": 92, "english": 88, "science": 95},
    {"name": "서준서", "korean": 45, "math": 52, "english": 72, "science": 78}
]

# 학생 10명에 대해서 1명씩 가져와서 총점과 평균을 구한다
# 총점은 모든 과목을 합한다
# 평균은 총점을 과목수로 나눈다

sum = 0 # 총점
avg = 0.0 # 평균

# 항목명 출력
print(" 이름", " 총점", "평균")

for student in students:
    # 점수의 총합과 평균을 구함
    sum = student["korean"] + student["math"] +\
          student["english"] + student["science"]
    avg = sum / 4
    # 성적 출력
    print(student["name"], sum, avg, sep=" ")
