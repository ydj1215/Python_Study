# while 1:
#     try:
#         print("나눗셈 계산기 입니다.")
#         num1 = int(input("첫 번째 숫자 입력 : "))  # 첫 번째 숫자 입력
#         num2 = int(input("두 번째 숫자 입력 : "))  # 두 번째 숫자 입력
#         result = int(num1 / num2)  # 나눗셈 결과 계산
#         print(f"{num1} / {num2} = {result}")  # 결과 출력
#     except ValueError:
#         print("오류 발생, 잘못된 값을 입력 하였습니다.")  # 입력 값이 숫자가 아닌 경우 예외 처리
#     except ZeroDivisionError as err:
#         print(err)  # 0으로 나누는 경우 예외 처리 및 에러 메시지 출력
#     except Exception as err:
#         print(err)  # 다른 예외 상황을 처리하고 에러 메시지 출력
#     else:  # 예외가 발생하지 않았을 때 실행 (정상 실행시 호출 조건 분기 되는 위치)
#         print("정상 처리 되었습니다.")
#     finally: # 예외 발생 여부와 관계없이 항상 실행
#         print("프로그램 실행이 완료되었습니다.\n")

try :
	score_file = open("score.txt", 'r', encoding='utf-8')
	print(score_file.read())
	score_file.close()
except FileNotFoundError:
	pass