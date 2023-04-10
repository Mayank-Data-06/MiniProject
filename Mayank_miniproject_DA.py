#!/usr/bin/env python
# coding: utf-8

# # Data Analysis

# 

# [CSV File](https://drive.google.com/file/d/1QlkP6X8MVxiKvXcKwcVvshxfFiQQK2a_/view?usp=share_link)

# #Q1. Find the number of episodes?
# 
# #Q2. Max, min , mean of asked amount,asked equity, asked valuation? 
# 
# #Q3. Max & Min asked- equity,asked-valuation and asked amount episode-wise? 
# 
# #Q4. Brand names in which 2 ,3 or 4 sharks are invested? 
# 
# #Q5. Episode wise minimum and maximum no. of sharks invested? 
# 
# #Q6. Find the brands in which only ashneer invested. 
# 
# #Q7. Brand names who ask for 1 crore and got a deal what was the deal amount? 
# 
# #Q8. Brand names where deal equity is between 1 to 50? 
# 
# #Q9. Find the number of brands participated in each episode? 
# 
# #Q10. How many sharks participated in this show and What were their names? 
# 
# #Q11. Find appearance of each sharks? 
# 
# #Q12. How many brands were present? 
# 
# #Q13. How many times each shark invested the deal? 
# 
# #Q14. Find the most attracted ideas accepted by sharks ?
# 
# #Q15. Find the total number of amount invested in this show? 
# 
# #Q16 Above 50% Equity taken by the shark in which brand
# 
# #Q17 what more insights you can gain from the dataset
# 
# Solution of each question has to found using coding only. Document your findings. Upload the notebook on github. In the repository add a Readme file showcase your insights from the project.   

# - what insights you have gained

# In[64]:


#Q1. Find the number of episodes?
import pandas as pd
import numpy as np
import statistics as stats
import os
os.getcwd()
os.chdir('C:\\Users\\sa\\Desktop\\basics_python\\Mini Project DA')
df=pd.read_csv('C:\\Users\\sa\\Desktop\\basics_python\\Mini Project DA\\DA_Shark_Tank_India.csv')
print("Number of episodes are", len(df['episode_number'].unique()))


# In[71]:


#Q2. Max, min , mean of asked amount,asked equity, asked valuation?
print("Mean, median and mode of asked amount are- ", round(np.mean(df['pitcher_ask_amount']),2)," , ", np.median(df['pitcher_ask_amount'])," , ",stats.mode(df['pitcher_ask_amount']))
print("Mean, median and mode of asked equity are- ", round(np.mean(df['ask_equity']),2)," , ", np.median(df['ask_equity'])," , ",stats.mode(df['ask_equity']))
print("Mean, median and mode of asked valuation are- ", round(np.mean(df['ask_valuation']),2)," , ", np.median(df['ask_valuation'])," , ",stats.mode(df['ask_valuation']))


# In[102]:


#Q3. Max & Min asked- equity,asked-valuation and asked amount episode-wise?
episode_num=df['episode_number'].unique()

for i in range(0,len(episode_num)):
    filtere=np.where(df['episode_number']==episode_num[i])
    print("Maximum and Minimum asked equity for epsiode ",episode_num[i], "are" ,np.max(df.loc[filtere]['ask_equity'])," , ",np.min(df.loc[filtere]['ask_equity']))
    print("Maximum and Minimum asked amount for epsiode ",episode_num[i], "are" ,np.max(df.loc[filtere]['pitcher_ask_amount'])," , ",np.min(df.loc[filtere]['pitcher_ask_amount']))
    print("Maximum and Minimum asked valuation for epsiode ",episode_num[i], "are" ,np.max(df.loc[filtere]['ask_valuation'])," , ",np.min(df.loc[filtere]['ask_valuation']))
    


# In[120]:


#Q4. Brand names in which 2 ,3 or 4 sharks are invested?
display(df.loc[(df['total_sharks_invested']).between(2,5)]['brand_name'])


