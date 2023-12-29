Zeilen und Spalten auswählen
============================

Namen von Spalten anzeigen
--------------------------

Du kannst Dir die Spaltennamen eines DataFrames als Liste anzeigen lassen:

.. code:: python

   df.columns

.. warning::

   Manchmal ist es wichtig zu wissen, ob eine Spalte ein **String** oder ein **Integer** ist.
   Achte auf Anführungszeichen in den Namen.


Eine Spalte auswählen
---------------------

Einzelne Spalten werden als `pd.Series` zurück gegeben:

.. code:: python

   df['species']


Mehrere Spalten auswählen
-------------------------

Mehrere Spalten erfordern doppelte Klammern.
Die innere Klammer ist eine Liste von Spaltennamen:

.. code:: python

   df[['bill_length_mm', 'bill_depth_mm']]

----

Spalten nach Position auswählen
-------------------------------

Die Python Slice-Notation lässt sich mit `df.iloc` anwenden.
Der erste Teil der Klammer wählt alle Zeilen aus,
der zweite die Spalten 2-5.

.. code:: python

   df.iloc[:, 1:4]

----

Zeilen nach Poistion auswählen
------------------------------

Du kannst den Teil mit den Spalten auch weglassen:

.. code:: python

   df.iloc[10:20]

----

Zeilen nach Index auswählen
---------------------------

Falls der Index eines DataFrames etwas anderes als Zahlen enthält, ist folgende Phrase sehr nützlich:

.. code:: python

   byspecies = df.set_index('species')
   byspecies.loc['Adelie']

----

Nach Werten filtern
---------------

Die Zeilen eines `DataFrame` lassen sich nach unterschiedlichen Kriterien filtern:

.. code:: python

   df[df['species'] == 'Gentoo']

   df[df['bill_length_mm'] < 45]

   df[df['bill_length_mm'].between(40, 44)]

   df[(df['bill_length_mm'] < 45) & (df['gender'] == "F")]

Das `&` ist der binäre UND-Operator. Es gibt auch ein binäres ODER (`|`).


Zufällige Zeilen
----------------

.. code:: python

   df.sample(7)
