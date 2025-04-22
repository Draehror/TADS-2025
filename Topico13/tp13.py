import pandas as pd

emp = pd.read_csv("./data/employees.csv").dropna(how = "all")

df_emp = pd.DataFrame(emp, columns=["First Name","Gender","Start Date","Last Login Time","Time","Salary","Bonus %","Senior Management","Team"])

df_emp["Senior Management"] = df_emp["Senior Management"].astype("bool")

df_emp["Start Date"] = pd.to_datetime(df_emp["Start Date"])
df_emp["Last Login Time"] = pd.to_datetime(df_emp["Last Login Time"], format="%I:%M %p")

df_emp["Gender"] = df_emp["Gender"].fillna("NI")

df_emp["Gender"] = df_emp["Gender"].astype("category")

gensal_df_emp = df_emp.groupby("Gender")["Salary"].mean()

print(gensal_df_emp)