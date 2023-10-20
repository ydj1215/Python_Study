# 집합 : 중복 제거 목적으로 자주 사요
# 순서 보장 X
# 중복 X
# mutable(read, write 가능하다는 뜻)

# 요소의 중복 제거 (set)
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3}
print(s3)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 교집합
print(s1.intersection(s2))
print(s1&s2)

# 차집합
print(s1.difference(s2))
print(s1-s2)

# 중복없는 로또 번호 만들기
import random
nums = set()
while 1:
    num = random.randrange(1,46)
    nums.add(num)
    if len(nums) == 6: break
print(nums)