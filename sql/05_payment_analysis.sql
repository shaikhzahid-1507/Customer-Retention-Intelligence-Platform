-- =====================================================
-- Customer Retention Intelligence Platform
-- File: 06_payment_analysis.sql
-- Description: Payment Method & Paperless Billing Analysis
-- =====================================================

USE customer_retention_db;

-- =====================================================
-- PAYMENT METHOD ANALYSIS
-- =====================================================

-- 1. Total Customers by Payment Method

SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Total_Customers DESC;


-- =====================================================
-- 2. Churned Customers by Payment Method
-- =====================================================

SELECT
    PaymentMethod,
    COUNT(*) AS Churned_Customers
FROM customer_churn
WHERE Churn = 'Yes'
GROUP BY PaymentMethod
ORDER BY Churned_Customers DESC;


-- =====================================================
-- 3. Churn Rate by Payment Method
-- =====================================================

SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;


-- =====================================================
-- PAPERLESS BILLING ANALYSIS
-- =====================================================

-- 4. Total Customers by Paperless Billing

SELECT
    PaperlessBilling,
    COUNT(*) AS Total_Customers
FROM customer_churn
GROUP BY PaperlessBilling;


-- =====================================================
-- 5. Churned Customers by Paperless Billing
-- =====================================================

SELECT
    PaperlessBilling,
    COUNT(*) AS Churned_Customers
FROM customer_churn
WHERE Churn='Yes'
GROUP BY PaperlessBilling;


-- =====================================================
-- 6. Churn Rate by Paperless Billing
-- =====================================================

SELECT
    PaperlessBilling,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY PaperlessBilling
ORDER BY Churn_Rate DESC;


-- =====================================================
-- 7. Average Monthly Charges by Payment Method
-- =====================================================

SELECT
    PaymentMethod,
    ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Avg_Monthly_Charges DESC;


-- =====================================================
-- 8. Average Total Charges by Payment Method
-- =====================================================

SELECT
    PaymentMethod,
    ROUND(AVG(TotalCharges),2) AS Avg_Total_Charges
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Avg_Total_Charges DESC;