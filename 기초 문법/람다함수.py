# 람다 : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현한 것
# 파이썬에서 람다 함수를 통해 이름이 없는 함수 생성 가능
# 장점 : 코드의 간결함, 메모리의 절약

# def add(a,b):
#     return a+b
#
# print(add(1,2))
# print((lambda a,b : a+b)(3,4))

def call_times(func):  # "매개변수 = 함수" 가 가능 → 함수형 프로그래밍의 특정
    for i in range(10):
        func()


def print_hello():
    print("Hello!")


call_times(print_hello)


# filter() 함수와 map 함수
# filter(함수, 리스트) : 리스트의 요소를 함수에 넣고,
# return 값이 True인 것으로 새로운 리스트를 구성

# map(함수, 리스트) : 리스트의 요소를 함수에 넣고.
# 새로운 리스트를 구성해주는 함수

def power(n):
    return n * n


input = [1, 2, 3, 4, 5]
output = list(map(power, input))
output_2 = list(map(lambda n: n * n, input))
print(output)
print(output_2)

# 리스트에 람다 함수를 넣는 방법도 가능
my_list = [lambda a, b: a * b, lambda a, b: a + b]
print(my_list[0](5,2))
print(my_list[1](5,2))
