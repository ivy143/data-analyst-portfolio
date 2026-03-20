CREATE DATABASE hr_analytics;
USE hr_analytics;

CREATE TABLE hr_employee (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    department VARCHAR(50),
    job_role VARCHAR(50),
    salary DECIMAL(10,2),
    experience_years INT,
    performance_rating INT,
    attrition VARCHAR(5),
    hire_date DATE,
    education_level VARCHAR(50),
    marital_status VARCHAR(20),
    city VARCHAR(50)
);
INSERT INTO hr_employee VALUES
(1,'Amit','Sharma',29,'Male','Sales','Sales Executive',45000,3,4,'No','2021-06-15','Bachelor','Single','Delhi'),
(2,'Priya','Verma',34,'Female','HR','HR Manager',65000,8,5,'No','2017-03-10','Master','Married','Mumbai'),
(3,'Rahul','Mehta',26,'Male','IT','Software Engineer',55000,2,3,'Yes','2022-01-12','Bachelor','Single','Bangalore'),
(4,'Sneha','Iyer',31,'Female','Finance','Financial Analyst',60000,6,4,'No','2019-07-01','Master','Married','Chennai'),
(5,'Arjun','Kapoor',28,'Male','Marketing','Marketing Executive',48000,4,3,'No','2020-09-20','Bachelor','Single','Delhi'),
(6,'Neha','Singh',30,'Female','Sales','Sales Manager',70000,9,5,'No','2016-04-18','Master','Married','Mumbai'),
(7,'Karan','Malhotra',27,'Male','IT','System Admin',52000,3,4,'No','2021-02-11','Bachelor','Single','Pune'),
(8,'Pooja','Nair',35,'Female','HR','HR Executive',50000,10,4,'Yes','2015-08-09','Master','Married','Bangalore'),
(9,'Vikas','Rao',32,'Male','Finance','Accountant',58000,7,3,'No','2018-05-14','Bachelor','Married','Hyderabad'),
(10,'Anjali','Desai',25,'Female','Marketing','Content Strategist',47000,2,4,'No','2022-06-01','Bachelor','Single','Ahmedabad'),

(11,'Rohit','Gupta',38,'Male','IT','Project Manager',90000,14,5,'No','2012-03-19','Master','Married','Delhi'),
(12,'Meera','Joshi',29,'Female','Sales','Sales Executive',46000,4,3,'Yes','2020-11-23','Bachelor','Single','Mumbai'),
(13,'Aditya','Roy',33,'Male','Finance','Finance Manager',85000,11,5,'No','2014-01-10','Master','Married','Kolkata'),
(14,'Kavya','Menon',26,'Female','IT','Software Engineer',56000,3,4,'No','2021-07-15','Bachelor','Single','Chennai'),
(15,'Sahil','Arora',41,'Male','HR','HR Director',95000,18,5,'No','2009-12-01','Master','Married','Delhi'),
(16,'Riya','Kapoor',28,'Female','Marketing','SEO Specialist',49000,3,3,'No','2021-03-12','Bachelor','Single','Pune'),
(17,'Manish','Yadav',36,'Male','Sales','Regional Manager',88000,12,5,'No','2013-09-25','Master','Married','Lucknow'),
(18,'Divya','Reddy',31,'Female','Finance','Auditor',62000,6,4,'No','2019-10-05','Master','Married','Hyderabad'),
(19,'Harsh','Patel',24,'Male','IT','Junior Developer',42000,1,3,'Yes','2023-02-17','Bachelor','Single','Ahmedabad'),
(20,'Nikita','Shah',29,'Female','HR','HR Executive',51000,5,4,'No','2020-04-21','Bachelor','Single','Mumbai'),

(21,'Tarun','Bansal',30,'Male','Marketing','Brand Manager',73000,7,4,'No','2018-08-30','Master','Married','Delhi'),
(22,'Simran','Kaur',27,'Female','Sales','Sales Executive',45000,3,3,'No','2021-01-14','Bachelor','Single','Chandigarh'),
(23,'Deepak','Mishra',34,'Male','Finance','Account Manager',78000,9,4,'No','2016-06-18','Master','Married','Varanasi'),
(24,'Ayesha','Khan',26,'Female','IT','QA Engineer',54000,2,4,'No','2022-03-22','Bachelor','Single','Bangalore'),
(25,'Gaurav','Sethi',39,'Male','HR','HR Manager',82000,15,5,'No','2011-07-11','Master','Married','Delhi'),
(26,'Isha','Pandey',28,'Female','Marketing','Marketing Analyst',50000,4,3,'Yes','2020-10-09','Bachelor','Single','Lucknow'),
(27,'Rakesh','Nanda',37,'Male','Sales','Sales Manager',76000,10,4,'No','2015-05-02','Master','Married','Jaipur'),
(28,'Tanya','Bose',29,'Female','Finance','Financial Analyst',61000,5,4,'No','2019-08-14','Master','Married','Kolkata'),
(29,'Akash','Jain',25,'Male','IT','Support Engineer',45000,2,3,'No','2022-09-19','Bachelor','Single','Indore'),
(30,'Shruti','Chopra',33,'Female','HR','Talent Acquisition',68000,8,4,'No','2017-12-12','Master','Married','Delhi'),

