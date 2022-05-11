# 네이버 뉴스 다운 받기 테스트
# 뉴스 - 국민일보 - 정치 데이터 여러 건 받아서 bs4로 html 파싱하기
# title, data 받아오기

from unittest import result
import requests
from bs4 import BeautifulSoup

# company, title, date 담기
result = {}

# aid=1~20까지인 기사의 title, date 담기
lists = []

# aid 기사 번호 : '0000000001'~'0000000020'
aid = []

# 숫자 1~20 -> 문자열 '0000000001'~'0000000020'
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
            news_company_el = soup.select_one(".media_end_linked_more_point")
            news_title_el = soup.select_one(".media_end_head_headline")
            news_date_el = soup.select_one(
                ".media_end_head_info_datestamp_time")
            result = {"company": news_company_el.get_text(),
                      "title": news_title_el.get_text(), "date": news_date_el.get_text()}
            lists.append(result)
            # print(news_company_el.get_text())  # 텍스트만 추출하는 함수 get_text()
    except Exception as e:
        pass

print(lists)
