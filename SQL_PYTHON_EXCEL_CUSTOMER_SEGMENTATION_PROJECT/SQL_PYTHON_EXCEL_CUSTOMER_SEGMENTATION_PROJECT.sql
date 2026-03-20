CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    signup_date DATE
);
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO customers VALUES
(1, 'Aman', 'Delhi', '2023-01-10'),
(2, 'Riya', 'Mumbai', '2023-02-15'),
(3, 'Karan', 'Bangalore', '2023-03-20'),
(4, 'Sneha', 'Delhi', '2023-04-05'),
(5, 'Arjun', 'Chennai', '2023-05-18'),
(6, 'Meera', 'Kolkata', '2023-06-22'),
(7, 'Rahul', 'Mumbai', '2023-07-11'),
(8, 'Pooja', 'Delhi', '2023-08-30'),
(9, 'Vikram', 'Hyderabad', '2023-09-12'),
(10, 'Neha', 'Pune', '2023-10-02');

INSERT INTO transactions VALUES
(101, 1, '2024-01-05', 2500),
(102, 1, '2024-02-10', 1800),
(103, 1, '2024-03-15', 2200),

(104, 2, '2024-01-20', 500),

(105, 3, '2024-02-25', 1200),
(106, 3, '2024-03-05', 1500),

(107, 4, '2023-11-10', 3000),

(108, 5, '2024-03-01', 700),
(109, 5, '2024-03-12', 900),

(110, 6, '2023-10-05', 4500),

(111, 7, '2024-02-14', 600),
(112, 7, '2024-02-20', 800),

(113, 8, '2024-01-08', 1500),

(114, 9, '2023-12-30', 2000),

(115, 10, '2024-03-18', 1000);

SELECT * FROM customers;
SELECT * FROM transactions;

-- Clean Customer Data
-- Step 1: Check NULL Values

-- 1. Customers Table
SELECT *
FROM customers
WHERE customer_id IS NULL
   OR customer_name IS NULL
   OR signup_date IS NULL;
   
   -- Clean Customer Data
-- Step 1: Check NULL Values

-- 2. Transactions Table
SELECT *
FROM transactions
WHERE customer_id IS NULL
   OR order_date IS NULL
   OR amount IS NULL;
   
   -- step 2: remove negative or zero amounts
   SELECT *
FROM transactions
WHERE amount <= 0;
-- if found
DELETE FROM transactions
WHERE amount <= 0;

-- step 3 : check duplicates customers
SELECT customer_id, COUNT(*)
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
SET SQL_SAFE_UPDATES = 0;
-- if duplicates exist
DELETE c1 FROM customers c1
JOIN customers c2
ON c1.customer_id = c2.customer_id
AND c1.signup_date > c2.signup_date;

-- step 4: check duplicate transaction
SELECT transaction_id, COUNT(*)
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- step 5: check orphan transactions
SELECT t.*
FROM transactions t
LEFT JOIN customers c
ON t.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
-- if found
DELETE t
FROM transactions t
LEFT JOIN customers c
ON t.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- step 6: check future dates( data error)
SELECT *
FROM transactions
WHERE order_date > CURDATE();

SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM transactions;


-- 2: CALCULATE RFM (Recency , Frequency , Monetary)
SELECT 
    c.customer_id,
    
    -- Recency (days since last purchase)
    DATEDIFF(CURDATE(), MAX(t.order_date)) AS recency,
    
    -- Frequency (total number of purchases)
    COUNT(t.transaction_id) AS frequency,
    
    -- Monetary (total spending)
    SUM(t.amount) AS monetary

FROM customers c
JOIN transactions t 
    ON c.customer_id = t.customer_id

GROUP BY c.customer_id;


-- what if coustomers never purchased?
-- then use lEFT JOIN instead of JOIN
SELECT 
    c.customer_id,
    
    -- Recency (days since last purchase)
    DATEDIFF(CURDATE(), MAX(t.order_date)) AS recency,
    
    -- Frequency (number of transactions)
    COUNT(t.transaction_id) AS frequency,
    
    -- Monetary (total spending)
    SUM(t.amount) AS monetary

FROM customers c
LEFT JOIN transactions t
    ON c.customer_id = t.customer_id

GROUP BY c.customer_id;

