# 추상화 :
# 부모 클래스에서 선언한 메서드에 대해 반드시 상속 받은 클래스에서 기능을 구현해야 한다.
# 추상 메서드가 포함된 부모 클래스는 객체로 만들 수 없고, 단지 상속을 주기 위해서 존재
from abc import * 

class NetworkAdaptor(metaclass=ABCMeta): # 추상 클래스 선언
	@abstractmethod
	def connect(self):
		pass # 구현할 내용이 없는 경우 pass 키워드를 사용

class WiFi(NetworkAdaptor):
	def __init__(self, company):
		self.company = company
	def connect(self):
		print(f"{self.company} WiFi에 연결했습니다.")

class FiveG(NetworkAdaptor):
	def __init__(self,company):
		self.company = company
	def connect(self):
		print(f"{self.company} 5G에 연결했습니다.")

net = input("연결한 네트워크를 선택 : [1] WiFi, [2] FiveG : ")
if net == '1':
	adapter = WiFi("KT")
	adapter.connect()
elif net == '2':
	adapter = FiveG("LG")
	adapter.connect()
else:
	print("연결할 네트워크가 없습니다.")