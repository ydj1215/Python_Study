# 문자의 ASCII 코드
# chr : 유니코드 값을 입력받아, 그 코드에 해당하는 문자를 출력
# ord : 문자를 유니코드 값으로 변환

for i in range(ord("A"), ord("Z") + 1):
    print(chr(i), end=" ")
print()
for i in range(90, 64, -1):
    print(chr(i), end=" ")
