-- Monthly Sales Analysis
SELECT 
    DATE_FORMAT(OrderDate, '%Y-%m') as Month,
    COUNT(DISTINCT OrderID) as TotalOrders,
    SUM(Sales) as TotalSales,
    SUM(Profit) as TotalProfit,
    (SUM(Profit)/SUM(Sales) * 100) as ProfitMargin
FROM sales_data
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
ORDER BY Month;

-- Regional Performance
SELECT 
    Region,
    COUNT(DISTINCT OrderID) as NumberOfOrders,
    SUM(Sales) as TotalSales,
    SUM(Profit) as TotalProfit,
    AVG(Sales) as AverageOrderValue
FROM sales_data
GROUP BY Region
ORDER BY TotalSales DESC;

-- Product Category Analysis
SELECT 
    Category,
    SubCategory,
    COUNT(DISTINCT OrderID) as Orders,
    SUM(Quantity) as UnitsSold,
    SUM(Sales) as Revenue,
    SUM(Profit) as Profit
FROM sales_data
GROUP BY Category, SubCategory
ORDER BY Revenue DESC;
