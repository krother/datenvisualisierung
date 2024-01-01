
Hochwertige Abbildungen
=======================

Hier findest Du ein Kochrezept, um qualitativ hochwertige Abbildungen zu erzeugen.

Schritt 1: Pakete importieren
-----------------------------

Importiere folgende Bibliotheken:

.. code:: python

   import pandas as pd
   import seaborn as sns
   from matplotlib import pyplot as plt


Schritt 2: Beginne mit sauberen Daten
-------------------------------------

Viele Probleme beim Plotten entstehen, weil die Daten unsauber sind.
Stelle sicher, dass Dein Datensatz sauber und konsistent ist:

* alle Spalten haben sinnvolle Namen
* der Zeilen haben sinnvolle Namen (das können aufsteigende Zahlen oder Text sein; bei Zeitreihen gehören Zeitstempel in den Index)
* prüfe die Datentypen der Spalten, die Du plotten möchtest
* es sollte wenig leere Werte geben
 
Pandas wirft beim Plotten Zeilen mit fehlenden Daten heraus.
Du möchtest trotzdem wissen, was passiert.

Wenn Du erst einmal herumprobieren möchtest, fange mit einem sauberen Beispieldatensatz an:

.. code:: python

   df = sns.load_dataset("penguins")


Schritt 3: Standardplot
-----------------------

Verwende eine Standardfunktion aus `seaborn`, um zu sehen ob die Daten wirklich das zeigen was Du Dir gedacht hast.
Die meisten Paarameters von `seaborn` sind Spaltennamen:

.. code:: python

   sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm')

Zum Verbessert des Diagramms verwenden wir `matplotlib`, eine Bibliothek die von `pandas` und `seaborn` hinter den Kulissen sowieso verwendet wird.


Schritt 4: Achsen formatieren
-----------------------------

Du solltest die Achsen so einstellen, dass auf allen Seiten etwas Platz ist.
Das Diagramm wird dadurch übersichtlicher.
Jede Achse braucht eine Beschriftung.

.. code:: python

   sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm')
   plt.xlim(-10, 110)
   plt.ylim(-10, 110)
   plt.xticks(color="white")
   plt.yticks(color="white")
   plt.tick_params(color="white")
   plt.xlabel("Schabellänge [mm]", color="white")
   plt.ylabel("Schnabelbreite [mm]", color="#ffffff")


Schritt 5: Gitterlinien
-----------------------

Mit Gitterlinien sind einzelne x/y-Werte leichter zu erkennen.

.. code:: python

   sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm')
   plt.grid()


Schritt 6: Markante Punkte markieren
------------------------------------

Du kannst einzelne Punkte besonders hervorheben, z.B. mit einem Pfeil:

.. code:: python
   
   sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm')
   plt.annotate('black hole $\epsilon_{23}$',
                xy=(50, 5),
                xycoords='data',
                xytext=(-90, -50),
                textcoords='offset points',
                fontsize=12,
                color="red",
                arrowprops={
                    'arrowstyle': "->",
                    'connectionstyle': "arc3,rad=.2",
                    'color': "red"
                })


Schritt 7: Titel
----------------

Ein Titel ist für das Verständnis wichtig.
Verwende eine Überschrift, wenn Du das Diagramm einzeln verschicken möchtest.
Wenn Du es in ein Dokument einbindest, ist eine Bildunterschrift (im Schreibprogramm) wohl besser.

.. code:: python

   sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm')
   plt.title('Panda sector x/y projection', color="black")


Schritt 8: Größe
----------------

Du kannst eine größer Abbildung wählen.
Die Größe wird aus historischen Gründen in Zoll angegeben.

.. code:: python

   plt.figure(figsize=(11, 7))
   sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm')


Schritt 9: Bild exportieren
---------------------------

Als letzten Schritt solltest Du das Bild als Bilddatei exportieren.
Hier kannst Du auch die Auflösung in Pixeln festlegen.
Dazu dient die Angabe `dpi` (dots per inch).
Die finale Größe berechnet sich also aus `figsize` und `dpi`:

Matplotlib kann viele Bildformate exportieren, darunter png, jpg und svg.

.. code:: python

   sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', size='flipper_length_mm')
   plt.savefig("abbildung_1.png")
