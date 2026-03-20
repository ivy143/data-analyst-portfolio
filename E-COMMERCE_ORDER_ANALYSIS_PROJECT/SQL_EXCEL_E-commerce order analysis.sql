CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    category VARCHAR(50),
    total_amount DECIMAL(10,2)
);
INSERT INTO orders (order_id, customer_id, order_date, category, total_amount)
VALUES
(1,101,'2024-01-05','Electronics',1200.00),
(2,102,'2024-01-10','Clothing',800.00),
(3,103,'2024-01-12','Home',450.00),
(4,101,'2024-02-02','Electronics',1500.00),
(5,104,'2024-02-05','Clothing',700.00),
(6,105,'2024-02-10','Beauty',300.00),
(7,102,'2024-03-01','Electronics',2000.00),
(8,106,'2024-03-05','Home',600.00),
(9,107,'2024-03-12','Clothing',900.00),
(10,101,'2024-03-20','Beauty',400.00),
(11,108,'2024-04-01','Electronics',1800.00),
(12,109,'2024-04-05','Home',750.00),
(13,110,'2024-04-10','Clothing',950.00),
(14,103,'2024-04-15','Beauty',500.00),
(15,102,'2024-05-02','Electronics',2200.00),
(16,111,'2024-05-06','Home',650.00),
(17,104,'2024-05-10','Beauty',350.00),
(18,105,'2024-05-15','Clothing',850.00),
(19,112,'2024-06-01','Electronics',1700.00),
(20,113,'2024-06-03','Home',550.00),
(21,101,'2024-06-10','Clothing',1000.00),
(22,114,'2024-06-12','Beauty',450.00),
(23,115,'2024-06-18','Electronics',2100.00),
(24,102,'2024-07-02','Home',700.00),
(25,103,'2024-07-05','Clothing',950.00),
(26,116,'2024-07-10','Beauty',400.00),
(27,104,'2024-08-01','Electronics',1600.00),
(28,105,'2024-08-05','Home',600.00),
(29,101,'2024-08-12','Clothing',1100.00),
(30,117,'2024-08-20','Beauty',500.00);
SELECT * FROM orders;
SELECT 
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,
    SUM(total_amount) AS monthly_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY order_year, order_month;

-- Monthly Sales Query 
SELECT 
    YEAR(order_date),
    MONTH(order_date),
    SUM(total_amount)
FROM orders
GROUP BY 
    YEAR(order_date),
    MONTH(order_date)
ORDER BY 
    YEAR(order_date),
    MONTH(order_date);
    
    -- ============================================
-- Customer Retention Analysis
-- Customers who placed more than 1 order
-- ============================================

SELECT 
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1
ORDER BY total_orders DESC;

-- ============================================
-- New vs Repeat Customers Analysis
-- ============================================

SELECT 
    customer_type,
    COUNT(*) AS total_customers
FROM (
    SELECT 
        customer_id,
        CASE 
            WHEN COUNT(order_id) = 1 THEN 'New'
            ELSE 'Repeat'
        END AS customer_type
    FROM orders
    GROUP BY customer_id
) AS customer_summary
GROUP BY customer_type;

-- ============================================
-- Top Categories by Revenue
-- ============================================
SELECT 
    category,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY category
ORDER BY total_revenue DESC;

-- Calculate Average Order Value (AOV)
SELECT 
    ROUND(SUM( total_amount) / COUNT(order_id), 2) AS average_order_value
FROM orders;


  
