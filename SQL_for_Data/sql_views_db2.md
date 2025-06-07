# SQL Views Lab - DB2

## Objectives
- Learn how to create and use SQL Views
- Understand the purpose of Views for simplifying queries and protecting data
- Practice SELECT statements on Views

## Example

### Create a View
```sql
CREATE VIEW TopCustomers AS
SELECT NAME, TOTAL_SPENT
FROM CUSTOMERS
WHERE TOTAL_SPENT > 1000;
Query a View
```
```sql
SELECT * FROM TopCustomers;
```
## Notes
Views act like virtual tables.
- They help encapsulate logic and can improve query readability.
- Cannot always be updated if based on multiple tables or aggregations.
