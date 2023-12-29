Pivot-Tabellen
==============

|image0|

*farbenfrohe Gottheit der Pivot-Tabellen (erstellt von deepdream.io)*

In dieser Übung untersuchen wir, wie sich Brettspiele unterschiedlicher
Kategorien im Lauf der Zeit entwickelt haben.

Dazu erstellen wir **Pivot-Tabellen**. Piovot-Tabellen fassen Daten
zusammen, die zwei kategorische und eine numerische Variable beinhalten.
Wir erweitern das Rezept aus der vorigen Übung um einen Punkt:

::

   1. Daten laden
   2. Daten aufbereiten
   3. Aggregieren
   4. Plotten

Es kommen allerdings einige Neuerungen hinzu.

Aufgabe 1: Daten laden
----------------------

Wir benötigen wieder einige Python-Bibliotheken. Eine neue ist dazu
gekommen:

.. code:: python3

   import pandas as pd
   import seaborn as sns
   from matplotlib import pyplot as plt

Du solltest eine Datei ``boardgamegeek.csv`` erhalten haben. Lade diese
mit dem Befehl

.. code:: python3

   df = pd.read_csv(...)

Klicke in Spyder auf **Variable Explorer** und dort auf **df**. Du
solltest eine Tabelle mit Brettspielen sehen.

**wie viele Zeilen/Spalten gibt es in der Tabelle?**

Aufgabe 2: Daten aufbereiten
----------------------------

Wir legen eine zusätzliche Spalte für das Jahrzehnt an:

.. code:: python3

   df["decade"] = df["YearPublished"] // 10 * 10

Um etwas besser lesbare Ergebnisse zu erhalten, lassen wir die ganz
alten Spiele weg:

.. code:: python3

   df = df[df["YearPublished"] >= 1960]

Prüfe, wie viele Einträge das *DataFrame* noch enthält.

Aufgabe 3: Aggregieren
----------------------

Um eine Pivot-Tabelle zu erstellen, müssen wir nach **zwei** Spalten mit
Kategorien gruppieren. Wir betrachten dazu die Spalten **category** und
**decade**.

Zunächst zählen wir die Anzahl Spiele für jede Kombination. Trage die
Spaltennamen ein

.. code:: python3

   pivot = df.pivot_table(
       index="...",
       columns="...",
       values="AvgRating",
       aggfunc="count",
       fill_value=0)

Das gleiche lässt sich auch mit der Funktion ``groupby`` erzielen, ist
aber etwas mühseliger:

.. code:: python3

   pivot = df.groupby(["...", "..."])["AvgRating"].count()

Du solltest mit ``pivot`` in jedem Fall eine Tabelle mit ca. 7 x 9
Feldern erhalten.

Aufgabe 4: Balken
-----------------

Die einfachste Möglichkeit, eine Pivot-Tabelle zu plotten, ist als
Balkendiagramm:

.. code:: python3

   pivot.plot.bar()

Vertausche die beiden Kategorien bei der Aggregation. Was ändert sich?

Aufgabe 5: Linien
-----------------

Wenn die Zeitachse über die Zeilen von oben nach unten geht, ist auch
ein Liniendiagramm sinnvoll

.. code:: python3

   pivot.plot.line()

Aufgabe 6: Heatmap
------------------

Mit der Bibliothek ``seaborn`` können wir auch eine farbige Matrix
darstellen:

.. code:: python3

   sns.heatmap(pivot)

Aufgabe 7: Variationen
----------------------

Probiere statt ``count`` auch ``mean``, ``median`` und ``sum`` zur
Aggregation.

Aufgabe 8: Normalisieren
------------------------

Manchmal macht es Sinn, die Zeilen oder Spalten auf Prozente zu
normalisieren:

.. code:: python3

   norm = pivot / pivot.sum() * 100

oder

.. code:: python3

   norm = pivot.T / pivot.T.sum() * 100

Inspiziere oder plotte ``norm``, um das Ergebnis zu sehen.


.. |image0| image:: god_of_pivot.png

.. hint::

   Du findest in :download:`pivot_tabelle.py` eine Musterlösung.
