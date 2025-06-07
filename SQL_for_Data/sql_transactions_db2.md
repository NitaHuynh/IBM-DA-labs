## Objectives
- Learn how to use transactions to ensure data consistency
- Practice COMMIT and ROLLBACK commands
- Understand atomicity of transactions

## Example

### Start Transaction
```sql
BEGIN;

UPDATE ACCOUNTS
SET BALANCE = BALANCE - 500
WHERE ACCOUNT_ID = 101;

UPDATE ACCOUNTS
SET BALANCE = BALANCE + 500
WHERE ACCOUNT_ID = 102;

COMMIT;
Rollback Example
```
```sql
BEGIN;

DELETE FROM CUSTOMERS WHERE CUSTOMER_ID = 1;

ROLLBACK;
```
## Notes
Transactions ensure that either all operations succeed or none do.

Always test critical operations inside a transaction before committing.
