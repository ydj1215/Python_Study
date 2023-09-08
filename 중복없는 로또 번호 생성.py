import random

result_list = []  # 결과를 저장할 리스트 생성

# 중복되지 않는 난수 6개 생성
while 1:
    n = random.randrange(1, 46)  # 1부터 45까지의 난수 생성
    # if n not in result_list:  # 결과 리스트에 중복이 없으면
    if list.__contains__(n) == 0: # 일반적으로 잘 사용X 문법, not in 을 사용하자.
        result_list.append(n)  # 결과 리스트에 추가
    if len(result_list) == 6:  # 결과 리스트에 6개의 숫자가 모이면 루프 종료
        break

print(result_list)  # 생성된 로또 번호 출력

# lambda, filter 연습
val = [2, 24, 123, 13, 64]
what = list(filter(lambda x: x % 2 == 0, val))  # 짝수만 필터링하여 리스트로 변환
print(what)  # 필터링된 결과 출력

