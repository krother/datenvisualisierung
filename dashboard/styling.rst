Layout und Styling
==================


Markdown
--------

In der ``st.write("Text")``-Anweisung kannst Du Text mit **Markdown** formatieren.
Folgendes sind häufige Formatierungselemente:

::

   # Überschrift 1

   ## Überschrift 2

   Dieser Text ist **fett**, dieser *kursiv*.

   - eins
   - zwei
   - drei

   [Wikipedia](https://www.wikipedia.org)

.. seealso::

   Auf der Seite `Daring Fireball <https://daringfireball.net/projects/markdown/basics>`__ findest Du eine ausführlichere Übersicht zu Markdown.

Bilder
------

Bilder lassen sich mit der Funktion ``st.image()`` einbinden:

.. code:: python3

   st.image("mein_bild.png")


Mehrere Tabs
------------

Du kannst mehrere Tabs definieren, in denen jeweils etwas unterschiedliches zu sehen ist.
Dabei definiert die Funktion ``st.tabs`` welche Tabs es gibt.
Jeder ``with..``-Block definiert was in dem jeweiligen Tab zu sehen sein soll.

.. code:: python3

   tab1, tab2, tab3 = st.tabs(["Bananen", "Orangen", "Melonen"])

   with tab1:
       st.write("# Alles über Bananen")
       ...

   with tab2:
       st.write("# Alles über Orangen")
       ...


Unterseiten
-----------

Du kannst eine Streamlit-App auch auf mehrere Unterseiten verteilen.
Erstelle dazu einige minimalistische Seiten in .py-Dateien wie diese:

::

   import streamlit as st

   st.write("""

   # Unterseite 1

   Hallo von Seite 1
   """)

Platziere die zusätzlichen .py-Dateien in einem Ordner ``pages/``, in
dem auch eine ``main.py`` mit der Startseite liegt.

Alles andere passiert automatisch. Streamlit sollte ein Menü mit den Seiten generieren.

Streamlit Thema
---------------

Du kannst die Farben für die gesamte Applikation recht einfach über RGB-Farbcodes einstellen.
Erstelle dazu im Projektordner eine Datei ``.streamlit/config.toml`` mit folgendem Inhalt:

::

   [theme]
   primaryColor="#F63366"
   backgroundColor="#FFFFFF"
   secondaryBackgroundColor="#F0F2F6"
   textColor="#262730"
   font="sans serif"

.. seealso::

   `Streamlit Doku <https://docs.streamlit.io/library/advanced-features/theming>`__
