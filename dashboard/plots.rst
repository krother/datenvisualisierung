
Diagramme in Streamlit
======================

Das wichtigste an einem Dashboard ist natürlich Diagramme anzuzeigen.

**Streamlit** hat einige eigene Funktionen, um einfache Plots darzustellen.
Du kannst aber auch die gewohnten pandas/Seaborn-Plots darstellen.

In der Datei :download:`penguin_dashboard.py` findest Du ein komplettes Beispiel.


Liniendiagramm
--------------

Ein Liniendiagramm mit Pinguinen ist nicht sinnvoll, aber als Demonstration möglich:

.. code:: python3

   st.line_chart(
                data=df,
                x="body_mass_g",
                y=["bill_length_mm", "flipper_length_mm"], 
                color=["#ff00ff", "#00ff00"],
                width=0, height=0,
                use_container_width=True
                )

Streudiagramm
-------------

.. code:: python3

   st.scatter_chart(
                data=df,
                x="bill_length_mm",
                y="body_mass_g",
                color="species",
                width=0, height=500,
                use_container_width=True
                )

Balkendiagramm
--------------

Ein Balkendiagramm mit einer kategorischen Variable:

.. code:: python3

   st.bar_chart(
                df[col]
                )  

Die übrigen Argumente sind die gleichen wie oben


Gestapelte Balken
-----------------

Ein Balkendiagramm mit zwei kategorischen Variablen:

.. code:: python3

   pivot = df.groupby(["species", "sex"])["body_mass_g"].count().unstack()
   st.bar_chart(pivot)

Die übrigen Argumente sind die gleichen wie oben


Seaborn-Diagramme einbinden
---------------------------

Der Trick ist, sich mit ``plt.figure()`` eine Variable mit der Abbildung zu erzeugen.
Streamlit futtert diese dann in der Regel anstandslos.

.. code:: python3

   fig = plt.figure()
   sns.histplot(df[column], kde=True)
   st.pyplot(fig)
