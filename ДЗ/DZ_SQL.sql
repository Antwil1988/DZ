
-- ЭТАП 1: СОЗДАНИЕ СТРУКТУРЫ БАЗЫ ДАННЫХ

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    order_date DATE NOT NULL
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id),
    product_name VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    price NUMERIC(12, 2) NOT NULL
);

-- ЭТАП 2: НАПОЛНЕНИЕ ТЕСТОВЫМИ ДАННЫМИ

INSERT INTO customers (name, email) VALUES
('Иван Иванов', 'ivan@example.com'),
('Мария Петрова', 'maria@example.com'),
('Алексей Смирнов', 'alexey@example.com');

INSERT INTO orders (customer_id, order_date) VALUES
(1, '2025-06-01'),
(1, '2025-06-10'),
(2, '2025-06-05');

INSERT INTO order_items (order_id, product_name, quantity, price) VALUES
(1, 'Монитор Samsung', 1, 12000.00),
(1, 'Кабель HDMI', 2, 500.00),
(2, 'Ноутбук Lenovo', 1, 45000.00),
(3, 'Мышь Logitech', 1, 1500.00),
(3, 'Клавиатура Logitech', 1, 2500.00);

-- ЭТАП 3: SQL-ЗАПРОСЫ НА ЧТЕНИЕ

-- Задание 1
SELECT o.id, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE c.name = 'Иван Иванов';

-- Задание 2
SELECT product_name, quantity, price
FROM order_items
WHERE order_id = 3
ORDER BY price DESC;

-- Задание 3
SELECT c.name, SUM(oi.quantity * oi.price) AS total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY c.name
HAVING SUM(oi.quantity * oi.price) > 5000
ORDER BY total_spent DESC;

-- МАССОВОЕ НАПОЛНЕНИЕ БАЗЫ

-- Создадим 10 000 заказов
INSERT INTO orders (customer_id, order_date)
SELECT
    (random() * 2 + 1)::int,  -- случайный customer_id от 1 до 3
    (current_date - (random() * 365)::int)  -- случайная дата за последний год
FROM generate_series(1, 10000) s;

-- Заполним order_items миллионом записей
INSERT INTO order_items (order_id, product_name, quantity, price)
SELECT
    (random() * 10000 + 1)::int,  -- случайный order_id от 1 до 10000
    'Товар ' || (random() * 500 + 1)::int,  -- Товар 1-500
    floor(random() * 10) + 1,  -- количество от 1 до 10
    round((random() * 99900 + 100)::numeric, 2)  -- цена от 100 до 100 000
FROM generate_series(1, 1000000) s;

-- УСТАНОВКА ИНДЕКСОВ

-- Индекс на customer_id
CREATE INDEX idx_orders_customer_id ON orders(customer_id);

-- Композитный индекс на order_id и price
CREATE INDEX idx_order_items_order_id_price ON order_items(order_id, price);

-- Индекс на product_name
CREATE INDEX idx_order_items_product_name ON order_items(product_name);

-- АНАЛИЗ ИСПОЛЬЗОВАНИЯ ИНДЕКСОВ

EXPLAIN ANALYZE
SELECT * FROM order_items
WHERE order_id = 123 AND price > 10000;

EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 1;

EXPLAIN ANALYZE
SELECT * FROM order_items WHERE product_name = 'Товар 42';


-- УДАЛЕНИЕ НЕЭФФЕКТИВНЫХ ИНДЕКСОВ
/*
Вывод: Ни один индекс не требует удаления, но
Несмотря на то, что idx_order_items_product_name используется, эффективность ограничена:
- Возвращает ~2000 строк, что близко к порогу, когда PostgreSQL может предпочесть Seq Scan.
- Селективность по product_name низкая, так как названия часто повторяются.
- Преимущество индекса незначительно по сравнению с полным сканированием.
*/
DROP INDEX IF EXISTS idx_order_items_product_name;

-- БИЗНЕС-ЛОГИКА С ИСП. ТРАНЗАКЦИЙ

BEGIN;

-- Добавляем заказ
INSERT INTO orders (customer_id, order_date)
VALUES (1, CURRENT_DATE)
RETURNING id;


-- Добавляем товары
INSERT INTO order_items (order_id, product_name, quantity, price)
VALUES
    (10001, 'Товар 1', 2, 500.00),
    (10001, NULL, 1, 1500.00),  -- << провоцируем ошибку
    (10001, 'Товар 3', 3, 200.00);

-- COMMIT;

ROLLBACK;

-- Проверим, остался ли заказ
SELECT * FROM orders WHERE id = 10001;

-- Проверим, остались ли товары
SELECT * FROM order_items WHERE order_id = 10001;
