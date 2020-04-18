# ウェブスクレイピング(Web scraping) + Pythonで羽田空港の駐車場空き状況を調べる
 夏休み、GWなど羽田空港の混雑が予想されるときは、駐車場を予約しておいたほうが安心かなあと思う方は結構いらっしゃるのではないでしょうか。
こどもがいらっしゃる方は特に車で空港まで向かいたいですよね。


> 駐車場予約は<b>入場日予定日の<font color='red'>30日前の午前10時から</font>予約できます</b> (2020年4月現在)
> ちなみに、駐車場予約には利用料の他に<b>+1000円</b>かかります。

しかし、予約開始日時に駐車場を予約しようとした先日のこと、、うっかりタイミングを逃してしまい、自分が見たときには満車になって予約が取れない状況になってしまいました。

これはもう、ときどき予約サイトを見に行って、キャンセルがでるのを待しかありません。でも、仕事もありますし、これ全て手作業で行うわけにはいきません。そこで、ウェブスクレイピングを使ってこの作業を自動化したのでご紹介します。


## 必要なもの

- [chrome driver](https://chromedriver.chromium.org/)
    - Google chromeのversionを調べます。
    - バージョンにあったchrome driverをダウンロードします。

- Pythonモジュール  (Anacondaでインストール）  
    - Beautifulsoup4
        - `conda install -c anaconda beautifulsoup4`
    - selenium
        - ` conda install -c conda-forge selenium `    
    - lxml
        - ` conda install -c conda-forge lxml `

## 使い方
- まずは、`scriptForCheckP2P3.py`の`driver = webdriver.Chrome(chrome_options=options,executable_path='*****/chromedriver')`の部分にchromedriverをインストール先に書き換えてください。
- 1日のみ、複数日、連続日(date,days)を指定して第２と第３駐車場に空きがあれば返します。
-　スクリプトを直接変更する場合：
  - 1日のみの場合　`if __name__ == "__main__":`の下の`date="2020/04/21"`などと変更してください。
  - 複数日程を指定する場合、　`date=["2020/04/21","2020/04/23","2020/04/25"]`などと変更してください。
  - 複数の連続する日程を指定する場合以下のように変更してください。

```
if __name__ == "__main__":
    date = '2020/04/21'
    days = 3
    CheckHNDParking(date,days=days).getavailablity()

```
-　入力で日程を指定する場合以下のように変更してください。
```
if __name__ == "__main__":
    print('example: type one date "2019/08/21" or multiple dates "2019/08/21 2019/08/22"')
    date = input().split()
    CheckHNDParking(date).getavailablity()
```
- 上記いづれかの変更を行ったら実行します。
```
python3 scriptForCheckP2P3.py
```

## 出力例
```
2020年 4月 19日 01:43
一般者枠カレンダー 第1ターミナル　P2
Click  https://hnd-rsv.aeif.or.jp/airport2/app/toppage
2020/04/21 Available
Click  https://hnd-rsv.aeif.or.jp/airport2/app/toppage
2020/04/22 Available
Click  https://hnd-rsv.aeif.or.jp/airport2/app/toppage
2020/04/23 Available
一般者枠カレンダー 第2ターミナル　P3
Click  https://hnd-rsv.aeif.or.jp/airport2/app/toppage
2020/04/21 Available
Click  https://hnd-rsv.aeif.or.jp/airport2/app/toppage
2020/04/22 Available
Click  https://hnd-rsv.aeif.or.jp/airport2/app/toppage
```
