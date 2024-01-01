Einfache Diagramme plotten
==========================

|image0|

*Pinguin surft auf der großen Welle von Kanagawa (nach Hokusai, erstellt
von deepdream.io)*

Aufgabe 1: Programmbibliotheken
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wir benötigen einige Python-Bibliotheken.
Glücklicherweise sind diese schon mit Anaconda installiert.
Führe folgende Befehle aus:

.. code:: python3

   import pandas as pd
   import seaborn as sns
   from matplotlib import pyplot as plt

Nach dem Ausführen passiert erst einmal nichts. Du solltest aber auch
keine Fehlermeldung erhalten.

Aufgabe 2: Daten laden
~~~~~~~~~~~~~~~~~~~~~~

In der Bibliothek ``seaborn`` sind bereits mehrere Datensätze zum Ausprobieren enthalten.
Wir verwenden einen mit 333 Pinguinen.
Lade ihn mit:

.. code:: python3

   df = sns.load_dataset("penguins")

In Spyder solltest Du im **Varibale Explorer** eine Tabelle mit 333 Zeilen finden.
Ansonsten versuche:

.. code:: python3

   print(df)


Aufgabe 3: Aggregieren
~~~~~~~~~~~~~~~~~~~~~~

Berechne das mittlere Gewicht der Pinguine nach Spezies:

.. code:: python3

   anzahl = df.groupby("species")["body_mass_g"].mean()

Auch **anzahl** sollte im **Variable Explorer** auftauchen und drei
Zahlen enthalten.

Aufgabe 4: Plotten
~~~~~~~~~~~~~~~~~~

Nun können wir endlich ein Diagramm zeichnen:

.. code:: python3

   anzahl.plot.bar()

Das ist alles! Klicke auf **plots**, und Du solltest ein Säulendiagramm
sehen.

Du kannst es auch abspeichern mit:

.. code:: python3

   plt.savefig("pinguin_gewichte.png", dpi=150)

Aufgabe 5: Weitere Plots
~~~~~~~~~~~~~~~~~~~~~~~~

Probiere folgendes aus:

-  aggregiere über andere Spalten als ``body_mass_g``
-  ersetze die **Aggregatfunktion** ``.mean`` durch ``median``, ``std``, ``count``, ``min`` oder ``max``
-  ersetze die Funktion zum Plotten durch ``barh``, ``pie`` oder ``line``


.. |image0| image:: kanagawa.png

