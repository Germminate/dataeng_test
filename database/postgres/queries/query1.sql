-- Query for list of customers and their spending.

SELECT CustName, SalesVolume 
FROM (SELECT Sales.CustID, Customer.CustName as CustName, SUM(Cars.Price) as SalesVolume
FROM Customer, Sales, Cars
WHERE Sales.CustID = Customer.CustID
AND Sales.CarSerial = Cars.CarSerial
GROUP BY Sales.CustID, Customer.CustName
ORDER BY SalesVolume DESC) as CustSpending;