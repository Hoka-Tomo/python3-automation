#! /Users/tomoyahokari/opt/anaconda3/bin python
# coding: utf-8
# downloadXkcd.py - XKCDコミックを一つずつダウンロードする

import requests, os, bs4, time

url = 'https://xkcd.com/' #開始URL
os.makedirs('xkcd', exist_ok=True) # osライブラリのmkdirしてxkcdディレクトリを作成。(os.mkdir()は成約が多いため、os.makedirs()を使う！)# ./xkcdに保存する
# exist_ok=Trueとすると既に末端ディレクトリが存在している場合もエラーが発生しない。末端ディレクトリが存在していなければ新規作成するし、存在していれば何もしない。前もって末端ディレクトリの存在確認をする必要がないので便利。

while not url.endswith('#'):
    # ページをダウンロードする
    print('ページをダウンロード中 {}...'.format(url)) # 今の状態を出力
    res = requests.get(url) # requests.get()関数で、ページをダウンロード
    res.raise_for_status()  # ダウンロードが失敗したら、例外を起こしてプログラムを終了させる。

    soup = bs4.BeautifulSoup(res.text, 'lxml') # ダウンロードが成功したら、ダウンロードしたページのテキストから、BeatifulSoupオブジェクトを生成
    # To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor. が出たので、'lxml'を追加

    # コミック画像のURLを見つける
    comic_elem = soup.select('#comic img') # コミック画像の<img>は、<div id="comic">の中にあるので、#comic imgとする。
    # 単純な画像ファイルでない特別なものは、スキップさせる。
    if comic_elem == []:
        print('コミック画像が見つかりませんでした。')
    # そうでなければ、<img>が入ったリストを返す。
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        # 画像をダウンロードする
        print('画像をダウンロード中 {}...'.format(comic_url))
        res = requests.get(comic_url)  # requests.get()関数で、ページをダウンロード
        res.raise_for_status()
        # この時点では、画像はresに格納されている。

        # 画像を ./xkcdに保存
        # ローカルのファイル名を指定し、open()にわたす必要がある。
        # comic_urlには、'https://imgs.xkcd.com/comics/barrel_cropped_(1).jpg'のような値が入っているが、これはファイルパスのようになっているので、
        # 最後部分barrel_cropped_(1).jpgをローカルに保存する際のファイル名として扱ってあげることとする。
        # open()のバイナリ書き込みモード 'wb' を指定する。
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        # Requestsオブジェクトを用いてダウンロードしたファイルを保存する場合には、iter_content()メソッドの値を用いてループさせる。
        for chunk in res.iter_content(100000): # 最大100000バイトごとにファイルに書き込んでからファイルを閉じる。
            image_file.write(chunk)
        image_file.close()
        #time.sleep(30) # 連続してページをダウンロードするとサーバ不可やアクセスBANになることがあるので、アクセス感覚を開けるために import timeして、time.sleep(秒数）を指定するといい。

    # PrevボタンのURLを取得する
    prev_link = soup.select('a[rel="prev"]')[0] # 'a[rel="prev"]'セレクタを指定して、ref属性がprevである<a>要素を取り出す
    # prev_linkの href属性から前のURLを取得し、urlに保存
    url = 'https://xkcd.com' + prev_link.get('href')

print('完了！')