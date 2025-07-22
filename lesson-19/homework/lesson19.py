# TASK 1
# 
# Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.
# Identify the top-selling product in each category based on the total quantity sold.
# Find the date on which the highest total sales (quantity * price) occurred.


# Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.
# Ex1
import pandas as pd

sales_data = pd.read_csv("sales_data.csv")
sales_data["TotalSales"] = sales_data["Quantity"] * sales_data["Price"]
category_sales = sales_data.groupby("Category")["TotalSales"].sum()
print(category_sales)

# Ex2
import pandas as pd

sales_data = pd.read_csv("sales_data.csv")
category_sales = sales_data.groupby("Category")["Price"].mean()
print(category_sales)

# Ex3
sales_data = pd.read_csv("sales_data.csv")
sales_data["TotalSales"] = sales_data["Quantity"] * sales_data["Price"]
category_sales = sales_data.groupby("Category")["TotalSales"].max()
print(category_sales)



# TASK 2
# Group the data by CustomerID and filter out customers who have made less than 20 orders.
# Identify customers who have ordered products with an average price per unit greater than $120.
# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

# Ex1
import pandas as pd 

customer_orders = pd.read_csv("customer_orders.csv")
order_counts = customer_orders.groupby("CustomerID")["OrderID"].count()
order_counts[order_counts >= 20]

# Ex2
import pandas as pd

price_greter = customer_orders.groupby("Product")["Price"].mean() > 120
expensive_products = customer_orders.groupby("Product")["Price"].mean()
expensive_products = expensive_products[expensive_products > 120].index
customers_with_expensive_orders = customer_orders[customer_orders["Product"].isin(expensive_products)]["CustomerID"].unique()
customers_with_expensive_orders

# Ex3
import pandas as pd

total_quantity = customer_orders.groupby("Product")["Quantity"].sum()
customer_orders["Total_sum"] = customer_orders["Quantity"] * customer_orders["Price"]
total_price = customer_orders.groupby("Product")["Total_sum"].sum()
less_product = total_quantity < 5
less_product_mask = total_quantity < 5
less_product_quantity = total_quantity[less_product_mask]
less_product_price = total_price[less_product_mask]
result = pd.DataFrame({
    "TotalQuantity": less_product_quantity,
    "TotalPrice": less_product_price
})



# TASK 3
# "task\population.db" sqlite database has population table.
# "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;
# Calculate the same measures in each State
# Note: Use SQL only to select data from database. All the other calculations should be done in python.
import sqlite3 as sq
import pandas as pd


conn = sq.connect("population.db")


population_df = pd.read_sql_query("SELECT * FROM population", conn)
print(population_df)
salary_band_df = pd.read_excel("population_salary_analysis.xls")
salary_band_df

population_df.groupby("salary")
