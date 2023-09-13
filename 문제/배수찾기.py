# https://www.acmicpc.net/problem/4504

n = int(input())
if n <= 0 or n >= 1000:
	exit()

while 1:
	a = int(input())
	if a==0:
		break
	elif 0<a<10000:
		if a%n == 0:
			print(f'{a} is a multiple of {n}.')
		else:
			print(f'{a} is Not a multiple of {n}.')
	else:
		exit()