SELECT EU.UNIQUE_ID,E.NAME 
FROM EMPLOYEES AS E
LEFT JOIN EMPLOYEEUNI AS EU
ON EU.ID = E.ID