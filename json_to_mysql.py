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
                            port=3306,
                            user='root',
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

            race_id_json = str(jsonData["id"])
            answer_column_json = jsonData["answer_column"]
            article_json = jsonData["article"]
            problem_json = jsonData["problem"]
            problem_type_json = jsonData["problem_type"]
            
            problem_type_json1 = problem_type_json[0]
            if len(problem_type_json) > 1:
                problem_type_json = str(problem_type_json)

            options = jsonData["options"]
            opt1 = options.get("A") 
            opt2 = options.get("B")
            opt3 = options.get("C")
            opt4 = options.get("D")
            opt5 = options.get("E")
            opt6 = options.get("F")

            if len(opt1) > 1:
                opt1 = str(opt1)
                opt2 = str(opt2)
                opt3 = str(opt3)
                opt4 = str(opt4)
                opt5 = str(opt5)
                opt6 = str(opt6)

            # ans_json = jsonData[""]別ファイル

            # SQL挿入


            if opt3 and opt4 == False:
                sql_data = (race_id_json, answer_column_json, article_json, problem_json, problem_type_json1, opt1, opt2, opt3)
                sql = "INSERT INTO race.race_converted(race_id, answer_column, article, problem, problem_type, option_1, option_2, option_3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, sql_data)
 
            elif opt4 and opt5 == False:
                sql_data = (race_id_json, answer_column_json, article_json, problem_json, problem_type_json1, opt1, opt2, opt3, opt4)
                sql = "INSERT INTO race.race_converted(race_id, answer_column, article, problem, problem_type, option_1, option_2, option_3, option_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, sql_data)                

            elif opt5 and opt6 == False:
                sql_data = (race_id_json, answer_column_json, article_json, problem_json, problem_type_json1, opt1, opt2, opt3, opt4, opt5)
                sql = "INSERT INTO race.race_converted(race_id, answer_column, article, problem, problem_type, option_1, option_2, option_3, option_4, option_5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, sql_data)                

            else:
                sql_data = (race_id_json, answer_column_json, article_json, problem_json, problem_type_json1, opt1, opt2, opt3, opt4, opt5, opt6)
                sql = "INSERT INTO race.race_converted(race_id, answer_column, article, problem, problem_type, option_1, option_2, option_3, option_4, option_5, option_6) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, sql_data)

            connect.commit() # コミットする

        
    insert_record()

    cursor.close()
    connect.close() # データベースオブジェクトを閉じる


if __name__ == '__main__':

    main()


