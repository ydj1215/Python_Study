# 생성자는 클래스가 객체로 만들어질 때, 자동으로 호출되면
# 객체의 초기화을 지정 가능
# 생성자 키워드 : __INIT__
# self 는 자신의 객체를 가르키는 변수

class TV:
	def __init__(self, name, is_on, channel, volume):
		# __init__ 에 자바에서의 "필드(멤버변수) 정의" 가 내포되있다.
		# self. 는 자바의 this. 와 유사
		# 파이썬의 모든 멤버는 기본적으로 public
		self.name = name
		self.is_on = is_on
		self.channel = channel
		self.volume = volume

	def set_in(self, is_on):
		self.is_on = is_on

	def set_channel(self, channel):
		self.channel = channel

	def set_volume(self, volume):
		self.volume = volume

	def get_on(self):
		return self.is_on

	def get_channel(self):
		return self.channel

	# TV 정보 출력 함수
	def view_tv(self):
		power = "OFF", "ON"
		print(f"이름 : {self.name}")
		print(f"전원 : {self.is_on}")
		print(f"채널 : {self.channel}")
		print(f"소리 : {self.volume}")


lg_tv = TV("LG", False, 40, 10)
lg_tv.view_tv()
