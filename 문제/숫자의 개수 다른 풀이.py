a,b,c = map(int, input("정수 3개 입력").split())

total_val = str(a*b*c)
for i in range(10):
    print(total_val.count(str(i))) # count() 는 문자열에 문자가 몇개 존재하는지 반환
    # i = 0 : 0 이 몇개 존재?
    # i = 1: 1 이 몇개 존재? ...