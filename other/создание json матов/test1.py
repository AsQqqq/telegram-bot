#импорт json
import json
#создание файла с матами
ar = []
with open('text_mat.txt', encoding='utf-8') as r:
	for i in r:
		n = i.lower().split('\n')[0]
		if n != ' ':
			ar.append(n)

with open('mat.json', 'w', encoding='utf-8') as e:
	json.dump(ar, e)