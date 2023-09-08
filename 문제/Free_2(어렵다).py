# https://www.acmicpc.net/problem/18437

# 입력
n = int(input())  # 직원의 수
up_number_list = list(map(int, input().split()))  # 상사 번호 입력
m = int(input())
for i in range(m):
    comand_list = list(map(int, input().split()))
    if comand_list[0] == 1:  # 1 i: i번 직원을 상사로 가지고 있는 모든 직원은 컴퓨터를 켠다.
        pass
    elif comand_list[0] == 2:  # 2 i: i번 직원을 상사로 가지고 있는 모든 직원은 컴퓨터를 끈다.
        pass
    elif comand_list[0] == 3:  # 3 i: i번 직원을 상사로 가지고 있는 직원 중에서 컴퓨터가 켜져있는 사람의 수를 출력한다.
        for i in range(len(up_number_list)):
            if up_number_list[i] < comand_list[1]:
                print()
