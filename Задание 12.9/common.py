import matplotlib.pyplot as plt
from dateutil.parser import parse


# Функция для чтения данных с файла
def read_sales_data(file_path):
	# Создаем словарь
	sales_data = list()

	# Открываем файл (только чтение)
	with (open(file_path, "r") as file):
		# Читаем построчно
		for readline in file.readlines():
			# Разбиваем по ","
			data = readline.replace('\n', '').split(', ')

			# Заполняем словарь о продаже
			sale = dict()
			sale['product_name'] = data[0]
			sale['quantity'] = int(data[1])
			sale['price'] = float(data[2])
			sale['date'] = parse(data[3])

			# Добавляем словарь в список продаж
			sales_data.append(sale)

	return sales_data


# Функция, которая принимает список продаж и возвращает словарь,
# где ключ - название продукта, а значение - общая сумма продаж этого продукта
def total_sales_per_product(sales_data):
	# Создаем список
	products = dict()

	# Заполняем сумму по каждому продукту
	for sale in sales_data:

		# Значение продукта
		product_name = sale['product_name']

		# Есть такой продукт в словаре? Добавляем с 0
		if product_name not in products:
			products[product_name] = 0

		# Суммируем
		products[product_name] += sale['quantity'] * sale['price']

	# Возвращаем
	return products


# Функция, которая принимает список продаж и возвращает словарь,
# где ключ - дата, а значение общая сумма продаж за эту дату.
def total_sales_over_time(sales_data):
	# Создаем список
	times = dict()

	# Заполняем сумму по каждому продукту
	for sale in sales_data:

		# Значение даты
		date = sale['date']

		# Есть такая дата в словаре? Добавляем с 0
		if date not in times:
			times[date] = 0

		# Суммируем
		times[date] += sale['quantity'] * sale['price']

	# Возвращаем
	return times


# Функция для построения графика общей суммы продаж по каждому продукту / дате
def plot_total_sales(sales_data):
	fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

	# 1. Подготовить шкалу для графика по каждому продукту
	sales_per_product = total_sales_per_product(sales_data)
	lines_x, lines_y = [], []

	for product in sales_per_product:
		lines_x.append(product)
		lines_y.append(sales_per_product[product])

	ax1.bar(lines_x, lines_y, color='orange')
	ax1.set_title('Общая сумма продаж по продукту')
	ax1.set_ylabel('Общая сумма')

	# 2. Подготовить шкалу для графика по каждой дате
	sales_over_time = total_sales_over_time(sales_data)
	lines_x, lines_y = [], []

	for date in sales_over_time:
		lines_x.append(date.date())
		lines_y.append(sales_over_time[date])

	ax2.bar(lines_x, lines_y, color='red')
	ax2.set_title('Общая сумма продаж по дате')
	ax1.set_ylabel('Общая сумма')

	plt.xticks(rotation=90)
	plt.show()
