# 네이버 뉴스 크롤링해서 몽고DB에 insert 하기
# 뉴스 - 국민일보 - 정치 데이터 여러 건 받아서 bs4로 html 파싱하기(company, title 받아오기)
# 현재 시간 insert 하기

from unittest import result
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import MongoClient
from pymongo.cursor import CursorType

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

# 현재시간
now = datetime.now()

for a in aid:
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")

        # http 상태 코드 보기
        # print(html.status_code)  # 200 뜨면 정상

        if(html.status_code == 200):
            soup = BeautifulSoup(html.text, 'html.parser')
            news_company_el = soup.select_one(
                ".media_end_linked_more_point")  # 신문사
            news_title_el = soup.select_one(
                ".media_end_head_headline")  # 기사 제목
            date = now.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간 담기
            result = {"company": news_company_el.get_text(),
                      "title": news_title_el.get_text(), "date": date}
            lists.append(result)
            # print(news_company_el.get_text())  # 텍스트만 추출하는 함수 get_text()
    except Exception as e:
        pass
# print(lists)


# 몽고DB에 insert 하기
def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


# Mongo 연결
mongo = MongoClient("localhost", 20000)

mongo_save(mongo, lists, "greendb", "navers")  # List안에 dict을 넣어야 함
