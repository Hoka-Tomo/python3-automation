from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#
# Seleniumをあらゆる環境で起動させるオプション
#
options = Options()
options.add_argument('--disable-gpu'); # headlessモードで暫定的に必要なフラグ
options.add_argument('--disable-extensions'); # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
options.add_argument('--proxy-server="direct://"'); # Proxy経由ではなく直接接続する
options.add_argument('--proxy-bypass-list=*'); # すべてのホスト名
options.add_argument('--start-maximized'); # 起動時にウィンドウを最大化する
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

#
# Chromeドライバーの起動
#
# Chrome DriverのPath
DRIVER_PATH = '/Users/tomoyahokari/PycharmProjects/Selenium/chromedriver'
# Chrome Driverを起動する
browser = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

browser.get('https://news.yahoo.co.jp/categories/it')

try:
    elem = browser.find_element_by_class_name('topics')
    print('そのクラス名を持つ要素 <{}>を見つけた！'.format(elem.tag_name))
except:
    print('そのクラス名を持つ要素は見つからなかった。')
