
Kontrollelemente in Streamlit
=============================

Mit Streamlit kannst Du allerlei Auswahlboxen, Knöpfe und Schieberegler einbauen.
Hier sind die wichtigsten vorgestellt.


Auswahl aus einer Liste von Strings
-----------------------------------

.. code:: python3

   options = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
   col_name = st.selectbox("pick a data column", options)
   str.write(col_name)


Zahl mit Schieberegler auswählen
--------------------------------

.. code:: python3

   value = st.slider("select value", 0, 100)
   st.write(str(value))


Texteingabe
-----------

.. code:: python3

   text = st.text_input("enter some text: ", value=":sunglasses:")
   st.write("**" + text + "**")


Auswahl mit mehreren Möglichkeiten
----------------------------------

.. code:: python3

   species = st.multiselect("species", options=["Adelie", "Chinstrap", "Gentoo"])
   df = df[df["species"].isin(species)]


Ein / Aus-Schalter
------------------

.. code:: python3

   show_plots = st.toggle('Show some plots')

   if show_plots:
      st.write("jetzt siehst Du etwas")
       ...
   else:
      st.write("jetzt siehst Du nichts")
       ...

