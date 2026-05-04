-- ========================================
-- BASIC ANALYTICS QUERIES
-- ========================================

--1. AVERAGE SALARY PER CITY (SORTED)
SELECT
	city,AVG(salary) as avg_salary
FROM
	customers
GROUP BY city
ORDER BY AVG(salary) DESC;

--2. Count of customers per city
SELECT
	city,COUNT(*) as customer_count
FROM
	customers
GROUP BY city
ORDER BY COUNT(id);

--3. Top 5 highest paid customers
SELECT
	*
FROM
	customers
ORDER BY salary desc
LIMIT 5;

--4. Monthly signup count
SELECT
	DATE_TRUNC('month', signup_date) as month,
	count(*) as monthly_count
FROM
	customers
GROUP BY month
ORDER BY month;

--5. City with highest average salary
SELECT
	city, AVG(salary) AS avg_salary
FROM
	customers
GROUP BY city
ORDER BY AVG(salary) DESC
LIMIT 1;

--6. Find customers earning above city average
SELECT
	name, city, salary
FROM
	customers c
WHERE salary > (select 
				AVG(salary) FROM customers
				WHERE city=c.city);

--7. Rank customers by salary
SELECT
	name, salary , RANK() OVER (ORDER BY salary DESC) as salary_rank
FROM
	customers;

--8. Top 3 customers per city
SELECT * FROM (
			SELECT name,city, 
			ROW_NUMBER() OVER (PARTITION BY city ORDER BY salary DESC) as row_number
			FROM customers ) 
WHERE row_number <= 3;

--9. Salary category segmentation
SELECT
	 name,
	 CASE 
	 	WHEN salary<50000 THEN 'Low'
	 	WHEN salary BETWEEN 50000 and 80000 THEN 'Medium'
	 	ELSE 'High'
	 END AS salary_category
FROM
	customers;

--10. Find duplicate customers
SELECT
	 name, email, COUNT(*)
FROM
	customers 
GROUP BY name, email
HAVING COUNT(*) > 1;

--11. Highest rated customer per city
SELECT * FROM (
		 SELECT name,city,salary, 
		 RANK() OVER (PARTITION BY city ORDER BY salary DESC) as salary_rank
		 FROM customers) customer_t
WHERE salary_rank = 1;
