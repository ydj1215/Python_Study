# 제어문 : 조건문과 반복문을 의미하며 순차적인 흐름을 제어하는 목적으로 사용

n = int(input("정수를 입력하세요 : "))
if n > 100:
    print(f"{n}은 100보다 크다.")
elif n < 100:
    print(f"{n}은 100보다 작다.")
else:
    print(f"{n}은 100이다.")

# 조건문에서 문자열 비교
while 1:  # 자바이외에는 모두 숫자로 TRUE/FALSE 표기 가능
    season = input("현재 계절을 입력하세요 : ")
    if season == "spring":
        print("지금은 봄입니다.")
        break
    elif season == "summer":
        print("지금은 여름입니다.")
        break
    # elif season == "fall" or "autoum":  # 오류는 안뜨지만 잘못된 표기
    elif season == "fall" or season == "autoum":
        print("지금은 가을입니다.")
        break
    elif season == "winter":
        print("지금은 겨울입니다.")
        break
    elif season == "exit":
        print("종료합니다")
        break
    else:
        pass
