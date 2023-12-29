
Passagiere auf der Titanic
==========================

In dieser Übung visualisierst Du die Passagierliste der Titanic.

Lade die Daten mit Python:

.. code:: python3
   
   import seaborn as sns

   df = sns.load_dataset('titanic')

Löse die folgenden Aufgaben:


Aufgabe 1
---------

Erstelle ein Balkendiagramm, auf dem die Anzahl der Passagiere
in der ersten, zweiten und dritten Klasse zu sehen ist.

Aufgabe 2
---------

Plotte ein Histogramm der Spalte `age`.

Aufgabe 3
---------

Stelle das Histogramm mit 20 bins dar.


Aufgabe 4
---------

Erstelle einen Box-Plot aus der Spalte `age`.


Aufgabe 5
---------

Erstelle einen Scatterplot des Fahrpreises (`fare`) über das Alter (`age`).


Aufgabe 6
---------

Erstelle ein Balkendiagramm, auf dem die Anzahl der überlebenden und gestorbenen Passagiere zu sehen ist.
Für jedes Geschlecht soll es eine eigene Balkengruppe geben.


Aufgabe 7
---------

Erstelle eine Heatmap aus der Korrelationsmatrix aller Spalten.
Die Korrelationsmatrix erhälst Du mit:

.. code:: python3

   cm = df.corr()
