.. _choropleth:

Covid Dashboard
===============

In dieser Übung werden wir Covid-Fälle pro Land auf einer Karte zeichnen.
Eine solche Karte nennt man auch **Choropleth**.


1. Plotly
---------

Zum Zeichnen von Karten benötigst du die Bibliothek **plotly**:

::

   pip install plotly

2. Choropleth
-------------

Führe folgenden Code aus. Dazu muss die Bibliothek ``plotly`` instaliert sein:

.. literalinclude:: choropleth_start.py

3. Daten
--------

Lade den `Covid-Datensatz von Our World in Data <https://ourworldindata.org/covid-cases>`__ als CSV-Datei
herunter.
Ersetze das CSV im Beispielprogramm durch die heruntergeladenen Daten.

4. Spaltennamen angeben
-----------------------

Wir müssen angeben, in welchen Spalten unserer Daten die relevanten Informationen stehen.

* In ``location`` steht, welches Land jeweils eingefärbt werden soll.
* In ``color`` steht, nach welchen Zahlen eingefärbt werden soll (also die Infektionszahlen).

Beide Felder müssen einen gültigen Spaltennamen enthalten.

5. GeoJSON
~~~~~~~~~~

Lade eine Weltkarte als GeoJSON herunter. Du findest sie auf
`geojson-maps.ash.ms/ <https://geojson-maps.ash.ms/>`__.

Die niedrig aufgelöste Karte reicht völlig.

6. GeoJSON Properties
~~~~~~~~~~~~~~~~~~~~~

Du musst im Aufruf der Funktion ``choropleth`` angeben, wo im GeoJSON das Feld mit den Ländernamen ist. 
Untersuche dazu die GeoJSON-Datei in einem Texteditor:

::

   featureidkey="properties.name"

7. Streamlit
~~~~~~~~~~~~

Die fertige Karte in Streamlit einzubinden ist mega einfach:

.. code:: python3

   st.plotly_chart(fig)

Und lösche das ``fig.show()``.
