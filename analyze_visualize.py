import matplotlib.pyplot as plt
from clean_data import avg_price, avg_price_per_sqft, commute, walkscore_df

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
