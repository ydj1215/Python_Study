# 6079
# a = int(input())
# b = []
# i=0
# for i in range(a):
# 	b.append(i)
# 	if sum(b)>=a:
# 		break
# print(i)
import math
import random

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
# a,b,c=map(int,input().split())
# print(f'{a*b*c/8/1024/1024:.2f} MB')

# 6086
a = int(input())
if a==1:
	print(1)
else:
	s = 0
	for i in range(a):
		s += i
		if s>= a:
			break
	print(s)

# 6087
# n = int(input())
# for i in range(n+1):
# 	if i%3!=0:
# 		print(i, end=' ')

# 6088
# a,b,c = map(int,input().split())
# n = a +b*(c-1)
# print(n)

# 6089
# a,b,c=map(int,input().split())
# d = a*(b**(c-1))
# print(d)

# 6090 (재귀)
# def func(a, b, c, n):
# 	if n == 1:
# 		r = a
# 	else:
# 		r = func(a,b,c, n-1) * b + c
# 	return r
#
# a,b,c,d = map(int,input().split())
# print(func(a,b,c,d))

# 6091
# a, b, c = map(int, input().split())
# for i in range(1,a * b * c+1):
# 	if i % a == 0 and i % b == 0 and i % c == 0:
# 		print(i)
# 		break

# 6092
# a = int(input())
# if a<1 or a>10000:
# 	exit()
# b = [0]*23
# c = list(map(int,input().split()))
# for i in range(len(c)):
# 	b[c[i]-1] += 1
# for e in b:
# 	print(e, end=' ')