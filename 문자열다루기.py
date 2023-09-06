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

# 문자열 변경 : replcae("")
input_str = "Hello Python Program Python..."
new_str = input_str.replace("Python", "")
print(new_str)

# 문자열에 포함된 문자의 개수 새기
input_str2 = "Hello Python Program"
print(input_str2.count("lo"))  # 문자열에서 포함된 문자(열)의 개수를 반환
print(len(input_str2))  # 문자열의 길이를 반환, 별도의 외부 함수를 사용하는 방식
