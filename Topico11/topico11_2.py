import pandas as pd
import pandas_datareader as pdr
import json

data = [
    {
        "Emp": "Jeff Russell",
        "Emp_email": "jeff.russell",
        "POs": [
            {"Pono": 2608, "Total": 35},
            {"Pono": 2617, "Total": 35},
            {"Pono": 2620, "Total": 139},
        ],
    },
    {
        "Emp": "Jane Boorman",
        "Emp_email": "jane.boorman",
        "POs": [{"Pono": 2621, "Total": 95}, {"Pono": 2626, "Total": 218}],
    },
]

df = pd.json_normalize(data, "POs", "Emp").set_index(["Emp", "Pono"])




#df.reset_index();

# json_doc = (
#     df.groupby(["Emp"], as_index=True)
#     .apply(lambda x: x[["Pono","Total"]].to_dict("records"))
#     .reset_index()
#     .rename(colums={0:"POs"})
#     .to_json(orient="records")
# )

#print(df)


spx_index = pdr.get_data_stooq("^SPX", "2025-01-01", "2025-04-01")

print(spx_index)



