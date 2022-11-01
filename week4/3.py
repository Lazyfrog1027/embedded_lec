import RPi.GPIO as GPIO
import random # 무작위 선정을 위한 random import
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

pinNum = [21, 20, 16, 26] # 핀번호를 무작위로 불러오기 위한 리스트 생성

i = 0 # 시행횟수를 위해 생성된 변수 i
choice = 0 # 무작위로 선정된 LED를 다시 끄기 위해 일시적으로 핀번호를 저장하기 위한 변수
while i < 10:
    choice = random.choice(pinNum) #매 시행마다 pinNum리스트에서 랜덤으로 핀번호를 선정하여 choice에 저장함
    GPIO.output(choice,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(choice,GPIO.LOW)
    i+=1
    
GPIO.cleanup() # 프로그램 종료시 입출력 설정을 reset하여 종료