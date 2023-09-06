print([1, 2, 3])  # 리스트
print({1, 2, 3})  # 세트 (중복된 원소를 허용X)
print((1, 2, 3))  # 튜플 (변경 불가능한 데이터 타입)
print({"key": "value"})  # 딕셔너리 (키와 값의 쌍을 포함)

print(38)  # 정수형
print("문자열")  # 문자열
print(1 + 3)
print("파" + "이" + "썬")
print("파""이""썬")
print("파", "이", "썬")  # 콤마 : 구분자로 한칸의 공백을 가진다.
print("파\n\n\n이\t\t썬")  # \n : 줄바꿈, \t : 한칸 띄우기

print("""동해물과 백두산이 마르고 닳도록 하느님이
보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
"""
      )

# end 와 sep 옵션
# end : 출력문에서 끝에 자동으로 삽입되는 문자를 지정하는 옵션:\n
# sep : 출력문의 중간에 삽입되는 문자를 지정하는 옵션 : 기본은 space
print("Hello", end=" ")
print("Hello")
print("Hello", end="*")
print("Hello")

print("life", "is", "too", "short", sep="\\")
print("010", "1234", "5678", sep="-")
year = 2023
month = 9
day = 6
print(year, month, day, sep="/")  # 2023/9/6


