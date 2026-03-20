CREATE DATABASE food_delivery_project;
USE food_delivery_project;
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    restaurant_id INT,
    city VARCHAR(50),
    order_time DATETIME,
    delivery_time DATETIME,
    order_status VARCHAR(20),  -- Delivered / Cancelled
    order_amount DECIMAL(10,2)
);
INSERT INTO orders 
(customer_id, restaurant_id, city, order_time, delivery_time, order_status, order_amount)
VALUES
(111, 2, 'Delhi', '2026-02-04 12:30:00', '2026-02-04 13:05:00', 'Delivered', 540.00),
(112, 5, 'Mumbai', '2026-02-04 20:10:00', '2026-02-04 20:55:00', 'Delivered', 760.00),
(113, 3, 'Bangalore', '2026-02-04 18:00:00', NULL, 'Cancelled', 430.00),
(114, 1, 'Chennai', '2026-02-05 14:15:00', '2026-02-05 14:50:00', 'Delivered', 310.00),
(115, 4, 'Hyderabad', '2026-02-05 21:40:00', '2026-02-05 22:20:00', 'Delivered', 880.00),
(116, 2, 'Delhi', '2026-02-06 19:20:00', '2026-02-06 20:00:00', 'Delivered', 470.00),
(117, 5, 'Mumbai', '2026-02-06 11:45:00', '2026-02-06 12:25:00', 'Delivered', 390.00),
(118, 3, 'Bangalore', '2026-02-06 22:05:00', NULL, 'Cancelled', 510.00),
(119, 1, 'Chennai', '2026-02-07 13:30:00', '2026-02-07 14:05:00', 'Delivered', 650.00),
(120, 4, 'Hyderabad', '2026-02-07 18:50:00', '2026-02-07 19:30:00', 'Delivered', 720.00);
SELECT COUNT(*) FROM orders;
-- ============================================================
-- Project: Food Delivery Performance Analysis
-- Metric: Delivery Time Analysis
-- ============================================================

-- Business Question:
-- What is the average delivery time, and how does it vary across cities?
-- This helps evaluate operational efficiency and identify slow-performing regions.

-- Approach:
-- 1. Consider only delivered orders (exclude cancelled orders).
-- 2. Calculate delivery duration using TIMESTAMPDIFF in minutes.
-- 3. Compute overall and city-wise average delivery time.
-- 4. Sort results to identify highest delay locations.


-- ============================================================
-- Step 1: Overall Average Delivery Time
-- ============================================================

SELECT 
    ROUND(
        AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)), 
        2
    ) AS avg_delivery_minutes

FROM orders

WHERE order_status = 'Delivered';



-- ============================================================
-- Step 2: City-wise Average Delivery Time
-- ============================================================

SELECT 
    city,
    
    ROUND(
        AVG(TIMESTAMPDIFF(MINUTE, order_time, delivery_time)), 
        2
    ) AS avg_delivery_minutes

FROM orders

WHERE order_status = 'Delivered'

GROUP BY city

ORDER BY avg_delivery_minutes DESC;


-- ============================================================
-- Project: Food Delivery Performance Analysis
-- Metric: Cancellation Rate
-- ============================================================

-- Business Question:
-- What percentage of total orders are getting cancelled?
-- This helps evaluate service reliability and operational stability.

-- Approach:
-- 1. Count total number of orders.
-- 2. Count number of cancelled orders.
-- 3. Divide cancelled orders by total orders.
-- 4. Multiply by 100 to get percentage.
-- 5. Round result to 2 decimal places for reporting clarity.


-- ============================================================
-- Overall Cancellation Rate
-- ============================================================

SELECT 

    ROUND(
        (COUNT(CASE WHEN order_status = 'Cancelled' THEN 1 END) * 100.0)
        / COUNT(*),
        2
    ) AS cancellation_rate_percentage

FROM orders;
SELECT COUNT(*) 
FROM orders 
WHERE order_status = 'Cancelled';

-- ============================================================
-- Project: Food Delivery Performance Analysis
-- Metric: Top Restaurants (Revenue Based)
-- ============================================================

-- Business Question:
-- Which restaurants generate the highest revenue?
-- This helps identify high-performing partners and key revenue contributors.

-- Approach:
-- 1. Consider only delivered orders (cancelled orders do not generate revenue).
-- 2. Aggregate total revenue using SUM(order_amount).
-- 3. Group results by restaurant_id.
-- 4. Sort in descending order to identify top performers.
-- 5. Limit results to top-performing restaurants.


-- ============================================================
-- Top Restaurants by Revenue
-- ============================================================

SELECT 
    restaurant_id,
    
    ROUND(SUM(order_amount), 2) AS total_revenue

FROM orders

-- Only delivered orders contribute to revenue
WHERE order_status = 'Delivered'

GROUP BY restaurant_id

-- Highest revenue first
ORDER BY total_revenue DESC

LIMIT 5;

-- ============================================================
-- Project: Food Delivery Performance Analysis
-- Metric: Peak Order Hours
-- ============================================================

-- Business Question:
-- During which hours of the day does the platform receive the highest number of orders?
-- This helps in workforce planning, delivery partner allocation, and demand forecasting.

-- Approach:
-- 1. Extract hour from order_time using HOUR().
-- 2. Count total orders per hour.
-- 3. Group results by order hour.
-- 4. Sort in descending order to identify peak demand hours.


-- ============================================================
-- Peak Order Hours
-- ============================================================

SELECT 
    HOUR(order_time) AS order_hour,
    
    COUNT(*) AS total_orders

FROM orders

GROUP BY order_hour

ORDER BY total_orders DESC;

-- ============================================================
-- Project: Food Delivery Performance Analysis
-- Metric: City-wise Revenue
-- ============================================================

-- Business Question:
-- Which cities contribute the most to total platform revenue?
-- This helps identify high-performing markets and supports expansion planning.

-- Approach:
-- 1. Consider only delivered orders (cancelled orders do not generate revenue).
-- 2. Aggregate revenue using SUM(order_amount).
-- 3. Group results by city.
-- 4. Sort in descending order to identify highest revenue cities.


-- ============================================================
-- City-wise Revenue
-- ============================================================
SELECT 
    city,
    
    ROUND(SUM(order_amount), 2) AS total_revenue

FROM orders

-- Only delivered orders generate revenue
WHERE order_status = 'Delivered'

GROUP BY city


-- Highest revenue city first
ORDER BY total_revenue DESC;








