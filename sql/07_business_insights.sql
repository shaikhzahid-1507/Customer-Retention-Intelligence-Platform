/*
=========================================================
Project : Customer Retention Intelligence Platform
Author  : Zahid Shaikh
Database: customer_retention_db
Dataset : customer_churn
=========================================================
*/

USE customer_retention_db;

-- =====================================================
-- SECTION 1 : CUSTOMER OVERVIEW
-- =====================================================
SELECT COUNT(*) AS total_customers
FROM customer_churn;

SELECT COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn = 'Yes';

SELECT COUNT(*) AS active_customers
FROM customer_churn
WHERE Churn = 'No';

SELECT
ROUND(
COUNT(CASE WHEN Churn='Yes' THEN 1 END) * 100.0 / COUNT(*),
2
) AS churn_rate
FROM customer_churn;

SELECT
    gender,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY gender;

SELECT
    gender,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn = 'Yes'
GROUP BY gender;

SELECT
    SeniorCitizen,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY SeniorCitizen;

SELECT
    SeniorCitizen,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn = 'Yes'
GROUP BY SeniorCitizen;

SELECT
    Partner,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY Partner;

SELECT
    Partner,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn = 'Yes'
GROUP BY Partner;