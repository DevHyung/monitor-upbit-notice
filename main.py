import requests
import json
import time
from bs4 import BeautifulSoup
from pygame import mixer
mixer.init()
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}
if __name__ == "__main__":
    DELAY =  int( input(">>> 감시 주기 초단위 입력 ( 정수 ) ::"))
    # 바이낸스
    binanceList = []
    binanceList.clear()
    html = requests.get("https://support.binance.com/hc/en-us/sections/115000106672-New-Listings", headers=header)
    bs4 = BeautifulSoup(html.text, 'lxml')
    div = bs4.find("ul", class_='article-list')
    bposts = div.find_all("li")
    for barticle in bposts:
        bpost = barticle.find("a")
        binanceList.append(bpost.get_text().strip())
    print(">>> [바이낸스] 감시 시작 ")
    # 빗썸
    postList = []
    postList.clear()
    html = requests.get("http://bithumb.cafe/archives/category/notice", headers=header)
    bs4 = BeautifulSoup(html.text, 'lxml')
    div = bs4.find("div", id="primary-left")
    # 최근 post만 가져오기
    posts = div.find_all("article")
    for article in posts:
        post = article.find("h3").find("a")
        post_title = post.get_text().strip()
        postList.append(post_title)
    print(">>> [빗썸] 감시 시작 ")

    # 업비트
    isFirst = True
    idList = []
    idList.clear()
    if isFirst:
        print("\t>>> 초기 공지사항 업데이트 완료 ")
        html = requests.get('https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20')
        jsonlists = json.loads(html.text)
        total_count = jsonlists['data']['total_count']
        print("\t>>> 총 {} 개 수집 ".format(total_count))
        lists = jsonlists['data']['list']
        for list in lists:
            idList.append(list['id'])
    print(">>> [업비트] 감시 시작 ")
    while True:
        now = time.localtime()
        s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        try:
            html = requests.get('https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20')
            jsonlists = json.loads(html.text)
            lists = jsonlists['data']['list']
            for list in lists:
                if list['id'] not in idList:
                    idList.append(list['id'])
                    print("\t>>> [업비트] 감지   : ", s)
                    print("\t>>> [업비트] TITLE  : ", list['title'])
                    print("\t>>> [업비트] CREATE : ", list['created_at'])
                    print("\t>>> [업비트] UPDATE : ", list['updated_at'])
                    mixer.music.load('./alarm.mp3')
                    mixer.music.play()
        except:
            print(">>> 업비트 확인바람 ")

        try:
            html = requests.get("http://bithumb.cafe/archives/category/notice", headers=header)
            bs4 = BeautifulSoup(html.text, 'lxml')
            div = bs4.find("div", id="primary-left")
            posts = div.find_all("article")
            for article in posts:
                post = article.find("h3").find("a")
                post_title = post.get_text().strip()
                if post_title not in postList:
                    postList.append(post_title)
                    print("\t>>> [빗썸] 감지   : ", s)
                    print("\t>>> [빗썸] TITLE  : ", post_title)
                    mixer.music.load('./alarm.mp3')
                    mixer.music.play()
        except:
            print(">>> 빗썸 확인바람 ")
        #
        try:
            html = requests.get("https://support.binance.com/hc/en-us/sections/115000106672-New-Listings", headers=header)
            bs4 = BeautifulSoup(html.text, 'lxml')
            div = bs4.find("ul", class_='article-list')
            bposts = div.find_all("li")
            for barticle in bposts:
                bpost = barticle.find("a")
                if bpost.get_text().strip() not in binanceList:
                    binanceList.append(bpost.get_text().strip())
                    print("\t>>> [바이낸스] 감지   : ", s)
                    print("\t>>> [바이낸스] TITLE  : ", bpost.get_text().strip())
                    mixer.music.load('./alarm.mp3')
                    mixer.music.play()
        except:
            print(">>> 바이낸스 확인바람 ")
        time.sleep(DELAY)


