# https://www.acmicpc.net/problem/10810
"""
n = int(input())
m = map(int, input())
map은 여러개의 변수를 동시에 입력 받을 때 사용,
보통 map(int, input().split()), list(map(int, input().split()))
와 같이 사용한다.
"""
# 입력
n, m = map(int, input().split())  # n : 바구니 개수, m : 공을 넣을 횟수
val = [0] * n  # m 크기의 list 생성, 모든 요소를 0으로 초기화
print(val)

# i = 0 굳이 안 써도 무방
for i in range(m):
    a, b, c = map(int, input().split())
    val[a - 1] += c

# 출력
print(val[0], val[1], val[2], val[3], val[4])