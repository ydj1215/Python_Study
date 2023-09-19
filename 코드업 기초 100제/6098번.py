def find(ls):
	# 테두리
	for i in range(10):
		ls[0][i] = 1
		ls[i][0] = 1
		ls[9][i] = 1
		ls[i][9] = 1
	# 출발
	ls[1][1] = 9
	for m in range(9):
		for n in range(9):
			if ls[m][n+1] != 1:


def printing(ls):
	for i in range(len(ls)):
		for j in range(len(ls[0])):
			print(ls[i][j], end=' ')
		print()


ls = [[0] * 10 for _ in range(10)]
find(ls)
printing(ls)
