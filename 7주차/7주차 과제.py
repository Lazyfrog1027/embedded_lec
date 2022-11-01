import RPi.GPIO as GPIO
import threading
import serial
import time

# 7주차 실습에서의 코드와 6주차 과제에서 사용했던 코드를 기반으로 작성되었습니다.


# 모터의 전원과 방향제어를 위한 핀번호를 변수로 지정
PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

# thread를 실행하여 휴대폰에서 전송된 문자를 gData에 저장하여 언제든 받을 수 있도록 함
def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data
        
# 이후 메인 함수를 통해 각 변수로 지정된 핀번호를 setup을 통해 설정하여 사용하도록 함
# 기본 설정 이후 try ~ while을 통해 gData에 저장된 글자에 따라 동작에 맞는 모터와 방향제어를 실행한다
def main():
    global gData
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PWMA,GPIO.OUT)
    GPIO.setup(PWMB,GPIO.OUT)
    GPIO.setup(AIN1,GPIO.OUT)
    GPIO.setup(AIN2,GPIO.OUT)
    GPIO.setup(BIN1,GPIO.OUT)
    GPIO.setup(BIN2,GPIO.OUT)
    
    L_Motor = GPIO.PWM(PWMA,500)
    R_Motor = GPIO.PWM(PWMB,500)
    L_Motor.start(0)
    R_Motor.start(0)

    try:
        while True:
            if gData.find("go") >=0:
                gData = ""
                print("ok go")
                GPIO.output(AIN1,0)
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1)
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(100)
            elif gData.find("back") >= 0:
                gData = ""
                print("ok back")
                GPIO.output(AIN1,1)
                GPIO.output(AIN2,0)
                GPIO.output(BIN1,1)
                GPIO.output(BIN2,0)
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(100)
            elif gData.find("left") >= 0:
                gData = ""
                print("ok left")
                GPIO.output(AIN1,0)
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1)
                L_Motor.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(100)
            elif gData.find("right") >= 0:
                gData = ""
                print("ok right")
                GPIO.output(AIN1,0)
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1)
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(0)
            elif gData.find("stop") >= 0:
                gData = ""
                print("ok stop")
                L_Motor.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)

    except KeyboardInterrupt:
        pass
    
GPIO.cleanup()

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()