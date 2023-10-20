# 회원 가입을 위한 아이디와 패스워드 입력 받기
user = input("아이디 입력 : ")
if len(user) >= 4:
    pw = input("비밀번호 입력 : ")
    if pw.__len__() < 8 or pw.__len__() > 16:
        print("비밀번호는 8~16자 이내로 입력해주세요.")
    elif pw.find(user) >= 0:
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print(f"""
아이디 : {user}
패스워드 : {pw}""")
else:
    print("아이디는 반드시 4자리 이상이여야 합니다.")
