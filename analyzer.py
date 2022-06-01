import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

print(*[filename.split(".")[0] for filename in os.listdir("./reviews")], sep="\n")
product_id = input("Podaj identyfokator produktu: ")

opinions = pd.read_json("reviews/"+product_id+".json")

opinions_count = len(opinions)
pros_count = opinions["pros"].astype(bool).sum()
cons_count = opinions["cons"].astype(bool).sum()
average_score = opinions["stars"].mean().round(2)
print(opinions_count)

recommendations = opinions["recommendation"].value_counts(dropna=False).sort_index().reindex([False, True, None], fill_value=0)
recommendations.plot.pie(
    autopct = "%.1f%%",
    label = "",
    title = "Rekomendacje",
    labels = ["Nie polecam", "Polecam", "Nie mam zdania"],
    colors = ["crimson", "forestgreen", "lightskyblue"]
)
plt.show()
plt.savefig("plots/"+product_id+"_recommendations.png")
plt.close()

stars = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value = 0)

stars.plot.bar(color = "blue")
plt.title("Stars")
plt.xlabel("# of stars")
plt.ylabel("# of reviews")
plt.savefig("plots/{}.png".format(product_id))
plt.show()
plt.close()

recomm = opinions.recomm.value_counts(dropna = False).sort_index()
recomm.plot.pie(colors = ["yellow", "green", "purple"])

plt.show()