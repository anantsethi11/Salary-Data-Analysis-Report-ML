import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

import os

df = pd.read_csv('D:/python/salaries.csv')
df.isnull().sum()
df["experience_level"].unique(), df["employment_type"].unique()
df['company_location'].unique(), len(df['company_location'].unique())
df_sal = df.groupby('company_location')['salary'].mean().reset_index()
currency_info = df.groupby('company_location')['salary_currency'].first().reset_index()

result = pd.merge(df_sal, currency_info, on='company_location', how='left')

df["job_title"].unique()
len(df["job_title"].unique())
df_dropped = df.drop(columns=["salary", "salary_currency"])

exp_df = df.groupby('experience_level')['salary_in_usd']

exp_df.mean()
exp_df.median()

jobtype_df = df.groupby('employment_type')['salary_in_usd']
jobtype_df.describe()
jobtype_df.median()
jobtype_df.mean()
jobtitle_df = df.groupby('job_title')['salary_in_usd']
pd.set_option('display.max_rows', None)
jobtitle_df1 = jobtitle_df.mean().reset_index()
jobtitle_df2 = jobtitle_df.median().reset_index()
jobtitle_df1
jobtitle_df2
top_titles_mean = jobtitle_df1.sort_values(by='salary_in_usd', ascending=False).head(20)
top_titles_median = jobtitle_df2.sort_values(by='salary_in_usd', ascending=False).head(20)
top_titles_mean
location_sal_df = df.groupby('remote_ratio')['salary_in_usd']
location_sal_df.mean(), location_sal_df.median()
plt.figure(figsize=(7, 5))

sns.barplot(x = 'experience_level', y = 'salary_in_usd', data=df, palette = 'muted')

plt.xlabel("Experience level of employee")
plt.ylabel("Salary of Employ in USD")
plt.title("Salary in USD by Experience Level")

plt.show()
mean_salary = jobtype_df.mean().reset_index()
median_salary = jobtype_df.median().reset_index()

fig, axes = plt.subplots(1 , 2, figsize=(14, 5))

sns.barplot(ax=axes[0], x = 'employment_type', y = 'salary_in_usd', data=mean_salary, palette='flare')

axes[0].set_title("Mean Salary in USD by Employment Type")
axes[0].set_xlabel("Employment Type of Employee")
axes[0].set_ylabel("Mean Salary in USD")

sns.barplot(ax=axes[1], x='employment_type', y='salary_in_usd', data=mean_salary, palette='flare')
axes[1].set_title("Median Salary in USD by Employment Type")
axes[1].set_xlabel("Employment Type of Employee")
axes[1].set_ylabel("Median Salary in USD")

plt.tight_layout()
plt.show()
plt.figure(figsize=(11, 6))

sns.barplot(x = 'remote_ratio', y = 'salary_in_usd', data=df, palette = 'flare')

plt.xlabel("Remote Ratio (0 for no remote work)")
plt.ylabel("Salary of Employ in USD")
plt.title("Salary in USD by Job Remote Ratio")

plt.show()
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

sns.barplot(ax=axes[0], x='job_title', y='salary_in_usd', data=top_titles_mean, palette='flare')
axes[0].set_title("Salary in USD (mean) by top 20 Job Titles")
axes[0].set_xlabel("Job Title")
axes[0].set_ylabel("Mean Salary in USD")
axes[0].tick_params(axis='x', rotation=80)

sns.barplot(ax=axes[1], x='job_title', y='salary_in_usd', data=top_titles_median, palette='flare')
axes[1].set_title("Salary in USD (median) by top 20 Job Titles")
axes[1].set_xlabel("Job Title")
axes[1].set_ylabel("Median Salary in USD")
axes[1].tick_params(axis='x', rotation=80)

plt.tight_layout()

plt.show()