# In[205]:


#Q5. Episode wise minimum and maximum no. of sharks invested?
episode_num=df['episode_number'].unique()

for i in range(0,len(episode_num)):
    filtere=np.where(df['episode_number']==episode_num[i])
    print("For epiosode ",episode_num[i]," - \n")
    print("Maximum and Minimum number of sharks invested are" ,np.max(df.loc[filtere]['total_sharks_invested'])," , ",np.min(df.loc[filtere]['total_sharks_invested']),"\n")


# In[147]:


#Q6. Find the brands in which only ashneer invested.
print("Ashneer delas are")
a= np.array((df.loc[df['ashneer_deal']==1]['brand_name']))
print(a)


# In[150]:


#Q7. Brand names who ask for 1 crore and got a deal what was the deal amount?
df.loc[(df['deal']==1) & (df['pitcher_ask_amount']==100),['brand_name','deal_amount']]


# In[154]:


#Q8. Brand names where deal equity is between 1 to 50?
df.loc[df['deal_equity'].between(1,50),['brand_name','deal_equity']]


# In[203]:


#Q9. Find the number of brands participated in each episode?
episode_num=df['episode_number'].unique()

for i in range(0,len(episode_num)):
    filtere=np.where(df['episode_number']==episode_num[i])
    print("For epiosode ",episode_num[i]," - \n")
    print("Number of brands are" ,len(df.loc[filtere]['pitch_number']),"\n")


# In[177]:


#Q10. How many sharks participated in this show and What were their names?
sum=0
sharks=[]
for data in df.columns:
    if data.endswith('_deal'):
        data=data[:-5]
        sharks.append(data.upper())
        sum=sum+1
        
print("Number of sharks are- ", sum)
print("Name of sharks are- ", sharks)


# In[192]:


#Q11. Find appearance of each sharks?
print("Ashneer appeared in", len(df.loc[df['ashneer_present']==1]), "episodes")
print("Anupam appeared in", len(df.loc[df['anupam_present']==1]), "episodes")
print("Aman appeared in", len(df.loc[df['aman_present']==1]), "episodes")
print("Namita appeared in", len(df.loc[df['namita_present']==1]), "episodes")
print("Vineeta appeared in", len(df.loc[df['vineeta_present']==1]), "episodes")
print("Peyush appeared in", len(df.loc[df['peyush_present']==1]), "episodes")
print("Ghazal appeared in", len(df.loc[df['ghazal_present']==1]), "episodes")


# In[182]:


#Q12. How many brands were present?
print("Number of brands are",len(df['brand_name']))


# In[193]:


#Q13. How many times each shark invested the deal?
print("Ashneer invested in", len(df.loc[df['ashneer_deal']==1]), "brands")
print("Anupam invested in", len(df.loc[df['anupam_deal']==1]), "brands")
print("Aman invested in", len(df.loc[df['aman_deal']==1]), "brands")
print("Namita invested in", len(df.loc[df['namita_deal']==1]), "brands")
print("Vineeta invested in", len(df.loc[df['vineeta_deal']==1]), "brands")
print("Peyush invested in", len(df.loc[df['peyush_deal']==1]), "brands")
print("Ghazal invested in", len(df.loc[df['ghazal_deal']==1]), "brands")


# In[204]:


#Q15. Find the total number of amount invested in this show?
print("Total amount invested in show is", round(df['deal_amount'].sum()))


# In[207]:


#Q16 Above 50% Equity taken by the shark in which brand
print("Brands are",np.array(df.loc[(df['deal_equity']/df['deal_amount'])*100>50,'brand_name']))


# In[208]:


df.head(10)


# #Q17 what more insights you can gain from the dataset
# 
# There are multiple insights that can be further gain from this dataset. some of the examples are:-
# 1. Do one shark affect the decision of another shark.
# 2. Comparison between asked valuation and the valuation on which the deal was made.
