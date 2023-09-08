# https://www.acmicpc.net/problem/1453

# n = int(input())
# if n>100:
#     exit()
# val = list(map(int, input().split()))
# val2 = []
# if len(val) != n:
#     exit()
# count = 0
# for i in val:
#     if i not in val2:
#         val2.append(i)
#     else:
#         count +=1
# print(count)

N = input()
seat = input().split()
print(len(seat)-len(set(seat))) # set (집합)은 중복을 허용X