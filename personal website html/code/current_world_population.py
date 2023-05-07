import requests

from bs4 import BeautifulSoup

import time

from selenium import webdriver



driver = webdriver.Safari()

url = 'https://www.worldometers.info/world-population/'

def send_population_data():

	
	driver.maximize_window()

	driver.get(url)




	time.sleep(1)




	content = driver.page_source.encode('utf-8').strip()

	soup = BeautifulSoup(content,"html.parser")

	# html_text = requests.get('https://www.worldometers.info/world-population/').text 

	# soup = BeautifulSoup(html_text, 'lxml')

	infos = soup.find('div', id="maincounter-wrap")

	name = infos.find('h1').text

	number_storage = infos.find('div', class_='maincounter-number')

	pop_data = number_storage.find('span', class_="rts-counter")




	decimals_1 = pop_data.find('span', class_="rts-nr-int rts-nr-10e9").text

	decimals_2 = pop_data.find('span', class_="rts-nr-int rts-nr-10e6").text

	decimals_3 = pop_data.find('span', class_="rts-nr-int rts-nr-10e3").text

	decimals_4 = pop_data.find('span', class_="rts-nr-int rts-nr-10e0").text



	current_world_population = str(decimals_1) + str(decimals_2) + str(decimals_3) + str(decimals_4)




	print(name, ":", current_world_population )



running = True

while running:
    
    send_population_data()


