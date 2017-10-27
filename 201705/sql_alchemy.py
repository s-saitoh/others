# !/usr/bin/env python
# coding: utf-8

import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String, Binary

Base = sqlalchemy.ext.declarative.declarative_base()
#表層形,左文脈ID,右文脈ID,単語コスト,品詞大分類,品詞中分類,品詞小分類,品詞細分類,
#活用型,活用形,語彙素読み,語彙素（語彙素表記+ 語彙素細分類）,書字形出現形,発音形出現形,
#書字形基本形,発音形基本形,語種,語頭変化型,語頭変化形,語末変化型,語末変化形

class mecab(Base):
	#__tablename__ = 'csvtest'
	__tablename__ = 'mecab_unidic_neologdDB'

	morph = sqlalchemy.Column(sqlalchemy.String(255))
	left_id = sqlalchemy.Column(sqlalchemy.Integer)
	right_id = sqlalchemy.Column(sqlalchemy.Integer)
	cost = sqlalchemy.Column(sqlalchemy.Integer)
	large_class = sqlalchemy.Column(sqlalchemy.String(255))
	middle_class = sqlalchemy.Column(sqlalchemy.String(255))
	small_class = sqlalchemy.Column(sqlalchemy.String(255))
	sub_class = sqlalchemy.Column(sqlalchemy.String(255))
	
	cType = sqlalchemy.Column(sqlalchemy.String(255))
	cForm = sqlalchemy.Column(sqlalchemy.String(255))
	lForm = sqlalchemy.Column(sqlalchemy.String(255))
	lemma = sqlalchemy.Column(sqlalchemy.String(255))
	orth = sqlalchemy.Column(sqlalchemy.String(255))
	pron = sqlalchemy.Column(sqlalchemy.String(255))
	
	orthBase = sqlalchemy.Column(sqlalchemy.String(255))
	pronBase = sqlalchemy.Column(sqlalchemy.String(255))
	goshu = sqlalchemy.Column(sqlalchemy.String(255))
	iType = sqlalchemy.Column(sqlalchemy.String(255))
	iForm = sqlalchemy.Column(sqlalchemy.String(255))
	fType = sqlalchemy.Column(sqlalchemy.String(255))
	fForm = sqlalchemy.Column(sqlalchemy.String(255))

	# 後でつける
	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
	

url = 'mysql+mysqlconnector://root:2fghxbzi8r@localhost/mecab?charset=utf8'
engine = sqlalchemy.create_engine(url, echo=True)

#スキーマ作成
Base.metadata.create_all(engine)

