#! /Users/tomoyahokari/opt/anaconda3/bin python
# coding: utf-8
# mapIt.py - コマンドラインから住所を取得する
# コマンドライン引数を読み込むために sysモジュールをインポート

import webbrowser, sys, pyperclip
import urllib.parse
# sys.argv変数には、プログラムのファイル名とコマンドライン引数のリストが格納されている。
# そいつにファイル名以外のものがあれば len(sys.argv) > 1 となる。
if len(sys.argv) > 1:
    # コマンドラインから住所を取得する
    # sys.argvは文字列のリストなので、join()に渡すと一つの文字列を返す。
    # プログラム名を文字列に含めたくないので、最初の0番目は含めず[1:]としている。
    address = ''.join(sys.argv[1:])
else:
    # クリップボードから住所を取得する
    address = pyperclip.paste()
address_quote = urllib.parse.quote(address)
webbrowser.open('https://www.google.com/maps/place/' + address_quote)
