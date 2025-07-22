# DataFrame 1: Student Grades
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
# Exercise 1: Calculate the average grade for each student.
df1["avg_grade"] = df1["Math"] + df1["English"] + df1["Science"]
each_student_mean = df1.groupby("Student_ID")["avg_grade"].mean()
print(each_student_mean)
# Exercise 2: Find the student with the highest average grade.
highest_grade = df1.nlargest(1,"avg_grade")
print(highest_grade)
# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1["total"] = df1["Math"] + df1["English"] + df1["Science"]
print(df1)
# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
# DataFrame 2: Sales Data
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product.
sum_of_each_p = df2[["Product_A","Product_B","Product_C"]].sum()
print(sum_of_each_p)
# Exercise 2: Find the date with the highest total sales.
df2["Total_sale"] = df2["Product_A"] + df2["Product_B"] + df2["Product_C"]
highest_total_sales =df2.nlargest(1,"Total_sale")
print(highest_total_sales)
# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
df2["Product_A_pct_change"] = df2["Product_A"].pct_change() * 100
df2["Product_B_pct_change"] = df2["Product_B"].pct_change() * 100
df2["Product_C_pct_change"] = df2["Product_C"].pct_change() * 100
print(df2)
# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
# DataFrame 3: Employee Information

import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
# Exercise 1: Calculate the average salary for each department.
avg_salary_by_dept = df3.groupby("Department")["Salary"].mean()
print(avg_salary_by_dept)
# Exercise 2: Find the employee with the most experience.
most_experienced = df3.loc[df3["Experience (Years)"].idxmax()]
print(most_experienced)
# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
min_salary = df3["Salary"].min()
df3["Salary Increase"] = ((df3["Salary"] - min_salary) / min_salary * 100).round(2)
print(df3)
# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
# DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
# Exercise 1: Calculate the total revenue from all orders.
total_revenue = df4["Total_Price"].sum()
print("Total Revenue:", total_revenue)
# Exercise 2: Find the most ordered product.
most_ordered_product = df4.groupby("Product")["Quantity"].sum().idxmax()
print("Most Ordered Product:", most_ordered_product)
print(df4.groupby("Product")["Quantity"].sum())
# Exercise 3: Calculate the average quantity of products ordered.
average_quantity = df4["Quantity"].mean()
print("Average Quantity Ordered:", round(average_quantity, 2))
# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
