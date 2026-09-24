import os
import pandas as pd
import tabulate as tb


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Market.csv")
df = pd.read_csv(file_path, sep=";")


df["Category"] = df["Category"].ffill()

df["Total"] = 0

df["Price"] = df["Price"].str.replace(" USD", "").str.replace(".", "").str.replace(",", ".").astype(float)

df["Total"] = df["Total"].astype(float)

new_row = pd.DataFrame([{
    "Category" : "Kitchen equipments",
    "Product Name" : "Blender",
    "Launch Date" : 2026,
    "Price" : 70,
    "Quantity" : 35,
}])

new_row_index = 4
df = pd.concat([df.iloc[:new_row_index], new_row, df.iloc[new_row_index:]], ignore_index=True)


df["Total"] = df["Price"] * df["Quantity"]

df["Discount"] = 0

df.loc[df["Total"] >= 10000, "Discount"] = df["Total"] * 0.10
df.loc[(df["Total"] >= 7500) & (df["Total"] < 10000), "Discount"] = df["Total"] * 0.08
df.loc[(df["Total"] >= 5000) & (df["Total"] < 7500), "Discount"] = df["Total"] * 0.05
df.loc[(df["Total"] >= 2500) & (df["Total"] < 5000), "Discount"] = df["Total"] * 0.02

df["Final Total"] = df["Total"] - df["Discount"]

print(tb.tabulate(df, headers="keys", tablefmt="grid"))