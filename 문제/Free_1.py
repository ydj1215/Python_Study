# https://www.acmicpc.net/problem/10810
"""
n = int(input())
m = map(int, input())
map은 여러개의 변수를 동시에 입력 받을 때 사용,
보통 map(int, input().split()), list(map(int, input().split()))
와 같이 사용한다.
"""
import sys

# 입력
n, m = map(int, input().split())  # n : 바구니 개수, m : 공을 넣을 횟수
if n < 1 or m > 100:
    sys.exit()
val = [0] * n  # m 크기의 list 생성, 모든 요소를 0으로 초기화
# print(val)


# i = 0 굳이 안 써도 무방
for a in range(m):  # 0 1 2 3
    i, j, k = map(int, input().split())
    if 1 > i or i > j or j > n or 1 > k or k > n:
        sys.exit()
    for b in range(i - 1, j):  # val[a-1] ~ val[b-1] → 0 → c
        val[b] = 0
        val[b] += k
# 출력
for c in range(n):
    print(val[c])
