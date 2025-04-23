import pandas as pd
from matplotlib import pyplot as plt

emp = pd.read_csv("./data/employees.csv").dropna(how = "all")

df_emp = pd.DataFrame(emp, columns=["First Name","Gender","Start Date","Last Login Time","Time","Salary","Bonus %","Senior Management","Team"])

df_emp["Senior Management"] = df_emp["Senior Management"].astype("bool")

df_emp["Start Date"] = pd.to_datetime(df_emp["Start Date"])
df_emp["Last Login Time"] = pd.to_datetime(df_emp["Last Login Time"], format="%I:%M %p")

df_emp["Gender"] = df_emp["Gender"].fillna("NI")

df_emp["Gender"] = df_emp["Gender"].astype("category")

gensal_df_emp = df_emp.groupby("Gender")["Salary"].mean()
# gensal_df_emp.drop("NI", inplace=True)

print(gensal_df_emp)

plt.pie(gensal_df_emp.tolist(), labels=gensal_df_emp.index, autopct='%1.1f%%')

plt.title("Comparativo de Salario por Genero")
plt.show()