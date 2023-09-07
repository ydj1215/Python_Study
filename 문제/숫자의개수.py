# https://www.acmicpc.net/problem/2577
import sys

a = int(input())
if a < 100 or a > 1000:
    sys.exit()

b = int(input())
if b < 100 or b > 1000:
    sys.exit()

c = int(input())
if c < 100 or c > 1000:
    sys.exit()

# 1000000(10^6) ~ 1000000000(10^9)
num = a * b * c
num_string = str(a * b * c)  # 17037300

val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if 1000000 <= num < 10000000:
    for i in range(7):
        index = int(num_string[i])
        val[index] +=1
elif 10000000 < num < 100000000:
    for i in range(8):
        index = int(num_string[i])
        val[index] +=1
elif 100000000 < num < 1000000000:
    for i in range(9):
        index = int(num_string[i])
        val[index] +=1

print(val)
