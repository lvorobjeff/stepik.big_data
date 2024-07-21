import common

# Загрузим данные с файла
sales_data = common.read_sales_data('Задание 12.9/source.txt')

# 1. Определить, какой продукт принес наибольшую выручку
products = common.total_sales_per_product(sales_data)
product, largest = '', 0
for product_name in products:
	if products[product_name] > largest:
		product, largest = product_name, products[product_name]
print(product)

# 2. Определить, в какой день была наибольшая сумма продаж.
times = common.total_sales_over_time(sales_data)
date, largest = '', 0
for time in times:
	if times[time] > largest:
		date, largest = time, times[time]
print(date.date())

# 3. Построить график продажи.
common.plot_total_sales(sales_data)

