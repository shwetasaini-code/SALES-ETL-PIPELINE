-- ========================================
-- ANALYTICS TABLES
-- ========================================

--city-level summary
CREATE TABLE city_metrics AS
SELECT city, 
	   COUNT(*) AS total_customer,
	   AVG(salary) AS avg_salary,
	   AVG(review_info_score) AS avg_score,
	   SUM(review_info_reviews) AS total_reviews
FROM customers
GROUP BY city;

