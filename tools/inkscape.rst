.. _Inkscape:
.. _Inkscape-Tool:

Inkscape
========

`Inkscape <http://inkscape.org/?lang=de>`__ ist ein umfangreicher
Vektorgraphik-Editor, der für Windows wie Linux gleichermaßen als
Open-Source-Tool frei verfügbar ist.

Unter Linux lässt sich Inkscape mittels des gleichnamigen Paketes installieren:

.. code-block:: bash

    sudo aptitude install inkscape fonts-mathjax fonts-mathjax-extras

Inkscape bietet bereits in der Grundversion den Import und Export der
gängigsten Graphik-Formate, darunter auch PNG und PDF.


.. _LaTeX-Formeln:

.. rubric:: LaTeX-Formeln einbinden

Möchte man auch LaTeX-Formeln in seine Zeichnungen integrieren, empfielt sich
die ``tex text``-Erweiterung. Sie kann von der `Homepage des Entwicklers
<http://pav.iki.fi/software/textext>`_ heruntergeladen werden. Zur Installation
muss lediglich das Archiv entpackt und der Inhalt in den Ordner
``~/.config/inkscape/extensions`` verschoben oder kopiert werden.

.. code-block:: bash

    tar xvzf textext-0.4.4.tar.gz
    cp textext.py textext.inx ~/.config/inkscape/extensions

Die Erweiterung benötigt mit ``pdf2svg`` und ``pstoedit`` zwei weitere Pakete,
die -- falls sie nicht verfügbar sind -- über die Paketverwaltung
installierbar sind:

.. code-block:: bash

    sudo aptitude install pdf2svg pstoedit

Anschließend kann die Erweiterung in der Menüzeile über ``Erweiterungen -> Tex
Text`` aufgerufen werden.

Zusätzlich kann mittels den "Mathjax"-Schriftfen auch normaler Text in einem
LaTeX-ähnlichen Stil gesetzt werden, um ein einheitliches Schriftbild im
Dokument zu erreichen.

.. Inkscape-Aufruf mit Option -l neuer-dateiname: Export als Plain SVG (kleiner!)

.. rubric:: Einheiten des Lineals und des Gitters anpassen

Die beiden Lineal-Leisten am linken und oberen Rand des Hauptfensters zeigen
Längen standardmäßig in Pixeln an. Um dies zu ändern, muss man in den
Dokumenteigenschaften (Tastenkürzel ``Ctrl D``) unter der Rubrik "Seite"
als Standard-Einheiten ``cm`` (oder ``mm``) einstellen.

Die Einstellungen des Gitters können im Menü über ``Datei ->
Inkscape-Einstellungen`` unter der Rubrik "Gitter" geändert werden. Ich selbst
verwende folgende Einstellungen:

.. figure:: gitter-einstellungen.png
    :name: fig-gitter-einstellungen
    :alt:  fig-gitter-einstellungen
    :align: center
    :width: 50%

Bei diesen Einstellungen werden die Gitterlinien (Tastenkürzel ``#``) bei
Vollansicht des gesamten Dokuments (bei mir meist DinA4, Tastenkürzel ``5``)
in ``cm``-Rasterung angezeigt; zoomt man näher in einen Bereich hinein, wechselt
die Rasterung auf ``mm``.

.. _Multilayer-SVG:
.. rubric:: Multilayer-SVG-Dateien exportieren

Leider unterstützt SVG (noch) keine Multipage-Dokumente. Man kann sich jedoch
damit behelfen, indem man für jede neue Seite eine neue Ebene ("Layer")
erstellt. Hierfür kann man das Menü ``Ebene`` nutzen, oder mit ``Ctrl L`` das
Ebenen-Werkzeug am rechten Bildschirmrand einblenden.

Während in PDF-Dateien die Seiten von vorne nach hinten nummeriert werden (in
Anzeigeprogrammen bzw. Inhaltsverzeichnissen von oben nach unten), so werden in
Inkscape die einzelnen Ebenen von unten nach oben nummeriert. Die zuletzt
hinzugefügte "Schicht" ist somit die oberste. Man kann die einzelnen Ebenen im
Ebenenwerkzeug leicht nach unten und oben verschieben, sollte aber auf die
passende Reihenfolge achten, wenn man die einzelnen Schichten als jeweils neue
Seiten einer PDF-Datei exportieren möchte.

Ein solcher Export einer mit Inkscape erstellten Multilayer-SVG-Datei in eine
Multipage-PDF-Datei ist dank des Skripts `svglayers2pdfpages.sh
<http://www.grund-wissen.de/_downloads/svglayers2pdfpages.sh>`_ von `Christoph
Haag <http://www.lafkon.net>`_  möglich: Gibt man im Verzeichnis der zu
exportierenden SVG-Datei ``svglayers2pdfpages.sh svgfile.svg`` ein, so wird im
gleichen Verzeichnis eine gleichnamige PDF-Datei erzeugt.

.. _Inkscape-Links:

.. rubric:: Links

* `Inkscape-Projektseite <http://inkscape.org/?lang=de>`_

Am besten lernt man Inkscape -- wie so oft -- mittels "Learning by doing".
Begleitend sind dabei z.B. folgende Tutorials hilfreich:

* `Inkscape-Wikibook <https://de.wikibooks.org/wiki/Inkscape>`_
* `Inkscape-Einführung der Universität Göttingen <http://lp.uni-goettingen.de/get/text/6356>`_
* `Offizielles Inkscape-Wiki <https://www.inkscape-forum.de/>`_
* `Inkscape-Crashcourse <http://www.chrishilbig.com/a-crash-course-in-inkscape/>`_
* `Guide to a Vector Drawing Program (en.) <http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.html>`_
* `Quick Guide to Inkscape (en.) <http://www.microugly.com/inkscape-quickguide/>`_

Einfache bis komplexere Beispiele finden sich als zusätzliche Anregungen auf
folgenden Seiten:

* `Guide to a vector drawing program (en.) <http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.html>`_
* `35 Tutorials to create vector graphics (en.) <http://speckyboy.com/2009/04/28/35-tutorials-to-create-amazing-vector-graphics-using-inkscape/>`_
* `Drawing Gears (en.) <http://howto.nicubunu.ro/gears/>`_


..  `Inkscape Tutorial List (en.) <http://inkscapetutorials.wordpress.com/suggest-a-tutorial/tutorial-list/>`_
..  rainbow: http://art.vinayraikar.com/2008/01/illustrating-rainbow-with-tiled-clones.html
..  Unbedingt lesen: FUN WITH GLASSES http://howto.nicubunu.ro/glass_shadow_inkscape/
..  shiny buttons | http://howto.nicubunu.ro/shiny_web_buttons_inkscape/
..  hackergochi | http://howto.nicubunu.ro/shiny_web_buttons_inkscape/
..  using brushes | http://howto.nicubunu.ro/inkscape_brushes/
..  photo to jigsaw puzzle | http://howto.nicubunu.ro/gimp_jigsaw_puzzle/
