from multiprocessing import Process, Queue, Pipe
import os

class car_information: 
  def __init(self): #선언 
    self.car_num = 0
    self.time_in = 0
    self.time_out = 0
    self.car_arr = 0
  def reset(self): #초기화
    self.car_num = 0
    self.time_in = 0
    self.time_out = 0
    self.car_arr = 0

# 0 <<

def main():
    amount_num = 0 # 주차중인 자동차 수 확인을 위한 변수
    car_info = car_information() #자료 타입선언 
    task_queue = Queue() #Led, Motor를 제어할 큐 생성(task_queue_process_func()와 공유)
    task_queue_process = Process(target=task_queue_process_func, args=(car_info, task_queue)) #프로세스 큐 독립생성
    while(1):
        car_info.reset(car_info) #초기화 
        when_car_entered(car_info, task_queue, amount_num)

if __name__ == '__main__':
  main()

# 1 <<

def when_car_entered(car_info, task_queue, amount_num):
    if (UI_for_enterd_car != 0):
        if (amount_num++ < 36):
            car_info = allocate_car(car_info)
            task_queue.put(car_info.arr)
            Led_manip_process = Process(target=manipulating_Led, args=(car_info.arr))
            """
            1. 캠에서 주차 끝났다는 리턴 파이프로 받음
            2. 캠에는 새로운 get을 받음
            3. LED 제어 프로세스를 종료시킴 
            """
        else: print("parking lot full")
    else: print("ready for car entered")


def task_queue_process_func(car_info, task_queue):
    Motor_manip_process = Process(target=manipulating_Motor, args=(car_info.arr))
    Cam_manip_process = Process(target=manipulating_Camera, args=(car_info.arr))
 

# 2 <<

def UI_for_enterd_car(car_info): 
    ## UI에서 값들 받아오는거 (인터럽트아님)
    return car_info

def allocate_car(car_info):
    ## 주차지 할당하는 코드
    return car_info

def manipulating_Led():
    ## LED제어 아두이노와 하는 통신 코드
    pass

def manipulating_Motor():
    ## 모터제어 아두이노와 하는 통신 코드
    pass

def manipulating_Camera():
    ## 차선인식 캠 제어 코드
    pass


"""
프로세스를 만들고 죽이는 법
프로세스를 만들고 종료시킬때 값을 리턴시킬수 있나? 아니면 파이프로 확인?
파이프의 이용 쓰는방법 
"""