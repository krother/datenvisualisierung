import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("seaice")
df.set_index("Date", inplace=True)

df = df.loc["2000-01-01":]  # Werte ab 1.1.2000

df.plot()
plt.ylim(0, 18)

plt.savefig("lineplot.png")
