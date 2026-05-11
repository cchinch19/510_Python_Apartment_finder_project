import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/apartments.csv")

avg_price = df.groupby("city")["price"].mean().round(2)

df_with_sqft = df.dropna(subset=["square_footage"]).copy()
df_with_sqft["price_per_sqft"] = df_with_sqft["price"] / df_with_sqft["square_footage"]
avg_price_per_sqft = df_with_sqft.groupby("city")["price_per_sqft"].mean().round(2)

commute = df.groupby("city")[["usc_commute", "work_commute"]].mean()

walkscore_df = df.groupby("city")[["walk_score", "bike_score"]].mean()

fig = plt.figure(figsize=(14, 10))
fig.suptitle('Apartment overview by city', fontsize=16)

ax1 = fig.add_subplot(2, 2, 1)
ax1.bar(avg_price.index, avg_price.values)
ax1.bar_label(ax1.containers[0], fmt='$%.0f')
ax1.set_title('Average price')
ax1.set_ylabel('$/month')
ax1.tick_params(axis='x', rotation=15)

ax2 = fig.add_subplot(2, 2, 2)
ax2.bar(avg_price_per_sqft.index, avg_price_per_sqft.values)
ax2.bar_label(ax2.containers[0], fmt='$%.2f')
ax2.set_title('Average price per sqft')
ax2.set_ylabel('$/sqft')
ax2.tick_params(axis='x', rotation=15)

ax3 = fig.add_subplot(2, 2, 3)
commute.plot(kind='bar', ax=ax3)
for container in ax3.containers:
    ax3.bar_label(container, fmt='%.0f min')
ax3.set_title('Commute times')
ax3.set_ylabel('Minutes')
ax3.tick_params(axis='x', rotation=15)

ax4 = fig.add_subplot(2, 2, 4)
walkscore_df[['walk_score', 'bike_score']].plot(kind='bar', ax=ax4)
for container in ax4.containers:
    ax4.bar_label(container, fmt='%.0f')
ax4.set_title('Walk / bike score')
ax4.set_ylabel('Score')
ax4.tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.savefig("results/overview.png")
plt.show()
