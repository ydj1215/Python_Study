"""
정적 메소드는 클래스와 관련이 있어서 클래스 안에 두기는 하나,
클래스나 인스턴스(객체)와는 무관하게 독립적으로 동작하는 함수를 만들고 싶을 때 사용한다.
함수를 정의할 때 인자로 self를 사용하지 않으며,
정적 메서드 안에서는 인스턴스 메서드나 인스턴스 변수에 접근 할 수 없습니다.
"""

class Car:
	isinstance_count = 0  # 클래스 변수로 객체 생성 횟수를 저장합니다.

	# 초기화 함수
	def __init__(self, size, model):
		self.size = size  # 인스턴스 변수: 객체마다 다른 값을 가집니다.
		self.model = model
		Car.isinstance_count = Car.isinstance_count + 1  # 클래스 변수를 업데이트하여 객체 생성 횟수를 증가시킵니다.
		print(f"자동차 객체 생성 수: {Car.isinstance_count}")

	def move(self, speed):
		self.speed = speed
		print(f"자동차 {self.size} & {self.model}가 시속 {self.speed}로 달립니다.")

	@staticmethod
	def check_type(code):
		if code >= 10:
			print("전기차입니다.")
		elif code >= 20:
			print("가솔린차입니다.")
		elif code >= 30:
			print("디젤차입니다.")
		else:
			print("분류 코드가 없습니다.")


# Car 클래스의 인스턴스 생성
car1 = Car("소형", "모닝")
car2 = Car("중형", "쏘나타")

# 인스턴스 메서드 호출
car1.move(90)  # car1 객체의 move 메서드를 호출하여 자동차 정보와 속도를 출력합니다.
# self 매개변수에 car1 이, speed 매개변수에 90이 들어간다.

# 정적 메서드 호출
Car.check_type(11)  # 정적 메서드 check_type을 호출하고 분류 코드를 전달하여 자동차 타입을 출력합니다.
# check_type 이	@staticmethod가 아니더라도,
# 함수 내부에서 클래스의 인스턴스 변수를 전혀 참조지에 않기에 오류 발생X

# 또 다른 인스턴스 메서드 호출
car2.move(70)  # car2 객체의 move 메서드를 호출하여 자동차 정보와 속도를 출력합니다.
