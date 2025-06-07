# SQL Basic Syntax & Functions – DB2

## Objectives
- Practice core SQL statements for data definition and manipulation in IBM DB2
- Understand DDL and DML concepts in DB2 syntax
- Perform CRUD operations and sort results using ORDER BY

## 🔧 DDL (Data Definition Language)

### Create Table
```sql
CREATE TABLE CUSTOMERS (
  ID INT PRIMARY KEY,
  NAME VARCHAR(100),
  EMAIL VARCHAR(100)
);
```
### Alter Table
```sql
ALTER TABLE CUSTOMERS ADD PHONE VARCHAR(15);
Drop Table
```
```sql
DROP TABLE CUSTOMERS;
```
## ✏️ DML (Data Manipulation Language)
### Insert Data
```sql
INSERT INTO CUSTOMERS (ID, NAME, EMAIL)
VALUES (1, 'Alice', 'alice@example.com');
Update Data
```
```sql
UPDATE CUSTOMERS
SET EMAIL = 'new_email@example.com'
WHERE ID = 1;
Delete Data
```
```sql
DELETE FROM CUSTOMERS
WHERE ID = 1;
```
## 📄 Read Data (CRUD - Read + Filter)
### Select All
```sql
SELECT * FROM CUSTOMERS;
Select with WHERE
```
```sql
SELECT NAME FROM CUSTOMERS
WHERE EMAIL LIKE '%gmail.com';
ORDER BY Clause
```
```sql
SELECT * FROM CUSTOMERS
ORDER BY NAME ASC;
```
## Notes
- DB2 uses standard SQL syntax with a few differences in function naming.
- DDL defines database structure; DML works with the data inside.
- ORDER BY allows sorting by columns in ascending (ASC) or descending (DESC) order.
