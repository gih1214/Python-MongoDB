# 네이버 뉴스 다운 받기 테스트
# 뉴스 - 국민일보 - 정치 데이터 여러 건 받아서 bs4로 html 파싱하기
# 기사 제목 받아오기

import requests
from bs4 import BeautifulSoup

# aid=1~20까지인 기사의 title 담기
lists = []

# '0000000001'~'0000000020'
aid = []

# 숫자 1~20 -> '0000000001'~'0000000020'
for i in range(1, 21):
    # print(str(i).zfill(10))
    aid.append(str(i).zfill(10))
# print(aid)

for a in aid:
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")

        # http 상태 코드 보기
        # print(html.status_code)  # 200 뜨면 정상

        if(html.status_code == 200):
            soup = BeautifulSoup(html.text, 'html.parser')
            news_el = soup.select_one(".media_end_head_headline")
            lists.append(news_el.get_text())
            # print(news_el.get_text())  # 텍스트만 추출하는 함수 get_text()
    except Exception as e:
        pass

# print(lists)
