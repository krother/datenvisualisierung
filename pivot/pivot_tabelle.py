
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = pd.read_csv("/home/kristian/Desktop/DataVisualization/boardgamegeek.csv", sep=",")

# Teilen mit Abrunden und Multiplizieren -> xxx0 als neue Spalte
# // : floor division
df["decade"] = df["YearPublished"] // 10 * 10
# df["decade"] = (df["YearPublished"] / 10).round() * 10

# alte Spiele weg
df = df[df["YearPublished"] >= 1970]
# misc Spiele weg
df = df[df["category"] != "misc"]

# Pivot-Tabelle erzeugen
pivot = df.pivot_table(
    index="decade",
    columns="category",
    values="MinPlayers",  # mit 'count' egal
    aggfunc="count",
    )

# speichern
pivot.to_excel("spielepivot.xlsx")
pivot.to_csv("spielepivot.csv")

pivot.plot.bar()
pivot.plot.line()

# neues Diagramm anfangen
plt.figure()
sns.heatmap(pivot)
plt.savefig("heatmap.png", dpi=150)


