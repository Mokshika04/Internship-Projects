import pandas as pd

df = pd.read_csv("Ames_Housing_Sales.csv")
total_sales = df['SalePrice'].sum()

max_sale = df['SalePrice'].max()
best_selling_index = df['SalePrice'].idxmax()
best_selling_house = df.loc[best_selling_index].to_dict()

best_neighborhood = (
    df.groupby("Neighborhood")["SalePrice"].sum().idxmax()
)
best_neighborhood_sales = (
    df.groupby("Neighborhood")["SalePrice"].sum().max()
)

# Basic Report:eport = f"""
Ames Housing Sales Report
------------------------
Number of sales: {len(df)}
Total sales (sum of SalePrice): ${total_sales:,.2f}
Average house price: ${df['SalePrice'].mean():,.2f}

Most expensive individual sale: ${max_sale:,.2f}
Details: {best_selling_house}

Top-grossing Neighborhood: {best_neighborhood}
  - Neighborhood total sales: ${best_neighborhood_sales:,.2f}

Top 5 neighborhoods by total sales:
{df.groupby("Neighborhood")["SalePrice"].sum().sort_values(ascending=False).head(5).to_string()}

Top 5 HouseStyles by total sales:
{df.groupby("HouseStyle")["SalePrice"].sum().sort_values(ascending=False).head(5).to_string()}
"""

print(report)