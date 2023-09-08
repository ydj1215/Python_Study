# https://www.acmicpc.net/problem/5543

ham = [0,0,0]
juice = [0,0]

ham[0] = int(input())
ham[1] = int(input())
ham[2] = int(input())
juice[0] = int(input())
juice[1] = int(input())

result = min(ham[0],ham[1],ham[2]) + min(juice[0],juice[1])
print(result-50)

