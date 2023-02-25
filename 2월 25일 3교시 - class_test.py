class Student:
    def __init__(self, school, name, level, age):
        self.school = school
        self.name = name
        self.level = level
        self.age = age
    
    def goto_school(self):
        return self.school

honggildong = Student("둔산초", "홍길동", 3, 10)
hong = Student("둔산초", "홍수아", 6, 13)
kim = Student("문정초", "김영철", 4, 11)
print(honggildong.name)
print(honggildong.goto_school())
print(honggildong.level)
print(honggildong.age)