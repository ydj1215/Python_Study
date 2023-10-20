# 각 사이트 비밀번호 만들기
# 규칙 [1] : http://naver.com 앞의 http:// 잘라내기
# 규칙 [2] : 처음 만나는 점 이후 제거 naver.com → naver
""" 규칙 [3] : 남은 글자 중 처음 세자리 + 글자 개수
+ 글자에 포함된 'o'의 개수 + 글자에 포함된 'k'의 개수 + "!" + 자신의 이니셜"""
file_name = "password.txt"
fd = open(file_name, "wt")  # 파일을 쓰기 모드로 열기, 없다면 생성

while True:
    url = input("사이트 주소를 입력해주세요: ")
    if url == 'exit':
        break
    my_str = url.replace("http://", "")  # http:// 잘라내기
    my_str = my_str[:my_str.index(".")]  # 슬라이싱 : (처음) ~ "." 인덱스 미만 (즉 "," 은 포함 X)
    # print(my_str)

    password = (my_str[:3] + str(len(my_str))  # 파이썬에서 줄바꿈을 하려면 ( ) 안에 있어야 한다.
                + str(my_str.count('o')) + str(my_str.count('k')) + "!" + "ydj")

    print("비밀번호 : " + password)

    fd.write(password + '\n')

fd.close()