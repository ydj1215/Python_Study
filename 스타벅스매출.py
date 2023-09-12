file_name = '스타벅스일일매출.txt'
f = open(file_name, 'r', encoding='utf-8')
head = f.readline()  # 파일의 첫번째 줄 읽기
head_list = head.split()  # 메뉴명을 공백 기준으로 잘라서 리스트로 변환

espresso = []
americano = []
cafelatte = []
cappucino = []

for line in f:  # f = 파일 객체, 파일의 읽는 위치를 가르키는 식별자,
	# 두번째 라인부터는 반복 처리
	data_list = line.split()
	espresso.append(int(data_list[1]))
	americano.append(int(data_list[2]))
	cafelatte.append(int(data_list[3]))
	cappucino.append(int(data_list[4]))
f.close()

print(f"{head_list[1]} 전체 판매량 : {sum(espresso)}, 일 평균 판매량 : {sum(espresso)/len(espresso)}")
print(f"{head_list[2]} 전체 판매량 : {sum(americano)}, 일 평균 판매량 : {sum(americano)/len(americano)}")
print(f"{head_list[3]} 전체 판매량 : {sum(cafelatte)}, 일 평균 판매량 : {sum(cafelatte)/len(cafelatte)}")
print(f"{head_list[4]} 전체 판매량 : {sum(cappucino)}, 일 평균 판매량 : {sum(cappucino)/len(cappucino)}")