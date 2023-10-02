Create a view ItemView that displays a list of records where each record is comprised of the itemId as iId, item name as
ItemName, the number of boxes of the item sold as NoOfBoxes, the item price as ItemPrice, the revenue generated by
each item as ItemRevenue, and the number of customers as ItemCustomers who bought the item boxes at any of the
Arlington Sprouts stores.

Write an SQL query to display the contents of the view ItemView.

Query : CREATE VIEW ItemView AS
SELECT 
    item.Iid, 
    item.Iname, 
    SUM(order_item.Icount) AS Noofboxes, 
    item.Sprice AS ItemPrice, 
    SUM(order_item.Icount * item.Sprice) AS ItemRevenue, 
    COUNT(DISTINCT orders.cid) AS ItemCustomers
FROM 
    item 
    JOIN order_item ON item.Iid = order_item.Iid
    JOIN orders ON order_item.Oid = orders.oid
GROUP BY item.Iid;
 
Select * from Itemview;
 



1.) Use the view ItemView to retrieve a list of records where each record is comprised of item Id, item name, the
number of boxes of items sold, and the price of each box of the item for all items that cost more than $3.00 and that have
been bought by customers.

Query : SELECT Iid, Iname, Noofboxes, ItemPrice
FROM ItemView
WHERE ItemPrice > 3.00 AND Noofboxes > 0;
 

2.) Use the view ItemView to retrieve a list of records where each record is comprised of the item Name and the ItemRevenue for the item(s) that generated the minimum revenue in the database.

Query : SELECT Iname, ItemRevenue AS MinItemRevenue
FROM ItemView
WHERE ItemRevenue = (
  SELECT MIN(ItemRevenue) FROM ItemView
);
 

3.) Use the view ItemView to generate the min, max and average revenue generated by all the items in the ItemView.

Query : SELECT MIN(ItemRevenue) AS min_revenue, MAX(ItemRevenue) AS max_revenue, AVG(ItemRevenue) AS avg_revenue
FROM ItemView;
 

4.) Use the view ItemView to retrieve a list of records where each record is comprised of an item name along with the number of customers who bought it. Sort the list by the number of customers in descending order followed by item names
in an ascending order.

Query : SELECT Iname, ItemCustomers
FROM ItemView
GROUP BY Iname
ORDER BY ItemCustomers DESC, Iname ASC;

 

5.) Use the view ItemView to retrieve the total revenue earned, the total number of boxes sold and the average revenue per box sold by Arlington Sprouts as stored in the database.
Query : SELECT SUM(ItemRevenue) AS TotalRevenue,
       SUM(Noofboxes) AS TotalBoxesBought,
       AVG(ItemRevenue) AS AverageRevenuePerBoxSold
FROM itemview;