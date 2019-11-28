from bs4 import BeautifulSoup
import requests
import json
import flask
import urls
import pymysql




#db 연결
def get_connection():
    con = pymysql.connect(host='localhost', user='min', password='alstlrdl1!',db='dongguk_alarm',charset='utf8')
    return con

    
# 디비에 저장된 최신 게시물 번호를 가져옴
def get_db_notice_num(con, type_):
    # sql 
    sql = "SELECT * FROM recent_notice WHERE type = %(type)s"
    cursor = con.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, {'type': type_ })
    # 데이타 Fetch
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print(row['id'], row['type'], row['notice_num'])
        print("db 최신게시물 번호 : " + str(row['notice_num']))
        con.close()
        return row['notice_num']


# 웹으로 최신 게시물 번호를 가져옴
def get_web_notice_num(notice_url, type : str):
    req = requests.get(notice_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    print("web 최신 게시물 번호: " + soup.find("img",{"src":"/Web-home/manager/images/mbsPreview/icon_new.gif" }).parent.parent.find_all('td')[0].text)
    return int(soup.find("img",{"src":"/Web-home/manager/images/mbsPreview/icon_new.gif" }).parent.parent.find_all('td')[0].text)



#웹 에서 가져온 게시물의 넘버와 디비에 저장된 게시물의 넘버와 비교하는 함수
def is_new(web_board_num, db_board_num : int):
    if web_board_num != db_board_num: 
        return True
    else:
        return False


# 최종적으로 확인하는 것!
def isNew(type_ : str):
    if is_new(get_web_notice_num(urls.returnUrl(type_), type_), get_db_notice_num(get_connection(), type_)):
        print("최신가져왓음")
        return True
    else :
        print("아직갱신안됨")
        return False        





#푀신 게이물 번호로 db업레이트 합니다.
def update_num(type_ : str, web_board_num : int):

    print("update_num 실행=> type :" + type_ + " / web_num" + str(web_board_num) );

    conn = get_connection()
    sql = "UPDATE recent_notice SET notice_num = %s WHERE type = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (web_board_num, type_))
    conn.commit() 
    conn.close()


