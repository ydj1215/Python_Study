# 다중 상속 : 여러 부모로부터 상속을 받는 것
# 다중 상속을 사용하는 예제

# Person 클래스 정의
class Person:
    def __init__(self, eat):
        self.eat = eat
        print("인간 입니다.")

    def set_eat(self):
        print(f"{self.eat} 밥을 먹습니다.")

# Student 클래스 정의, Person 클래스를 상속
class Student(Person):
    def __init__(self, eat, study):
        # 부모 클래스(Person)의 생성자 호출
        Person.__init__(self, eat)
        self.study = study
        print("학생 입니다.")

    def set_study(self, study):
        self.study = study
        print("공부 합니다.")

# Worker 클래스 정의, Person 클래스를 상속
class Worker(Person):
    def __init__(self, eat, work):
        # 부모 클래스(Person)의 생성자 호출
        Person.__init__(self, eat)
        self.work = work
        print("직장인 입니다.")

    def set_work(self, work):
        self.work = work
        print("일 합니다.")

# Developer 클래스 정의, Student와 Worker 클래스를 다중 상속
class Developer(Student, Worker):
    def __init__(self, eat, study, work):
        # 다중 상속 시 부모 클래스(Student, Worker)의 생성자 호출
        Student.__init__(self, eat, study)
        Worker.__init__(self, eat, work)
        print("개발자 입니다.")

# Developer 클래스의 인스턴스 생성
dev = Developer(1, 1, 1)

# Developer 클래스의 eat 속성 변경
dev.eat = 200

# Developer 클래스의 set_eat 메서드 호출
dev.set_eat()


