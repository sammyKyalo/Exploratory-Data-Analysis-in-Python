#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Data manipulation 
import pandas as pd
import numpy as np

#Data visualization
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')
#styling
plt.style.use("ggplot")
rcParams['figure.figsize'] = (12,6)


# In[4]:


#Importing cancer patient dataset

df = pd.read_csv("G:\cancer-patient-datasets.csv")



# In[10]:


#provides the first five rows of the dataset
df.head()


# In[11]:


#it provides purely descriptive information about the dataset.
df.describe()


# In[14]:


#.info() gives us a shorter summary of our dataset. It returns us information about the data type, non-null values and memory usage. 
df.info()


# In[ ]:


#We do not have missing values in th dataset.


# In[ ]:


#Data Cleaning


# In[7]:


#checking for duplicates
#this will print us the number of duplicated rows in our dataset
df.duplicated().sum()


# In[20]:


#getting descriptive statistic of a single variable
df.Gender.describe()


# In[12]:


df["Gender"].unique()


# In[15]:


#creating another dataframe
#data provided is for people whose age is 30 yrs and above
df2 = df[df["Age"]> 30]


# In[17]:


df2.head()


# In[47]:


#Drawing Boxplots to check outliers
df.boxplot("Age","Gender")
plt.show()


# In[42]:


#Age has an outlier. However, they are not an extreme outlier.


# In[49]:


df.boxplot("Alcohol use")
plt.show()


# In[50]:


#No outliers


# In[51]:


df.boxplot("Dust Allergy")
plt.show()


# In[52]:


#No outliers


# In[56]:


df["Dust Allergy"].unique()


# In[58]:


np.array(["Dust Allergy", "Age"], dtype=object)


# In[65]:


df["Dust Allergy"].hist()
plt.title("Dust Allergy Distribution")
plt.show()


# In[5]:


df["Age"].hist()
plt.title("Age Distribution")
plt.show()


# In[16]:


#Reading data from a single column in a dataframe
Gender = df.Gender


# In[17]:


print(Gender)


# In[22]:


#if a variable has spaces, use square brackets
Dust_allergy = df['Dust Allergy']


# In[23]:


print(Dust_allergy)


# In[ ]:





# In[ ]:




