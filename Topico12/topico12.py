import pandas as pd


orders = [
 (9423517, '2024-02-04', 9001),
 (4626232, '2024-02-04', 9003),
 (9423534, '2024-02-04', 9001),
 (9423679, '2024-02-05', 9002),
 (4626377, '2024-02-05', 9003),
 (4626412, '2024-02-05', 9004),
 (9423783, '2024-02-06', 9002),
 (4626490, '2024-02-06', 9004)
]

details = [
 (9423517, 'Jeans', 'Rip Curl', 87.0, 1),
 (9423517, 'Jacket', 'The North Face', 112.0, 1),
 (4626232, 'Socks', 'Vans', 15.0, 1),
 (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
 (9423534, 'Socks', 'DC', 10.0, 2),
 (9423534, 'Socks', 'Quiksilver', 12.0, 2),
 (9423679, 'T-shirt', 'Patagonia', 35.0, 1),
 (4626377, 'Hoody', 'Animal', 44.0, 1),
 (4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
 (4626412, 'Shirt', 'Volcom', 78.0, 1),
 (9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
 (9423783, 'Shorts', 'Globe', 26.0, 1),
 (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
 (4626490, 'Sweater', 'Dickies', 56.0, 1)
]

emps = [
 (9001, 'Jeff Russell', 'LA'),
 (9002, 'Nick Boorman', 'San Francisco'),
 (9003, 'Tom Heints', 'NYC'),
 (9004, 'Maya Silver', 'Philadelphia')
]

locations = [
 ('LA', 'West'),
 ('San Francisco', 'West'),
 ('NYC', 'East'),
 ('Philadelphia', 'East')
]


df_orders = pd.DataFrame(orders, columns=["OrderNo","Date","Empno"])

df_details = pd.DataFrame(details, columns=["OrderNo","Item","Brand","Price","Quantity"])

df_emps = pd.DataFrame(emps, columns=["Empno","Empname","Location"])

df_locations = pd.DataFrame(locations, columns =['Location', 'Region'])


df_sales = df_orders.merge(df_details)

df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']

df_sales["Month"] = pd.to_datetime(df_sales["Date"]).dt.month_name()

#Filtra as colunas
df_sales = df_sales[['Date','Empno','Total']]


df_sales_emps = df_sales.merge(df_emps)

df_result = df_sales_emps.merge(df_locations)

df_result = df_result[['Date','Region','Total']]

df_date_region = df_result.groupby(['Date','Region']).sum()

#verificando se index possui no dataframe, faz para cada item 
#print(df_date_region.index.isin([('2024-02-05','West')]))

#print(df_date_region[df_date_region.index.isin([('2024-02-05','West')])])
#print(df_date_region[df_date_region.index.isin([('2024-02-05','West'),('2024-02-05','East')])])
#fatia de um index ao outro
#print(df_date_region[('2024-02-05','West'):('2024-02-05','East')])
#print(df_date_region)
#slice com apenas um indice
#df_date_region['2024-02-05':'2024-02-05']
#dois pontos no final é do metodo loc para trabalhar com linha
#print(df_date_region.loc[slice('2024-02-05','2024-02-05'), slice('East'),:])

ps = df_date_region.sum(axis=0)

ps.name = ("All","All")

df_date_region_total = pd.concat([df_date_region,ps.to_frame().T])
#df_date_region.append(ps.to_frame().T)

df_totals = pd.DataFrame()

# for (date, date_df) in df_date_region.groupby(level=0):
#     df_totals = df_totals._append(date_df)
#     ps = date_df.sum(axis=0)
#     ps.name = (date,"All")
#     df_totals = df_totals._append(ps)

for (date, date_df) in df_date_region.groupby(level=0):
    df_totals = pd.concat([df_totals,date_df])
    ps = date_df.sum(axis=0)
    ps.name = (date,"All")
    df_totals = pd.concat([df_totals,ps.to_frame().T])

df_totals = pd.concat([df_totals,df_date_region_total.loc[("All","All")].to_frame().T])

# print(df_totals)

group = df_result.groupby(['Date','Region'])

#print(group.get_group(('2024-02-04','West')))

ex = pd.DataFrame()
for (date,date_df) in df_date_region.groupby(level=0):
    ex = ex._append(date_df)
    ps = date_df.sum(axis=0)
    ps.name = (date,"Total")
    ex = ex._append(ps)


#vendas_por_regiao = df_vendas.groupby("Região")["Valor"].sum().reset_index()



print(ex)