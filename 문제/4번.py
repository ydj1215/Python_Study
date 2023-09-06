# [4] 개수가 정해지지 않은 여러 개의 정수를 입력 받아, 합계와 평균 구하기

val = list(map(int, input("정수를 여러 개 입력해주세요 : ").split()))

num = len(val)  # 요소의 개수
i = 0
sum_number = 0

# for(int i=0; i<num; i++) 는 아래와 같이 구현 가능
# for i in range(num):
#     sum_number += val[i]

sum_number = sum(val) # 간단하게 이렇게도 가능
avr = sum_number / num

print(f"""
합계 : {sum_number}
평균 : {avr}
""")