-- Write your query below
WITH agg_ord AS (
    SELECT
        o.customer_id,
        SUM(o.id)
    FROM orders o
    GROUP BY
        o.customer_id
)

SELECT
    c.name
FROM customers c
WHERE c.id NOT IN (
    SELECT
        customer_id
    FROM agg_ord
)