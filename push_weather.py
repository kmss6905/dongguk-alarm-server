from bs4 import BeautifulSoup
import requests
import json
import urls



req = requests.get("https://www.weather.go.kr/weather/forecast/timeseries.jsp")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
#print(soup.select('tbody')[0].tr)
i = 0
a = []
is_rain = False
for tr in soup.select('tbody'):
    for tr_ in tr.select('tr'):
        i = i + 1
        if i == 4:
            for is_now in tr_.select('td'):
                # print(is_now.get('class'))
                if not is_now.get('class'):
                    if is_now.text != "":
                        print(is_now.text)
                        a.append(is_now.text)
                        if int(is_now.text) >= 60:
                            is_rain = True

print("감수확률 모음 : " + str(a))
print("최고 강수확률 : " + max(a))

content = ""
if is_rain:
    content = "우산 꼭 챙겨서 나가세요!! \n\n 오늘 같은 날 파전? (feat 너만알람) \n 동국대 최고 강수확률 : " + str(max(a))
else:
    content = "오늘 우산은 필요없어요! ^^\n\n 좋은하루 되세요 (feat 너만알람) \n 동국대 최고 강수확률 : " + str(max(a))


title_ = "[날씨 알람]"
payload = {
        "to": "/topics/weather"
        ,
        "data": {
            "title": title_,
            "content": content,
            "max": max(a),
            "icon:": "ic_new",
        }
    }
url = 'https://fcm.googleapis.com/fcm/send'
access_token = "AAAAYAsKOKc:APA91bEHFYNMhpS4sjJagX-UnVjmZRJEXTTRmtdA0UDAWml6uHinY-GTUfSTWUuyU9AIDqYI_WACZr31apXJPb1qYC6uT0L4Wl1rU-Ur9QK-rntM8bDB_qe6lkgNPOdogV5-_OXXBKmv"
headers = {'content-type': 'application/json', 'Authorization': 'key={}'.format(access_token)}
response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.status_code)
