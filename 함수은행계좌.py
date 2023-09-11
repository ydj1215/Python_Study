# balance = 0 # immutable, 외부에서 선언했지만 매개변수로 전달하여 결과를 return 받는다.
balance = [0]  # mutable

# 계좌 개설
def open_account(name):
    print(f"{name}님의 계좌가 개설되었습니다.")
    return name  # 반환 값으로 이름을 전달

# 입금 함수
def deposit(input):  # 잔고, 입금액
    # global balance  # balance = 0 일때는 global 이 필요하다
    balance[0] += input
    print(f"{input}원이 입금되었습니다. 현재 잔액은 {balance[0]}원 입니다.")

# 출금 함수
def withdraw(output):  # 잔고, 입금액
    # global balance
    if balance[0] >= output:
        balance[0] -= output
        print(f"{output}원이 출근되었습니다. 현재 잔액은 {balance[0]}원 입니다.")
    else:
        print("잔액이 부족합니다.")

name = open_account("유동재")
deposit(1000)
withdraw(500)
print(f"{name}님 계좌의 현재 잔액은 {balance[0]}원 입니다.")
