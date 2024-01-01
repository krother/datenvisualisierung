
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("penguins")

# kürzere Notation mit pandas
df.groupby(["species", "sex"])["body_mass_g"].mean().unstack().plot.bar()

# besserer Plot mit seaborn
plt.figure()
sns.catplot(
    data=df, 
    x="species",
    y="body_mass_g",
    hue="sex",
    kind="bar",
    estimator="mean",
    errorbar=None,
)
plt.savefig("grouped_barplot.png")
