# ウェブスクレイピング(Webs craping) + Pythonで羽田空港の駐車場空き状況を調べる
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

- Pythonモジュール    
    - Beautifulsoup4
        - `conda install -c anaconda beautifulsoup4`
    - selenium
        - ` conda install -c conda-forge selenium `    
    - lxml
        - ` conda install -c conda-forge lxml `
        
## 使い方
- 1日のみ、複数日、連続日(date,days)を指定して第２と第３駐車場に空きがあれば返します。
