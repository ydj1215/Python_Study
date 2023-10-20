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
	for p in range(19):
		a[x - 1][p] = reverse(a[x - 1][p])
	for q in range(19):
		a[q][y - 1] = reverse(a[q][y - 1])

printing(a)
