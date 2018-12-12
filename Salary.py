import pandas as pd

# Read Salaries.csv as a dataframe
sal = pd.read_csv('Salaries.csv')
print(sal)

# Check the head of the dataframe
sal.head()

# Use the .info() to find ut hw many entries there are
sal.info()

# What is the average BasePay
(sal['BasePay'].mean())

# What is the highest amount of overtimePay
sal['BasePay'].max()

#JobTitle of JOSEPH DRIXOLL
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

# How much does Joseph Drixoll made
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

# Name of the highest paid person
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName']

# Average BasePay of all employee per year
sal.groupby('Year').mean()['BasePay']

# How many unique JobTitle are there
sal['JobTitle'].nunique()

# what are the top 5 most common jobs
sal['JobTitle'].value_counts().head(5)

# How many JobTitles were represented by one person in 2013
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

                                               
