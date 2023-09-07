# n 입력 받기
n = int(input("숫자의 개수를 입력하세요: "))

# 숫자들을 스페이스바로 구분하여 입력받기
user_input = input(f"{n}개의 숫자를 스페이스바로 구분하여 입력하세요: ")

# 입력 받은 숫자를 스페이스바로 구분하여 리스트로 변환
numbers = user_input.split()

# 리스트의 각 숫자를 정수로 변환
numbers = [int(num) for num in numbers]

# 변환된 숫자 리스트 출력
print("입력된 숫자:", numbers)

# 한줄 코드
num = list(map(int, input("정수 입력 : ").split()))
print(num)
