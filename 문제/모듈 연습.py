# # math 모듈을 사용하기 위해 import
# import math
#
# print(math.sin(1))  #
#
# # 모듈 내에 함수(메서드)가 여러개 존재하는 경우
# from math import sin, cos, tan
#
# print(cos(30))
# print(tan(45))
#
# # 모듈을 가지고 올 때, 충돌이나 긴 이름을 간결하게 사용하기 위해 별칭을 부여
# import math as m
#
# print(math.sin(34))
# # 위에 import math가 존재해서 되는 것, import math as m만 있다면 math. 불가능
# print(m.sin(40))
#
# # sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈
# import sys
#
# print("명령줄 인수 : ", sys.argv)
# print("실행 경로 : ", sys.path[0])
# sys.stdout.write("Hello, world!\n")  # low level 입출력
# sys.stderr.write("Error!\n")
# # sys.exit()  # 강제 종료
#
# # os 모듈 : 운영 체제와 상호 작용하기 위한 기능을 제공
# # 파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등
import os

cwd = os.getcwd() # 현재 작업 디렉터리 읽어오기
print("현재 작업 디렉터리 : ", cwd)

file_list = os.listdir("test_dir")
if not file_list:
    print("test_dir 디렉터리는 비어 있습니다.")
else:
    print("test_dir 디렉터리에 파일이 있습니다.")

# 디렉터리 생성
is_dir = os.path.isdir("test_dir")
if not is_dir:
    os.mkdir("test_dir")

# "test_dir" 디렉터리의 존재 여부 확인
is_dir = os.path.isdir("test_dir")
print(is_dir)
