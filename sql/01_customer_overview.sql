-- =====================================================
-- Customer Retention Intelligence Platform
-- File: 02_customer_overview.sql
-- Description: Basic customer overview and churn statistics
-- =====================================================

USE customer_retention_db;

-- =====================================================
-- 1. Total Customers
-- =====================================================

SELECT COUNT(*) AS total_customers
FROM customer_churn;

-- =====================================================
-- 2. Churned Customers
-- =====================================================

SELECT COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn = 'Yes';

-- =====================================================
-- 3. Active Customers
-- =====================================================

SELECT COUNT(*) AS active_customers
FROM customer_churn
WHERE Churn = 'No';

-- =====================================================
-- 4. Overall Churn Rate (%)
-- =====================================================

SELECT
    ROUND(
        COUNT(CASE WHEN Churn = 'Yes' THEN 1 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM customer_churn;

-- =====================================================
-- 5. Verify Total Rows
-- =====================================================

SELECT COUNT(*) AS total_rows
FROM customer_churn;

-- =====================================================
-- 6. Display First 10 Records
-- =====================================================

SELECT *
FROM customer_churn
ORDER BY customerID
LIMIT 10;