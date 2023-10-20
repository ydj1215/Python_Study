# list : 크기가 정해지지 않은 요소들에 대해 값을 저장하기 위한 자료형
# 아무 자료형으로 와도 상관X
# 중첩 사용이 가능 : [ [], [[], []], [], ]
# 뮤터블 객체 : 읽고 쓰기가 가능

number = [1, 2, 3, 4, 5, 6]
fruits = ["apple", "banana", "orange"]
mixed = [1, True, "seoul", 12.345]
dup = [[1, 2, 3, 4], ["apple", "키위"]]

# 변수와 리스트의 비교
kor, eng, mat = map(int, input("성적 입력 : ").split())
print(sum([kor, eng, mat]))

score = list(map(int, input("성적 : ").split()))
print(sum(score))


str_name = ['seoul', 'gangnam', 'suwon', 'inchun']
print(str_name)
print(str_name[1])

# 슬라이싱
name = "slice"
slice = str_name[1:3]  # 1~2 요소
print(slice)
print(len(slice[0]))  # gangnam

primes = [2, 3, 5, 7]
print(primes[0])
print(primes[-1])  # 7
print(primes[-2])  # 5

# 리스트 연산자 : 연결(+), 반복(*), len()
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)
print(list_a * 3)
print(len(list_a + list_b))

# 리스트 요소 추가하기 :
# append() : 리스트의 맨 마지막에 추가
# insert(index, value) : 해당 인덱스에 값을 삽입
list_a = [1, 2, 3]
list_a.append(4)
list_a.append(5)
list_a.insert(1, 10)
print(list_a)

# 리스트 제거하기 : pop(), remove(), clear(), del list(index)
# pop() : 인덱스가 없으면, 마지막 인덱스의 값을 반환 후 삭제,
# 인덱스가 있으면 해당 위치의 값을 삭제
# remove(value) : 해당하는 값을 제거, 만약 동일한 값이 여러개인 경우, 낮은 인덱스 값 제거
# clear() : 모든 값을 삭제, 리스트 지우지 X
list_all = [0,1,2,3,4,5,2,2,2,2,2]
print(list_all)
print(list_all.pop())
print(list_all.pop(2))
print(list_all)
list_all.remove(2) # 반환값 X
print(list_all)
list_all.clear()
print(list_all)
del list_all[3] # 해당 인덱스의 값을 지운다.

# # 중복 제거
my_list = [11,2,3,4,5,6,7,8,9,0,1,2,3,4,5,1,2,3,4,5]
new_list = []
for e in my_list:
    if e not in new_list:
        new_list.append(e)
print(new_list)

# map(반환함수, 입력자료형), filter(반환함수, 입력자료형) 동작 확인
num = list(map(lambda e: int(e) * int(e), input("값: ").split()))
print(num)

# map 리시트의 원소 스캔하기
x = ['John', 'George', 'Pau', 'Ringo']

for e in x: # 향상된 for문과 비슷한 형태
    print(e)

for i in range(len(x)): # 범위 기반 for문
    print([i])


