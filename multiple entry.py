from multiprocessing import Process, Queue, Pipe
import os, os.path

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
    task_queue = Queue() #Led, Motor�� ������ ť ����(task_queue_process_func()�� ����) task�� ������ �������� 
    led_manip_queue = Queue() # Led�� ���μ����� ��������ֱ� ���� ť
    task_queue_process = Process(target=task_queue_process_func, args=(task_queue)) #���μ��� ť �������� (����, ī�޶�)
    led_queue_erase_process = Process(target=Led_erase, args=(led_manip_queue)) #���μ��� ť �������� (Led)
    while(1):
        car_info.reset(car_info) #�ʱ�ȭ 
        when_car_entered(car_info, task_queue, led_manip_queue, amount_num) #���� �޼ҵ� ���� 

if __name__ == '__main__':
  main()

# 1 <<

def when_car_entered(car_info, task_queue, led_manip_queue, amount_num): #���� �޼ҵ�
    if (UI_for_enterd_car != 0): #UI�Է� ��ٸ�
        if (amount_num < 36): #���� Ȯ��
            amount_num = amount_num + 1 #���� ī��Ʈ
            car_info = allocate_car(car_info) #������ �Ҵ� 
            task_queue.put(car_info.arr) #������ ť�� ���� 
            Led_manip_process = Process(target=manipulating_Led, args=(car_info.arr)) #LED���μ��� ����
            led_manip_queue.put(Led_manip_process) #���μ��� IDť�� ���� 
        else: print("parking lot full")
    else: print("ready for car entered")

def task_queue_process_func(car_info, task_queue):
    while(1):
        #ť�� �ƹ��͵� ���� ��츦 ���� ����ó�� 
        from_queue = task_queue.get() #from_queue���� �ִ� �½�ũ (.arr)
        if (from_queue != 0): pass # ť�� ������ �ٽ� ������ ��~
        else: #������ ���ġ�� ���������� ��ٸ��ٰ� ������ �����ȣ singal���Ͽ� �ۼ���
            manipulating_Motor(from_queue)
            signal = manipulating_Camera(from_queue) #signal ����ñ׳�
            while (1):
                if (signal == 1): #Ȯ���ؼ� �����ȣ ������ ���� �½�Ʈ .arr ���������
                    fname = './signal'
                    if not os.path.exists(fname): 
                        os.mkfifo(fname)
                    if os.path.exists(fname):
                        fp_fifo = open(fname, "w")
                        fp_fifo.write(from_queue)
                        break

def Led_erase(led_manip_queue): #�����ȣ(.arr��������ȣ) Ȯ���ؼ�
    fname = './signal'
    while (1):
        if os.path.exists(fname): fp_fifo = open(fname, "r")
        with open(fname, 'r') as fifo:
            data = fifo.read()
            if (data != 0): 
                task_overed_processs_pid = led_manip_queue.get()
                os.kill(task_overed_processs_pid,)  #led��ȣ �׸������� ���μ��� ����
            else: pass

# 2 <<

def UI_for_enterd_car(car_info): 
    ## UI���� ���� �޾ƿ��°� (���ͷ�Ʈ�ƴ�)
    return car_info

def allocate_car(car_info):
    ## ������ �Ҵ��ϴ� �ڵ�
    return car_info

def manipulating_Led(car_info.arr):
    ## LED���� �Ƶ��̳�� �ϴ� ��� �ڵ�
    pass

def manipulating_Motor(next_task): #ť�� �ִ� ���� task
    ## �������� �Ƶ��̳�� �ϴ� ��� �ڵ�
    pass

def manipulating_Camera(next_task): #ť�� �ִ� ���� task
    ## �����ν� ķ ���� �ڵ�
    ## ������ ������ ���� return 1 �ؾ��� 
    return 1