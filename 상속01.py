#부모 클래스(공통단)
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스(특화된 코드)
class Student(Person):
    #상속받은 메서드를 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모의 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 재정의
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))        
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))  

#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201122")
#다중 라인 주석: ctrl + /
# print( p.__dict__ )
# print( s.__dict__ )
p.printInfo()
s.printInfo()

print("---issubclass()---")
print( issubclass(Student, Person) )
print( issubclass(Person, Student) )
