SELECT * FROM order.sales_data;
INSERT INTO sales_data VALUES
(1, '2023-01-12', 101, 201, 2, 500, 1000, 'North'),
(2, '2023-02-18', 102, 202, 3, 450, 1350, 'South'),
(3, '2023-03-10', 103, 203, 1, 800, 800, 'East'),
(4, '2023-04-05', 104, 204, 2, 400, 800, 'West'),
(5, '2023-05-22', 105, 205, 4, 600, 2400, 'North'),
(6, '2023-06-14', 106, 201, 3, 550, 1650, 'South'),
(7, '2023-07-19', 107, 202, 5, 500, 2500, 'East'),
(8, '2023-08-25', 108, 203, 2, 750, 1500, 'West'),
(9, '2023-09-09', 109, 204, 3, 650, 1950, 'North'),
(10, '2023-10-30', 110, 205, 4, 700, 2800, 'South'),
(11, '2023-11-15', 111, 201, 6, 800, 4800, 'East'),
(12, '2023-12-20', 112, 202, 7, 900, 6300, 'West'),

(13, '2024-01-11', 113, 203, 3, 600, 1800, 'North'),
(14, '2024-02-16', 114, 204, 2, 750, 1500, 'South'),
(15, '2024-03-08', 115, 205, 4, 700, 2800, 'East'),
(16, '2024-04-12', 116, 201, 2, 500, 1000, 'West'),
(17, '2024-05-27', 117, 202, 5, 650, 3250, 'North'),
(18, '2024-06-18', 118, 203, 4, 700, 2800, 'South'),
(19, '2024-07-22', 119, 204, 6, 750, 4500, 'East'),
(20, '2024-08-30', 120, 205, 3, 800, 2400, 'West'),
(21, '2024-09-14', 121, 201, 4, 850, 3400, 'North'),
(22, '2024-10-29', 122, 202, 5, 900, 4500, 'South'),
(23, '2024-11-17', 123, 203, 7, 950, 6650, 'East'),
(24, '2024-12-21', 124, 204, 8, 1000, 8000, 'West'),

(25, '2025-01-09', 125, 205, 3, 700, 2100, 'North'),
(26, '2025-02-20', 126, 201, 4, 750, 3000, 'South'),
(27, '2025-03-15', 127, 202, 5, 800, 4000, 'East'),
(28, '2025-04-11', 128, 203, 2, 600, 1200, 'West'),
(29, '2025-05-24', 129, 204, 6, 850, 5100, 'North'),
(30, '2025-06-28', 130, 205, 5, 900, 4500, 'South');

SELECT DATE_FORMAT(order_date, '%Y-%m')
FROM sales_data;

SELECT 
    DATE_FORMAT(order_date, '%Y-%m-01') AS month_start,
    SUM(revenue) AS total_sales
FROM sales_data
GROUP BY DATE_FORMAT(order_date, '%Y-%m-01')
ORDER BY month_start;

-- 1: historical monthly sales
SELECT 
    DATE_FORMAT(order_date, '%Y-%m-01') AS month_start,
    SUM(revenue) AS total_sales
FROM sales_data
GROUP BY DATE_FORMAT(order_date, '%Y-%m-01')
ORDER BY month_start;

-- 2:data cleaning
-- step 1: check for NULL values
SELECT *
FROM sales_data
WHERE order_date IS NULL
   OR revenue IS NULL
   OR quantity IS NULL
   OR unit_price IS NULL;
   
   -- step 2: check for negative or zero revenue
   SELECT *
FROM sales_data
WHERE revenue <= 0;

-- step 3: validae revenue logic
-- revenue should equal : quantity x unit_price
SELECT *
FROM sales_data
WHERE revenue <> quantity * unit_price;

-- step 4: check for duplicate orders
SELECT order_id, COUNT(*)
FROM sales_data
GROUP BY order_id
HAVING COUNT(*) > 1;

-- step 5: remove invalid records before aggregation
SELECT 
    DATE_FORMAT(order_date, '%Y-%m-01') AS month_start,
    SUM(revenue) AS total_sales
FROM sales_data
WHERE revenue > 0
  AND quantity > 0
  AND unit_price > 0
GROUP BY DATE_FORMAT(order_date, '%Y-%m-01')
ORDER BY month_start;

SELECT 
    DATE_FORMAT(order_date, '%Y-%m-01') AS month_start,
    SUM(revenue) AS total_sales
FROM sales_data
WHERE revenue > 0
  AND quantity > 0
  AND unit_price > 0
GROUP BY DATE_FORMAT(order_date, '%Y-%m-01')
ORDER BY month_start;