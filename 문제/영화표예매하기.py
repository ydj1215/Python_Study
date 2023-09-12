TICKET_PRICE = 12000
ls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pic = ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']


def printing(pic):
	for i in range(len(ls)):
		if ls[i] == 1:
			pic[i] = '[V]'
	for j in pic:
		print(j, end=" ")
	print("\n")


def ticketing(ls):
	printing(pic)
	index = int(input("좌석번호를 입력하세요 : "))
	if ls[index - 1] == 1:  # 예약 실패
		print("이미 예매가 완료된 좌석입니다.\n")
	else:  # 예약 완료
		ls[index - 1] = 1
		printing(pic)


def ending():
	print("종료합니다.")
	cnt = 0
	for i in range(len(ls)):
		if ls[i] == 1:
			cnt += 1
	printing(pic)
	print(f"총 비용은 {cnt * TICKET_PRICE}원 입니다.")
	# 내부에서 TICKET_PRICE 의 값이 변경이 없기 때문에,
	# global을 사용하지 않아도 되는 것.
	# 만약 TICKET_PRICE의 값의 변경이 존재했다면 global 이 필요하다.
	exit()


while 1:
	choice = int(input("[1] 예매하기, [2] 종료하기 : "))
	if choice == 1:  # 예매하기
		ticketing(ls)
	elif choice == 2:
		ending()
	else:
		print("올바른 선택지를 입력해주세요.")
