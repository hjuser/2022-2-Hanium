# mysql���, localhost�� ����, ��й�ȣ�� 0000���� ������ ��
# DB�� �����صΰ� ���̺��� �ʿ��� 4���� �÷��� ������ ���õǾ��ִٴ� �����Ͽ�
# Ŀ������ pytosql�� ��.

"""
�����ͺ��̽�   :
��Ű��         :
���̺�         :
������         :
Ŀ��           :
"""

import pymysql #���� ��ġ���־���ϴ� ���̺귯����

def init() :
    pytosql = pymysql.connect(host='localhost' , user=��root��, password=��0000��, db=��car_information��, charset=��utf8��)
    #1. �����ڻ���, pytosql�̶�� �����ڸ� root/0000���� ���������ؼ� car_information�� '����'�Ѵٴ� �ǹ���

    cursor = pytosql.cursor()
    #2. Ŀ������, cur�̶�� Ŀ���� ������ ��� �����ۼ�����

    sql =   '''
            ''' 
            #

    cursor.execute(sql) 
    #3. Ŀ���� �̿��� ������ ������ ���������� ���� 

def save_data() :
    sql =   '''
            ''' 
            #

    cursor.execute(sql) 
    #3. Ŀ���� �̿��� ������ ������ ���������� ���� 

def delete_data() :
    sql =   '''
            ''' 
            #

    cursor.execute(sql) 
    #3. Ŀ���� �̿��� ������ ������ ���������� ����

def get_data() :
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


def quit() :
    pytosql.commit()
    #DB�� �������� complete

    pytosql.close()
    #DB ���� �ݱ�


