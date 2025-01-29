import pandas as pd

#Create a DataFreame from a dictionary
data = {
    "Name" : ["Alice", "Bob", "Charlie"],
    "Age" : [25, 30, 35], 
    "City" : ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

#Read data from csv file
#(Assume 'data.csv' exists in the current directory)
#df = pd.read_csv("data.csv")

#Display the first few rows of the DataFrame
print("\nFirst 2 rows:")
print(df.head(2))

#Filter rows where Age > 25
filtered_df = df[df["Age"] > 25]
print("\nFiltered DataFrame:")
print(filtered_df)

#Add a new column
df["Score"] = [85, 90, 88]
print("\nDataFrame with new column:")
print(df)

#Save the DataFrame to a CSV file
df.to_csv("output.csv", index = False)
print("\nData saved to output.csv")

import pandas as pd
import numpy as np
data={
     "Name":["Alice","Bob","Charlie","David"],
     "Age":[25,np.nan,35,40],
     "City":["New York","Los Angeles","Chicago",None],

}
df=pd.DataFrame(data)
print("Original Dataframe:")
print(df)

# fill missing values
df["Age"].fillna(df["Age"].mean(),inplace=True)
df["City"].fillna("Unknown", inplace = True)
print("\nDataFrame after filling missing values:")
print(df)

#Drop rows with missing values
df = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df)

import panda as pd
data={
    "Department":["HR","IT","HR","IT","Finanace"],
    "Employee":["Alice","Bob","Charlie","David","Eve"],
    "Salary":[50000,70000,45000,80000,60000]
}
df=pd.DataFrame(data)
# Group by department and calculate the average salary
avg_salary=df.groupby("Department")["Salary"].mean()
print("Average salary by departmenrt:")
print(avg_salary)

data1={
    "ID":[2,3,4],
    "Score":[85,90,98],
}
data2={
    "ID":[2,3,4],
    "Score":[85,90,88]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
# merge the two Dtata Frame on the ID Column
merge_df=pd.merge(df1,df2,on="ID",how="inner")
print("Merged DataFrame:")
print(merge_df)

data={
     "Name":["Alice","Bob","Charlie","David"],
     "Age":[85,92,88,75]
}
df=pd.DataFrame(data)
# Sort by Score in descending order
sorted_df=df.sort_value( by="Score",ascending=False)
print("DataFrame sorted by Score")
print(sorted_df)
# Add a rank column
df["Rank"]=df["Score"].rank(ascending=False)
print("\nDataFrame with Rank:")
print(df)


import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Product': ['Product A', 'Product B', 'Product C'],
    'Price': [10, 20, 15],
    'Quantity': [5, 2, 4]
}
df = pd.DataFrame(data)

# Step 2: Add the Total column
df['Total'] = df['Price'] * df['Quantity']

# Step 3: Save to a CSV file
df.to_csv('products.csv', index=False)
print("DataFrame saved to 'products.csv'")


# Birthday Email Automator
# Objective: Send automated birthday wishes to friends and family.
# Tasks:
# Use a CSV file or dictionary to store names, birthdays, and email addresses.
# Check the current date and match it to birthdays.
# Use smtplib to send a personalized birthday wish email.
# Automate the script to run daily with schedule.







