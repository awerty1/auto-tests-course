from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)

	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "100")
		)
	browser.find_element_by_id("book").click()

	# решаем уравнение
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	
	# Берём элемент x и подставляем его в формулу calc
	x_element = browser.find_element_by_id("input_value").text
	y = calc(x_element)
	#print("y: ", y)
	
	# Заполняем поле с ответом на captcha
	browser.find_element_by_id("answer").send_keys(y)
	
	# Отправляем заполненную форму
	browser.find_element_by_id("solve").click()
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(5)
	# закрываем браузер после всех манипуляций
	browser.quit()
