import pandas as pd
from get_data import all_results
from integrate_data import score_data, usc_commutes, work_commutes

df = pd.DataFrame(all_results)

df["usc_commute"] = df["city"].map(usc_commutes)
df["work_commute"] = df["city"].map(work_commutes)
df["walk_score"] = df["city"].map({k: v["walk_score"] for k, v in score_data.items()})
df["bike_score"] = df["city"].map({k: v["bike_score"] for k, v in score_data.items()})

avg_price = df.groupby("city")["price"].mean().round(2)

df_with_sqft = df.dropna(subset=["square_footage"]).copy()
df_with_sqft["price_per_sqft"] = df_with_sqft["price"] / df_with_sqft["square_footage"]
avg_price_per_sqft = df_with_sqft.groupby("city")["price_per_sqft"].mean().round(2)

commute = df.groupby("city")[["usc_commute", "work_commute"]].mean()

walkscore_df = pd.DataFrame.from_dict(score_data, orient="index")
walkscore_df.index.name = "city"

df.to_csv("data/processed/apartments.csv", index=False)
