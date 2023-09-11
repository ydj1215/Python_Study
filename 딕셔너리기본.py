# 딕셔너리 : key와 value이 한쌍으로 이루어진 구조 (자바의 map 과 유사)
# 중괄호{}로 감싸서 선언, 쉼표(,)로 구분
# 키와 값은 콜론(:)으로 구분

coffee_menu = {"Americano": 2500, "Esspresso": 3000, "Latte": 4000}
tea_menu = {"Black tea": 4000, "Green tea": 4000, "Milk tea": 5000}
food_menu = {"Cake": 5000, "Bakery": 6000, "Ice Cream": 7000}

print(coffee_menu)
print(coffee_menu.keys())
print(coffee_menu["Americano"])  # key로 값을 확인하는 방법
print(coffee_menu.get("Latte"))  # get 메서드로 키를 넣어서 값을 확인하는 방법
print(coffee_menu.values())

# update 함수 : 딕셔너리의 데이터를 한꺼번에 변경
dict_ex = {"곰돌이": 90, "안유진": 88, "장원영": 77}
dict_ex.update({"곰돌이": 100, "장원영": 90})
print(dict_ex)

# 정보 얻기 : keys(), values(), items()
dict1 = {"자바": 80, "자바 스크립트": 88, "HTML": 70}
print(dict1.keys())  # 딕셔너리에 포함된 키를 확인
print(dict1.values())  # 딕셔너리에 포함된 값 확인
print(dict1.items())  # 딕셔너리의 키와 값을 확인

# 키의 포함 여부 확인
print("HTML" in dict1)  # 해당 딕셔너리에 키가 포함되어 있는지 확인
print("Python" in dict1)
print(dict1.get("Python")) # 없으면 None,
print(dict1.get("HTML")) # 있으면 키에 해당하는 값을 보여준다.

# 반복문 사용으로 키를 사용해 값을 가져오기
for key in coffee_menu : # 딕셔너리를 for 문으로 수행하면, 요소의 키값을 자동으로 접근 가능
    print(key, ":", coffee_menu[key])