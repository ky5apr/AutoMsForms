#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#LINE連携
#from lineNotify import sendNotify

from wordList import randomWord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#sendNotify("Test")

words = randomWord()

driver = webdriver.Chrome("chromedriverのパス")
driver.get("アンケートフォームのURL")

time.sleep(1)
input_id = driver.find_element_by_id("i0116")
input_id.send_keys("メールアドレス")
time.sleep(1)
input_id_button = driver.find_element_by_id("idSIButton9")
input_id_button.click()
#sendNotify("OK: ID")

input_pass = driver.find_element_by_id("i0118")
input_pass.send_keys("パスワード")
time.sleep(1)
input_pass_button = driver.find_element_by_id("idSIButton9")
input_pass_button.click()
#sendNotify("OK: Pass")

time.sleep(1)
input_no_button = driver.find_element_by_id("idBtn_Back")
input_no_button.click()
#sendNotify("OK: Login")

time.sleep(1)
driver.get("ログイン後の遷移先URL")

time.sleep(1)
selectButton = driver.find_element_by_xpath("//*[@id='form-container']/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[4]/div/label/input")
selectButton.click()

input_textField = driver.find_element_by_xpath("//*[@id='form-container']/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div/textarea")
input_textField.send_keys("・" + words[0])
#sendNotify("Send:" + words[0])

input_textField2 = driver.find_element_by_xpath("//*[@id='form-container']/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[3]/div/div/div/textarea")
input_textField2.send_keys("・" + words[1])
#sendNotify("Send:" + words[1])

selectSubmit = driver.find_element_by_xpath("//*[@id='form-container']/div/div/div[1]/div/div[1]/div[2]/div[3]/div/button/div")
selectSubmit.click()
#sendNotify("AllOK")