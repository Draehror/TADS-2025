import pandas as pd

nba = pd.read_csv("./data/nba.csv",index_col="Name")

#type(nba[["Name","Team"]])
#nba.insert(3,column="Sport",value="Basketball")
#nba.dropna(how = "all") dropa os vazios(todas colunas), any dropa se tiver vazio em qualquer uma das colunas
#nba["Salary"].fillna(0, inplace=True)
#nba["College"].fillna("None", inplace=True)
#nba["Salary"] = nba["Salary"]astype("int")
#nba["Position"] = nba["Position"]astype("category")
#nba.["Position"].nunique() 
#nba.sort_values("Name",ascending=False)  sort_index 


print(nba.info())