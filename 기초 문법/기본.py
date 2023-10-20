print("Hello, world")
print('Hello, world')
print(100)
print(33.33)
print(110 * 220)
print(1100 % 33)

# 변수를 선언하고 값을 대입
# num # 오류 발생
num = 100  # 데이터형은 값이 대입되는 순간에 결정
print(num)
num = "200"  # num의 형식은 문자열로 변경
_num = 300

# 변수 활용
name = "유동재"
email = "asdf@gmail.com"
age = 20
addr = '서울시 강남구 역삼동'
print(name + ' ' + email + ' ' + addr)

"""
여기는 범위 주석 구간입니다.
"""

print(f"""
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}
""")

print(f'''
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}
''')

# 파이썬은 boolean 값이 대문자로 시작
is_adult = True
if is_adult:
    print("나는 성인입니다")

else:
    print("나는 성인이 아닙니다.")
