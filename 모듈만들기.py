# 모듈 : 코드가 저장된 파일
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def password(url):
	my_str = url.replace("http://", "")
	my_str = my_str[:my_str.index(".")]  # 슬라이싱, 처음부터 . 위치 미만까지
	password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
	return password

# 아래 코드는 다른 파일에서 모듈 만들기를 import 한 경우에도 실행이 되어버린다.
# print(add(1,4))
# print(sub(4,2))

if __name__ == "__main__": # 현재 파일이 엔트리 포인트인지 확인할 때 사용
	# 이를 사용하면, 다른 파일에서 모듈만들기를 import했을때는 아래 코드가 실행되지 않는다.
	print(add(1,4))
	print(sub(4,2))
