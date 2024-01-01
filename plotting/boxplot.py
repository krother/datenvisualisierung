import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("penguins")

sns.boxplot(
    data=df,
    y="body_mass_g",
    x="species",
    hue="sex",
)
plt.savefig("boxplot.png")
