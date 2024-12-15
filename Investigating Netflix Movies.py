#!/usr/bin/env python
# coding: utf-8

# # Netflix 1990s Movie Analysis
# # Author: James Weaver

# # Section 1: Importing Libraries

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Set visualizations style

# In[3]:


sns.set(style="whitegrid")


# # Section 2: Load Dataset

# In[5]:


df = pd.read_csv("netflix_data.csv")


# # Preview the first 5 rows of the dataset

# In[7]:


print("Dataset Preview:")
df.head()


# # Section 3: Filter Movies Released in the 1990s

# In[8]:


df_90s = df[(df['release_year'] >= 1990) & (df['release_year'] <= 1999) & (df['type'] == 'Movie')]
print("\nNumber of Movies Released in the 1990s:", len(df_90s))


# # Section 4: Analyze Movie Durations
# # Find the most frequent movie duration

# In[9]:


duration_counts = df_90s['duration'].value_counts().head(5)
print("\nTop 5 Most Frequent Movie Durations in the 1990s:")
print(duration_counts)


# # Visualization: Most common movie durations

# In[10]:


plt.figure(figsize=(8, 6))
sns.barplot(x=duration_counts.index, y=duration_counts.values, palette="coolwarm")
plt.title("Top 5 Most Frequent Movie Durations (1990s)")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.show()


# # Section 5: Count Short Action Movies (<90 min)

# In[11]:


short_action_movies = df_90s[(df_90s['genre'] == 'Action') & (df_90s['duration'] < 90)]

print("\nNumber of Short Action Movies (Duration <90 min) in the 1990s:", len(short_action_movies))


# # Visualization: Short Action Movies by Country

# In[12]:


plt.figure(figsize=(10, 6))
sns.countplot(data=short_action_movies, x="country", order=short_action_movies['country'].value_counts().index)
plt.title("Short Action Movies by Country (1990s)")
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("Number of Movies")
plt.show()


# # Section 6: Summary Insights

# In[13]:


print("\n### Key Insights ###")
print("1. The most frequent movie duration in the 1990s was 94 minutes.")
print(f"2. There were {len(short_action_movies)} short action movies released in the 1990s.")
print("3. Short action movies were primarily produced in countries like the United States and Hong Kong.")


# # Save filtered 1990s movie data as a new CSV

# In[15]:


df_90s.to_csv("netflix_90s_movies.csv", index=False)
print("\nFiltered 1990s movie data saved as 'netflix_90s_movies.csv'.")

