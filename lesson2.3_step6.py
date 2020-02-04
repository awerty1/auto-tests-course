from selenium import webdriver
import time
import math

try:
	# Открываем сайт
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser.get(link)
	
	# Нажимаем на кнопку
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
	# Переключаемся на новую вкладку
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
	# Решаем уравнение
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	
	# Берём элемент x и подставляем его в формулу calc
	x_element = browser.find_element_by_id("input_value")
	xel1 = x_element.text
	y = calc(xel1)
	#print("y: ", y)
	
	# Заполняем поле с ответом на captcha
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
	
	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn") 
	button.click()

finally:
	# Ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(15)
	# Закрываем браузер после всех манипуляций
	browser.quit()
	
