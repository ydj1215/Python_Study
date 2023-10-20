# 파일 쓰기 :
# 파일을 읽거나 쓰기 위해서는 반드시 open() 이 필요,
# 끝나면 close()
# 파일 객체 = open(파일명, 파일모드, 인코딩)
# 파일명 : 파일 경로+파일명 (파일 경로 입력x → 현재 위치에 저장)
# 파일모드 : r(read), w(write), a(append=추가,
# 파일이 없으면 생성 후 추가,
# 있다면 파일의 마지막에 내용 추가)

# score_file = open("score.txt", "w", encoding='utf-8') # t를 생략해도 기본적으로 text 형태이다.
# # w 는 지워버리고 새로 쓰기, a 는 이어서 쓰기
# print("수학: 50", file=score_file) # 내용 자체가 파일에 추가된다.
# print("영어 : 90", file=score_file)
# score_file.write("국어: 98" + "\n"+ "과학 : 45" + "\n")
# score_file.close()


# 파일 읽기 :
# read() : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# 파일 내용이 너무 길면 버퍼 오버 플로우가 발생
# readline() : 파일의 내용을 한 라인씩 읽어 들여, 문자열로 반환
# 더 이상 읽을 내용이 없으면 None 반환
# readlines() : 파일의 모든 라인을 순서대로 읽어 각각의 라인을 하나의 요소로 저장하는 리스트를 반환

# score_file = open("score.txt", "r", encoding='utf-8')

# print(score_file.read())

# while 1:
# 	line = score_file.readline()  # 한줄씩 읽는다.
# 	if not line:  # 더이상 읽을 라인이 없다면 None 값이 되고,
# 		break  # None = False
# 	print(line, end='')  # 한줄씩 읽어서 출력하기 때문에,
# # 줄바꿈 문자가 포함되어 있다.
# score_file.close()

# lines = score_file.readlines() # 해당 파일의 모든 라인을 순서대로 읽어서 리스트 생성
# for e in lines:
# 	print(e, end="")
# score_file.close()

# with 키워드 사용하기 : open() 이후에 자동으로 close()를 호출해주는 기능
# with open("score.txt", "r", encoding="utf-8") as score_file :
# 	print(score_file.read())
# print("프로그램의 끝")

from datetime import datetime

with open("password.txt", "w") as f:
    date = str(datetime.today().year) + str(datetime.today().month) \
        + str(datetime.today().day)
    while True:
        url = input("사이트 : ")
        if url == "exit": break
        my_str = url.replace("http://", "")
        my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
        password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + date + "!" + "jks"
        print("비밀번호 : " + password)# 각 사이트 비밀번호 자동으로 만들기
        f.write(password + "\n")