# https://www.acmicpc.net/problem/18437

import sys

n = int(input())  # 직원의 수
if 1 > n or n > 100000:
    sys.exit()
val = []
# for a in range(n):  # 직원의 수

m = int(input())  # 쿼리의 수
if 1 > m or m > 100000:
    sys.exit()
for b in range(m):
    i, j = map(int, input().split())
