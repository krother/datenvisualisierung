import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("penguins")

# kürzere Notation mit pandas
df["body_mass_g"].plot.hist(bins=20)

# nicht unbedingt besserer Plot mit seaborn
plt.figure()
no_chin = df[df["species"]!="Chinstrap"]
sns.histplot(
    data=no_chin, 
    x="body_mass_g",
    hue="species",
    bins=20,
    kde=True,
    alpha=1.0,
)
plt.savefig("histogramm.png")
