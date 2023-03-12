from selenium import webdriver

# Google Chromeのドライバーをインストールする
# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver_path = "/driver/chromedriver"

# Google Chromeを起動する
driver = webdriver.Chrome(executable_path=driver_path)

# Googleのトップページを開く
driver.get("https://www.google.com/")

# スクリーンショットを撮る
driver.save_screenshot("google.png")

# ブラウザを終了する
driver.quit()