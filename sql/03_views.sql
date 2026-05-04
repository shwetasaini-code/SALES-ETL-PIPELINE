-- ========================================
-- ANALYTICS VIEWS
-- ========================================

--For each city, show top 3 customers based on a combined performance score”
CREATE VIEW top_customers_by_city AS
SELECT * FROM (
		SELECT city, 
			   name,
			   salary,
			   review_info_score,
			   review_info_reviews,
			   -- performance score
			   salary + (review_info_score * review_info_reviews) AS performance_score,
			   -- ranking within each city
			   RANK() OVER (PARTITION BY city 
			   		  ORDER BY (salary + (review_info_score * review_info_reviews)) DESC)
			   AS rank_in_city
		FROM customers) t
WHERE rank_in_city <= 3;