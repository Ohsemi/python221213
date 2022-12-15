# class1.py
#클래스 정의
class Person:
    #클래스 멤버 변수(일종의 공통 데이터로 사용)
    num_person = 0
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = "전우치"
p3 = Person()
#메서드 호출
p1.print()
p2.print()
print("인스턴스 갯수:{0}".format(Person.num_person))

#런타임시에 추가 
Person.title = "new title"
print( p1.title )
print( p2.title )
print( Person.title )
p1.age = 30
print(p1.age)
print(p2.age)



