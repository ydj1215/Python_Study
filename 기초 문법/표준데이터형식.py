# 값을 할당하는 방법
a = b = c = 1
print(a, b, c)
a, b, c = 3, False, "유동재"  # 여러개의 변수를 한번에 대입 가능
print(a, b, c)

# 타입 확인
# age = int(input("나이를 입력하세요 : "))
# print(type(age))

value = 0o77  # 8진수
print(value)

value_2 = 0x224
print(value_2)

# boolean 타입
print(bool(1))  # 참
print(bool(0))  # 거지
print(bool(-100))  # 참
print(bool(""))  # 거짓
print((bool(None)));  # 값이 정해지지 않았다.
val = None

# 문자열 타입
str_ex = "Hello Pyhton!"  # str로 선언하면 str() 형 변환 할때 오류가 뜬다.
print(str_ex)
print(str_ex[2:])
print(str_ex[2:5])
print(str_ex*3)
print(str_ex+"Test")

# 형변환 : 파이썬은 같이 할당되는 순간 형이 결정
# 이후 데이터 형을 변경하고자 할 때 형 변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(1+3.141592)