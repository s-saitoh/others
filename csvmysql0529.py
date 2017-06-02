# !/usr/bin/env python
# coding: utf-8
# 完成版
# bulk insertでMySQLにCSVファイルを流し込む（1000行ずつ）
# cf. http://blog.nikuniku.me/entry/%3Fp%3D306_1

import csv
import sys
import MySQLdb

def main():
	conn = MySQLdb.connect(
		db="mecab",
		port=3306,
		user="root",
		host='localhost',
		passwd="2fghxbzi8r",
		charset="utf8"
	)
	
	cursor=conn.cursor()


	with open("mecab-unidic-user-dict-seed.20170515.csv", "r", encoding="utf-8") as f:
	#with open("csvtest0602.csv", "rU", encoding="utf-8") as f:	
		reader = csv.reader(f)
		valuelist = []
		#conn.set_character_set('utf8')
		#header = next(reader)
		for row in reader:
			valuelist.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
			row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]))
			
			if len(valuelist) >= 1000:
				cursor.executemany(
					"INSERT IGNORE INTO mecab_unidic_neologdDB(morph, left_id, right_id, cost,\
				 large_class, middle_class, small_class, sub_class, cType,\
				cForm, lForm, lemma, orth, pron, orthBase, pronBase, goshu, iType, iForm, fType, fForm, id) \
					VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)",valuelist
				)
				valuelist = []

		if valuelist:
			cursor.executemany(
				"INSERT IGNORE INTO mecab_unidic_neologdDB(morph, left_id, right_id, cost,\
				 large_class, middle_class, small_class, sub_class, cType,\
				cForm, lForm, lemma, orth, pron, orthBase, pronBase, goshu, iType, iForm, fType, fForm, id) \
				VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)",valuelist)
		
			
		#conn.set_character_set('utf8')		
		conn.commit()

		cursor.close()
		conn.close()

if __name__ == '__main__':

	main()

#3179030行　元データ
