-- Write your query below
SELECT c.customer_id
FROM customers c
WHERE year = 2020
    AND revenue > 0