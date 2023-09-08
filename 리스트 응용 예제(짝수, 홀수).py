val = list(map(int, input().split()))
# 짝수 = []
# 홀수 = []
# for i in range(len(val)):
#     if val[i] % 2==0:
#         짝수.append(val[i])
#     else:
#         홀수.append(val[i])
# print(f"짝수 : {짝수}, 홀수 : {홀수}")

# filter 이용
even = list(filter(lambda x: x%2 == 0, val))
odd = list(filter(lambda x: x%2 != 0, val))

print(f"짝수 : {even}")
print(f"홀수 : {odd}")
        
        