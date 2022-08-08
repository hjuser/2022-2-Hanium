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
    task_queue_process = Process(target=task_queue_process_func, args=(task_queue)) #���μ��� ť ��������
    while(1):
        car_info.reset(car_info) #�ʱ�ȭ 
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
            1. ķ���� ���� �����ٴ� ���� �������� ����
            2. ķ���� ���ο� get�� ����
            3. LED ���� ���μ����� �����Ŵ 
            """
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


"""
���μ����� ����� ���̴� �� start, run, join�� �ȳ־���...���� folk�� �ѹ��� ���ֱ��ϴµ�...
���μ����� ����� �����ų�� ���� ���Ͻ�ų�� �ֳ�? �ƴϸ� �������� Ȯ��?
�������� �̿� ���¹��  -> a.pipe()�̷��� �����ؼ� recv()������ �ߴµ� ������ �ѹ��� ������ �׳�
�ܺ������� ���� ������� �ٲ���.

�ܺ����Ͽ��°ɷ� Ȯ���� ����Ű����� pid�� �����������. �׳� �׷��� pid�� ť�� �־��������.

task_queue���� ������ ����Ǿ���� task��

�Ʊٵ� �����غ��ϱ� ��ź����� �ű�� ���� ���̴ϱ� ���μ����� ��� ���ʿ䰡 ����,,,,,,,,,,�� ����û�̾���....
�׳� led�� Motor, Cam�� �и��ؼ� ���Ͷ� ķ�� ť ������� ���� ���������� led pid���ִ� ����ϸ� �ɰŰ���....
pipe���� ť�� ���� �Ǵ°ſ���..

���̽㿡�� goto���� ���ٰ� �� funcmap�� ���ų� while -break�� �����ؾ��ҵ�
LED�� ����� ��� �ұ� �����. �������μ����� ���� ����� ��� ����� �ұ� �ƴϸ� �����ٴ� ��ȣ�� ���� �����ٱ�
���ڰ� ������ ������ ���� ���ڸ� �غ���.... �ȵǸ� ���ڷ� �� 
"""