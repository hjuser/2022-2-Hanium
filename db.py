"""
# mysql사용, localhost로 접속, 비밀번호는 0000으로 세팅할 것
# DB는 설정해두고 테이블은 필요한 4개의 컬럼을 포함해 세팅되어있다는 가정하에
# 커서명은 pytosql로 씀.

데이터베이스   :
스키마         :
테이블         :
연결자         :
커서           :
"""


""" 사용예시
while(프로그램 작동):
    init()
    if(입차 이벤트 발생):
        save_data()
        quit()
    if(출차 이벤트 발생):
        delete_data()
        quit()
    if(allocate()함수 작동):
        get_data()
        quit()
"""


""" 요구할것.
    하드웨어로 주차지를 구획할때 3배수로 n~ n+2로 주차지를 나눠야 탐색할 때 편할 것 같음

"""

import pymysql #따로 설치해주어야하는 라이브러리임

def init() :
    pytosql = pymysql.connect(host='localhost' , user=’root’, password=’0000′, db=’car_information’, charset=‘utf8’)
    #1. 연결자생성, pytosql이라는 연결자명를 root/0000으로 로컬접속해서 car_information에 '접속'한다는 의미임

    cursor = pytosql.cursor()
    #2. 커서생성, cur이라는 커서를 생성해 대신 쿼리작성해줌

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

def save_data(key_carin) :
    sql =   '''
            ''' 
            # 입차 이벤트 발생시 정보를 저장할 쿼리
            # 입력을 받아서 해당 키의 정보를 삭제한다

    cursor.execute(sql) 
    #3. 커서를 이용해 서버에 쿼리를 간접적으로 보냄 

def delete_data(key_carout) :
    sql =   '''
            ''' 
            # 출차 이벤트 발생시 정보를 제거할 쿼리
            # 입력을 받아서 해당 키의 정보를 삭제한다

    cursor.execute(sql) 
    #3. 커서를 이용해 서버에 쿼리를 간접적으로 보냄

def get_data() : #리턴할값이 중간 자리차량의 여부검사를 하고 그 차량의 출차시간이 필요할듯 (가능하면 평균도?) 해서 리턴은 다음검사를 시킬지 주차시킬지 <<<
    sql =   '''
            ''' 
             # allocate()함수 발생시 정보탐색을 쓸 쿼리

    cursor.execute(sql) 
    if (carexist): 
        if (already_parked < time_out): #입력과 중간차량과의 시간비교 오래 있는다면 
            return 0 #다음 배열을 검사하라는 의미
        else: #
            return 1 #바깥 자리라는 의미의1
    else:
        return 2 #중간 자리에 세우라는 의미의2
        
    #3. 커서를 이용해 서버에 쿼리를 간접적으로 보냄


def quit() :
    pytosql.commit()
    #DB에 수정내용 complete

    pytosql.close()
    #DB 연결 닫기





