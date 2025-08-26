# Experiment 03: Dataset Cleaning

## Aim
Clean a dataset by identifying and handling missing values using `fillna()` or `dropna()`, and remove duplicates using `drop_duplicates()`.

## Dataset
The dataset used is the **California Housing Test Dataset** provided in Google Colab 

## Steps Performed
1. **Load the dataset** using Pandas.  
2. **Check missing values** using `isnull().sum()`.  
3. **Handle missing values**:
   - Option 1: Fill with median → `df.fillna(df.median())`  
   - Option 2: Drop rows → `df.dropna()`  
4. **Remove duplicates** using `df.drop_duplicates()`.  
5. **Preview the cleaned dataset** with `head()`. 
