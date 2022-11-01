import RPi.GPIO as GPIO
import time
# 기본적으로 1번문제의 코드를 기반으로 작성하여 스위치동작은 동일함

# 각 버튼에 대응하는 라즈베리파이의 포트번호를 변수를 통해 지정하여 사용
BUZZER = 12
SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19
beforeSwitch = 0

# 보드모드를 BCM으로 설정하고 이후 지정된 스위치를 사용하기 위해서 setup으로 설정
# 이때 버튼이 눌리지 않았을 때 0이 될 수 있도록 풀다운 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# 펄스형태로 사용할 수 있도록 PWM설정
p = GPIO.PWM(BUZZER,261)

try:
    while True:
        #각 SW변수를 input으로 받아 작동여부를 판단하기 위한 변수 설정
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)
        
        # 주파수 표의 도, 레, 미, 솔에 대응하는 주파수값을 ChangeFrequency를 통해 할당
        # 스위치 1,2,3,4의 순서대로 도,레,미,솔이 출력되며, 코드의 형태는 sw4까지 동일
        if sw1Value == 1 and beforeSwitch == 0:
            p.start(50)
            p.ChangeFrequency(523)
            print("C")
            time.sleep(0.3)
            p.stop()
            beforeSwitch = 1

        elif sw2Value == 1 and beforeSwitch == 0:
            p.start(50)
            p.ChangeFrequency(586)
            print("D")
            time.sleep(0.3)
            p.stop()
            beforeSwitch = 1

        elif sw3Value == 1 and beforeSwitch == 0:
            p.start(50)
            p.ChangeFrequency(659)
            print("E")
            time.sleep(0.3)
            p.stop()
            beforeSwitch = 1

        elif sw4Value == 1 and beforeSwitch == 0:
            p.start(50)
            p.ChangeFrequency(784)
            print("G")
            time.sleep(0.3)
            p.stop()
            beforeSwitch = 1
        # 만일 SwValue의 변수들이 버튼이 올라가 0이 되고 이전 버튼 눌림여부를 결정하는 beforeSwitch가 1이라면 0으로 되돌려 다시 버튼의 눌림 여부를 판단할 수 있도록 함
        elif (sw1Value == 0 and beforeSwitch == 1) & (sw2Value == 0 and beforeSwitch ==1 ) & (sw3Value == 0 and beforeSwitch ==1) & (sw4Value == 0 and beforeSwitch ==1):
            beforeSwitch = 0

        time.sleep(0.1)
        
# ctrl+c를 통해 인터럽트 발생시 빠져나오고 cleanup()을 실행하여 할당한 setup과 p를 초기화함
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()