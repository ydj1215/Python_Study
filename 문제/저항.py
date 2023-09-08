# https://www.acmicpc.net/problem/1076

color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
num1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num2 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
val1 = 0
val2 = 0
val3 = 0

a = input()
if a in color:
    val1 = num1[color.index(a)]
b = input()
if b in color:
    val2 = num1[color.index(b)]
c = input()
if c in color:
    val3 = num2[color.index(c)]

result = (val1 * 10 + val2) * val3

print(result)
