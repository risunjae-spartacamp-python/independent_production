# モジュールのimport
import os
import shutil
import sys
import time
import urllib.request
from selenium.webdriver.common.by import By
from selenium import webdriver


def main():
    # 引数チェック
    target = ""
    per_page = 0
    try:
        target = sys.argv[1]
        per_page = int(sys.argv[2])
    except IndexError:
        print("BTS", "2")
        exit()
    except ValueError:
        print("BTS", "2")
        exit()

    # プリ画像のURL
    BASE_URL = "https://prcm.jp"

    # 保存先のディレクトリ
    save_dir = "images/" + target
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    else:
        # すでにディレクトリがあったら全削除して再作成
        shutil.rmtree(save_dir)
        os.mkdir(save_dir)

    # ブラウザ操作のインスタンス作成(Firefox)
    driver = webdriver.Chrome()
    # リクエスト間隔
    wait_time = 1
    try:
        # プリ画像のTOPページを表示し、検索ボックスに指定したキーワードを入力・検索
        driver.get(BASE_URL)
        driver.find_element(By.CSS_SELECTOR, ".search__input").send_keys(target)
        driver.find_element(By.CSS_SELECTOR, ".search__btn").click()
        time.sleep(wait_time)
        # 画像一覧の要素を取得し、画像をダウンロード
        for i in range(per_page):
            image_list = driver.find_element(By.ID, "imglist_container").find_elements(
                By.CLASS_NAME, "list-pic__item"
            )
            for image in image_list:
                image_url = image.find_element(
                    By.CSS_SELECTOR, "a > div > img"
                ).get_attribute("src")
                file_path = save_dir + "/" + image_url.split("/")[-1]
                data = urllib.request.urlopen(image_url).read()
                with open(file_path, "wb") as f:
                    f.write(data)
            # 次のページへアクセス
            page_navigation = driver.find_element(By.CLASS_NAME, "page-navigation")
            next_link = page_navigation.find_element(
                By.CLASS_NAME, "page-navigation__next"
            )
            link_url = next_link.find_element(By.CSS_SELECTOR, "a").get_attribute(
                "href"
            )
            driver.get(link_url)
            time.sleep(wait_time)
    except Exception as e:
        print("エラー : ", e)
        driver.quit()
        exit()

    # ブラウザを閉じる
    driver.quit()


if __name__ == "__main__":
    main()
