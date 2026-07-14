-- =====================================================
-- Customer Retention Intelligence Platform
-- File: 03_demographic_analysis.sql
-- Description: Demographic Analysis
-- =====================================================

USE customer_retention_db;

-- =====================================================
-- GENDER ANALYSIS
-- =====================================================

-- 1. Total Customers by Gender

SELECT
    gender,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY gender;


-- 2. Churned Customers by Gender

SELECT
    gender,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn = 'Yes'
GROUP BY gender;


-- 3. Churn Rate by Gender

SELECT
    gender,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY gender
ORDER BY Churn_Rate DESC;


-- =====================================================
-- SENIOR CITIZEN ANALYSIS
-- =====================================================

-- 4. Total Customers by Senior Citizen

SELECT
    SeniorCitizen,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY SeniorCitizen;


-- 5. Churned Customers by Senior Citizen

SELECT
    SeniorCitizen,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn='Yes'
GROUP BY SeniorCitizen;


-- 6. Churn Rate by Senior Citizen

SELECT
    SeniorCitizen,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY SeniorCitizen
ORDER BY Churn_Rate DESC;


-- =====================================================
-- PARTNER ANALYSIS
-- =====================================================

-- 7. Total Customers by Partner Status

SELECT
    Partner,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY Partner;


-- 8. Churned Customers by Partner Status

SELECT
    Partner,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn='Yes'
GROUP BY Partner;


-- 9. Churn Rate by Partner Status

SELECT
    Partner,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY Partner
ORDER BY Churn_Rate DESC;


-- =====================================================
-- DEPENDENTS ANALYSIS
-- =====================================================

-- 10. Total Customers by Dependents

SELECT
    Dependents,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY Dependents;


-- 11. Churned Customers by Dependents

SELECT
    Dependents,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn='Yes'
GROUP BY Dependents;


-- 12. Churn Rate by Dependents

SELECT
    Dependents,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY Dependents
ORDER BY Churn_Rate DESC;