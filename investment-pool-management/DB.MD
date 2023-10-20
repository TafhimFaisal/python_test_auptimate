**Entities:**

1. **Users Table:**

| Field           | Type         | Description                   |
| --------------- | ------------ | ----------------------------- |
| UserID          | INT          | Unique User ID                |
| Username        | VARCHAR(50)  | User's username               |
| Password        | VARCHAR(100) | Hashed user password           |
| Email           | VARCHAR(100) | User's email address           |
| Role            | ENUM         | User role (e.g., Fund Manager) |

2. **Investment Pools Table:**

| Field           | Type         | Description                   |
| --------------- | ------------ | ----------------------------- |
| PoolID          | INT          | Unique Pool ID                |
| PoolName        | VARCHAR(100) | Name of the investment pool   |
| FundManagerID   | INT          | ID of the fund manager        |
| CreationDate    | DATE         | Date the pool was created     |

3. **Investors Table:**

| Field           | Type         | Description                   |
| --------------- | ------------ | ----------------------------- |
| InvestorID      | INT          | Unique Investor ID            |
| InvestorName    | VARCHAR(100) | Investor's name               |
| Email           | VARCHAR(100) | Investor's email address      |

4. **InvestorPoolMapping Table:**

| Field           | Type         | Description                   |
| --------------- | ------------ | ----------------------------- |
| MappingID       | INT          | Unique Mapping ID             |
| InvestorID      | INT          | ID of the investor            |
| PoolID          | INT          | ID of the investment pool     |
| InvestmentAmount| DECIMAL(10,2)| Amount invested by the investor |

5. **Transactions Table:**

| Field           | Type         | Description                   |
| --------------- | ------------ | ----------------------------- |
| TransactionID   | INT          | Unique Transaction ID         |
| PoolID          | INT          | ID of the investment pool     |
| InvestorID      | INT          | ID of the investor            |
| Amount          | DECIMAL(10,2)| Transaction amount             |
| TransactionType | ENUM         | Type of transaction (e.g., Deposit, Withdrawal) |
| TransactionDate | DATETIME     | Date and time of the transaction |
