# SQL JOINs Lab - MySQL with phpMyAdmin

## Objectives
- Practice INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN
- Understand how to combine rows from two or more tables based on related columns

## Types of JOINs
- **INNER JOIN**: Only rows with matching values in both tables
- **LEFT JOIN**: All rows from the left table + matching rows from the right
- **RIGHT JOIN**: All rows from the right table + matching rows from the left
- **FULL OUTER JOIN**: All rows when there's a match in either table

## Tool used
MySQL via phpMyAdmin

## Notes
This lab was completed via browser-based interface, not Jupyter.

## Example Query
```sql
SELECT customers.name, orders.id
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id;
