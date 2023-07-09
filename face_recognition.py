import struct
import serial, time 
import sqlite3
import datetime 
import time 


#데이터베이스 파일에 저장
con= sqlite3.connect('C:/projects/mysite/db.sqlite3')

#커서 객체를 생성
cur = con.cursor()
#테이블 구조를 만들기(테이블 스키마 생성)

cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='iot_check_times';");
if cur.fetchone()[0]==1:
    print('Table exists.')
else:
    cur.execute("create table iot_check_times (id integer primary key autoincrement,subject_id integer, face_id integer, pfr integer , c_date datetime, out_times integer);")

    print("새로 생성됨")



#cur.execute("insert into iot_check_times (subject_id,face_id,pfr,c_date,out_times) values (6,6,2,2022,33);")
#con.commit()

#원도우용으로 시리얼 포트를 연다.

ser = serial.Serial(port = "COM12", baudrate=9600, timeout=1)
i = 0
pfr = 2
crt = datetime.datetime.now()
t1 = crt.strftime('%Y-%m-%d %H')

cur.execute("select id from auth_user where is_staff = 0;")
a_list=[]
for a in cur:
    a = int(a[0])
    a_list.append(a)
try:
    while True:
        if ser.readable()==True:
            tt=datetime.datetime.now()
            t2 = tt.strftime('%Y-%m-%d %H')

            if t1 == t2 :
              
                now_crt=datetime.datetime.now()
                if ser.readable()==True:
                    cc = ser.read(i)
                    ct=datetime.datetime.now()
                    ct1=datetime.datetime.strftime(ct , '%Y-%m-%d %H:%M:%S')
                    a = cc[:len(cc)-1].decode()
                    if a :
                        tmp = int(ct.strftime('%M'))
                        tmp_ct1 = int(ct.strftime('%H'))
                        a = a.split()
                        a = int(a[0])
                        if a in a_list and tmp <=15:
                            print("a in a_list ok")
                            if 0<= tmp <=10:
                                pfr = 2
                                print("너 출석")
                                sql = "insert into iot_check_times (subject_id,face_id,pfr,c_date,out_times) values (?,?,?,?,?);"
                                con.commit() 
                                val = (1, a, pfr, ct1, 0)
                                cur.execute(sql,val)
                                print(val)
                                a_list.pop(a)
                                
                            elif 10<= tmp <= 15:
                                pfr = 1
                                print("너 지각")
                                sql = "insert into iot_check_times (subject_id,face_id,pfr,c_date,out_times) values (?,?,?,?,?);"
                                con.commit() 
                                val = (1, a, pfr, ct1, 0)
                                cur.execute(sql,val)
                                print(val)
                                print(a_list.remove(a))
                                print(a_list)
                        elif tmp >15 :
                            print("외출함")
                            pfr = 0
                            print("너 외출")
                            #past = datetime.datetime.strptime(crt , '%Y-%m-%d %H:%M:%S')
                            past = crt.strftime('%M')
                            ct = ct.strftime('%M')
                            diff = int(ct) - int(past)
                            sql = "insert into iot_check_times (subject_id,face_id,pfr,c_date,out_times) values (?,?,?,?,?);"
                            con.commit() 
                            val = (1, a, pfr, ct1, diff) 
                            cur.execute(sql,val)
                            print(val)
                            if diff >= 1 :
                                sql = "update iot_check_times set pfr = 0 where pfr = 1 or pfr = 2 and out_times >= 10;"
                                con.commit()
                                cur.execute(sql)
                                print("결석")
                time.sleep(0.1)
                i += 1
            else :
                t1 = t2 
                        
finally:
    print('끝')    
