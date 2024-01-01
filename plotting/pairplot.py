import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("penguins")

sns.pairplot(df, hue="species")
plt.savefig("pairplot.png", dpi=150)
