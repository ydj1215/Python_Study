# https://www.acmicpc.net/problem/4153

# while 1:
# 	a,b,c = map(int,input().split())
# 	if a==0 and b==0 and c==0:
# 		exit()
# 	else:
# 		if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
# 			print('right')
# 		else:
# 			print('wrong')
#

# 리스트 및 정렬 사용
while 1:
	a = list(map(int,input().split()))
	if a == [0] and a[1] == 0 and a[2] == 0:
		exit()
	a.sort()
	if a[2]**2 == a[0]**2 + a[1]**2:
		print('right')
	else:
		print('wrong')
