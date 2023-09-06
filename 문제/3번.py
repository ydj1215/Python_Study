# [3] 주민등록번호를 입력 받아, 생년월일, 성별, 나이 출력하기
# current_year = datetime.today().year
from datetime import datetime

a = input("주민등록번호를 입력해주세요 : ")
current_year = datetime.today().year  # 2023
# a = "901212-1234567"

year = 1900 + int(a[0:2])
month = a[2:4]
day = a[4:6]

if a[7] == "1" or a[7] == "3":
    gender = "남성"
else:
    gender = "여성"

age = current_year - 1900 - int(a[0:2]) + 1

print(f""" 
생년월일 : {year}년 {month}월 {day}일
성별 : {gender}
나이 : {age}
""")
