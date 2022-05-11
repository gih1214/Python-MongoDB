# 네이버 뉴스 다운 받기 테스트
# 뉴스 - 국민일보 - 정치 데이터 한건 받아서 bs4로 html 파싱하기

import requests
from bs4 import BeautifulSoup

try:
    html = requests.get(
        "https://n.news.naver.com/mnews/article/005/0000000001?sid=100")

    # http 상태 코드 보기
    print(html.status_code)  # 200 뜨면 정상

    if(html.status_code == 200):
        soup = BeautifulSoup(html.text, 'html.parser')
        news_el = soup.select_one(".media_end_head_headline")

        print(news_el.get_text())  # 텍스트만 추출하는 함수 get_text()
except Exception as e:
    pass
