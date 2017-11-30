
# coding: utf-8

# In[2]:


import pandas as pd
from datetime import datetime


# In[62]:


austin_data = pd.read_csv("../raw data/Austin.csv")
louisville_data = pd.read_csv("../raw data/Louisville.csv")


# In[4]:


louisville_data.head()


# In[65]:


louisville_data['Time from Intake to Outcome']=''

for row in range(0,len(louisville_data)):
    print(row)
    try: 
        intake_date=str(louisville_data.iloc[row,2])
        outcome_date=str(louisville_data.iloc[row,15])                 
        intake_datetime = datetime.strptime(intake_date, '%Y-%m-%d %H:%M:%S')
        outcome_datetime = datetime.strptime(outcome_date, '%Y-%m-%d %H:%M:%S')                 
        time_to_outcome=outcome_datetime-intake_datetime
        louisville_data.iloc[row,22]=time_to_outcome
    except ValueError:
        continue


# In[66]:


louisville_data.head()


# In[68]:


louisville_data.to_csv('../raw data/Louisville_with_time_deltas.csv')

