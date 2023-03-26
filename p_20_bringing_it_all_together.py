#ウェブスクレイパー
#ウェブサイトのページを取得してほしい情報を収集・分析・抽出するプログラム

#パース（構文解析）
#データフォーマットを読み取って、プログラミング言語を使って構造化すること

import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin #urlを扱うモジュールを追加

class Scraper:
    def __init__(self, site):
        self.site = site
        self.urls = set() #収集済みURLを入れておく変数

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        #urlopen関数 ウェブサイトへのリクエスト
        #responseオブジェクトが返され、HTMLと追加情報が格納される
        html = r.read()
        #HTMLデータがResponseオブジェクトから返される
        parser = "html.parser" #HTMLをパースしてほしいことを伝える
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            #<a></a>タグをすべて集めて返す tagオブジェクト
            url = tag.get("href")
            if url is None:
                continue
            if "atcl/contents" not in url: #atcl/contentsを含まないURLは対象外
                continue
            full_url = urljoin(r.url, url) #ドメイン名を含むURLに変換
            if full_url in self.urls: #既に収集済みのURLは対象外にする
                continue
            self.urls.add(full_url) #収集済みURLに追加
            print("\n" + full_url) #URLを表示
                
news = "https://xtrend.nikkei.com/atcl/contents/new/"

Scraper(news).scrape()
