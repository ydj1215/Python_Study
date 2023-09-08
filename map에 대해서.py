"""
맵(Map) 함수는 많은 프로그래밍 언어에서 사용되는 개념으로,
주어진 함수를 컬렉션(예: 리스트, 배열 등)의 각 요소에 적용하여 새로운 컬렉션을 생성하는 기능을 제공합니다.
이때, 원본 컬렉션의 각 요소를 함수에 전달하고,
함수는 그 요소를 가공하여 새로운 값을 반환합니다.
"""

# new_collection = map(function, iterable)
# 리스트 정의
numbers = [1, 2, 3, 4, 5]

# 각 요소를 제곱하는 함수 정의
def square(x):
    return x ** 2

# map 함수를 사용하여 리스트의 각 요소를 제곱
squared_numbers = map(square, numbers)

# 결과를 리스트로 변환
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)

# filter : 전달받은 값을 함수 내부에서 조건에 일치하는 것만 골라서 반환