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
    task_queue_process = Process(target=task_queue_process_func, args=(task_queue)) #프로세스 큐 독립생성
    while(1):
        car_info.reset(car_info) #초기화 
        when_car_entered(car_info, task_queue, amount_num)

if __name__ == '__main__':
  main()

# 1 <<

def when_car_entered(car_info, task_queue, amount_num):
    if (UI_for_enterd_car != 0):
        if (amount_num < 36):
            amount_num = amount_num + 1
            car_info = allocate_car(car_info)
            task_queue.put(car_info.arr)
            manipulating_Led(car_info.arr)
            """
            1. 캠에서 주차 끝났다는 리턴 파이프로 받음
            2. 캠에는 새로운 get을 받음
            3. LED 제어 프로세스를 종료시킴 
            """
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
                if (signal == 1):
                    fname = './signal'
                    if not os.path.exists(fname): 
                        os.mkfifo(fname)
                    if os.path.exists(fname):
                        fp_fifo = open(fname, "w")
                        fp_fifo.write(from_queue)
                        break

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


"""
프로세스를 만들고 죽이는 법 start, run, join을 안넣었네...ㅎㅎ folk는 한번에 해주긴하는데...
프로세스를 만들고 종료시킬때 값을 리턴시킬수 있나? 아니면 파이프로 확인?
파이프의 이용 쓰는방법  -> a.pipe()이렇게 선언해서 recv()쓰려고 했는데 여러개 한번에 보려고 그냥
외부파일을 여는 방식으로 바꿨음.

외부파일여는걸로 확인은 쉬울거가은데 pid를 적어놔야했음. 그냥 그래서 pid는 큐에 넣어놓을까함.

task_queue에는 다음에 실행되어야할 task가

아근데 생각해보니까 통신보내서 옮기고 나면 끝이니까 프로세스가 계속 돌필요가 없네,,,,,,,,,,아 개멍청이었다....
그냥 led랑 Motor, Cam만 분리해서 모터랑 캠은 큐 순서대로 돌고 끝날때마다 led pid꺼주는 통신하면 될거같음....
pipe없이 큐만 쓰면 되는거였다..

파이썬에는 goto문이 없다고 함 funcmap을 쓰거나 while -break로 구현해야할듯
LED에 통신을 어떻게 할까 고민임. 독립프로세스를 따로 만들어 계속 통신을 할까 아니면 끝났다는 신호를 따로 보내줄까
후자가 쉽지만 연습을 위해 전자를 해본다.... 안되면 후자로 감 
"""