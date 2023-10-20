# 클래스 메서드 : 클래스 변수를 사용하기 위한 함수
# 클래스 메서드는 첫 번째 인자로 클래스를 넘겨 받는 cls가 필요하며,
# 이를 이용해 클래스 변수에 접근

class Person:
	count = 0  # 클래스 변수 count를 선언하고 초기화합니다.

	def __init__(self):
		Person.count += 1  # 클래스 변수 count를 증가시켜 객체가 생성될 때마다 카운트를 증가시킵니다.

	@classmethod
	def print_count(cls):
		print(f"{cls.count}명 생성되었습니다.")  # 클래스 메서드 print_count를 정의하고 클래스 변수 count를 출력합니다.
		# print_count가 클래스 메서드로 선언되지 않았다면,
		# 메서드 내에서 클래스 변수 count에 접근할 수 없다.

# Person 클래스의 인스턴스 생성
james = Person()  # james 객체가 생성될 때, 클래스 변수 count가 1 증가합니다.
maria = Person()  # maria 객체가 생성될 때, 클래스 변수 count가 다시 1 증가합니다.

Person.print_count()  # 클래스 메서드 print_count를 호출하여 현재까지 생성된 객체의 수를 출력합니다.
