-- Query for top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month.

SELECT Cars.Manufacturer as Manufacturer, COUNT(Sales.CarSerial) as CarsSold FROM Cars, Sales
WHERE Sales.CarSerial = Cars.CarSerial 
GROUP BY Manufacturer
ORDER BY CarsSold DESC
LIMIT 3;