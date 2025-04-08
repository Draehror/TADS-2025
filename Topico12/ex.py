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

df_vendas = pd.DataFrame(vendas, columns=["Data", "Região", "Estado", "Valor"])

df_vendas["Mês"] = pd.to_datetime(df_vendas["Data"]).dt.month_name()

#vendas_por_regiao = df_vendas.groupby("Região")["Valor"].sum().reset_index()

#vendas_por_regiao["Mês"] = pd.to_datetime(vendas_por_regiao["Data"]).dt.month_name()
df_vendas_mes_total = df_vendas.groupby("Mês")["Valor"].sum()

#df_final = df_vendas_mes_total.groupby("Região")["Valor"].sum()

print(df_final)
#df_sales["Month"] = pd.to_datetime(df_sales["Date"]).dt.month_name()