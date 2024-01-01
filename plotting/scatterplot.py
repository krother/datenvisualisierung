import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("penguins")

# kürzere Notation mit pandas
df.plot.scatter(x="flipper_length_mm", y="body_mass_g")

# besserer Plot mit seaborn
plt.figure()
sns.scatterplot(
    data=df, 
    x="flipper_length_mm",
    y="body_mass_g",
    hue="sex",
)
plt.savefig("scatterplot.png")
