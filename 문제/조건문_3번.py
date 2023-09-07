# 3번 문제 : 문자열 추가하기
# 2개의 문자열을 포인터 변수 s와 k에, 양의 정수를 정수형 변수 n에 각각 전달 받아,
# s 문자열의 뒷 부분에  n 개 문자를 문자열 k의 앞에 끼워 넣는 코드 작성
# s : seoul
# k : korea
# n : 2
# 결과 : ulkorea

s = input("s : ")
k = input("k : ")
n = int(input("n : "))

# front = s[len(s)-n:]  # [-n:0] -가 붙으면 문자를 뒤에서부터 탐색하는 것
front = s[-n:]
print(front+k)
