-- =====================================================
-- Customer Retention Intelligence Platform
-- File: 04_contract_analysis.sql
-- Description: Contract-wise Customer & Churn Analysis
-- =====================================================

USE customer_retention_db;

-- =====================================================
-- CONTRACT ANALYSIS
-- =====================================================

-- 1. Total Customers by Contract Type

SELECT
    Contract,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY Contract
ORDER BY total_customers DESC;


-- =====================================================
-- 2. Churned Customers by Contract Type
-- =====================================================

SELECT
    Contract,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE Churn = 'Yes'
GROUP BY Contract
ORDER BY churned_customers DESC;


-- =====================================================
-- 3. Churn Rate by Contract Type
-- =====================================================

SELECT
    Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC;


-- =====================================================
-- 4. Average Monthly Charges by Contract
-- =====================================================

SELECT
    Contract,
    ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charge
FROM customer_churn
GROUP BY Contract
ORDER BY Avg_Monthly_Charge DESC;


-- =====================================================
-- 5. Average Tenure by Contract
-- =====================================================

SELECT
    Contract,
    ROUND(AVG(tenure),2) AS Avg_Tenure
FROM customer_churn
GROUP BY Contract
ORDER BY Avg_Tenure DESC;