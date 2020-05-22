# coding: UTF-8
import requests
import termcolor
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class CheckHNDParking:

    def __init__(self, date, days=1, multidate = False):
        self.date = date
        self.days = days
        self.multidate = multidate

        # 入力日付が１要素のリストで与えられた場合
        if len(date) == 1:
            date = str(date[0])
        # 入力日付がstrでなけば複数日程と仮定する。
        if not isinstance(self.date,str):
            self.multidate = True
        # 日付とそれに続く日数で指定された場合。
        if days > 1 :
            self.multidate = True
            self.date  = [self.date.split('/')[0]+'/'+self.date.split('/')[1]+'/'+str(int(self.date.split('/')[-1])+i) for i in range(self.days)]
            print('Checking availability for the date', self.date)


    def getavailablity(self):

        available_sentence = termcolor.colored('Available', 'red')
        target_url = 'https://hnd-rsv.aeif.or.jp/airport2/app/toppage'

        def printavailable(singledate,row):
            if singledate in str(row):
                if row['class'][0] == 'full':
                    return 'Full'
                else:
                    print('Click ',target_url)
                    return available_sentence
        get_url_info = requests.get(target_url)
        bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'lxml')
        print('... accessing to ', bs4Obj.title.string)

        # ブラウザのオプションを格納する変数をもらってきます。
        options = Options()

        # ブラウザを立ち上げないようにHeadlessモードを有効にする
        options.set_headless(True)

        # ブラウザを起動する
        # chromedrivrをインストールした場所を指定する。
        driver = webdriver.Chrome(chrome_options=options,executable_path='*****/chromedriver')

        # ブラウザでtarget_urlにアクセスする
        driver.get(target_url)

        # HTMLを文字コードをUTF-8に変換してから取得します。
        html = driver.page_source.encode('utf-8')

        # BeautifulSoupで扱えるようにパースします
        soup = BeautifulSoup(html, "html.parser")

        # ブラウザーの開発ツールで必要な場所のタグを探して検索
        print(soup.select_one("#current_status").find_all("div")[0].string)

        cal_title = soup.select_one('#area_box').find_all('p',class_="cal_title")
        table_list = soup.findAll('table')

        # sanitary check
        for tableid in range(len(table_list)):
            #print('Table#',tableid,end=',')
            if (table_list[tableid].has_attr('id')) and ('cal' not in table_list[tableid]['id']):
                print('This may not a calendar but',table_list[tableid]['id'])
            #else:
            #    print('sanitary check: PASS')
        #print('\n')

        for tableid in range(2): #range(len(cal_title)): #一般駐車場に限定
            print(cal_title[tableid].findAll('img')[0]['alt'])
            rows = table_list[tableid].findAll('td')
            for row in rows:
                if self.multidate == True:
                    for singledate in self.date:
                        if singledate in str(row):
                            print(singledate,printavailable(singledate,row))
                elif self.date in str(row):
                    print(date,printavailable(date,row), end='\n-----\n')


if __name__ == "__main__":
    date = '2020/04/21'
#    date = ['2019/08/21','2019/08/22','2019/08/23','2019/08/24','2019/08/25']
#    date = '2019/08/21'
#    days = 3
#    print('example: type one date "2019/08/21" or multiple dates "2019/08/21 2019/08/22"')
#    date = input().split()
    CheckHNDParking(date).getavailablity()
