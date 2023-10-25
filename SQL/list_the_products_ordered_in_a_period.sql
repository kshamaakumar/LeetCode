WITH CTE AS(SELECT product_id, sum(unit) as unit
FROM Orders
WHERE YEAR(order_date)=2020
AND MONTH(order_date)=2
GROUP BY product_id)

SELECT product_name, unit FROM Products ,CTE
WHERE Products.product_id=CTE.product_id
AND unit>=100;