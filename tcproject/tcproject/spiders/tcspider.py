# -*- coding: utf-8 -*-
import scrapy


from tcproject.items import Article # ItemsからArticleクラスをインポートする


class TcspiderSpider(scrapy.Spider):
    name = 'tcspider' # spiderの名前、実行時に指定
    allowed_domains = ['jp.techcrunch.com'] # クロールを許可するドメインを指定
    start_urls = ['http://jp.techcrunch.com/'] # クロールを開始するページのURLを指定

    def parse(self, response):
        """
        トップページから個別記事ページへのリンク文字列を抜き出して1つずつ順番に処理する
        """
        for url in response.css('h2.post-title a::attr("href")').extract(): # トップページから個別記事へのリンク文字列を抜き出し、1つずつ順にparse_articlesに渡す
            yield scrapy.Request(url, self.parse_articles) # urlをscrapy.Requestにわたし、レスポンスをparse_articlesで処理

    def parse_articles(self, response):
    	"""
    	記事詳細ページからタイトルと本文を抜き出してitemsに格納する
    	"""
    	item = Article() # items.pyで定義したArticleクラスのオブジェクトを作成
    	item['title'] = response.css('h1::text').extract_first()
    	item['body'] = response.css('.article-entry.text').xpath('string()').extract_first()
    	yield item
