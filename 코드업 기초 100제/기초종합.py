# 6079
# a = int(input())
# b = []
# i=0
# for i in range(a):
# 	b.append(i)
# 	if sum(b)>a:
# 		break
# print(i-1)
import math

# 6080
# a,b = map(int,input().split())
# for i in range(1,a+1):
# 	for j in range(1,b+1):
# 		print(i,j)

# 6081 (16진수 구구단)
# a = int(input(), 16)  # 입력받은 걸 16진수로 받는다.
# for i in range(1, 16):
# 	print('%X*%X=%X' % (a, i, a * i))

# 6082
# a = int(input())
# b = []
# for i in range(1, a + 1):
# 	b.append(str(i))
#
# for j in range(0, len(b)):
# 	if b[j].__contains__('3') or b[j].__contains__('6') or b[j].__contains__('9'):
# 		b[j] = 'X'
# 	print(b[j], end=' ')

# 6083
# a,b,c=map(int, input().split())
# count = 0
# for i in range(0,a):
# 	for j in range(0,b):
# 		for m in range(0,c):
# 			count += 1
# 			print(i,j,m)
# print(count)

# 6084
# a,b,c,d = map(int, input().split())
# d = a*b*c*(d/10)/80000
# e  = math.floor(d)/10
# # 버림하고, 10으로 나누면 소수점 첫째자리에서 버린것과 같다.
# #print(e)
# print(f'{e} MB')

# 6085
a,b,c=map(int,input().split())
print(f'{a*b*c/8/1024/1024:.2f} MB')

