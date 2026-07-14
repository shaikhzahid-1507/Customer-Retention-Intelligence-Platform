-- =====================================================
-- Customer Retention Intelligence Platform
-- File: 05_service_analysis.sql
-- Description: Service-wise Customer & Churn Analysis
-- =====================================================

USE customer_retention_db;

-- =====================================================
-- INTERNET SERVICE ANALYSIS
-- =====================================================

-- 1. Total Customers by Internet Service

SELECT
    InternetService,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY InternetService;


-- 2. Churned Customers by Internet Service

SELECT
    InternetService,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn='Yes'
GROUP BY InternetService;


-- 3. Churn Rate by Internet Service

SELECT
    InternetService,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY InternetService
ORDER BY Churn_Rate DESC;


-- 4. Average Monthly Charges by Internet Service

SELECT
    InternetService,
    ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charge
FROM customer_churn
GROUP BY InternetService;

-- =====================================================
-- PHONE SERVICE ANALYSIS
-- =====================================================

-- 5. Total Customers by Phone Service

SELECT
    PhoneService,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY PhoneService;


-- 6. Churn Rate by Phone Service

SELECT
    PhoneService,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY PhoneService;

-- =====================================================
-- MULTIPLE LINES ANALYSIS
-- =====================================================

-- 7. Customer Distribution

SELECT
    MultipleLines,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY MultipleLines;


-- 8. Churn Rate

SELECT
    MultipleLines,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY MultipleLines
ORDER BY Churn_Rate DESC;

-- =====================================================
-- ONLINE SECURITY ANALYSIS
-- =====================================================

SELECT
    OnlineSecurity,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY OnlineSecurity
ORDER BY Churn_Rate DESC;

-- =====================================================
-- ONLINE BACKUP ANALYSIS
-- =====================================================

SELECT
    OnlineBackup,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY OnlineBackup
ORDER BY Churn_Rate DESC;

-- =====================================================
-- DEVICE PROTECTION ANALYSIS
-- =====================================================

SELECT
    DeviceProtection,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY DeviceProtection
ORDER BY Churn_Rate DESC;

-- =====================================================
-- TECH SUPPORT ANALYSIS
-- =====================================================

SELECT
    TechSupport,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY TechSupport
ORDER BY Churn_Rate DESC;

-- =====================================================
-- STREAMING TV ANALYSIS
-- =====================================================

SELECT
    StreamingTV,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY StreamingTV
ORDER BY Churn_Rate DESC;

-- =====================================================
-- STREAMING MOVIES ANALYSIS
-- =====================================================

SELECT
    StreamingMovies,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY StreamingMovies
ORDER BY Churn_Rate DESC;