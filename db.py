# mysql사용, localhost로 접속, 비밀번호는 0000으로 세팅할 것
# DB는 설정해두고 테이블은 필요한 4개의 컬럼을 포함해 세팅되어있다는 가정하에
# 커서명은 pytosql로 씀.

"""
데이터베이스   :
스키마         :
테이블         :
연결자         :
커서           :
"""

import pymysql #따로 설치해주어야하는 라이브러리임

def init() :
    pytosql = pymysql.connect(host='localhost' , user=’root’, password=’0000′, db=’car_information’, charset=‘utf8’)
    #1. 연결자생성, pytosql이라는 연결자명를 root/0000으로 로컬접속해서 car_information에 '접속'한다는 의미임

    cursor = pytosql.cursor()
    #2. 커서생성, cur이라는 커서를 생성해 대신 쿼리작성해줌

    sql =   '''
            ''' 
            #

    cursor.execute(sql) 
    #3. 커서를 이용해 서버에 쿼리를 간접적으로 보냄 

def save_data() :
    sql =   '''
            ''' 
            #

    cursor.execute(sql) 
    #3. 커서를 이용해 서버에 쿼리를 간접적으로 보냄 

def delete_data() :
    sql =   '''
            ''' 
            #

    cursor.execute(sql) 
    #3. 커서를 이용해 서버에 쿼리를 간접적으로 보냄

def get_data() :
    sql =   '''
             CREATE TABLE userTable (
             id INT(4) NOT NULL, 
             car_num INT(4) NOT NULL, 
             time_in INT(10) NOT NULL, 
             time_out INT(10) NOT NULL
             ''' 
             #클래스 내 4개 파람+키를 포함한 내용물을 포함한 테이블을 만드는 쿼리

    cursor.execute(sql) 
    #3. 커서를 이용해 서버에 쿼리를 간접적으로 보냄


def quit() :
    pytosql.commit()
    #DB에 수정내용 complete

    pytosql.close()
    #DB 연결 닫기