(31,'Varun','Goyal',28,'Male','Marketing','Content Manager',52000,4,3,'No','2020-06-06','Bachelor','Single','Noida'),
(32,'Preeti','Malik',35,'Female','Finance','Finance Executive',64000,9,4,'No','2016-04-15','Master','Married','Delhi'),
(33,'Naveen','Rathore',31,'Male','IT','Data Analyst',72000,6,5,'No','2018-11-03','Master','Married','Bangalore'),
(34,'Komal','Verghese',27,'Female','Sales','Sales Executive',46000,3,3,'Yes','2021-05-27','Bachelor','Single','Chennai'),
(35,'Abhishek','Saxena',42,'Male','Finance','Finance Director',99000,20,5,'No','2008-02-02','Master','Married','Mumbai'),
(36,'Mansi','Ahuja',26,'Female','IT','Frontend Developer',53000,2,4,'No','2022-07-08','Bachelor','Single','Pune'),
(37,'Yash','Trivedi',30,'Male','HR','HR Executive',52000,5,4,'No','2019-09-13','Bachelor','Married','Ahmedabad'),
(38,'Ritu','Sinha',34,'Female','Marketing','Marketing Manager',75000,9,5,'No','2016-01-21','Master','Married','Patna'),
(39,'Mohit','Chawla',29,'Male','Sales','Sales Executive',47000,4,3,'No','2020-12-17','Bachelor','Single','Delhi'),
(40,'Alisha','Thomas',32,'Female','IT','Backend Developer',68000,7,4,'No','2018-03-30','Master','Married','Bangalore'),

(41,'Sandeep','Kulkarni',36,'Male','Finance','Senior Accountant',73000,11,4,'No','2014-10-10','Master','Married','Pune'),
(42,'Lavanya','Iyer',28,'Female','HR','HR Executive',50000,4,3,'No','2020-02-02','Bachelor','Single','Chennai'),
(43,'Pratik','Das',27,'Male','IT','DevOps Engineer',65000,3,5,'No','2021-06-25','Bachelor','Single','Kolkata'),
(44,'Ankita','Ghosh',31,'Female','Marketing','Digital Marketer',62000,6,4,'No','2019-04-14','Master','Married','Kolkata'),
(45,'Rohan','Pillai',33,'Male','Sales','Area Manager',82000,9,5,'No','2016-08-08','Master','Married','Hyderabad'),
(46,'Bhavna','Kapadia',25,'Female','Finance','Junior Accountant',42000,1,3,'Yes','2023-01-15','Bachelor','Single','Ahmedabad'),
(47,'Tejas','Naik',29,'Male','IT','Software Engineer',57000,4,4,'No','2020-05-05','Bachelor','Single','Goa'),
(48,'Saloni','Bhatia',30,'Female','HR','HR Manager',74000,8,5,'No','2017-09-09','Master','Married','Delhi'),
(49,'Kunal','Agarwal',28,'Male','Marketing','Growth Analyst',60000,5,4,'No','2019-12-20','Master','Single','Noida'),
(50,'Reema','Chatterjee',35,'Female','Finance','Finance Manager',88000,12,5,'No','2013-03-03','Master','Married','Mumbai');
SELECT COUNT(*) FROM hr_employee;
-- ============================================
-- 1️-Attrition Rate
-- Business Question: What percentage of employees left the company?
-- Approach: (Employees with Attrition = 'Yes' / Total Employees) * 100
-- Purpose: Helps HR measure employee turnover and workforce stability.
-- ============================================

SELECT 
    ROUND(
        (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) 
        / COUNT(*)) * 100, 
    2
    ) AS attrition_rate_percentage
FROM hr_employee;
-- ============================================
-- 2️-Department Wise Average Salary
-- Business Question: What is the average salary in each department?
-- Approach: Use AVG(salary) and GROUP BY department.
-- Purpose: Helps compare salary distribution across departments.
-- ============================================

SELECT 
    department,
    ROUND(AVG(salary), 2) AS avg_salary
FROM hr_employee
GROUP BY department
ORDER BY avg_salary DESC;

-- ============================================
-- 3️-Gender Distribution
-- Business Question: What is the distribution of employees by gender?
-- Approach: Count employees grouped by gender.
-- Purpose: Helps measure workforce diversity.
-- ============================================

SELECT 
    gender,
    COUNT(*) AS employee_count,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hr_employee)), 2) 
    AS percentage
FROM hr_employee
GROUP BY gender
ORDER BY employee_count DESC;
-- ============================================
-- 4️-Experience vs Salary
-- Business Question: How does salary vary with experience?
-- Approach: Group employees by years of experience
--           and calculate average salary.
-- Purpose: Helps analyze salary growth trend.
-- ============================================
SELECT 
    experience_years,
    ROUND(AVG(salary), 2) AS avg_salary
FROM hr_employee
GROUP BY experience_years
ORDER BY experience_years;

-- ============================================
-- 5️-Identify High Performers
-- Business Question: Who are the high performing employees?
-- Approach: Filter employees with high performance rating.
-- Purpose: Helps in promotion and reward decisions.
-- ============================================

SELECT 
    employee_id,
    department,
    salary,
    performance_rating
FROM hr_employee
WHERE performance_rating >= 4
ORDER BY performance_rating DESC, salary DESC;
-- ============================================
-- 6️-Employees earning more than department average
-- Using CTE + Subquery
-- ============================================

WITH dept_avg_salary AS (
    SELECT 
        department,
        AVG(salary) AS avg_salary
    FROM hr_employee
    GROUP BY department
)

SELECT 
    e.employee_id,
    e.department,
    e.salary,
    d.avg_salary
FROM hr_employee e
JOIN dept_avg_salary d
    ON e.department = d.department
WHERE e.salary > d.avg_salary
ORDER BY e.department, e.salary DESC;


 
