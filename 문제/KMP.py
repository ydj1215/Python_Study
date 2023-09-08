# https://www.acmicpc.net/problem/2902

# a = list(input().split('-'))
# if len(a)>100:
#     exit()
# for i in range(len(a)):
#     if a[i][0].isupper() == 0:
#         exit()
#     elif a[i][1:].islower() == 0:
#         exit()
# print(f"{a[0][0]}{a[1][0]}{a[2][0]}")

# print(*filter(str.isupper,input()),sep='')
# * = 언패킹 연산자 : 필터링된 문자열을 개별적인 요소로 분리
# * 를 붙임으로서, 리스트의 모든 각 요소에 filter를 적용
# map(int, input().split())을 생각하자
# map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))

# 문자열에서 대문자만 추출하고 결합
print(''.join(map(lambda x: x if x.isupper() else '', input())))
# join() 메서드를 사용하면 문자열 조각들이 공백같은것이 없이 자연스럽게 연결된다.

# upper_str=""
# for e in input():
#     if e.isupper() : upper_str += e
# print(upper_str)