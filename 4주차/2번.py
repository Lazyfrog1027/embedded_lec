import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #BCM모드로 사용하도록 설정
GPIO.setup(21, GPIO.OUT) #GPIO 21번을 GPIO.OUT을 통해 출력으로 설정함
GPIO.setup(20, GPIO.OUT) #GPIO 20을 사용하며 설정은 위와 동일
GPIO.setup(16, GPIO.OUT) #GPIO 16을 사용하며 설정은 위와 동일
GPIO.setup(26, GPIO.OUT) #GPIO 26을 사용하며 설정은 위와 동일

# ctrl+c의 입력으로 꺼지는 것을 확인하기 위해 while문을 이용함
# try~except구문을 이용하며, 일반적인 실행상황인 try일때 모든 LED핀에 출력을 넣음
# 실행도중 KeyboardInterrupt를 사용하여 ctrl+c가 입력되면 입력되었던 모든 LED핀에 LOW가 출력되도록 함
while True:
    try:
        GPIO.output(21,GPIO.HIGH)
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.output(21,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        # 모든 LED핀의 출력이 LOW로 바뀐이후 각 GPIO핀에 설정되었던 입출력설정을 리셋함
        GPIO.cleanup()
        print("reset complete")
        break # 이후 break를 통해 프로그램 종료