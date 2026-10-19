import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, 6, 7, 8])
print (s)
print (s[0:3])
#dataframe
df = pd.DataFrame({"name": ["tom", "nick", "raj", "harsh"],
                   "age": [23, 34, 54, 36],
                   "salary": [10000, 20000, 50000, 45000],
                   "city ": ["delhi", "mumbai", "pune", "banglore"]})
#print (df)
'''print (df[0:3])
print (df.head(4))
print (df.tail())
df.info()'''
df.to_csv("data.csv",index = True)
df ["HRA"]  = df["salary"]*0.12
print(df)
df ["NET SALARY"] = df["HRA"]+df ["salary"]
print(df)

def AGE_CHECK(age):
    if age>30:
        return "Age is greater than 30"
    else:
        return "Age is less than 30"

df["AGECHECK"] = df["age"].apply(AGE_CHECK)
print(df)
def SALARY_CHECK(age):
    if age >30 :
        return "your salary is good ",df["salary"]
    else :
         return "your salary is poor  ",df["salary"]
df["SALARYCHECK"] = df["age"].apply(SALARY_CHECK)
print(df)

