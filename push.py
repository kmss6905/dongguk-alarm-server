import requests
from bs4 import BeautifulSoup
import json
import flask
import threading
import check_board
import urls




#print(urls.get_urls_dic())



for _type_ in urls.get_urls_dic():

    ## 새로운 것인지 판단한다.
    ## 새로운 것이면 ? 파싱 더 하고 보내준다 + db 게시물 번호 업데이트
    if check_board.isNew(_type_):
        req = requests.get(urls.returnUrl(_type_))
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        title_ = ""
        if _type_ == "nomal":
            title_ = "[일반공지]"
        elif _type_ == "haksa":
            title_ = "[학사공지]"
        elif _type_ == "admission":
            title_ = "[입시공지]"
        elif _type_ == "scholarship":
            title_ = "[장학공지]"
        elif _type_ == "international":
            title_ = "[국제공지]"
        elif _type_ == "event":
            title_ = "[학술/행사 공지]"

        ## 1차 파싱
        ## new 라고 되어 있는 목록정보를 파싱합니다.
        ## 파싱내용 : 게시물 링크, 목록 타이틀
        for td_title in soup.select('td.title'):
            img = td_title.select('img')
            print(img)
            title_text = td_title.select('a')



            # ## 2차 파싱 : 해당 게시물이 이미지로 되어있는 게시물인지 확인하고 이미지가 있을 경우 해당 이미지를 알림 이미지 정보에 추가합니다.
            # print("1차 파싱결과 [링크] : " + "https://www.dongguk.edu/mbs/kr/jsp/board/" + title_text[0].get("href") +"\n"
            #       + "1차 파싱결과 [타이틀] : " + title_text[0].text)
            #
            # req_content = requests.get("https://www.dongguk.edu/mbs/kr/jsp/board/" + title_text[0].get("href"))
            # html_content = req_content.text
            # soup_content = BeautifulSoup(html_content, 'html.parser')
            # img_ = ""
            # for divs in soup_content.select("td.memo"):
            #     print(divs.find("div"))



                # soup.find("img", {"src": "/Web-home/manager/images/mbsPreview/icon_new.gif"}).parent.parent.find_all(
                #     'td')[0].text

            if img:
                url = 'https://fcm.googleapis.com/fcm/send'
                payload = {
                    "to": "/topics/test-topic"
                    ,
                    "data": {
                        "link": title_text[0].get("href"),
                        "title": title_,
                        "content": title_text[0].text,
                        "icon:":"ic_new",
                    }
                }
                #access_toke => you put fcm-server-key
                headers = {'content-type': 'application/json', 'Authorization': 'key={}'.format(access_token)}
                response = requests.post(url, data=json.dumps(payload), headers=headers)
                print(response.status_code)
                print(img)
                print(title_text[0].text)
                print(title_text[0].get("href"))

                 # db num update
                web_board_num = check_board.get_web_notice_num(urls.returnUrl(_type_), _type_)
                check_board.update_num(_type_, web_board_num)

    else:
        print("보내지 않습니다")











