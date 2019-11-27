import requests
from bs4 import BeautifulSoup
import json
import flask
import threading
import check_board


req = requests.get('https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000')
html = req.text
soup = BeautifulSoup(html, 'html.parser')



for td_title in soup.select('td.title'):
    img = td_title.select('img')
    title_text = td_title.select('a')

    if img :
        url = 'https://fcm.googleapis.com/fcm/send'
        payload = {
                    "to":"/topics/test-topic"
                    ,
                    "data":{
                        "key1": "https://www.dongguk.edu/mbs/kr/jsp/board/"+title_text[0].get("href"),
                        "key2":"nice"
                        }
                    ,
                    "notification":{
                        "title":"[너만알람] 새로운 공지입니다.",
                        "body": title_text[0].text,
                        "image":"http://www.dongguk.edu/file/upload/board/3646/editor/2019/11/20191125_092532160_28289.png",
                        "icon":"ic_new",
                        "color":"#0000FF"
                        }
                    }


        access_token = "AAAAYAsKOKc:APA91bEHFYNMhpS4sjJagX-UnVjmZRJEXTTRmtdA0UDAWml6uHinY-GTUfSTWUuyU9AIDqYI_WACZr31apXJPb1qYC6uT0L4Wl1rU-Ur9QK-rntM8bDB_qe6lkgNPOdogV5-_OXXBKmv"
        headers = {'content-type': 'application/json', 'Authorization': 'key={}'.format(access_token)}
        if test2.isNew("nomal"):    
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            print(response.status_code)
            print(img)
            print(title_text[0].text)
            print(title_text[0].get("href"))
        else:
            print("보내지 않습니다")

