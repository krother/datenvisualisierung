
Karten mit Markern
==================

Die Bibliothek folium
---------------------

`folium` ist eine Python-Bibliothek zum Plotten von Karten, die auf der JavaScript-Bibliothek **leaflet** aufsetzt (daher der Name).
`folium` verwendet Kartenteile von `OpenStretMap <https://www.openstreetmap.org>`__
und produziert HTML-Dokumente:

Instlliere `folium` mit `pip` aus dem **Anaconda Prompt**:

.. code::

   pip install folium


Eine Karte zeichnen
-------------------

Du benötigst Koordinaten im Format **(Breitengrad, Längengrad)**:


.. code:: python3

   import folium

   coord = (52.515, 13.35)
   berlin = folium.Map(location=coord, zoom_start=14)

   folium.Marker(
      (52.5158645, 13.3773881),
      popup="Brandenburger Tor",
      icon=folium.Icon(icon="map-marker", color="blue"),
   ).add_to(berlin)

   folium.Marker(
      (52.5129613,13.3487917),
      popup="Siegessäule",
      icon=folium.Icon(icon="map-marker", color="blue"),
   ).add_to(berlin)

In Jupyter kannst Du Dir die Karte direkt anzeigen lassen:

.. code::

    berlin

Abspeichern
-----------

You can save the map to a HTML file:

.. code::

   berlin.save("berlin.html")

:download:`[Beispielskript zum Download] <map_markers.py>`

.. seealso:

   Doku zu folium: `python-visualization.github.io/folium/quickstart.html <https://python-visualization.github.io/folium/quickstart.html>`__
