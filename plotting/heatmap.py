import seaborn as sns
from matplotlib import pyplot as plt


df = sns.load_dataset("penguins")

corr_mtx = df.corr()

plt.figure(figsize=(10, 9))
sns.heatmap(
    data=corr_mtx,
    annot=True,
    vmin=-1.0,
    vmax=1.0,
    cmap="coolwarm",
    )

plt.savefig("heatmap.png")
