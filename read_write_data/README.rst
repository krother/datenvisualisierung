Daten lesen und schreiben
=========================

CSV Dateien einlesen
--------------------

Die Funktion ``pd.read_csv`` wird oft als allererstes verwendet.
Sie enthält eine Menge optionaler Parameter, von denen hier drei vorgestellt werden:

.. code:: python

   import pandas as pd

   df = pd.read_csv(r'penguins.csv', index_col=0, sep=',', header=True)

Die erste Spalte (`0`) wird als Index verwendet, die erste Spalte als Kopfzeilen.

.. hint::

   Das ``r`` vor dem Dateinamen erlaubt es, einen vollständigen Windows-Pfad einzugeben.
   Sonst erkennt Python nämlich die Backslashes nicht als Pfadtrenner.


Excel-Tabellen einlesen
-----------------------

Excel-Tabellen lassen sich fast genauso einlesen:

.. code:: python

   df = pd.read_excel('penguins.xlsx', index_col=0)

Falls die Spaltennamen Zahlen sind, werden sie in Integers umgewandelt.
Bei `pd.read_csv()` sind die Spaltennamen stets Strings.


Read JSON
---------

JSON-Dokumente lassen sich problemarm einlesen, falls sie eine tabellenähnliche Struktur aufweisen:

.. code:: python

   df = pd.read_json('penguins.json') 


Einlesen aus der Zwischenablage
-------------------------------

Wenn du mit Strg-C Daten kopiert hast (z.B. auf einer Webseite), kannst du diese schnell in Python importieren.

.. code:: python

   df = pd.read_clipboard()


Dateien schreiben
-----------------

Das Schreiben von Daten in eine Datei ist einfacher. Hier drei Beispiele:

.. code:: python

   df.to_csv("output.csv")
   df.to_excel("output.xlsx")
   df.to_json("output.json")
