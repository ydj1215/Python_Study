from simple_colors import *  # 화면 출력시 컬러 지원
import threading  # 쓰레드 기능을 위한 import
import time  # sleep() 을 쓰기 위해 import
import random

from simple_colors import *  # 화면 출력에 컬러 넣기
import threading
import time
import random


class Unit:
	def __init__(self, pp, mp, ph, mh, hp):
		self.pPower = pp  # Physical Power
		self.mPower = mp  # Magical Power
		self.pHit = ph  # 물리 적중률
		self.mHit = mh  # 마법 적중률
		self.hp = hp  # 체력
		self.isAlive = True  # 생사 여부


class Charactor(Unit): # Unit 을 상속받아 캐릭터 클래스 생성
	def __init__(self, pp, mp, ph, mh, hp, um, job):
		Unit.__init__(self, pp, mp, ph, mh, hp) # 부모의 생성자 호출
		self.ultimate = um  # 궁극기 특성 추가
		self.job = job # 직업 추가

	def p_attack(self): # 물리 공격
		return self.pPower * self.pHit

	def m_attack(self): # 마법 공격
		return self.mPower * self.mHit

	def attack_ultra(self): # 궁국기
		return self.ultimate

	def is_alive(self): # 생사 여부 확인
		return self.isAlive

	def setDamage(self, damage): # 받은 데미지 계산
		if self.hp > damage:
			self.hp -= damage
			print(f"남아 있는 {green(self.job)}의 체력은 {blue(self.hp)} 입니다.")
			self.isAlive = True
		else:
			print(f"{green(self.job)}가 죽었습니다. 게임을 종료 합니다.")
			self.isAlive = False


# 스레드에서 실행할 함수
def wizard_th():
	print(f"{wizard.job}가 전투 준비를 완료 했습니다.")
	time.sleep(1)
	while True:
		time.sleep(5)
		if warrior.is_alive() == False or wizard.is_alive() == False:
			break
		val = random.randrange(0, 2)
		ul = random.randrange(0, 18)
		if val == 0:
			print(f"{blue('물리공격')} >> {warrior.job}에게 {yellow(wizard.p_attack())} 데미지를 입혔습니다.")
			warrior.setDamage(wizard.p_attack())
		else:
			print(f"{yellow('마법공격')} >> {warrior.job}에게 {yellow(wizard.m_attack())} 데미지를 입혔습니다.")
			warrior.setDamage(wizard.m_attack())
		if ul == 1:
			print(f"{red('궁극기 발동')} >> {warrior.job}에게 {red(wizard.attack_ultra())} 데미지를 입혔습니다.")
			warrior.setDamage(wizard.attack_ultra())


# 메인 영역
if __name__ == "__main__":  # main thread 흐름을 타는 시작점

	name1 = input("전사는 강력한 체력의 물리공격형 캐릭터 (이름 입력) : ")
	name2 = input("마법사는 강력한 마법 공격형 캐릭터 (이름 입력) :  ")

	warrior = Charactor(8, 2, 0.8, 0.5, 150, 40, name1)  # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기
	wizard = Charactor(2, 20, 0.5, 0.9, 60, 55, name2)  # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기
	x = threading.Thread(target=wizard_th) # 스레드 생성
	print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
	time.sleep(1)
	x.start()  # 서브 스레드 시작
	while True:
		time.sleep(5)
		if warrior.is_alive() == False or wizard.is_alive() == False: # 둘 중의 한명이 죽으면,
			break
		val = random.randrange(0, 2) # 일반 공격
		ul = random.randrange(0, 12) # 궁극기
		if val == 0:
			print(f"{blue('물리공격')} >> {wizard.job}에게 {warrior.p_attack()} 데미지를 입혔습니다.")
			wizard.setDamage(warrior.p_attack())
		else:
			print(f"{yellow('마법공격')} >> {wizard.job}에게 {warrior.m_attack()} 데미지를 입혔습니다.")
			wizard.setDamage(warrior.m_attack())
		if ul == 1:
			print(f"{red('궁극기 발동')} >> {wizard.job}에게 {red(warrior.attack_ultra())} 데미지를 입혔습니다.")
			wizard.setDamage(warrior.attack_ultra())

"""
주어진 코드에서는 2개의 스레드가 동시에 동작합니다.
1. main 스레드: 이 스레드는 프로그램이 시작될 때 메인 스레드로 실행됩니다.
	사용자로부터 입력을 받고, 물리 공격 및 마법 공격을 실행하는 역할을 합니다.
2. wizard_th 스레드: 이 스레드는 x 스레드로 시작하며,
	마법사 캐릭터의 동작을 시뮬레이션하는 역할을 합니다.
	물리 공격, 마법 공격 및 궁극기 발동을 무작위로 선택하여 실행하고,
	결과를 출력합니다.
"""