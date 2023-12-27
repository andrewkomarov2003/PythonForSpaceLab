# Завдання 2_1 "Скрапер"

import random
import time
from bs4 import BeautifulSoup
from requests import get

laptops = []
laptops_on_page_data = []
result_info = []

page_number = 1
max_page_number = 20

print("\nЗачекайте, триває збір інформації з сайту...")

for i in range(1, max_page_number + 1):
    url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=' + str(i)
    print('URL: ', url)

    data = get(url)
    html_data = BeautifulSoup(data.text, 'html.parser')

    laptops_on_page_data = html_data.find_all('div', class_="col-md-4 col-xl-4 col-lg-4")

    if laptops_on_page_data:
        for lap in range(0, len(laptops_on_page_data)):
            laptops.append(laptops_on_page_data[lap])
        latency = 1 + random.random() * 2
        print('Затримка ', round(latency, 3), 'сек.')
        print('Знайдено ', len(laptops_on_page_data), ' ноутбуків на поточній сторінці.')
        print('\n')
        time.sleep(latency)
    else:
        print('Сторінка номер ', i, ' не знайдена!')
        break

    page_number += 1

print('\n')
if laptops:
    print("Знайдені на сайті ноутбуки (", len(laptops), " ШТУК):")
    for i in range(0, len(laptops)):
        result_info.append(laptops[i].find('p', {"class": "description card-text"}).text + ', ' + laptops[i].find(
            "h4", {"class": "float-end price card-title pull-right"}).text)

        print('Ноутбук №', i + 1, ': ', result_info[i])
else:
    print("Жодного ноутбуку не було знайдено.")




