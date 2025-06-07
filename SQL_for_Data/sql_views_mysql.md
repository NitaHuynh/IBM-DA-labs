# SQL JOINs Lab - MySQL with phpMyAdmin

## Objectives
- Practice INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN
- Understand how to combine rows from multiple tables using keys

## Types of JOINs
- **INNER JOIN**: Only rows with matching values in both tables
- **LEFT JOIN**: All rows from left table, and matching from right
- **RIGHT JOIN**: All rows from right table, and matching from left
- **FULL OUTER JOIN**: Not supported directly — emulate using `UNION`

## Example Query
```sql
SELECT c.name, o.order_id
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id;
Notes
FULL OUTER JOIN can be emulated:
```
```sql
SELECT * FROM A LEFT JOIN B ON A.id = B.id
UNION
SELECT * FROM A RIGHT JOIN B ON A.id = B.id;
```
## Tool used
MySQL via phpMyAdmin
