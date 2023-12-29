#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

dateiname = "/home/kristian/Desktop/DataVisualization/climate/TG_STAID011736.txt"

df = pd.read_csv(
    dateiname,
    sep=",",
    skiprows=19
    )
df.columns = ['SOUID', 'DATE', 'TG', 'Q_TG']

# Temperatur durch 10 teilen auf Grad Celsius
df['temp'] = df['TG'] / 10

# Datum formatieren
df['datum'] = df['DATE'].astype(str)
df['jahr'] = df['datum'].str[0:4]
df['monat'] = df['datum'].str[4:6]
df['tag'] = df['datum'].str[6:]

zeitstempel = df['jahr'] + '-' + df['monat'] + '-' + df['tag']
datum = pd.to_datetime(zeitstempel)
df = df.set_index(datum)  # steht ganz links

# fehlende Werte behandeln anhand der Qualitätsspalte
df_clean = df[df['Q_TG'] != 9]  # 9 = missing

# nur der heutige Tag
oct12 = df_clean[
    (df_clean['monat'] == '10') &
    (df_clean['tag'] == '12')
    ]
#oct12['temp'].plot()  # index-> x-Achse, Werte-> y-Achse

# erst bei 1950 anfangen
df_clean = df_clean.loc['Jan 1st 1950':'2022-12-31']

# Aggregation: Median pro Jahr
median = df_clean.resample('1Y')['temp'].median()
median.plot()

# Heatmap
daten = pd.DataFrame(median).transpose()  # dreht Tabelle um 90° 
cmap = plt.get_cmap('coolwarm')

# schön große Abbildung
plt.figure(figsize=(15, 5))  # Länge x Breite in Zoll
plt.title('Median der Temperatur in Berlin Adlershof')
sns.heatmap(daten, cmap=cmap, cbar=True,
            #xticklabels=ticks,
            yticklabels=[]
            )

# Beschriftung basteln: alle 10 Jahre ein Strich
plt.xticks(
    ticks=range(0, 72, 5), 
    labels=range(1950, 2022, 5),
)

plt.savefig('klimastreifen.png', dpi=150)









