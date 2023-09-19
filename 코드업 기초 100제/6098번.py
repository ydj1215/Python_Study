def find():
	pass

ls = [[0]*10 for _ in range(10)]
for e in ls:
	print(e)
	print()
for i in range(10):
	for j in range(10):
		ls[i][j] = map(int,input().split())

for e in ls:
	print(e)
	print()