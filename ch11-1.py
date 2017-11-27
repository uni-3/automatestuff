# config utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time
# 仮想ディスプレイを開始。
display = Display(visible=0, size=(1280, 960))
display.start()

import logging

logging.basicConfig(level=logging.INFO,
    format=' %(asctime)s - %(levelname)s - %(message)s')


def send_gmail(from_mail, password, to_mail, text):
    url = 'https://mail.google.com/mail'
    browser = webdriver.Firefox()
    browser.get(url)

    logging.info('connecting...')

    # input email
    email_elem = browser.find_element_by_id('identifierId')
    email_elem.send_keys(from_mail)
    next_elem = browser.find_element_by_id('identifierNext') # next button click
    next_elem.click()
    # wait for open another screen
    time.sleep(5)

    # input password
    pass_elem = browser.find_element_by_name('password')
    pass_elem.send_keys(password)
    next_elem = browser.find_element_by_id('passwordNext') # next button click
    next_elem.click()

    # wait for open another screen
    time.sleep(5)

    logging.info('login success...')

    # メール作成ボタン
    #create_elem = browser.find_element_by_css_selector('.T-I.J-J5-Ji.T-I-KE.L3')
    #create_elem.click()
    divs = browser.find_elements_by_xpath("//div[@role='button']")
    for d in divs:
        if d.text == '作成':
            d.click()
            break
    # wait for open another screen
    time.sleep(5)

    logging.info('create mail...')

    # to フォームに入力
    to_elem = browser.find_element_by_id(':n9')
    to_elem.send_keys(to_mail)

    # 件名
    to_elem = browser.find_element_by_id(':ms')
    to_elem.send_keys('test')

    # 本文
    to_elem = browser.find_element_by_id(':nt')
    to_elem.send_keys(text)

    # 送信
    next_elem = browser.find_element_by_id(':mi')
    next_elem.click()

    logging.info("送信しました")


def main():
    print('送信元を教えてください')
    from_mail = input()
    print('パスワードを入力してください')
    password = input()
    print('送信先を教えてください')
    to_mail = input()
    print('本文を入力してください')
    text = input()

    send_gmail(from_mail, password, to_mail, text)



if __name__ == '__main__':
    main()
