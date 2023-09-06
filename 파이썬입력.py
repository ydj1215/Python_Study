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
str1, str2 = input("이름과 주소 입력 : ").split(',')
print(str1, str2)
