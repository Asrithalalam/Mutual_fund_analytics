--1.Top 5 funds by AUM--
SELECT fund_house,SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

--2.Average NAV per Month
SELECT strftime('%Y-%m', date) AS month,AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

--3.SIP YoY Growth
SELECT strftime('%Y', transaction_date) AS year,SUM(amount_inr) AS sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'  
GROUP BY year
ORDER BY year;

--4.Transactions by State
SELECT state, COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;

--5.Funds with Expense Ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

--6.Top 5 funds by 1-Year Return
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

--7.Average Transaction Amount
SELECT AVG(amount_inr) AS average_transaction_amount    
FROM fact_transactions;

--8.Total Redemption Amount
SELECT SUM(amount_inr) AS total_redemption_amount
FROM fact_transactions
WHERE transaction_type = 'Redemption';

--9.Transactions by Gender
SELECT gender, COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY gender;

--10.Average Return by Category
SELECT category, AVG(return_5yr_pct) AS average_5yr_return
FROM fact_performance
GROUP BY category
ORDER BY average_5yr_return DESC;