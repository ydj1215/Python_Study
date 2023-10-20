# 딕셔너리를 사용해 학생의 인적사항 등록, 검색, 저장, 불러오기 기능 구현
# 저장한 Rest API의 기본 형태인 JSON으로 저장 및 불러오기 (웹 API 기본 format)
# 함수로 구현

import json  # json 형식으로 데이터를 저장 및 불러오기 위한 모듈

student_dic = {}  # 학생 정보를 저장할 빈 딕셔너리 생성


# 학생 정보 등록 함수
def reg_student():
    print("<학생 등록>")
    student_id = input("학번 : ")
    name = input("이름 : ")
    addr = input("주소 : ")
    student_dic[student_id] = {"이름": name, "주소": addr}  # 값을 딕셔너리에 추가
    print(f"{name}님의 정보가 등록되었습니다.")


def search_student():
    print("<학생 찾기>")
    student_id = input("학번 : ")
    student_info = student_dic.get(student_id)  # get(key)
    if student_info:
        print(f"학번 : {student_id}")
        print(f"이름 : {student_info['이름']}")
        print(f"주소 : {student_info['주소']}")
    else:
        print("해당 학번의 학생 정보를 찾을 수 없습니다.")

# 학생 정보 저장
def save_student():
    with open('student.json', 'w', encoding='utf-8') as file:
        json.dump(student_dic,file,ensure_ascii=False)
    print("학생 정보가 저장되었습니다.")

# 저장된 데이터 불러오기
def load_student():
    try:
        with open('student.json', 'r', encoding='utf-8') as file:
            student_dic.clear() # 현재 데이터에 있는 데이터 초기화
            student_dic.update(json.load(file))
        print("학생 정보를 불러왔습니다.")
    except FileExistsError:
        print("저장된 학생 정보 파일을 찾을 수 없습니다.")

# 학생 정보 변경
def modify_student():
    print("<학생 정보 수정>")
    student_id = input("학번")
    student_info = student_dic.get(student_id)  # 학번을 key로 하여 해당하는 value(이름, 주소로 구성된 딕셔너리) 호출
    if student_info:
        name = input("새로운 이름 : ")
        addr = input("새로운 주소 : ")
        student_info['이름'] = name
        student_info['주소'] = addr
        print(f"{name}님의 정보가 수정되었습니다.")
    else:
        print("해당 학번의 학생 정보를 찾을 수 없습니다.")


# 학생 정보 삭제
def delete_student():
    print("<학생 정보 삭제>")
    student_id = input("학번 : ")
    if student_dic.get(student_id):
        del student_dic[student_id]  # 해당 딕셔너리를 키로 삭제
        print("학생 정보가 삭제되었습니다.")
    else:
        print("해당 학번의 학생이 존재하지 않습니다.")

    # 학생 전체 보기


def view_all_student():
    for student_id in student_dic:
        student_info = student_dic[student_id]
        print(f"학번 : {student_id}")
        print(f"이름 : {student_info['이름']}")
        print(f"주소 : {student_info['주소']}")
    # for student_id, student_info in student_dic.items(): # .items() 이용한 코드
    #     print(f"학번 : {student_id}")
    #     print(f"이름 : {student_info['이름']}")
    #     print(f"주소 : {student_info['주소']}")

while 1:
    print("<학생 정보 관리 프로그램>")
    choice = input("[1] 등록, [2] 검색, [3] 수정, [4] 삭제, [5] 전체보기, [6] 저장, [7] 불러오기, [8] 종료 : ")
    if choice == "1":
        reg_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        modify_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        view_all_student()
    elif choice == "6":
        save_student()
    elif choice == "7":
        load_student()
    elif choice == "8":
        break
    else:
        print("선택한 메뉴가 없습니다.")
