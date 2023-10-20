class TV:
    cnt = 0  # 클래스 멤버 (클래스 변수)

    def __init__(self, name, isOn, channel, volume):
        self.__name = name  # 인스턴스 멤버 (인스턴스 변수, private 변수)
        self.__isOn = isOn
        self.__channel = channel
        self.__volume = volume
        TV.cnt += 1  # 클래스 변수 cnt를 1 증가시켜 객체 생성 횟수를 추적합니다.

    def set_on(self, isOn):
        self.__isOn = isOn

    def set_channel(self, cnl):
        if 0 < cnl < 1000:
            self.__channel = cnl
        else:
            print("채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.__volume = vol

    def get_on(self):
        return self.__isOn

    def get_channel(self):
        return self.__channel

    def get_volume(self):
        return self.__volume

    def view_tv(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.__name}")
        print(f"전원 : {power[self.__isOn]}")
        print(f"채널 : {self.__channel}")
        print(f"볼륨 : {self.__volume}")

# TV 클래스의 인스턴스 생성
lg_tv = TV("LG", True, 10, 20)
sam_tv = TV("Samsung", True, 10, 20)

# private 변수 변경 시도, 하지만 변경되지 않음 (자바와 달리 오류는 발생X)
lg_tv.__name = "SAMSUNG"  # 이 코드는 새로운 인스턴스 변수를 생성하고 변경하지 않습니다.
lg_tv.__isOn = False  # 이 코드도 새로운 인스턴스 변수를 생성하고 변경하지 않습니다.

# set_channel 메서드를 통해 채널 변경
lg_tv.set_channel(999)

# TV 정보 출력
lg_tv.view_tv()  # TV 정보를 출력합니다.

# 클래스 변수 cnt 출력 (TV 객체 생성 횟수)
print(TV.cnt)
