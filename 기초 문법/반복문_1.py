# 반복문 : 조건이 참인 동안 계속 수행되는 구문
# n = int(input("정수를 입력하세요 : "))
# sum = 0
# while n:
#     sum += n
#     n -= 1  # n = 0 이면 거짓
#
# while True:
#     age = int(input("나이를 입력하세요 : "))
#     if 0 < age < 200:
#         break
#     print("나이 입력 범위가 벗어냈습나다.")
#
# for 요소 in sequence : sequence 각 요소를 순화하는데 사용 (자바의 향상된 for문과 비슷)
fruits = ["apple", "banna", "cherry", ["seoul", "korea"]]
print(fruits[3][1][0])
"""
[3] ["seoul", "korea"]
[1] "korea"
[0] k
# """
#
# for e in fruits:
#     print(e[0])
#
# str1 = "서울시 강남구 역삼동"
# for e in str1:  # 각 문자를 e에 할당
#     print(e, end="/")
#
# # for 변수 in range(시작값, 종료값, 증감값)
# n = int(input("정수를 입력하세요"))
# m = 0
# for i in range(1, n + 1):  # 1 이상 n+1 미만
#     sum += i
# print(sum)

# 이중 for문
# n = int(input("정수를 입력하세요 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         print("*", end=' ')
#     print()  # 기본적으로 줄바꿈의 의미가 존재

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print()

# 홀수/짝수 나누어 찍기
n = int(input("정수 입력 : "))
for i in range(0, n):
    for j in range(0, n):
        if j % 2 == 0:
            print(f"{j}은 짝수입니다.")
        else:
            print(f"{j}은 홀수입니다.")
    print()
