# for문을 역순으로 반복하기
for i in range(10, -1, -1):  # 10~0까지 출력, 10에서 시작해서 1씩 감소하며 -1까지(미만)
    print(i)

# 사각형 찍기
# 정수값 n 을 입력받아 n * n 크기의 행렬을 출력하는 프로그램 작성

n = int(input("정수값을 입력하세요 : "))
# 별 찍기
# for i in range(n):
#     print("* "*n)

for i in range(1, n**2+1, 1):
    print(f"{i:>4}", end=" ") # 4칸, 오른쪽 정렬
    if(i%n) == 0:
        print()