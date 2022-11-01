import RPi.GPIO as GPIO
import time



# 각 버튼에 대응하는 라즈베리파이의 포트번호를 변수를 통해 지정하여 사용
SW1 = 5 
SW2 = 6
SW3 = 13
SW4 = 19

# 이후 각 버튼의 사용횟수를 저장하기 위한 4칸짜리 리스트 생성
List = [0, 0, 0, 0]

# 이전에 버튼이 눌린상태인지 아닌상태인지를 판단하기 위한 변수
# 이를 통해 up, down시의 조작을 관리할 수 있도록 하였다.
# 이전에 버튼이 눌린상태라면 1 아니라면 0이 출력되도록 하여 사용
beforeSwitch = 0

# 보드모드를 BCM으로 설정하고 이후 지정된 스위치를 사용하기 위해서 setup으로 설정
# 이때 버튼이 눌리지 않았을 때 0이 될 수 있도록 풀다운 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


try:
    while True:
        #각 SW변수를 input으로 받아 작동여부를 판단하기 위한 변수 설정
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)
        
        # 이전에 버튼이 눌리지 않은상태이며 sw버튼이 눌렸을 경우 리스트의 숫자 증가 및 출력
        # 이후 버튼이 눌렸으므로 beforeSwitch를 1로 설정하여 다른 if문이 사용되지 못하도록 한다.
        # sw4Value까지 동일함
        if sw1Value == 1 and beforeSwitch == 0:
            List[0] = List[0] + 1
            print('click1', List[0])
            beforeSwitch = 1

        elif sw2Value == 1 and beforeSwitch == 0:
            List[1] = List[1] + 1
            print('click2', List[1])
            beforeSwitch = 1

        elif sw3Value == 1 and beforeSwitch == 0:
            List[2] = List[2] + 1
            print('click3', List[2])
            beforeSwitch = 1

        elif sw4Value == 1 and beforeSwitch == 0:
            List[3] = List[3] + 1
            print('click4', List[3])
            beforeSwitch = 1
        
        # 만일 SwValue의 변수들이 버튼이 올라가 0이 되고 이전 버튼 눌림여부를 결정하는 beforeSwitch가 1이라면 0으로 되돌려 다시 버튼의 눌림 여부를 판단할 수 있도록 함
        elif (sw1Value == 0 and beforeSwitch == 1) & (sw2Value == 0 and beforeSwitch ==1 ) & (sw3Value == 0 and beforeSwitch ==1) & (sw4Value == 0 and beforeSwitch ==1):
            beforeSwitch = 0
            
        # 스위치 작동시 입력중복을 방지하기 위한 대기시간사용
        time.sleep(0.1)

# ctrl+c를 통해 인터럽트 발생시 빠져나오고 cleanup()을 실행하여 할당한 setup을 해제함
except KeyboardInterrupt:
    pass

GPIO.cleanup()