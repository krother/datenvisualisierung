
import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt

df = pd.read_csv(r"/home/kristian/Desktop/data/population.csv")

st.write("# Histogramm der Bevölkerung im Jahr 1999")
st.write("für alle Länder")


figure = plt.figure()
df["1999"].hist(bins=20)

st.table(df.head())

plt.ylabel("Anzahl Länder")
plt.xlabel("Bevölkerung im Jahr 1999")
st.pyplot(figure)
