n = int(input())

val = list(map(int, input().split()))

# 영식 요금제
money = 0
for i in range(n):
    money += (val[i] // 30 + 1) * 10
# print(f"money:{money}")

# 민식 요금제
money_2 = 0
for i in range(n):
    money_2 += (val[i] // 60 + 1) * 15
# print(f"money:{money_2}")

if min(money, money_2) == money:
    print(f"M {money}")
else :
    print(f"Y {money_2}")
