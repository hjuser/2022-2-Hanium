from multiprocessing import Process, Queue, Pipe
import os, os.path

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
    task_queue = Queue() #Led, Motor를 제어할 큐 생성(task_queue_process_func()와 공유) task의 순서를 넣은거임 
    led_manip_queue = Queue() # Led를 프로세스를 종료시켜주기 위한 큐
    task_queue_process = Process(target=task_queue_process_func, args=(task_queue)) #프로세스 큐 독립생성 (모터, 카메라)
    led_queue_erase_process = Process(target=Led_erase, args=(led_manip_queue)) #프로세스 큐 독립생성 (Led)
    while(1):
        car_info.reset(car_info) #초기화 
        when_car_entered(car_info, task_queue, led_manip_queue, amount_num) #입차 메소드 실행 

if __name__ == '__main__':
  main()

# 1 <<

def when_car_entered(car_info, task_queue, led_manip_queue, amount_num): #입차 메소드
    if (UI_for_enterd_car != 0): #UI입력 기다림
        if (amount_num < 36): #만차 확인
            amount_num = amount_num + 1 #입차 카운트
            car_info = allocate_car(car_info) #주차지 할당 
            task_queue.put(car_info.arr) #배차지 큐에 넣음 
            Led_manip_process = Process(target=manipulating_Led, args=(car_info.arr)) #LED프로세스 실행
            led_manip_queue.put(Led_manip_process) #프로세스 ID큐에 넣음 
        else: print("parking lot full")
    else: print("ready for car entered")

def task_queue_process_func(car_info, task_queue):
    while(1):
        #큐에 아무것도 없을 경우를 위한 예외처리 
        from_queue = task_queue.get() #from_queue돌고 있는 태스크 (.arr)
        if (from_queue != 0): pass # 큐에 없으면 다시 받으러 가~
        else: #있으면 통신치고 끝날때까지 기다리다가 끝나면 종료신호 singal파일에 작성해
            manipulating_Motor(from_queue)
            signal = manipulating_Camera(from_queue) #signal 종료시그널
            while (1):
                if (signal == 1): #확인해서 종료신호 들어오면 끝난 태스트 .arr 파이프출력
                    fname = './signal'
                    if not os.path.exists(fname): 
                        os.mkfifo(fname)
                    if os.path.exists(fname):
                        fp_fifo = open(fname, "w")
                        fp_fifo.write(from_queue)
                        break

def Led_erase(led_manip_queue): #종료신호(.arr파이프신호) 확인해서
    fname = './signal'
    while (1):
        if os.path.exists(fname): fp_fifo = open(fname, "r")
        with open(fname, 'r') as fifo:
            data = fifo.read()
            if (data != 0): 
                task_overed_processs_pid = led_manip_queue.get()
                os.kill(task_overed_processs_pid,)  #led신호 그만보내게 프로세스 종료
            else: pass

# 2 <<

def UI_for_enterd_car(car_info): 
    ## UI에서 값들 받아오는거 (인터럽트아님)
    return car_info

def allocate_car(car_info):
    ## 주차지 할당하는 코드
    return car_info

def manipulating_Led(car_info.arr):
    ## LED제어 아두이노와 하는 통신 코드
    pass

def manipulating_Motor(next_task): #큐에 있던 다음 task
    ## 모터제어 아두이노와 하는 통신 코드
    pass

def manipulating_Camera(next_task): #큐에 있던 다음 task
    ## 차선인식 캠 제어 코드
    ## 끝나면 조건을 거쳐 return 1 해야함 
    return 1