# 함수 : 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램

# 이름, 주소, 전화번호를 매개변수로 출력하는 함수
# def name_card(name, addr, phone):
#     print(f"주소 : {addr}")
#     print(f"전화번호 : {phone}")
#     print(f"이름 : {name}")
#     print("회사 : KH정보교육원")
#
# # 함수는 선언 이후 호출해야만 동작,
# # 한번 만들어진 함수를 여러번 호출하여 반복되는 코드를 줄이는 것이 가능
# name_card("안유진", "서울시 강남구 삼성동", "010-1234-5678")
# name_card("장원영", "서울시 강남구 역삼동", "010-0000-0000")
# name_card("이서", "서울시 강남구 청담동", "010-1111-2222")

# 순차 검색
# def search_list(a,x):
#     for i in range(len(a)):
#         if x == a[i] : return i
#     return -1
#
# v = [17,92,32,535]
# print(search_list(v,32))

# 기본값 인자 : 함수 선언 시 매개변수에 대해서 기본값 정의 가능
# 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시,
# 인자 값을 넣지 않으면 기본값이 호출된다.
# def profile(name, year=2, age=15, school="화산고"):
#     print(f"이름 : {name}, 학교 : {school}, 나이 : {age}, 학년 : {year}")
#
#
# profile("유동재")  # 나머지 값들은 default 값으로 자동 입력
# profile("백이진", 3, None)
#
#
# # 가변 매개변수 : 변수의 개수가 정해지지 않은 경우에 사용 : *(별 표)
# # *(별표)를 붙여주면, 함수의 배개변수가 몇개가 입력되던 함수 내에서 튜플로 인식
# def profile(name, age, *lang):
#     print(f"이름 : {name}, 나이 : {age}", end=' ')
#     for e in lang:
#         print(e, end=" ")
#     print()
#
# profile("나희도", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
# profile("조세호", 38, "Python", "Java", )
# profile("유재석", 48, "Python", "Java", "C", "C++", )

knife = 10  # 칼이 열자루 존재,


# 정수형 전역 변수 → global 필요

def game(player):
    global knife
    knife -= player
    print(f"남아 있는 칼은 {knife}자루 입니다.")


player = int(input("경기에 참여 하는 학생이 몇명입니까? : "))
game(player)
print(f"경기에 사용하고 남은 칼은 {knife}입니다.")
