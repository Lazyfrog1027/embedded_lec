import RPi.GPIO as GPIO
import time

# 기본적으로 1번문제의 코드를 기반으로 작성하여 스위치동작은 동일함

# 각 모터를 작동하기 위한 변수를 사용하기 위해 보드의 포트넘버를 할당
PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24
SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19
beforeSwitch = 0

# 보드모드를 BCM으로 설정하고 이후 지정된 스위치를 사용하기 위해서 setup으로 설정
# 이때 버튼이 눌리지 않았을 때 0이 될 수 있도록 스위치에 대해서는 풀다운 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)

# 모터의 사용 및 속도 조절을 위한 PWM설정과 start명령
L_Motor = GPIO.PWM(PWMA,500)
R_Motor = GPIO.PWM(PWMB,500)
L_Motor.start(0)
R_Motor.start(0)


try:
    while True:
        #각 SW변수를 input으로 받아 작동여부를 판단하기 위한 변수 설정
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)
        
        # 앞으로 가기 위해서 각 모터의 방향을 설정하고 양쪽 모터를 구동하여 앞으로 이동
        # 이후 1초간의 구동 이후 양쪽 모터의 회전을 0으로 바꿈
        # 그 뒤 스위치의 중복입력을 방지하기 위한 beforeSwitch의 값을 1로 설정함
        if sw1Value == 1 and beforeSwitch == 0:
            print('forward')
            GPIO.output(AIN1,0)
            GPIO.output(AIN2,1)
            GPIO.output(BIN1,0)
            GPIO.output(BIN2,1)
            L_Motor.ChangeDutyCycle(100)
            R_Motor.ChangeDutyCycle(100)
            time.sleep(1.0)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)            
            beforeSwitch = 1
            
        # 오른쪽으로 가기 위해서 위의 앞으로 가는 모터부분에서 우측 바퀴회전을 줄여 왼쪽 바퀴만 회전하여 오른쪽으로만 가도록 조절함
        elif sw2Value == 1 and beforeSwitch == 0:
            print('right')
            GPIO.output(AIN1,0)
            GPIO.output(AIN2,1)
            GPIO.output(BIN1,0)
            GPIO.output(BIN2,1)
            L_Motor.ChangeDutyCycle(100)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)  
            beforeSwitch = 1
            
        
        # 왼쪽으로 가기 위해서 위의 앞으로 가는 모터부분에서 좌측 바퀴회전을 줄여 오른쪽 바퀴만 회전하여 왼쪽으로만 가도록 조절함
        elif sw3Value == 1 and beforeSwitch == 0:
            print('left')
            GPIO.output(AIN1,0)
            GPIO.output(AIN2,1)
            GPIO.output(BIN1,0)
            GPIO.output(BIN2,1)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(100)
            time.sleep(1.0)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)  
            beforeSwitch = 1
            
        # 뒤로가기 위해서 AIN과 BIN의 방향값을 전환하고 양쪽 모터회전을 100으로 설정하여 뒤로 가도록 조절함
        elif sw4Value == 1 and beforeSwitch == 0:
            print('back')
            GPIO.output(AIN1,1)
            GPIO.output(AIN2,0)
            GPIO.output(BIN1,1)
            GPIO.output(BIN2,0)
            L_Motor.ChangeDutyCycle(100)
            R_Motor.ChangeDutyCycle(100)
            time.sleep(1.0)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)  
            beforeSwitch = 1
        
        # 만일 SwValue의 변수들이 버튼이 올라가 0이 되고 이전 버튼 눌림여부를 결정하는 beforeSwitch가 1이라면 0으로 되돌려 다시 버튼의 눌림 여부를 판단할 수 있도록 함
        elif (sw1Value == 0 and beforeSwitch == 1) & (sw2Value == 0 and beforeSwitch ==1 ) & (sw3Value == 0 and beforeSwitch ==1) & (sw4Value == 0 and beforeSwitch ==1):
            beforeSwitch = 0

        time.sleep(0.1)

# ctrl+c를 통해 인터럽트 발생시 빠져나오고 cleanup()을 실행하여 할당한 setup을 해제함
except KeyboardInterrupt:
    pass

GPIO.cleanup()