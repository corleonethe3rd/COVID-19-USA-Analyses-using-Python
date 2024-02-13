#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#importing csv files and rename the header
df = pd.read_csv(r"C:\Users\solop\Downloads\data sets\us-counties-recent.csv")


# In[4]:


df.info()


# In[5]:


#find any missing value
print ("missing values",df.isnull().values.any())


# In[6]:


df.dropna(axis=0)


# In[7]:


#check for duplicates 
df.duplicated().any()


# In[8]:


pd.set_option('display.float_format',lambda x:'%.2f' %x)


# In[9]:


# Convert 'date' column to datetime type
df['date'] = pd.to_datetime(df['date'])


# In[10]:


# Aggregate data by date
agg_data = df.groupby('date').agg({'cases':'sum', 'deaths':'sum'}).reset_index()


# In[16]:


# Plotting
plt.figure(figsize=(12, 6))
plt.plot(agg_data['date'], agg_data['cases'], label='Cases', color='blue')
plt.plot(agg_data['date'], agg_data['deaths'], label='Deaths', color='red')
plt.title('COVID-19 Cases and Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Number')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[12]:


# Identifying the top 5 counties with the highest number of cases and deaths
top_cases = df.groupby(['county', 'state']).agg({'cases':'max'}).reset_index().nlargest(5, 'cases')
top_deaths = df.groupby(['county', 'state']).agg({'deaths':'max'}).reset_index().nlargest(5, 'deaths')

# Plotting the top 5 counties with the highest cases
plt.figure(figsize=(10, 5))
plt.bar(top_cases['county'] + ', ' + top_cases['state'], top_cases['cases'], color='blue')
plt.title('Top 5 Counties with Highest COVID-19 Cases')
plt.xlabel('County, State')
plt.ylabel('Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting the top 5 counties with the highest deaths
plt.figure(figsize=(10, 5))
plt.bar(top_deaths['county'] + ', ' + top_deaths['state'], top_deaths['deaths'], color='red')
plt.title('Top 5 Counties with Highest COVID-19 Deaths')
plt.xlabel('County, State')
plt.ylabel('Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[17]:


# Summarizing total cases and deaths by state
state_summary = df.groupby('state').agg({'cases':'sum', 'deaths':'sum'}).reset_index().sort_values(by='cases', ascending=False)

# Plotting total cases by state
plt.figure(figsize=(15, 8))
plt.bar(state_summary['state'], state_summary['cases'], color='blue')
plt.title('Total COVID-19 Cases by State')
plt.xlabel('State')
plt.ylabel('Total Cases')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Plotting total deaths by state
plt.figure(figsize=(15, 8))
plt.bar(state_summary['state'], state_summary['deaths'], color='red')
plt.title('Total COVID-19 Deaths by State')
plt.xlabel('State')
plt.ylabel('Total Deaths')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[20]:


import seaborn as sns

# Distribution of cases
plt.figure(figsize=(10, 6))
sns.histplot(df['cases'], bins=50, color='blue', kde=True)
plt.title('Distribution of COVID-19 Cases Across Counties')
plt.xlabel('Cases')
plt.ylabel('Frequency')
plt.xscale('log')
plt.tight_layout()
plt.show()

# Distribution of deaths
plt.figure(figsize=(10, 6))
sns.histplot(df['deaths'], bins=50, color='red', kde=True)
plt.title('Distribution of COVID-19 Deaths Across Counties')
plt.xlabel('Deaths')
plt.ylabel('Frequency')
plt.xscale('log')
plt.tight_layout()
plt.show()


# In[21]:


# Merging the top cases and deaths dataframes to calculate the ratio
top_combined = pd.merge(top_cases, top_deaths, on=['county', 'state'], suffixes=('_cases', '_deaths'))
top_combined['case_death_ratio'] = top_combined['cases'] / top_combined['deaths']

# Sorting by case_death_ratio
top_combined_sorted = top_combined.sort_values(by='case_death_ratio', ascending=False)

# Plotting the case to death ratio
plt.figure(figsize=(10, 5))
plt.bar(top_combined_sorted['county'] + ', ' + top_combined_sorted['state'], top_combined_sorted['case_death_ratio'], color='green')
plt.title('Case to Death Ratio in Top 5 Most Affected Counties')
plt.xlabel('County, State')
plt.ylabel('Case to Death Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




