 
import pandas as pd
import pandas_profiling

online_sales = pd.read_csv('Onlinesales_info.csv')
customers_data = pd.read_csv('Customer_info.csv')
discount_coupon = pd.read_csv('Discount_info.csv')
marketing_spend = pd.read_csv('Marketing_info.csv')
tax_amount = pd.read_csv('Tax_info.csv')
profile = online_sales.profile_report()
profile

