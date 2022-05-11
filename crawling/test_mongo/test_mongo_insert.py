from pymongo import MongoClient
from pymongo.cursor import CursorType


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


test = [{"company": "국민", "title": "안녕"}, {"company": "몽고",
                                           "title": "들어가라"}, {"company": "테스트", "title": "ㅠㅠ"}]

# Mongo 연결
mongo = MongoClient("localhost", 20000)

mongo_save(mongo, test, "greendb", "navers")  # List안에 dict을 넣어야 함
