## Objectives
- Understand the structure and syntax of stored procedures in DB2
- Learn how to declare variables, use control flow (IF, WHILE), and handle parameters

## Example

### Create Procedure
```sql
CREATE OR REPLACE PROCEDURE AddOrder 
(
 IN cust_id INT, 
 IN prod_id INT, 
 IN quantity INT
)
BEGIN
  INSERT INTO ORDERS (CUSTOMER_ID, PRODUCT_ID, QUANTITY)
  VALUES (cust_id, prod_id, quantity);
END;
```
## Call Procedure
```sql
CALL AddOrder(1, 101, 3);
```
## Notes
- Procedures are stored in the database and can be reused.
- Useful for business logic, especially when combining multiple SQL statements.
