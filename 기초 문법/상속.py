# 오버라이딩 : 부모 클래스를 상속받아 동일한 메서드에 대해 재정의하여 사용하는 것

# def sum(num1, num2, num3 = 100):
# 	return num1 + num2 + num3
#
# print(sum(100,200)) # 굳이 파이썬에서 오버로딩 지원X
# print(sum(100,200, 300))
# # print(sum('korea','seoul'))


class ProtoTV:
	def __init__(self, isOn, channel, volume):
		self.isOn = isOn
		self.channel = channel
		self.volume = volume

	def set_on(self, isOn):
		self.isOn = isOn

	def set_channel(self, cnl):
		if 0 < cnl < 1000:
			self.channel = cnl
			print(f"채널을 {cnl}로 변경 하였습니다.")
		else:
			print(f"채널 설정 범위가 아닙니다.")

	def set_volume(self, vol):
		self.volume = vol

	def get_on(self):
		return self.isOn

	def get_channel(self):
		return self.channel

	def get_volume(self):
		return self.volume


class TV(ProtoTV):  # ProtoTV로부터 상속을 받았다.
	def set_channel(self, cnl):  # 부모가 가진 메서드를 상속받아 재정의 (오버라이딩)
		if 0 < cnl < 2000:
			self.channel = cnl
			print(f"채널을 {cnl}로 변경 하였습니다.")
		else:
			print(f"채널 설정 범위가 아닙니다.")


lg_tv = TV(False, 10, 10)
samsung_tv = TV(False, 20, 20)
samsung_tv.set_channel(1200) # 1~-1999

proto = ProtoTV(False, 10, 10)
proto.set_channel(1000)  # 1~999
