# E-Commerce ETL Pipeline and Business Intelligence Dashboard

## Project Overview

This project implements an end-to-end data engineering and analytics pipeline using Python, MySQL, SQL, and Power BI. It processes a large e-commerce dataset through data extraction, cleaning, validation, transformation, database loading, and business intelligence reporting.

The project demonstrates how raw transactional data can be converted into structured data suitable for analysis and decision-making.

> **Dataset note:** The source data represents general e-commerce transactions, not verified subscription-box transactions. The project title reflects the original project concept; subscription-specific behavior is not claimed by the current dataset.

## Objectives

* Build a repeatable ETL workflow using Python.
* Clean and validate raw transactional data.
* Store structured data in a MySQL database.
* Design related tables for customers, products, payments, dates, and sales.
* Perform SQL-based business analysis.
* Develop a Power BI dashboard to explore transaction value, order volume, customers, and product categories.

## Technology Stack

* **Python** — ETL processing and data validation
* **Pandas** — Data manipulation and cleaning
* **MySQL** — Relational database and data warehouse
* **SQL** — Business analysis and data quality checks
* **Power BI** — Data visualization and dashboard reporting
* **Git and GitHub** — Version control

## Pipeline Architecture

```text
Raw E-Commerce Dataset (CSV)
            |
            v
     Python ETL Pipeline
   Extract, Clean, Validate,
       and Transform
            |
            v
       MySQL Database
            |
            v
       SQL Analysis
            |
            v
      Power BI Dashboard
```

## ETL Workflow

### 1. Extract

Load the source CSV dataset into Python for processing.

### 2. Clean

* Standardize column names and text fields.
* Convert date and numeric columns to appropriate data types.
* Handle missing values in important fields.
* Prepare a cleaned dataset for validation and loading.

### 3. Validate

Check for duplicate item identifiers, missing required fields, invalid dates, negative prices, and invalid quantities.

### 4. Load

Load the processed data into MySQL tables.

### 5. Analyze and Visualize

Use SQL queries to examine transaction value, orders, customers, payment methods, product categories, order statuses, and monthly trends. Present selected results through Power BI.

## Database Design

The MySQL database contains five related tables:

| Table       | Purpose                                             |
| ----------- | --------------------------------------------------- |
| `customers` | Customer identifiers and customer-since information |
| `products`  | Product identifiers, SKUs, and categories           |
| `payments`  | Payment method lookup                               |
| `dates`     | Transaction dates and calendar attributes           |
| `sales`     | Item-level transaction records and measures         |

The `sales` table stores transaction line items, so one order may contain multiple records.

## Data Validation Results

The processed dataset contained:

* **584,524** item-level records
* **408,782** distinct order identifiers
* **115,327** distinct customer identifiers in the loaded sales data, including the unknown-customer placeholder
* **16** product categories
* **18** payment methods

Validation checks reported no duplicate item identifiers, negative prices, invalid quantities, or invalid transaction dates.

These results describe the processed dataset and should not be interpreted as proof that every business field is complete or accurate.

## Key Analytical Areas

The SQL analysis covers:

* Recorded transaction value and order volume
* Monthly transaction trends
* Transaction value by product category
* Orders by payment method and status
* Product-level transaction value
* Customer purchasing activity
* Discounts and canceled/refunded transactions

**Important:** Recorded transaction value includes transactions with canceled and refunded statuses. It should not be interpreted as realized revenue without additional status-aware business rules.

## Project Structure

```text
Subscription_Box_ETL/
├── data/
│   ├── raw/          # Source data (excluded from Git)
│   ├── staging/      # Cleaned data (excluded from Git)
│   └── rejected/
├── src/
│   ├── inspect_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   ├── test_mysql.py
│   ├── load_customers.py
│   ├── load_products.py
│   ├── load_payments.py
│   ├── load_dates.py
│   └── load_sales.py
├── sql/
├── logs/
├── reports/
├── dashboard/
└── README.md
```

## Setup

1. Install Python and MySQL.
2. Clone this repository.
3. Create and activate a Python virtual environment.
4. Install the required packages, including `pandas` and `mysql-connector-python`.
5. Create the MySQL database and required tables.
6. Obtain the source dataset from its original provider and place it in `data/raw/`.
7. Configure database credentials using environment variables rather than hardcoding passwords.
8. Run the ETL scripts in the appropriate order.
9. Connect Power BI to the MySQL database and open or recreate the dashboard.

The raw and cleaned datasets are excluded from GitHub because of their size. You must obtain the source dataset separately.

## Security

Database credentials must not be committed to the repository. Configure the `MYSQL_PASSWORD` environment variable locally before running scripts that connect to MySQL. Never publish database passwords, private credentials, or sensitive data.

## Limitations and Future Improvements

* Automate the complete ETL workflow with a single entry point or scheduler.
* Add structured logging and error handling.
* Improve repeatable loading and duplicate-run handling.
* Add automated tests for data quality and database relationships.
* Add order-level metrics with clearly defined business rules.
* If the project is extended to subscription analytics, introduce a clearly documented subscription dataset or explicitly labeled synthetic subscription records.
* Add screenshots of the Power BI dashboard and database model.

## Conclusion

This project demonstrates a practical data engineering workflow, from raw CSV processing through relational database storage and SQL analysis to Power BI reporting. It provides a foundation for further development in automated analytics and data warehousing.
