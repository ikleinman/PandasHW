
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[3]:


purchase_data.head(10)


# ## Player Count

# * Display the total number of players
# 

# In[4]:


total_players= len(purchase_data["SN"].unique())

total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[5]:


purchase_data.describe()

unique_items = len(purchase_data["Item ID"].unique())
average_price= purchase_data["Price"].mean()
average_age= purchase_data["Age"].mean()
purchases= len(purchase_data["Purchase ID"].unique())
summary_table = pd.DataFrame({"Total Items": unique_items,
                              "Average Price": [average_price],
                              "Average Age": [average_age],
                              "Number of Purchases": [purchases]})
summary_table



# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[6]:


count_male = purchase_data.loc[purchase_data["Gender"]=="Male"]
total_male= len(count_male["SN"].unique())
percent_male= total_male/total_players*100


count_female = purchase_data.loc[purchase_data["Gender"]=="Female"]
total_female= len(count_female["SN"].unique())
percent_female= total_female/total_players*100

count_other = purchase_data.loc[purchase_data["Gender"]=="Other / Non-Disclosed"]
total_other= len(count_other["SN"].unique())
percent_other= total_other/total_players*100



gender_summary = pd.DataFrame({"Gender": ["Male", "Female", "Other"],
                               "Percent_Total": [percent_male, percent_female, percent_other],
                              "Count": [total_male, total_female, total_other]})
gender_summary


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[9]:


#tried the below comments
#calc1= purchase_data["Gender"].value_counts()
#calc= purchase_data.describe()
grouped_purchase_data= purchase_data.groupby(['Gender'])

item_count= grouped_purchase_data["Item Name"].count()

avg_price=grouped_purchase_data["Price"].mean()

total_purchase_value= grouped_purchase_data["Price"].sum()

total_gender=grouped_purchase_data["SN"].nunique()

avg_total_purchase= total_purchase_value/total_gender
avg_total_purchase


purchasing_summary= pd.DataFrame({
                                 "Purchase Count": item_count,
                                 "Average Purchase Price": avg_price,
                                 "Total Purchase Value": total_purchase_value,
                                 "Average Total Purchase Per Person": avg_total_purchase})
purchasing_summary


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[27]:


#creating bins and bin labels
bin=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

bin_labels= ["0 to 5", "5 to 10", "15 to 20", "20 to 25", "25 to 30", "30 to 35", "35 to 40", "40 to 45", "45 to 50", "50 to 55", "55 to 60"]


# In[28]:


purchase_data["Age Range"]= pd.cut(purchase_data["Age"], bin, labels =bin_labels)

purchase_data.head()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[29]:


age_demo_df = purchase_data.groupby("Age Range")
age_purchase_count = age_demo_df["Item ID"].count()


#Average Purchase Price
age_avg_purch_price = age_demo_df["Price"].mean()
age_avg_purch_price

age_purchase_price = age_demo_df["Price"].sum()
age_purchase_price.head()

#Age count
age_ct = age_demo_df["SN"].nunique()
age_total = round(age_purchase_price/age_ct,2)
age_total

#summary
purchase_analysis_age = pd.DataFrame({"Purchase Count": age_purchase_count,
                                       " Average Purchase Price": age_avg_purch_price,
                                       "Total Purchase Value": age_purchase_price,
                                       "Average Purchase Total per Person by Age Group ": age_total})

purchase_analysis_age


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[32]:


top_spender = purchase_data.groupby(["SN"])
spending = top_spender["Price"].sum()
item_count_sp = top_spender["Item ID"].count()
item_average_sp = round(spending/item_count_sp, 2)


summary_top_spenders = pd.DataFrame({"Purchase Count": item_count_sp,
                          "Average Price": item_average_sp, 
                          "Total Purchase Value": spending})
summary_top_spenders.sort_values("Total Purchase Value", ascending=False).head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[37]:


items_df = purchase_data.groupby(["Item ID"])
purchase_count_pi = items_df["Item ID"].count()
item_total_purchase = items_df["Price"].sum()

summary_items = pd.DataFrame( {"Item Name": purchase_data["Item Name"],
                           "Purchase Count":purchase_count_pi, 
                           "Item Price": purchase_data["Price"], 
                           "Total Purchase Value": item_total_purchase})
summary_cleanup = summary_items.reset_index()
summary_cleanup.sort_values("Purchase Count", ascending=False).head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[38]:


most_profitable = summary_cleanup.sort_values("Total Purchase Value", ascending = False)
most_profitable.head()

