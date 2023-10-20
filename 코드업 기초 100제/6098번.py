def print_ls(ls):
	for i in range(10):
		for j in range(10):
			print(ls[i][j], end=' ')
		print()


def find(ls):
	# 시작점 설정
	a = 1
	b = 1
	ls[a][b] = 9
	for i in range(100):
		# 오른쪽 요소에 벽이 없으면 오른쪽으로 한칸 이동
		if ls[a][b + 1] != 1:
			b = b + 1
		# 아래 벽이 없다면, 아래로 한칸 이동
		elif ls[a + 1][b] != 1:
			a = a + 1
		if(ls[a][b]) == 2:
			ls[a][b] = 9
			break
		# 발자취
		ls[a][b] = 9

# 입력
x = [[0] * 10 for _ in range(10)]
y = [0] * 10
for i in range(10):
	y = list(map(int, input().split()))
	x[i] = y

find(x)
print_ls(x)
