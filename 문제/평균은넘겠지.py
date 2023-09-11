# https://www.acmicpc.net/problem/4344

c = int(input())
for i in range(0,c):
	n = list(map(int, input().split()))
	if len(n) > n[0]+1:
		exit()
	sum = 0
	avr = 0
	for j in range(1,len(n)):
		sum += n[j]
	avr = sum/n[0]
	# print(avr)
	count = 0
	for e in range(1,len(n)):
		if n[e]> avr:
			count +=1
	result = count/n[0] * 100
	print(f"{result:.3f}%")

