def input_age():
    while True:
        age = input("나이: ")
        if age.isdigit():
            age = int(age)
            if 0 < age < 200:
                return age
        print("나이를 잘못 입력했습니다.")


def input_gender():
    while True:
        gender = input("성별 (M/F): ")
        if gender.lower() == 'm':
            return '남성'
        elif gender.lower() == 'f':
            return '여성'
        print("성별을 잘못 입력했습니다.")


def input_jobs():
    while True:
        jobs = input("직업 (1-4): ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 1 <= jobs <= 4:
                return jobs
        print("직업을 잘못 입력했습니다.")


def print_info(name, age, gender, jobs):
    jobs_str = "", "학생", "회사원", "주부", "무직"  # 튜플
    print("=" * 4 + "회원정보 " + "=" * 4)
    return f"""이름 : {name}
나이: {age}
성별: {gender}
직업: {jobs_str[jobs]}
    """


# 함수는 선언 이후 호출해야 동작
member_info = "member.txt"
fd = open(member_info, "at", encoding='utf-8')  # at는 파일 초기화X, 내용 추가
# ↑ member_info 가 아니라 바로 "member.txt"를 인자로 넣어도 된다.
while 1:
    name = input("이름: ")
    if name == "quit":
        break
    age = input_age()
    gender = input_gender()  # input_gender() 자체를 함수의 인자를 넣을 수 있다.
    jobs = input_jobs()
    result = print_info(name, gender, gender, jobs)
    fd.write(result + '\n')
fd.close()
