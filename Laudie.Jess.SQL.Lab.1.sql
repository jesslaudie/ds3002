# 1. Write a query to get Product name and quantity/unit.  
Select northwind.products.product_name, northwind.products.quantity_per_unit FROM northwind.products;
# 2. Write a query to get current Product list (Product ID and name)
Select northwind.products.id, northwind.products.product_name FROM northwind.products;
# 3. Write a query to get discontinued Product list (Product ID and name). 
Select northwind.products.discontinued, northwind.products.product_name, northwind.products.id FROM northwind.products;
# 4. Write a query to get most expense and least expensive Product list (name and unit price).  
Select max(northwind.products.product_name), max(northwind.order_details.unit_price), min(northwind.products.product_name), 
min(northwind.order_details.unit_price) FROM northwind.products INNER JOIN northwind.order_details 
ON northwind.products.id = northwind.order_details.product_id;
# 5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.  
Select northwind.products.id, northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products
INNER JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id 
WHERE unit_price < 20;
# 6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
Select northwind.products.id, northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products
INNER JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id 
WHERE unit_price > 15 < 25;
# 7. Write a query to get Product list (name, unit price) of above average price.  
Select northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products
INNER JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id
WHERE northwind.order_details.unit_price > (Select AVG(northwind.order_details.unit_price) FROM northwind.order_details);
# 8. Write a query to get Product list (name, unit price) of ten most expensive products
Select northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products
INNER JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id
ORDER by northwind.order_details.unit_price desc limit 10;
# 9. Write a query to count current and discontinued products. 
Select COUNT(northwind.products.discontinued = 1), COUNT(northwind.products.discontinued =0) FROM northwind.products;
# 10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  
Select northwind.products.product_name, northwind.order_details.quantity as units_in_stock, northwind.inventory_transactions.quantity as units_on_order
FROM northwind.products
INNER JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id
INNER JOIN northwind.inventory_transactions ON northwind.products.id = northwind.inventory_transactions.id
WHERE northwind.order_details.quantity < northwind.inventory_transactions.quantity;