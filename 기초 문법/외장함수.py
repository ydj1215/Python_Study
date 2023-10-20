# 외장함수 : 파이썬이 기본적으로 제공, import 필요
import math
import random
from datetime import datetime  # datetime 모듈에서 datetime 함수만 import
import math

# 랜덤
n = random.randint(0, 4)  # 0~4 까지의 임의의 정수값 반환
m = random.randrange(0, 4)  # 0~4 미만의 임의의 정수값 반환

# 현재 시간 가져오기
time = datetime.today()
time_2 = datetime.today().year
print(f"정확한 현재 시간: {time}")
print(f"올해 년도: {time_2}")
# .month .day .hour .minute .second 도 존재

# 수학 계산을 위한 math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(100))
print(math.ceil(100.999))  # 올림
print(math.floor(100.999))  # 내림

# 중복값 X 로또 번호 생성
print("로또 번호 자동 생성기")
ls = []
while 1:
    rand = random.randrange(1, 46)
    if rand not in ls:  # 중복값 확인
        ls.append(rand) # ls = rand 는 ls에 를 그냥 전부 n과 같게 만든다. 값을 추가하려면 append() 사용
    if len(ls) == 6:
        break
print(ls)
