import pandas as pd

data = ['Huguinho','Zezinho','Pedrinho']

emps_names = pd.Series(data, index=[9001,9002,9003])

print(emps_names)
