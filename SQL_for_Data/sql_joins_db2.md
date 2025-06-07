# SQL JOINs Lab - DB2 (using IBM DB2 on Coursera)

## Objectives
- Practice different types of SQL JOINs on DB2 database
- Understand the logic and syntax of INNER, LEFT, RIGHT, and FULL OUTER JOINs
- Retrieve related data from multiple tables using JOIN clauses

## Types of JOINs

- **INNER JOIN**: Returns only matching rows in both tables
- **LEFT JOIN**: Returns all rows from the left table, and matching rows from the right table
- **RIGHT JOIN**: Returns all rows from the right table, and matching rows from the left table
- **FULL OUTER JOIN**: Returns all rows when there is a match in either left or right table

## Example Query (DB2 syntax)
```sql
SELECT C.NAME, O.ORDER_ID
FROM CUSTOMERS C
INNER JOIN ORDERS O
ON C.CUSTOMER_ID = O.CUSTOMER_ID;
```
## Tool Used
IBM DB2 database via Skills Network Labs (Jupyter or SQL console)

## Notes
- In DB2, JOIN behavior is standard SQL.
- Pay attention to table aliases and matching column names.
- FULL OUTER JOIN may not be supported directly in some DB2 setups; you can emulate it using UNION of LEFT and RIGHT JOINs:

```sql
SELECT * FROM A LEFT JOIN B ON A.id = B.id
UNION
SELECT * FROM A RIGHT JOIN B ON A.id = B.id;
```
✅ This lab was completed using the IBM DB2 environment provided in the Coursera course.
