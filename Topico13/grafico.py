from matplotlib import pyplot as plt
import pandas as pd


emp = pd.read_csv("./data/employees.csv").dropna(how = "all")

emp["MediaSalary"] = emp.groupby("Gender")["Salary"].mean()

# emp_gender = emp.groupby("Gender")["Salary"].mean()

print(emp)

# plt.pie(emp_gender["Salary"], labels=emp_gender["Gender"], autopct='%1.1f%%')

# plt.show()
# plt.plot(emp["Salary"], emp["Bonus %"], "o")