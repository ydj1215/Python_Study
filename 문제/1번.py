# [1] 정해진 형식으로 시간을 입력 받아 출력
# 입력 형식 : 22:5:5 → 오후 10시 05분 05초

hour, minute, sec = map(int, input("시간을 입력해주세요 : ").split(':'))
if hour > 12:
    hour = hour - 12
    print(f"오후 {hour:02}시 {minute:02}분 {sec:02}초")
else:
    print(f"오전 {hour:02}시 {minute:02}분 {sec:02}초")
