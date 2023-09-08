# # 내장함수 : 파이썬이 기본적으로 제공, import 필요 X

# # 큰 값, 작은 값 찾기
# print(max(1, 2, 8, 6, 243, 234, 29, 63, 127, 600))
# print(min(1, 2, 8, 6, 243, 234, 29, 63, 127, 600))
#
# # 총합 구하기
# print(sum([1, 2, 8, 6, 243, 234, 29, 63, 127, 600]))  # list
# print(sum((1, 2, 8, 6, 243, 234, 29, 63, 127, 600)))  # tuple
# print(sum({1, 2, 8, 6, 243, 234, 29, 63, 127, 600}))  # dictionary
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력받은 수의 총합: {sum(num)}")
# print(f"입력받은 수의 총합: {sum(num) / len(num)}")  # 평균
#
# # 몫과 나머지
# print(divmod(101,4)) # (몫, 나머지) 반환
# print(f"몫 : {divmod(102,4)[0]}")
# print(f"나머지: {divmod(102,4)[1]}")

# 여러개의 값을 한번에 입력받아 리스트로 만들고,
# 리스트에서 최대값, 최소값, 합계, 평균, 몫과 나머지 구하기
#
# num = list(map(int, input().split()))
# print(num)
# print(f"""최대값 : {max(num)}
# 최소값 : {min(num)}
# 합계 : {sum(num)}
# 평균 : {sum(num)/len(num)}
# 몫 : {divmod(max(num),min(num))[0]}
# 나머지 : {divmod(max(num),min(num))[1]}
# """)

# 오름차순 정렬
print(sorted([2, 3, 45, 43, 213, 34, 76, 765, 8, 696, 85, 90]))

# 내림차순 정렬
list = sorted([2, 3, 45, 43, 213, 34, 76, 765, 8, 696, 85, 90], reverse = True)
print(list)
