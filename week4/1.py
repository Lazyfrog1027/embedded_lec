import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #보드 모드를 사용하기 위해 BCM이 아니라 BOARD를 사용함
GPIO.setup(36, GPIO.OUT) #GPIO 16의 BOARD번호인 36을 이용하였으며 GPIO.OUT을 통해 출력으로 이용하도록 설정함
GPIO.setup(37, GPIO.OUT) #GPIO 26의 BOARD번호인 37을 사용하며 설정은 위와 동일
GPIO.setup(38, GPIO.OUT) #GPIO 38의 BOARD번호인 38을 사용하며 설정은 위와 동일
GPIO.setup(40, GPIO.OUT) #GPIO 21의 BOARD번호인 40을 사용하며 설정은 위와 동일

#차량 키트가 왼쪽을 바라보는 것을 기준으로 1시방향 LED4부터 0.3초 간격으로 꺼졌다 켜짐
GPIO.output(40,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(40,GPIO.LOW)
time.sleep(0.3)
GPIO.output(38,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(38,GPIO.LOW)
time.sleep(0.3)
GPIO.output(37,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(37,GPIO.LOW)
time.sleep(0.3)
GPIO.output(36,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(36,GPIO.LOW)

# 마지막으로 사용이 끝난 GPIO를 리셋하여 다른 프로그램과의 충돌이 일어나지 않도록 함
GPIO.cleanup()