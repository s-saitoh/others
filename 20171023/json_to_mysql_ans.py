# !/usr/bin/env python

# PythonではJSONは辞書型で扱われる
# 用意されたJSONファイルをMySQLに流し込む

import MySQLdb
import json
import csv
import glob


def main():
    
    
    # DBに接続しカーソルを取得する
    connect = MySQLdb.connect(host='localhost', db='race',
                            port=3306, user='root',
                            passwd='', charset='utf8')
    cursor = connect.cursor()
    
    # 処理するファイル一覧を取得
    json_files = glob.glob('*.json')

    # レコードの挿入
    def insert_record():

        # JSONファイルの読み込み

        for f in json_files:
            try:
                with open(f, "r", encoding="utf-8") as files:
                    jsonData = json.load(files)
                    
            except json.JSONDecodeError as e:
                print('JSONDecodeError:', e)

            # jsonの中身を確認
            print(json.dumps(jsonData, sort_keys = True, indent = 4))

            ans_number = list(jsonData.keys())
            ans_str = list(jsonData.values())
            id_get = str(f)
            id_get = id_get[:-7]


            # SQL挿入


            sql_data = (id_get, ans_str)
            sql = "INSERT INTO race.race_answer(race_id, ans) VALUES (%s, %s)"
            cursor.execute(sql, sql_data)

            connect.commit() # コミットする

        
    insert_record()

    cursor.close()
    connect.close() # データベースオブジェクトを閉じる


if __name__ == '__main__':

    main()


