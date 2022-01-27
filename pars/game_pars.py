"""ИМПОРТЫ ФАЙЛОВ"""
import requests
from bs4 import BeautifulSoup
import json
"""ИМПОРТЫ ФАЙЛОВ"""



"""САМ ПАРСЕР"""
def get_ferst_news():

	#выбор сайта(агент)
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
	}

	#страница новостей
	url = "https://www.igromania.ru/news/game/"
	r = requests.get(url=url, headers=headers)

	soup = BeautifulSoup(r.text, "lxml")
	aubl_item = soup.find_all('div', class_='aubl_item')

	#создание первого словаря
	news_dist = {}
	for aubl in aubl_item:

		#поиск имени новости
		aubl_title = aubl.find('a', class_='aubli_name').text.strip()
		#поиск ссылки на новость
		aubl_url = f'https://www.igromania.ru{aubl.find("a", "href", class_="aubli_name")}'
		#поиск даты на новость
		aubl_datess = f"{aubl.find('div', class_='aubli_date')}"

		#форматирование даты
		dates_id_1 = aubl_datess.split(">")[1]
		dates_id_print = dates_id_1.split("<")[0]
		dates_over = f'дата выхода: {dates_id_print}'

		#форматирование ссылки
		aubl_id = aubl_url.split("/")[-3]
		aubl_url_split = aubl_url.split('"')[-2]
		aubl_url_split_print = f'https://www.igromania.ru{aubl_url_split}'

		
		#вывод итога
		print(f'{aubl_title} | https://www.igromania.ru{aubl_url_split} | {aubl_id} | {dates_over}\n')

		#создание библеотеки(json)
		news_dist[aubl_id] = {
			"aubl_title": aubl_title,
			"aubl_url_split_print": aubl_url_split_print,
			"dates_id_print": dates_over,
			"aubl_id": aubl_id
		}

	#запись в json
	with open("pars/game_dist.json", "w") as file:
		json.dump(news_dist, file, indent=4, ensure_ascii=False)

#поиск свежих новостей
def check_news_update():
	#открытие уже созданого файла
	with open('pars/game_dist.json') as file:
		news_dist = json.load(file)

	#выбор сайта(агент)
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
	}

	#страница новостей
	url = "https://www.igromania.ru/news/game/"
	r = requests.get(url=url, headers=headers)

	soup = BeautifulSoup(r.text, "lxml")
	aubl_item = soup.find_all('div', class_='aubl_item')

	#создание словаря с новыми новостями
	news_new = {}
	for aubl in aubl_item:
		aubl_url = f'{aubl.find("a", "href", class_="aubli_name")}'
		aubl_datess = f"{aubl.find('div', class_='aubli_date')}"

		dates_id_1 = aubl_datess.split(">")[1]
		dates_id_print = dates_id_1.split("<")[0]
		dates_over = f'дата выхода: {dates_id_print}'

		aubl_id = aubl_url.split("/")[-3]
		aubl_url_split = aubl_url.split('"')[-2]
		aubl_url_split_print = f'https://www.igromania.ru{aubl_url_split}'

		if aubl_id in news_dist:
			continue
		else:
			aubl_title = aubl.find('a', class_='aubli_name').text.strip()

			news_dist[aubl_id] = {
				"aubl_title": aubl_title,
				"aubl_url_split_print": aubl_url_split_print,
				"dates_id_print": dates_over,
				"aubl_id": aubl_id
			}

			news_new[aubl_id] = {
				"aubl_title": aubl_title,
				"aubl_url_split_print": aubl_url_split_print,
				"dates_id_print": dates_over,
				"aubl_id": aubl_id
			}


	with open("pars/game_dist.json", "w") as file:
		json.dump(news_dist, file, indent=4, ensure_ascii=False)

	return news_new


"""ЕГО ЗАДАНИЕ"""
def main():
	#get_ferst_news()
	#print(chek_news_update())
	check_news_update()
"""ЕГО ЗАДАНИЕ"""



"""ПАРСЕРА_1"""
if __name__ == "__main__":
	main()