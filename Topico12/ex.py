import pandas as pd

vendas = [
      ("2024-01-05", "Sudeste", "SP", 1500),
      ("2024-01-12", "Sul", "RS", 800),
      ("2024-01-18", "Nordeste", "BA", 1200),
      ("2024-02-03", "Sudeste", "RJ", 2000),
      ("2024-02-10", "Sul", "SC", 950),
      ("2024-02-15", "Nordeste", "PE", 750),
      ("2024-03-08", "Sudeste", "MG", 1800),
      ("2024-03-22", "Nordeste", "CE", 1100),
  ]

df_vendas = pd.DataFrame(vendas, columns=["Data", "Regiao", "Estado", "Valor"])

df_vendas["Mes"] = pd.to_datetime(df_vendas["Data"]).dt.month_name()

#vendas_por_regiao = df_vendas.groupby("Região")["Valor"].sum().reset_index()

#vendas_por_regiao["Mês"] = pd.to_datetime(vendas_por_regiao["Data"]).dt.month_name()
df_vendas_mes_total = df_vendas.groupby("Mes")["Valor"].sum()

#df_final = df_vendas_mes_total.groupby("Região")["Valor"].sum()

#df_sales["Month"] = pd.to_datetime(df_sales["Date"]).dt.month_name()

df_vendas_mes_regiao = df_vendas.groupby(["Mes","Regiao"]).sum()

df_vendas_mes_regiao = df_vendas_mes_regiao[["Valor"]]

df_totais = pd.DataFrame()

for (mes,df_mes) in df_vendas_mes_regiao.groupby(level=0):
    df_totais = pd.concat([df_totais,df_mes])
    ps = df_mes.sum(axis=0)
    ps.name = (mes,"Subtotal")
    df_totais = pd.concat([df_totais,ps.to_frame().T])
    
ps = df_vendas_mes_regiao.sum(axis=0)
ps.name = ("Total","")

df_totais = pd.concat([df_totais,ps.to_frame().T])

print(df_totais)