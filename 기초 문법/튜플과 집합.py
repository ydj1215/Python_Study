# 튜플 : 변경X 시퀸스 자료형
# 튜플의 정의  : () 괄호 or 생략 가능
person = '곰돌이사육사', '서울시 강남구 역삼동', 20
print(person)

# 튜플 요소 접근하기
print(person[0])
print(person[1])

# 튜플의 언패킹
이름, 주소, 나이 = person
print(이름)
print(주소)
print(나이)

# 튜플의 언패킹 기능을 이용한 함수
def get_person():
    name = '가을'
    age = 23
    addr = '서울시 강남구 역삼동'
    return name, age, addr


result = get_person()  # 언패킹되서 전달되는 반환값을 패킹해서 받음
print(result)

a, b, c = get_person()
print(a)
print(b)
print(c)

tp = 1, 1, 2, 2, 2, 3, 3, 3, 3
print(tp.count(3))  # 매개 변수로 전달한 변수가 몇번 나오는지 확인하는 점수
print(tp.index(2))  # 매개 변수로 전달한 변수의 시작 인덱스를 반환

