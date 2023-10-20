# 인덱싱과 슬라이싱
jumin = "901120-1234567"
gender = jumin[7]  # 성별
year = jumin[:2]  # [0:2]
month = jumin[2:4]  # index : 2 이상 4 미만
day = jumin[4:6]

print("생년월일 : " + year + month + day)
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

if gender == "1":
    print("남성입니다.")
else:
    print("여성입니다.")

a = "Life is too short, You need Pythin."
b = a[0] + a[1] + a[2] + a[3]
print(b)
# a[1] = "L" # 오류 발생

# 대소문자 바꾸기
aa = "Hello Python Program..."
bb = aa.upper()
print(bb)
print(aa.lower())

# 문자열 변경 : replace("")
input_str = "Hello Python Program Python..."
new_str = input_str.replace("Python", "")
print(new_str)

# 문자열에 포함된 문자의 개수 새기
input_str2 = "Hello Python Program"
print(input_str2.count("lo"))  # 문자열에서 포함된 문자(열)의 개수를 반환
print(len(input_str2))  # 문자열의 길이를 반환, 별도의 외부 함수를 사용하는 방식

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"길이{len(test)}")
print(input_str2.__len__())  # 문자열에 포함된 내장 함수

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 첫 번째 인덱스를 반환, 못 찾으면 -1 을 반환
# index() : 찾은 문자열의 첫 번째 인덱스를 반환, 못 찾으면 ValueError 예외 발생
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("실수"))
print(phrase.find("가장"))
print(phrase.rfind("가장"))  # 뒤(reverse)에서 부터 찾는데, index는 앞에서부터 계산

print(phrase.find("나에게"))
print(phrase.rfind("나에게"))  # 못 찾으면 -1 반환
# print(phrase.index("나에게")) # 못 찾으면value error

new_phrase = phrase.replace("가장", "나에게")
print(phrase)

# 문자열 연산
print("태양고" + "나희도")
print("안녕하세요"*3)

# 문자열 앞/뒤 공백 제거 : strip()
input_a = """
    안녕하세요.
문자열 함수를 알아봅니다.
    
    """
print(input_a.strip())
