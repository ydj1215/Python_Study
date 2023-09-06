# 파이썬 입력
# 사용자의 입력을 받아 그 값을 프로그램에서 사용하고자 할 때 input() 함수를 사용
# input 함수를 통해 입력받은 데이터는 문자열을 반환
# 원하는 데이터형으로 변환이 필요

# print("이름을 입력하세요 : ")
# name = input()
# print((f"당신의 이름은 {name} 입니다"))
#
# age = int(input("나이를 입력하세요:"))
# print(f"당신의 나이는 {age} 입니다.")
#
# gender = input("성별을 입력하세요 : ")
# addr = input("주소를 입력하세요 : ")
# jobs = input("직업을 입력하세요 : ")
# score = float(input("성적을 입력하세요 : "))
# print(f"""
# 안녕하세요 '{name}'님
# 당신의 성별은 {gender}이고,
# 직업은 {jobs}이며,
# 주소는 {addr}이고,
# 성적은 {score}점입니다.
# """)

# split 함수의 기본은 공백 기준
# str1, str2 = input("이름과 주소 입력 : ").split(',')
# print(str1, str2)

# kor, eng, mat = map(int, input("국어 영어 수학 : ").split())  # 형 변환
# print(kor, eng, mat)

# 형 변환 후 리스트로 받기
# val = list(map(int, input("성적 입력 : ").split()))
# print(val)
#
# hour, min, sec = input("시:분:초 : ").split(":")
# print(f"현재 시작 : {hour}시 {min}분 {sec}초")

# 시간을 24시간제이며 : 기준으로 입력 받은 후 오전과 오후로 출력하도록 변경
hour, min, sec = map(int, input("시간을 입력하세요 : ").split(":"))
if (hour > 12):
    hour -= 12
    print(f"오후{hour:02}시{min:02}분{sec:02}초") # 9시 -> 09시
else:
   print(f"오전{hour:02}세{min:02}분{sec:02}초")