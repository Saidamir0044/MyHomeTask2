import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')

# Find all questions that were created before 2014
# Find all questions with a score more than 50
# Find all questions with a score between 50 and 100
# Find all questions answered by Scott Boston
# Find all questions answered by the following 5 users
# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
# Find all questions that are not answered by Scott Boston

# Find all questions that were created before 2014
filter_data = df.creationdate < "2014-01-01"
df[filter_data]
# Find all questions with a score more than 50
filter_score = df.score > 50
df[filter_score]
# Find all questions with a score between 50 and 100
filter_score2 = df.score < 100
comb_filt = filter_score & filter_score2
df[comb_filt]
# Find all questions answered by Scott Boston
filter_name = df.ans_name == "Scott Boston"
df[filter_name]
# Find all questions answered by the following 5 users
# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
filter_data1 = df.creationdate > "2014-03-31"
filter_data2 = df.creationdate < "2014-10-01"
filter_name1 = df.ans_name == "Unutbu"
filter_score3 = df.score < 5
comb_filt1 = filter_data1&filter_data2&filter_name1&filter_score3
df[comb_filt1]
# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
filter_score4 = df.score > 5
filter_score5 = df.score < 10
filter_viewcount = df.viewcount > 10000
comb_filt2 = filter_score4&filter_score5
comb_filt3 = comb_filt2 | filter_viewcount
df[comb_filt3]
# Find all questions that are not answered by Scott Boston
filter_name = df.ans_name != "Scott Boston"
df[filter_name]




titanic_df = pd.read_csv("titanic.csv")

# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.# 
# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).# 
# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.# 
# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive. 
# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.# 
# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers. 
# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

titanic_df.columns
# Ex1
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]
# Ex2
fare_above_100 = titanic_df[titanic_df['Fare'] > 100]
# Ex3
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
# Ex4
embarked_c_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
# Ex5
with_family = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
# Ex6
young_didnt_survive = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
# Ex7
cabin_and_highfare = titanic_df[
    titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)
]
# Ex8
odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]
# Ex9
ticket_counts = titanic_df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
unique_ticket_passengers = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]
# Ex10
miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Sex'] == 'female')
]
