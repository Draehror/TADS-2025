import pandas as pd
import json

data = ['Huguinho','Zezinho','Pedrinho']

emps_names = pd.Series(data, index=[9001,9002,9003])

data = ["huguinho.silva@email.com","zezinho.pereira@email.com","luizinho.matos@email.com"]

emps_emails = pd.Series(data,index=[9001,9002,9003], name="emails")

emps_names.name = "names"

df = pd.concat([emps_names,emps_emails], axis = 1)

data = ["(32)1312-1312","(32)4394-2312","(32)4324-2432"]

emps_phones = pd.Series(data,index=[9001,9002,9003], name = "phones")

df = pd.concat([emps_names,emps_emails,emps_phones], axis=1)



data = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500}
]

json_data = json.dumps(data)

salary = pd.read_json(json_data)

salary = salary.set_index("Empno")

# print(salary)

data = [
    ["9001","Huguinho","sales"],
    ["9002","Zezinho","sales"],
    ["9003","Luizinho","sales"],
    ["9004","Florzinha","sales"]
]

emps = pd.DataFrame(data, columns=["Empno","Name","Job"])

column_types = {"Empno": int, "Name": str, "Job": str}

emps = emps.astype(column_types)

emps = emps.set_index("Empno")

emps_salary = emps.join(salary, how='inner')

print(emps_salary)

