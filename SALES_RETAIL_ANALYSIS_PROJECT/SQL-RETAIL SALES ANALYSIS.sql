CREATE DATABASE retail_portfolio;
USE retail_portfolio;
CREATE TABLE retail_sales (
order_id VARCHAR(20),
order_date DATE,
ship_date DATE,
customer_id VARCHAR(20),
customer_name VARCHAR(100),
segment VARCHAR(50),
region VARCHAR(50),
state VARCHAR(50),
city VARCHAR(50),
product_id VARCHAR(20),
product_name VARCHAR(50),
category VARCHAR(50),
sub_category VARCHAR(50),
sales DECIMAL(10,2),
quantity INT,
discount DECIMAL(5,2),
profit DECIMAL(10,2)
);
INSERT INTO retail_sales VALUES
('ORD-1001','2023-01-05','2023-01-08','C-101','Amit Sharma','Consumer','North','Delhi','Delhi','P-11','HP Laptop 15inch','Technology','Laptops',80000,1,0.10,12000),

('ORD-1002','2023-01-07','2023-01-10','C-102','Priya Singh','Corporate','West','Maharashtra','Mumbai','P-22','Office Chair','Furniture','Chairs',5000,2,0.15,500),

('ORD-1003','2023-01-15','2023-01-18','C-103','rahul verma','Consumer','South','Karnataka','Bangalore','P-33','Samsung Galaxy','Technology','Mobiles',40000,1,0.05,6000),

('ORD-1004','2023-02-01','2023-02-05','C-101','Amit Sharma','Consumer','North','Delhi','Delhi','P-44','Canon Printer','Office Supplies','Printers',15000,1,0.20,2000),

('ORD-1005','2023-02-12','2023-02-15','C-104','Neha Jain','Home Office','East','West Bengal','Kolkata','P-55','Wooden Table','Furniture','Tables',7000,1,0.25,-500),

('ORD-1006','2023-03-05','2023-03-09','C-105','Karan Mehta','Corporate','West','Gujarat','Ahmedabad','P-66','Dell Monitor','Technology','Accessories',12000,2,0.30,1000),

('ORD-1007','2023-03-15','2023-03-18','C-102','Priya Singh','Corporate','West','Maharashtra','Mumbai','P-22','Office Chair','Furniture','Chairs',5000,3,0.40,-1000);
/*
Project: Retail Sales Analysis
Database: MySQL
Objective: Analyze retail sales data to identify top products,
monthly revenue trends, customer performance, and regional insights.
*/

-- ============================================
-- 1️-Top Selling Products
-- Business Question: Which products generate the highest sales revenue?
-- Approach: Aggregate total sales by product and sort in descending order.
-- ============================================

SELECT product_name,
       SUM(sales) AS total_revenue
FROM retail_sales
GROUP BY product_name
ORDER BY total_revenue DESC;



-- ============================================
-- 2️-Monthly Revenue Trends
-- Business Question: How does revenue vary month over month?
-- Approach: Extract year & month from order_date and sum total sales.
-- ============================================

SELECT 
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS monthly_revenue
FROM retail_sales
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;



-- ============================================
-- 3️-Profit by Category
-- Business Question: Which category generates the highest profit?
-- Approach: Aggregate total profit grouped by category.
-- ============================================

SELECT category,
       SUM(profit) AS total_profit
FROM retail_sales
GROUP BY category
ORDER BY total_profit DESC;



-- ============================================
-- 4️-Top 10 Customers by Revenue
-- Business Question: Who are the top 10 customers contributing most revenue?
-- Approach: Sum sales by customer and limit results to top 10.
-- ============================================

SELECT customer_name,
       SUM(sales) AS total_revenue
FROM retail_sales
GROUP BY customer_name
ORDER BY total_revenue DESC
LIMIT 10;



-- ============================================
-- 5️-Region-wise Performance
-- Business Question: How does performance vary across regions?
-- Approach: Calculate total sales and profit by region.
-- ============================================

SELECT region,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit
FROM retail_sales
GROUP BY region
ORDER BY total_sales DESC;



-- ============================================
-- 6️-Ranking Top Products (Window Function)
-- Business Question: Rank products based on total revenue.
-- Approach: Use RANK() window function over total sales.
-- ============================================


-- ============================================
-- 7️-Discount Impact on Profit
-- Business Question: How does discount percentage affect average profit?
-- Approach: Group data by discount and calculate average profit 
--           to analyze the relationship between discount and profitability.
-- ============================================

SELECT 
    discount,
    ROUND(AVG(profit), 2) AS avg_profit
FROM retail_sales
GROUP BY discount
ORDER BY discount ASC;

