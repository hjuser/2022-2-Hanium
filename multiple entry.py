from multiprocessing import Process, Queue, Pipe
import os

class car_information: 
  def __init(self): #���� 
    self.car_num = 0
    self.time_in = 0
    self.time_out = 0
    self.car_arr = 0
  def reset(self): #�ʱ�ȭ
    self.car_num = 0
    self.time_in = 0
    self.time_out = 0
    self.car_arr = 0

# 0 <<

def main():
    amount_num = 0 # �������� �ڵ��� �� Ȯ���� ���� ����
    car_info = car_information() #�ڷ� Ÿ�Լ��� 
    task_queue = Queue() #Led, Motor�� ������ ť ����(task_queue_process_func()�� ����)
    task_queue_process = Process(target=task_queue_process_func, args=(car_info, task_queue)) #���μ��� ť ��������
    while(1):
        car_info.reset(car_info) #�ʱ�ȭ 
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
            1. ķ���� ���� �����ٴ� ���� �������� ����
            2. ķ���� ���ο� get�� ����
            3. LED ���� ���μ����� �����Ŵ 
            """
        else: print("parking lot full")
    else: print("ready for car entered")


def task_queue_process_func(car_info, task_queue):
    Motor_manip_process = Process(target=manipulating_Motor, args=(car_info.arr))
    Cam_manip_process = Process(target=manipulating_Camera, args=(car_info.arr))
 

# 2 <<

def UI_for_enterd_car(car_info): 
    ## UI���� ���� �޾ƿ��°� (���ͷ�Ʈ�ƴ�)
    return car_info

def allocate_car(car_info):
    ## ������ �Ҵ��ϴ� �ڵ�
    return car_info

def manipulating_Led():
    ## LED���� �Ƶ��̳�� �ϴ� ��� �ڵ�
    pass

def manipulating_Motor():
    ## �������� �Ƶ��̳�� �ϴ� ��� �ڵ�
    pass

def manipulating_Camera():
    ## �����ν� ķ ���� �ڵ�
    pass


"""
���μ����� ����� ���̴� ��
���μ����� ����� �����ų�� ���� ���Ͻ�ų�� �ֳ�? �ƴϸ� �������� Ȯ��?
�������� �̿� ���¹�� 
"""