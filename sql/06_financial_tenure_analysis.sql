-- =====================================================
-- Customer Retention Intelligence Platform
-- File: 07_financial_tenure_analysis.sql
-- Description: Financial & Tenure Analysis
-- =====================================================

USE customer_retention_db;

-- =====================================================
-- MONTHLY CHARGES ANALYSIS
-- =====================================================

-- 1. Average Monthly Charges

SELECT
    ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customer_churn;

-- =====================================================
-- 2. Average Monthly Charges by Churn Status
-- =====================================================

SELECT
    Churn,
    ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customer_churn
GROUP BY Churn;

-- =====================================================
-- TOTAL CHARGES ANALYSIS
-- =====================================================

-- 3. Average Total Charges

SELECT
    ROUND(AVG(TotalCharges),2) AS Avg_Total_Charges
FROM customer_churn;

-- =====================================================
-- 4. Average Total Charges by Churn Status
-- =====================================================

SELECT
    Churn,
    ROUND(AVG(TotalCharges),2) AS Avg_Total_Charges
FROM customer_churn
GROUP BY Churn;

-- =====================================================
-- TENURE ANALYSIS
-- =====================================================

-- 5. Average Tenure

SELECT
    ROUND(AVG(tenure),2) AS Avg_Tenure
FROM customer_churn;

-- =====================================================
-- 6. Average Tenure by Churn Status
-- =====================================================

SELECT
    Churn,
    ROUND(AVG(tenure),2) AS Avg_Tenure
FROM customer_churn
GROUP BY Churn;

-- =====================================================
-- 7. Tenure Distribution
-- =====================================================

SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS Tenure_Group,
    COUNT(*) AS Total_Customers
FROM customer_churn
GROUP BY Tenure_Group
ORDER BY Total_Customers DESC;

-- =====================================================
-- 8. Churn Rate by Tenure Group
-- =====================================================

SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS Tenure_Group,

    COUNT(*) AS Total_Customers,

    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,

    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate

FROM customer_churn
GROUP BY Tenure_Group
ORDER BY Churn_Rate DESC;

-- =====================================================
-- 9. Total Revenue by Churn Status
-- =====================================================

SELECT
    Churn,
    ROUND(SUM(TotalCharges),2) AS Total_Revenue
FROM customer_churn
GROUP BY Churn;

-- =====================================================
-- 10. Top 10 Highest Paying Customers
-- =====================================================

SELECT
    customerID,
    MonthlyCharges,
    TotalCharges,
    tenure,
    Contract,
    InternetService
FROM customer_churn
ORDER BY TotalCharges DESC
LIMIT 10;