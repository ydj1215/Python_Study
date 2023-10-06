def print_ls(ls):
	for i in range(10):
		for j in range(10):
			print(ls[i][j], end=' ')
		print()


def find(ls):
	# 출발 지점
	a = 1
	b = 1
	ls[a][b] = 9
	while True:
		# 도착 시 탈출
		if ls[a][b] == 2:
			ls[a][b] = 9
			return
		# 현재 위치 좌표
		if ls[a][b + 1] != 1:
			ls[a][b + 1] = 9
			b = b + 1
		else:
			ls[a + 1][b] = 9
			a = a + 1
		if a == 9 or b == 9:
			return


# 입력
x = [[0] * 10 for _ in range(10)]
y = [0] * 10
for i in range(10):
	y = list(map(int, input().split()))
	x[i] = y

find(x)
print_ls(x)
