# run with: streamlit run penguin_dashboard.py

import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt


df = sns.load_dataset('penguins')

general, flippers, beaks = st.tabs(["Übersicht", "Flossen", "Schnäbel"])

with general:
    st.write("# Übersicht")

    st.write("### Verteilung der Spezies")
    st.bar_chart(df["species"].value_counts())

    st.write("### Histogramm")
    columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    colname = st.selectbox("wähle eine Spalte", columns)

    fig = plt.figure()
    sns.histplot(df[colname], kde=True, bins=20)
    st.pyplot(fig)

    st.write("### Tabellenausgabe")
    st.write(df.head(5))


with flippers:
    st.write("# Flossen")

    min_flip = st.slider("minimale Länge", 200, 300)
    max_flip = st.slider("maximale Länge", 200, 300)

    df = df[df["flipper_length_mm"].between(min_flip, max_flip)]
    number = df.shape[0]

    st.write(f"Gesamtzahl Pinguine: {number}")


with beaks:
    st.write("# Schnäbel")

    # Scatterplot mit Seaborn
    figure = plt.figure()
    sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
    st.pyplot(figure)

    # Scatterplot mit Streamlit
    st.scatter_chart(
        data=df,                                    # Tabelle mit den zu plottenden Daten
        x="bill_length_mm",                         # Spaltenname für x-Achse
        y="bill_depth_mm",                     # Spaltenname(n) für y-Achse
        # color=["#ff00ff", "#00ff00"],             # default Farben sind normalerweise gut
        width=0, height=600,                        # Größe in Pixeln (0=default)
        use_container_width=True
    )
