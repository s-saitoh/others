# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Article(scrapy.Item):
	"""
	記事から抜き出したタイトルと本文を格納するItem
	"""
	title = scrapy.Field() # 記事タイトルを格納するフィールドtitleを定義
	body = scrapy.Field() # 記事の本文を格納するフィールドbodyを定義
	