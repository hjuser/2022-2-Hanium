"""
# mysql���, localhost�� ����, ��й�ȣ�� 0000���� ������ ��
# DB�� �����صΰ� ���̺��� �ʿ��� 4���� �÷��� ������ ���õǾ��ִٴ� �����Ͽ�
# Ŀ������ pytosql�� ��.

�����ͺ��̽�   :
��Ű��         :
���̺�         :
������         :
Ŀ��           :
"""


""" ��뿹��
while(���α׷� �۵�):
    init()
    if(���� �̺�Ʈ �߻�):
        save_data()
        quit()
    if(���� �̺�Ʈ �߻�):
        delete_data()
        quit()
    if(allocate()�Լ� �۵�):
        get_data()
        quit()
"""


""" �䱸�Ұ�.
    �ϵ����� �������� ��ȹ�Ҷ� 3����� n~ n+2�� �������� ������ Ž���� �� ���� �� ����

"""

import pymysql #���� ��ġ���־���ϴ� ���̺귯����

def init() :
    pytosql = pymysql.connect(host='localhost' , user=��root��, password=��0000��, db=��car_information��, charset=��utf8��)
    #1. �����ڻ���, pytosql�̶�� �����ڸ� root/0000���� ���������ؼ� car_information�� '����'�Ѵٴ� �ǹ���

    cursor = pytosql.cursor()
    #2. Ŀ������, cur�̶�� Ŀ���� ������ ��� �����ۼ�����

    sql =   '''
             CREATE TABLE userTable (
             id INT(4) NOT NULL, 
             car_num INT(4) NOT NULL, 
             time_in INT(10) NOT NULL, 
             time_out INT(10) NOT NULL
             
            ''' 
            #Ŭ���� �� 4�� �Ķ�+Ű�� ������ ���빰�� ������ ���̺��� ����� ����

    cursor.execute(sql) 
    #3. Ŀ���� �̿��� ������ ������ ���������� ���� 

def save_data(key_carin) :
    sql =   '''
            ''' 
            # ���� �̺�Ʈ �߻��� ������ ������ ����
            # �Է��� �޾Ƽ� �ش� Ű�� ������ �����Ѵ�

    cursor.execute(sql) 
    #3. Ŀ���� �̿��� ������ ������ ���������� ���� 

def delete_data(key_carout) :
    sql =   '''
            ''' 
            # ���� �̺�Ʈ �߻��� ������ ������ ����
            # �Է��� �޾Ƽ� �ش� Ű�� ������ �����Ѵ�

    cursor.execute(sql) 
    #3. Ŀ���� �̿��� ������ ������ ���������� ����

def get_data() : #�����Ұ��� �߰� �ڸ������� ���ΰ˻縦 �ϰ� �� ������ �����ð��� �ʿ��ҵ� (�����ϸ� ��յ�?) �ؼ� ������ �����˻縦 ��ų�� ������ų�� <<<
    sql =   '''
            ''' 
             # allocate()�Լ� �߻��� ����Ž���� �� ����

    cursor.execute(sql) 
    if (carexist): 
        if (already_parked < time_out): #�Է°� �߰��������� �ð��� ���� �ִ´ٸ� 
            return 0 #���� �迭�� �˻��϶�� �ǹ�
        else: #
            return 1 #�ٱ� �ڸ���� �ǹ���1
    else:
        return 2 #�߰� �ڸ��� ������ �ǹ���2
        
    #3. Ŀ���� �̿��� ������ ������ ���������� ����


def quit() :
    pytosql.commit()
    #DB�� �������� complete

    pytosql.close()
    #DB ���� �ݱ�





