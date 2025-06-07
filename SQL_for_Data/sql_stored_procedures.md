# SQL Views Lab - MySQL

## Objectives
- Learn how to create and use views to simplify queries
- Protect and abstract underlying table logic

## Example

### Create a View
```sql
CREATE VIEW high_spenders AS
SELECT name, total_spent
FROM customers
WHERE total_spent > 1000;
Query the View
```
```sql
SELECT * FROM high_spenders;
```
## Notes
- Views are virtual tables, useful for reusable logic
- In MySQL, you can update through views if they meet certain conditions (e.g., no GROUP BY or JOIN)
