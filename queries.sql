-- ====================================================================
-- AMAZON AOP BUSINESS ANALYST CASE STUDY: RETAIL OPERATIONS ANALYSIS
-- Target Database Schema: Retail_Operations_v2
-- Purpose: Extract Operational KPIs for Fulfillment Performance
-- ====================================================================

-- 1. EXECUTIVE METRICS BY PRODUCT CATEGORY
SELECT 
    Category,
    COUNT(OrderID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(COUNT(CASE WHEN DeliveryStatus = 'On-Time' THEN 1 END) * 100.0 / COUNT(OrderID), 2) AS On_Time_Delivery_Rate_Pct,
    ROUND(COUNT(CASE WHEN ReturnRequested = 'Yes' THEN 1 END) * 100.0 / COUNT(OrderID), 2) AS Return_Rate_Pct
FROM 
    orders
GROUP BY 
    Category
ORDER BY 
    Total_Orders DESC;

-- 2. REGIONAL SHIPPING EFFICIENCY & TRAFFIC BOTTLENECKS
SELECT 
    Region,
    COUNT(OrderID) AS Total_Fulfillment_Volume,
    ROUND(COUNT(CASE WHEN DeliveryStatus = 'Delayed' THEN 1 END) * 100.0 / COUNT(OrderID), 2) AS Regional_Delay_Rate_Pct,
    ROUND(COUNT(CASE WHEN DeliveryStatus = 'Cancelled' THEN 1 END) * 100.0 / COUNT(OrderID), 2) AS Regional_Cancellation_Rate_Pct
FROM 
    orders
GROUP BY 
    Region
ORDER BY 
    Regional_Delay_Rate_Pct DESC;

-- 3. DEEP DIVE: CRITICAL RETURN ANOMALIES
SELECT 
    OrderID,
    Category,
    Sales,
    Region,
    DeliveryStatus
FROM 
    orders
WHERE 
    ReturnRequested = 'Yes'
    AND Sales > 300.00
ORDER BY 
    Sales DESC
LIMIT 5;
