# SQL Basic Syntax & Functions – MySQL

## Objectives
- Practice core SQL statements for data creation, manipulation, and retrieval
- Understand DDL and DML concepts
- Use CRUD operations and ORDER BY in MySQL

## 🔧 DDL (Data Definition Language)

### Create Table
```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
```
### Alter Table
```sql
ALTER TABLE customers ADD phone VARCHAR(15);
## Drop Table
```
```sql
DROP TABLE customers;
```
## ✏️ DML (Data Manipulation Language)
### Insert Data
```sql
INSERT INTO customers (id, name, email)
VALUES (1, 'Alice', 'alice@example.com');
```
### Update Data
```sql
UPDATE customers
SET email = 'new_email@example.com'
WHERE id = 1;
Delete Data
```
```sql
DELETE FROM customers
WHERE id = 1;
📄 Read Data (CRUD - Read + Filter)
Select All
```
```sql
SELECT * FROM customers;
Select with WHERE
```
```sql
SELECT name FROM customers
WHERE email LIKE '%gmail.com';
ORDER BY Clause
```
```sql
SELECT * FROM customers
ORDER BY name ASC;
```
## Notes
- DDL affects the structure of database objects (tables, columns).
- DML works with the data inside those structures.
- ORDER BY is used to sort query results by column values (ASC/DESC).
