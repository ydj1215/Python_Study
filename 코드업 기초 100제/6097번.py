# 6097번
def func(a, b, c, d, ls):
	if b == 0:  # 가로
		for i in range(d-1,d-1+a,1):
			if ls[c - 1][i] == 0:
				ls[c - 1][i] = 1
			else:
				continue
	elif b == 1:  # 세로
		for i in range(c-1,c-1+a,1):
			if ls[i][d-1] == 0:
				ls[i][d - 1] = 1
			else:
				continue
	return ls


def printing(ls):
	for e in range(h):
		for i in range(w):
			print(ls[e][i], end=' ')
		print()


h, w = map(int, input().split())
# ls = [[0] * w for _ in range(h)]
ls = [[0]*100 for _ in range(100)]
x = int(input())
for e in range(x):
	a, b, c, d = map(int, input().split())
	func(a, b, c, d, ls)
printing(ls)
