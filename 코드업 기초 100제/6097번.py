# 6097번
def func(a,b,c,d,ls):
	if b == 0: # 가로
		for i in range(0,c):
			ls[c-1][i] = 1
	elif b == 1: # 세로
		for i in range(0, c):
			ls[i][d-1] = 1

def printing(ls):
	for e in range(len(ls)):
		for i in range(len(ls[0])):
			print(ls[e][i],end=' ')
		print()

h,w=map(int,input().split())
ls = [[0]*w for _ in range(h)]
#n = int(input())
# for i in range(n):