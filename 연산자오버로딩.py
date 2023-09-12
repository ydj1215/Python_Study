# Vector2D 클래스 정의
class Vector2D:
	# 생성자 메서드: x와 y 좌표를 초기화
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# 연산자 오버로딩 - 덧셈 연산자 (+)에 대한 정의
	def __add__(self, other):
		# 두 Vector2D 객체의 x와 y 좌표를 더한 결과를 새로운 Vector2D 객체로 반환
		return Vector2D(self.x + other.x, self.y + other.y)

	# # 연산자 오버로딩 - 곱셈 연산자 (*)에 대한 정의
	# def __mul__(self, other):
	#     # 현재 객체의 x와 y 좌표를 다른 객체의 x와 y 좌표와 곱한 후 각각에 100을 더한 결과를 새로운 Vector2D 객체로 반환
	#     return Vector2D((self.x * other.x) + 100, (self.y * other.y) + 100)
	def __mul__(self, other):
		if isinstance(other, int):
			# 정수와의 곱셈 연산 처리
			return Vector2D((self.x * other) + 100, (self.y * other) + 100)
		elif isinstance(other, Vector2D):
			# 다른 Vector2D 객체와의 곱셈 연산 처리
			return Vector2D((self.x * other.x) + 100, (self.y * other.y) + 100)
		else:
			raise ValueError("Unsupported multiplication")


# Vector2D 객체 생성
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

# 숫자끼리의 곱셈 예시 출력
print(100 * 200)  # 20000
print(100.1 * 200.1)  # 20020.01

# 연산자 오버로딩을 이용한 Vector2D 객체의 덧셈과 곱셈 연산
v3 = v1 + v2  # v1과 v2를 더한 결과를 v3에 저장
v4 = v1 * v2  # v1과 v2를 곱한 결과를 v4에 저장
v5 = v1 * 100

# 결과 출력
print(v3.x, v3.y)  # v3의 x와 y 좌표 출력 (4, 6)
print(v4.x, v4.y)  # v4의 x와 y 좌표 출력 (103, 108)
print(v5.x, v5.y)

"""
v1 + v2와 같이 두 객체를 더하는 연산은 일반적으로 파이썬에서는 허용되지 않습니다.
그러나 이 연산이 가능하게 하려면 연산자 오버로딩을 사용하여 + 연산자에 대한 특수한 동작을 정의해야 합니다.
이를 위해 Vector2D 클래스에서 __add__ 메서드를 정의한 것입니다.

따라서 v1 + v2와 같은 연산이 수행될 때,
파이썬은 v1 객체의 __add__ 메서드를 호출하고 v2 객체를 인자로 전달하여 사용자 정의된 덧셈 연산을 수행하게 됩니다.
이러한 방식으로 연산자 오버로딩을 활용하여 객체 간에 사용자 지정 연산을 수행할 수 있습니다.
"""
