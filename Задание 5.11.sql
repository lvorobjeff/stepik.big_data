-- Начало скрипта по заданию № 5.11

-- Создаем таблицу "Фамилия"
CREATE TABLE last_names (
    id INT PRIMARY KEY,
    name VARCHAR
);

-- Создаем таблицу "Имя"
CREATE TABLE first_names (
    id INT PRIMARY KEY,
    name VARCHAR
);

-- Создаем таблицу "Отчество"
CREATE TABLE middle_names (
    id INT PRIMARY KEY,
    name VARCHAR
);


-- Создаем таблицу для связи между ФИО
CREATE TABLE relation_fio (
	last_id INT,
    first_id INT,
	middle_id INT,
	FOREIGN KEY (last_id) REFERENCES last_names(id),
    FOREIGN KEY (first_id) REFERENCES first_names(id),
	FOREIGN KEY (middle_id) REFERENCES middle_names(id)
);

-- Заполняем данные
INSERT INTO last_names VALUES 
	(1, 'Иванов'),
	(2, 'Петров'),
	(3, 'Сидоров');

INSERT INTO first_names VALUES 
	(1, 'Иван'),
	(2, 'Петр'),
	(3, 'Сидор');

INSERT INTO middle_names VALUES 
	(1, 'Иванович'),
	(2, 'Петрович'),
	(3, 'Сидорович');

INSERT INTO relation_fio VALUES 
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 3);

-- Выводить все ФИО в обратном алфавитном порядке
SELECT
	 last_names."name" "Фамилия"
	,first_names."name" "Имя"
	,middle_names."name" "Отчество"
FROM
	relation_fio
	INNER JOIN last_names ON last_names.id = relation_fio.last_id
	INNER JOIN first_names ON first_names.id = relation_fio.first_id
	INNER JOIN middle_names ON middle_names.id = relation_fio.middle_id
ORDER BY
	"Фамилия" DESC, "Имя" DESC, "Отчество" DESC;

-- Конец скрипта
	