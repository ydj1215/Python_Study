# 6093
# a = int(input())
# b = list(map(int, input().split()))
# if len(b) != a:
# 	exit()
# for i in range(a-1, -1, -1):
# 	print(b[i], end=' ')

# 6094
# a= int(input())
# b= list(map(int,input().split()))
# if len(b) != a:
# 	exit()
# print(min(b))

# 6095 (이차원 리스트)
# n = int(input())
# x = [[0] * 20 for i in range(20)] # 20*20의 이차원 리스트
# for j in range(n):
# 	a, b= map(int,input().split())
# 	x[a-1][b-1] = 1
#
# for e in range(19):
# 	for f in range(19):
# 		print(x[e][f], end=' ')
# 	print()

# 6096
a = [[0] * 19 for _ in range(19)]
for i in range(19):
	b = list(map(int, input().split()))
	a[i] = b
n = int(input())
for m in range(n):
	x, y = map(int, input().split())
	for p in range(19):
		if a[p][x-1] == 0:
			a[p][x - 1] =1
		else:
			a[p][x - 1] = 0
	for q in range(19):
		if a[y-1][q] == 0:
			a[y - 1][q] =1
		else:
			a[y - 1][q] =0
	# 출력
	for t in range(len(a)):
		for u in range(len(a[1])):
			print(a[t][t], end=' ')
		print()
	print()

		# 출력
for t in range(len(a)):
	for u in range(len(a[1])):
		print(a[t][t], end=' ')
	print()
