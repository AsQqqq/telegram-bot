"""ИМПОРТЫ ФАЙЛОВ"""
import requests
from bs4 import BeautifulSoup
import json
"""ИМПОРТЫ ФАЙЛОВ"""



"""ДЛЯ УСЛОВИЙ"""

jy = 'января'
fy = 'февраля'
mh = "марта"
al = "апреля"
my = "мая"
je = "июня"
jy_2 = "июля"
at = "августа"
sr = "сентября"
or_1 = "октября"
nr = "ноября"
dr = "декабря"

b = None

"""ДЛЯ УСЛОВИЙ"""




"""САМ ПАРСЕР"""
def get_ferst_news():

	#выбор сайта(агент)
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
	}

	#страница новостей
	url = "https://gamebomb.ru/news"
	r = requests.get(url=url, headers=headers)

	soup = BeautifulSoup(r.text, "lxml")
	gamebomb_item = soup.find_all('tr', class_='gbnews-listShort')

	#создание первого словаря
	news_dist = {}
	for gamebomb in gamebomb_item:

		#поиск имени новости
		gamebomb_title = gamebomb.find('h3').text.strip()
		#поиск ссылки на новость
		gamebomb_url = f'{gamebomb.find("a", "href", class_="img")}'
		#поиск даты на новость
		gamebomb_dates = f"{gamebomb.find('div', class_='sub')}"

		#форматирование даты
		dates_1 = gamebomb_dates.split(">")[1]
		dates_2 = dates_1.split("<")[0]
		dates_3 = dates_2[:-8]

		#форматирование ссылки
		input_url = gamebomb_url.split('"')[3]

		#получение айди
		input_id = input_url.split('/')[-1]

		chislo = dates_3.split(' ')[0]
		god = dates_3.split(' ')[2]

		gods = god[2:]

		a = dates_3.split(' ')[1]

		if a == jy:
			b = a.replace(a, '01')
		elif a == fy:
			b = a.replace(a, '02')
		elif a == mh:
			b = a.replace(a, '03')
		elif a == al:
			b = a.replace(a, '04')
		elif a == my:
			b = a.replace(a, '05')
		elif a == je:
			b = a.replace(a, '06')
		elif a == jy_2:
			b = a.replace(a, '07')
		elif a == at:
			b = a.replace(a, '08')
		elif a == sr:
			b = a.replace(a, '09')
		elif a == or_1:
			b = a.replace(a, '10')
		elif a == nr:
			b = a.replace(a, '11')
		elif a == dr:
			b = a.replace(a, '12')
		else:
			print('???')

		input_dates = f'дата выхода: {chislo}.{b}.{gods}'

		#вывод итога
		print(f'{gamebomb_title} | {input_url} | {input_id} | {input_dates}\n')		
		#print(f'{aubl_title} | https://www.igromania.ru{aubl_url_split} | {aubl_id} | {dates_over}\n')


		#создание библеотеки(json)
		news_dist[input_id] = {
			"gamebomb_title": gamebomb_title,
			"input_url": input_url,
			"input_dates": input_dates,
			"input_id": input_id
		}

	#запись в json
	with open("news_dist_gamebomb.json", "w") as file:
		json.dump(news_dist, file, indent=4, ensure_ascii=False)

#поиск свежих новостей
def check_news_update_2():
	#открытие уже созданого файла
	with open('news_dist_gamebomb.json') as file:
		news_dist = json.load(file)

	#выбор сайта(агент)
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
	}

	#страница новостей
	url = "https://gamebomb.ru/news"
	r = requests.get(url=url, headers=headers)

	soup = BeautifulSoup(r.text, "lxml")
	gamebomb_item = soup.find_all('tr', class_='gbnews-listShort')

	#создание словаря с новыми новостями
	news_new_1 = {}
	for gamebomb in gamebomb_item:
		#поиск ссылки на новость
		gamebomb_url = f'{gamebomb.find("a", "href", class_="img")}'
		#поиск даты на новость
		gamebomb_dates = f"{gamebomb.find('div', class_='sub')}"


		#форматирование ссылки
		input_url = gamebomb_url.split('"')[3]

		#форматирование даты
		dates_1 = gamebomb_dates.split(">")[1]
		dates_2 = dates_1.split("<")[0]
		dates_3 = dates_2[:-8]

		chislo = dates_3.split(' ')[0]
		god = dates_3.split(' ')[2]

		gods = god[2:]

		a = dates_3.split(' ')[1]

		if a == jy:
			b = a.replace(a, '01')
		elif a == fy:
			b = a.replace(a, '02')
		elif a == mh:
			b = a.replace(a, '03')
		elif a == al:
			b = a.replace(a, '04')
		elif a == my:
			b = a.replace(a, '05')
		elif a == je:
			b = a.replace(a, '06')
		elif a == jy_2:
			b = a.replace(a, '07')
		elif a == at:
			b = a.replace(a, '08')
		elif a == sr:
			b = a.replace(a, '09')
		elif a == or_1:
			b = a.replace(a, '10')
		elif a == nr:
			b = a.replace(a, '11')
		elif a == dr:
			b = a.replace(a, '12')
		else:
			print('???')

		input_dates = f'дата выхода: {chislo}.{b}.{gods}'


		#получение айди
		input_id = input_url.split('/')[-1]


		if input_id in news_dist:
			continue
		else:
			#поиск имени новости
			gamebomb_title = gamebomb.find('h3').text.strip()

			news_dist[input_id] = {
				"gamebomb_title": gamebomb_title,
				"input_url": input_url,
				"input_dates": input_dates,
				"input_id": input_id
			}

			news_new_1[input_id] = {
				"gamebomb_title": gamebomb_title,
				"input_url": input_url,
				"input_dates": input_dates,
				"input_id": input_id
			}


	with open("news_dist_gamebomb.json", "w") as file:
		json.dump(news_dist, file, indent=4, ensure_ascii=False)

	return news_new_1


"""ЕГО ЗАДАНИЕ"""
def main():
	#get_ferst_news()
	print(check_news_update_2())
	#check_news_update_2()
"""ЕГО ЗАДАНИЕ"""



"""ПАРСЕРА_1"""
if __name__ == "__main__":
	main()