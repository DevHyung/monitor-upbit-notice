import requests
import json
import time
from pygame import mixer
mixer.init()
if __name__ == "__main__":
    DELAY =  int( input(">>> 감시 주기 초단위 입력 ( 정수 ) ::"))
    isFirst = True
    idList = []
    idList.clear()
    if isFirst:
        print(">>> 초기 공지사항 업데이트 완료 ")
        html = requests.get('https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20')
        jsonlists = json.loads(html.text)
        total_count = jsonlists['data']['total_count']
        print(">>> 총 {} 개 수집 ".format(total_count))
        lists = jsonlists['data']['list']
        for list in lists:
            idList.append(list['id'])
    print(">>> 감시 시작 ")
    while True:
        now = time.localtime()
        s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        html = requests.get('https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20')
        jsonlists = json.loads(html.text)
        lists = jsonlists['data']['list']
        for list in lists:
            if list['id'] not in idList:
                idList.append(list['id'])
                print("\t>>> 감지   : ", s)
                print("\t>>> TITLE  : ", list['title'])
                print("\t>>> CREATE : ", list['created_at'])
                print("\t>>> UPDATE : ", list['updated_at'])
                mixer.music.load('./alarm.mp3')
                mixer.music.play()
        time.sleep(DELAY)



