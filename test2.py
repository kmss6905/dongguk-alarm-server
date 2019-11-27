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
def get_db_notice_num(con, type):
    # sql 
    sql = "SELECT * FROM recent_notice WHERE type = %(type)s"
    cursor = con.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, {'type': type })
    # 데이타 Fetch
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print(row['id'], row['type'], row['notice_num'])
        con.close()
        return row['notice_num']


# 웹으로 최신 게시물 번호를 가져옴
def get_web_notice_num(notice_url, type : str):
    req = requests.get(notice_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    return int(soup.find("img",{"src":"/Web-home/manager/images/mbsPreview/icon_new.gif" }).parent.parent[0].text)



#웹 에서 가져온 게시물의 넘버와 디비에 저장된 게시물의 넘버와 비교하는 함수
def is_new(web_board_num, db_board_num):
    if web_board_num != db_board_num: 
        return True
    else:
        return False


#새로운 게시물일 경우 True 반환 아니면 False
def isNew(type_ : str):
    
    if is_new(get_web_notice_num(urls.returnUrl[type_]), type_) , get_db_notice_num(get_connection(), type_) :
        return True
    else :
        return False








#get_web_notice_num(urls.returnUrl('nomal'), 'hello')


#print("notice_num : " + str(get_notice_num(get_connection(), 'nomal')))
'''

req = requests.get(urls.returnUrl("nomal"))
html = req.text
soup = BeautifulSoup(html, 'html.parser')

for tr in soup.select("tr"):
    print(tr)'''
