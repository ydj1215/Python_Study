import sys

name = input("이름 : ")

# age = int(input("나이 : "))
# if age < 1 or age > 199:
#     sys.exit()

while True:
    age = input("나이 :")
    if age.isdigit():  # 문자열이 숫자로 구성되어 있는지 확인
        age = int(age)
        if 0 < age < 200: break
    print("나이를 잘못 입력했습니다.")

while 1:
    gender = input("성별 : ")
    if gender == "M" or gender == "m":
        gender = "남성"
        break
    elif gender == "F" or gender == "f":
        gender = "여성"
        break
    else:
        print("다시 입력해주세요.")
        continue

while 1:
    job = int(input("직업 : "))
    if job == 1:
        job = "학생"
        break
    elif job == 2:
        job = "회사원"
        break
    elif job == 3:
        job = "주부"
        break
    elif job == 4:
        job = "무직"
        break
    else:
        print("다시 입력해주세요")
        continue

print(f"""이름 : {name}
나이: {age}
성별: {gender}
직업: {job}
""")
