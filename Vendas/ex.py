import pandas as pd

vendas = pd.read_csv("./vendas.csv")

vendas = vendas.groupby("Categoria")["Preco_Unitario"].sum()

vendas["Total"] = vendas.sum()


print(vendas)