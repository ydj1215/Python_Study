# 6096
# 십자 뒤집기
def reverse(a):
	if a == 0:
		a = 1
	elif a == 1:
		a = 0
	else:
		exit()
	return a


# 출력
def printing(a):
	for t in range(19):
		for u in range(19):
			print(a[t][u], end=' ')
		print()


a = [[0] * 19 for _ in range(19)]
for i in range(19):
	b = list(map(int, input().split()))
	a[i] = b
n = int(input())
for m in range(n):
	x, y = map(int, input().split())
	p = 0
	q = 0
	for p in range(19):
		a[p][x - 1] = reverse(a[p][x - 1])
	for q in range(19):
		a[y - 1][q] = reverse(a[y - 1][q])
	printing(a)

printing(a)