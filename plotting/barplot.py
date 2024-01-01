
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("penguins")

# kürzere Notation mit pandas
df.groupby("species")["body_mass_g"].mean().plot.bar()

# besserer Plot mit seaborn
plt.figure()
sns.barplot(
    data=df, 
    x="species",
    y="body_mass_g",
    estimator="mean",
    errorbar=None,
)
plt.savefig("barplot.png")
