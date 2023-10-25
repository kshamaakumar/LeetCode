WITH CTE as(
  SELECT *
  FROM Employees
  WHERE manager_id IS NOT NULL
)

SELECT e.employee_id FROM 
CTE as e LEFT JOIN Employees AS e2
ON e2.employee_id =e.manager_id 
WHERE e.salary <30000 AND e2.employee_id IS NULL
ORDER BY e.employee_id 