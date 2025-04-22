import pandas as pd

df_jb = pd.read_csv("./data/jamesbond.csv").dropna(how="all")

# df_jb = pd.DataFrame(jb, columns=["Film","Year","Actor","Director","Box Office","Budget","Bond Actor Salary"])

df_jb = df_jb.set_index(["Film","Year"])

# print(df_jb.loc[("Casino Royale",2006),["Actor","Director"]])

#df_jb = df_jb.dropna(how="any")

# print(df_jb.groupby("Actor")["Salary"].sum())

# print(df_jb.nlargest(n=4,columns="Box Office"))

mask = df_jb["Actor"] == "Sean Connery"

# print(df_jb[mask])


df_jb.columns = [columns_name.replace(" ","_") for columns_name in df_jb.columns]


# print(df_jb.query("Box_Office > 500"))

# print(df_jb.nlargest(n=5,columns="Budget"))

def convert_to_millions(number):
    return str(number)+" Millions!"

df_jb["Box_Office_M"] = df_jb["Box_Office"].apply(convert_to_millions)

print(df_jb)