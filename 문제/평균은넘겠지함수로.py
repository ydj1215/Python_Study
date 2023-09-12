# 각 케이스에서 평균이 넘는 비율 구하는 함수
def over_rate():
	ls = list(map(int,input().split()))
	avr = sum(ls[1:])/len(ls[1:])
	cnt = 0
	for i in range(1,len(ls)):
		if ls[i]>avr:
			cnt+=1
	return cnt/len(ls[1:]) * 100

n = int(input())
rst = [] # 각 케이스에 대한 결과값을 받기 위한 리스트
for i in range(n):
	rst.append(over_rate())

for e in rst:
	print(f"{e:.3f}%")
	# 자동으로 4번째 자리에서 반올림해 소수점 세자리를 만들어준다.
	