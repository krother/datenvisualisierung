
Deskriptive Statistik
=====================

Ein sinnvoller Start in die Datenanalyse ist, die Daten mit einigen Kennzahlen zu beschreiben.
Diese sind zusätzlich zu den Abbildungen sinnvoll.
Wenn Du die Kennzahlen für mehrere Spalten oder Untergruppen berechnest, kannst Du daraus auch gut ein eigenes Diagramm entwickeln.

Beispieldaten
-------------

Die Bibliothek `seaborn` enthält einen Datensatz von 333 Pinguinen, der als Übungsbeispiel herhalten muss.
Lade ihn mit:

.. code:: python3

   import seaborn as sns

   df = sns.load_dataset("penguins")

Lagemaße
--------

Die Lagemaße beschreiben, wo sich die Mitte einer einzelnen Variable (eine Spalte) befindet.
Drei Maße sind üblich:

Arithmetisches Mittel
+++++++++++++++++++++

Das **arithmetische Mittel** ist die Summe aller Werte geteilt durch deren Anzahl:

.. code:: python3

   df["bill_length_mm"].mean()

Oft ist es sinnvoll, die Metrik für mehrere Kategorien zu berechnen:

.. code:: python3

   df.groupby("species")["bill_length_mm"].mean()

.. note::

    ``pandas`` gibt stets die maximale Anzahl Dezimalstellen aus.
    In einem Bericht ist das aber irreführend.
    Runde daher das Ergebnis mit ``.round(2)`` auf eine Anzahl Nachkommastellen.

Median
++++++

Der **Median** sortiert die Daten und verwendet den Punkt in der Mitte (oder den Mittelwert der beiden Punkte falls deren Anzahl gerade ist):

.. code:: python3

    df["bill_length_mm"].median()

Der Median ist weniger anfällig für Ausreißer als das arithmetische Mittel.

Modus
+++++

Der Modus ist der häufigste Wert einer Variable.
Er macht nur Sinn, wenn Deine Variable **diskret** ist (eine ganze Zahl, eine ordinale oder kategorische Variable).
Es kann auch mehrere Modi geben.

.. code:: python3

    df["species"].mode()

Mit einer Fließkommazahl ist ein Histogramm die bessere Wahl:

.. code:: python3

    df["bill_length_mm"].hist(bins=20)



Streumaße
---------

Ein zweiter Aspekt einer Variable ist, wie weit diese um die Mitte streut.
Auch hier gibt es drei wichtige Maße:

Spannweite
++++++++++

Die **Spannweite** ist der Abstand zwischen dem kleinsten und größten Wert.

.. code:: python3
 
   range = df["bill_length_mm"].max() - df["bill_length_mm"].min()

Standardabweichung
++++++++++++++++++

Die Standardabweichung ist etwas weniger anfällig für Ausreißer, aber auch weniger intuitiv:

.. math::

    sd = \sqrt{\frac{1}{n} \sum_i (x_i - \bar x)^2}

Etwa 67% der Werte liegen innerhalb der einfachen Standardabweichung, falls die Variable annähernd normalverteilt ist.

.. code:: python3

   df["bill_length_mm"].std()

Die Standardabweichung ist auch die Quadratwurzel der **Varianz**.

Quartile
++++++++

**Quartile** sind Bereiche, in denen jeweils **25%** der Daten liegen.
Du kannst sie alle mit einer einzigen Funktion berechnen:

.. code:: python3

   df["bill_length_mm"].describe()
