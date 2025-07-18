# Homework 1:
# 
# import pandas as pd
# 
# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)
# 
# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
# Print the first 3 rows of the DataFrame
# Find the mean age of the individuals
# Select and print only the 'Name' and 'City' columns
# Add a new column 'Salary' with random salary values
# Display summary statistics of the DataFrame

import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df = pd.DataFrame(data)

def rename_func(col):
    if col == 'First Name':
        return 'first_name'
    elif col == 'Age':
        return 'age'
    else:
        return col  

df = df.rename(columns=rename_func)
df

# Print the first 3 rows of the DataFrame
print(df.head(3))

# Find the mean age of the individuals
df.age.mean()

# Select and print only the 'Name' and 'City' columns
df[["first_name","City"]]

# Add a new column 'Salary' with random salary values

import numpy as np

df['Salary'] = np.random.randint(50000, 100001, size=len(df))

# Display summary statistics of the DataFrame
df.describe()






# #Homework 2:
# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', 
# representing monthly sales and expenses data. Use below table.
# Month	Sales	Expenses
# Jan	5000	3000
# Feb	6000	3500
# Mar	7500	4000
# Apr	8000	4500
# Calculate and display the maximum sales and expenses.
# Calculate and display the minimum sales and expenses.
# Calculate and display the average sales and expenses.

# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', 
# representing monthly sales and expenses data. Use below table.
data = {
    "Month" : ["Jan", "Feb", "Mar", "Apr"],
    "Sales" : [5000, 6000, 7500, 8000],
    "Expenses" : [3000, 3500 , 4000, 4500]    
}
df = pd.DataFrame(data)

# Calculate and display the maximum sales and expenses.

print("Maksimal savdo:",df.Sales.max())
print("Maksimal xarajat:",df.Expenses.max())

# Calculate and display the minimum sales and expenses.
print("Minimal savdo:",df.Sales.min())
print("Minimal xarajat:",df.Expenses.min())

# Calculate and display the average sales and expenses.
print("O'rtacha savdo:",df.Sales.mean())
print("O'rtacha xarajat:",df.Expenses.mean())





# Homework 3:
# 
# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', 
#  monthly expenses for different categories. Use below table.
# Category	January	February	March	April
# Rent	1200	1300	1400	1500
# Utilities	200	220	240	250
# Groceries	300	320	330	350
# Entertainment	150	160	170	180
# Calculate and display the maximum expense for each category.
# Calculate and display the minimum expense for each category.
# Calculate and display the average expense for each category.
# In this task, use .set_index method to make Category column as index.
# 
# Try this code, learn it and use it in the task.
# 
# expenses.set_index('Category')


# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', 
#  monthly expenses for different categories. Use below table.
data = {
    "Category" : ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January" : [1200, 200, 300, 150],
    "February" : [1300, 220, 320, 160],
    "March" : [1400, 240, 330, 170],
    "April" : [1500, 250, 350, 180]
}

df = pd.DataFrame(data)
df = df.set_index("Category")
df


# Calculate and display the maximum expense for each category.
max_expenses = df.max(axis=1)
print(max_expenses)

# Calculate and display the minimum expense for each category.
min_expenses = df.min(axis=1)
print(min_expenses)

# Calculate and display the average expense for each category.
mean_expenses = df.mean(axis=1)
print(mean_expenses)
