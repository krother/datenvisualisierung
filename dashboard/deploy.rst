
Streamlit Cloud Deployment
==========================

In der **Streamlit Community Cloud** kannst Du ein Dashboard öffentlich verfügbar machen, so dass andere es sehen können.

Schritt 1: GitHub
-----------------

Erstelle einen Acount auf `GitHub <https://www.github.com/>`__ .
Dort wird der Code liegen.

Schritt 2: Community Cloud
--------------------------

Gehe auf `streamlit.io <https://streamlit.io/>`__ und wähle **Community Cloud**.

Logge Dich über Github ein und gib Streamlit die nötigen Berechtigungen.


Schritt 3: App
--------------

Erstelle eine neue App.
Wähle dazu **"from sample app template"** aus.

Sobald die Streamlit App in der Community Cloud eingerichtet ist, solltest Du einen Link angezeigt bekommen, auf dem zunächst eine Dummy-Seite zu sehen ist.

Schritt 4: Code
---------------

Finde das von Streamlit neu erstellte Repository auf deinem GitHub Account.

Lade Deine Daten und das streamlit Python Skript hoch.


Schritt 5: Requirements
-----------------------

Es sollte auf GitHub eine Datei ``requirementst.txt`` geben.
Dort stehen alle benötigten Python-Bibliotheken.
Mindestens die folgenden Zeilen sollten dort enthalten sein:

::

   seaborn
   pandas
   matplotlib
   streamlit
