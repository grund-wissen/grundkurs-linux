.. _Zusätzliche Shell-Programme:

Zusätzliche Shell-Programme
===========================

Die folgenden, meiner Meinung nach durchaus nützlichen Programme sind auf frisch
installierten Systemen zwar (meist) nicht von Grund auf enthalten, lassen sich
jedoch einfach mittels der Paketverwaltung nachinstallieren.

.. index:: abcde
.. _abcde:

``abcde``
---------

``abcde`` steht für "A better CD encoder" und bietet in der Tat eine elegante
Möglichkeit, eine Audio-CD automatisch als ``ogg`` oder ``mp3``-Dateien
einzulesen.

``abcde`` ist über die Paketverwaltung mittels des gleichnamigen Pakets
installierbar:

.. code-block:: bash

    sudo aptitude install abcde

Nach dem Einlegen einer Audio-CD und dem Aufruf von ``abcde`` wird eine
CD-Datenbank durchsucht und gegebenenfalls passende Einträge angezeigt. Nach
Wunsch können die Meta-Daten noch bearbeitet werden, ansonsten wird nach
Bestätigung mit ``Enter`` automatisch der Einlese- und Kodierungsprozess
gestartet.

Mehr Infos zu ``abcde`` gibt es unter `Abcde im Ubuntu-Wiki
<http://wiki.ubuntuusers.de/abcde>`_.

.. index:: antiword
.. _antiword:

``antiword``
------------

Mit ``antiword`` lassen sich MS-Word-Dokumente (``.doc``) bequem in einem
Shell-Fenster als Textform anzeigen.

``antiword`` kann mittels der Paketverwaltung ``aptitude`` einfach installiert
werden:

.. code-block:: bash

    sudo aptitude install antiword

Die Ausgabe eines Word-Dokuments auf dem Bildschirm lässt sich dann
folgendermaßen erreichen:

.. code-block:: bash

    antiword file.doc

Die Ausgabe kann selbstverständlich auch in eine Textdatei umgeleitet werden:

.. code-block:: bash

    antiword file.doc > file.txt

Das erspart oftmals ein Öffnen von Libre-Office, Abiword oder dergleichen.. ;-)


.. index:: cmus
.. _cmus:

``cmus``
--------

Der Console-Music-Player ``cmus`` bietet eine schlichte und übersichtliche
Bedienoberfläche, um alle gängigen Audio-Formate (``ogg``, ``mp3``, ``wav``,
``flac``, ``aac``) sowie Playlisten (``m3u`` und ``pls``) innerhalb eines
Shell-Fensters abzuspielen.

``cmus`` ist über die Paketverwaltung mittels des gleichnamigen Pakets installierbar:

.. code-block:: bash

    sudo aptitude install cmus

Anschließend kann der Player durch den Aufruf von ``cmus`` gestartet werden.
Mittels der Tasten ``1`` bis ``7`` kann zwischen verschiedenen Ansichten
gewechselt werden:

.. list-table::
    :name: tab-cmus-ansichten
    :widths: 10 30 120

    * - ``1``
      - Bibliothek
      - Zweispaltige Ansicht: Links werden Künstler und Album aufgelistet, rechts die jeweiligen Lieder
    * - ``2``
      - Sortierte Bibliothek
      - (Flache Listenansicht aller Lieder, mit der Möglichkeit, die Sortierreihenfolge selbst festzulegen)
    * - ``3``
      - Wiedergabeliste
      - Anzeige der (editier- und speicherbaren) Wiedergabeliste
    * - ``4``
      - Warteliste (Queue)
      - Anzeige der unmittelbar abzuspielenden Lieder
    * - ``5``
      - Datei-Browser
      - Dateisystemansicht mit der Möglichkeit zum Hinzufügen von Liedern zur Sammlung, der Wiedergabeliste oder Warteliste
    * - ``6``
      - Datei-Filter
      - Anzeige benutzerdefinierter Filter
    * - ``7``
      - Einstellungen
      - Mit ``d`` kann man Einstellungen löschen, mit ``Enter`` modifizieren sowie
        mit ``Leertaste`` konkrete Variablen ändern.

Beim erstmaligen Starten von ``cmus`` sollte zunächst ein Verzeichnis mit
Audio-Dateien in die Bibliothek geladen werden. Hierfür wechselt man mittels
``:`` auf die Kommandozeile und gibt dort folgende Anweisung ein: [#]_

.. code-block:: bash

    :add ~/Musik

Nachdem die Sammlung eingelesen wurde, werden die Lieder in den
Bibliotheks-Ansichten ``1`` und ``2`` den Namen der Interpreten sortiert
angezeigt.

In den einzelnen Ansichten (``1`` bis ``5``) können mittels der jeweiligen
Tasten folgende Funktionen aufgerufen werden:

.. list-table::
    :name: tab-cmus-tasten
    :widths: 10 50

    * - ``Enter``
      - Datei abspielen beziehungsweise Verzeichnis öffnen
    * - ``c``
      - Pause-Modus an- und ausschalten ("continue")
    * - ``b``
      - Nächsten Titel abspielen
    * - ``/``
      - nach Suchmuster in Dateinamen oder ID-Tags suchen
    * - ``n``
      - zur nächsten Datei gehen, auf die Suchmuster zutrifft
    * - ``N``
      - zur vorherigen Datei gehen, auf die Suchmuster zutrifft
    * - ``y``
      - Datei oder Verzeichnis unter Cursor zur Wiedergabeliste (``3``) hinzufügen
    * - ``e``
      - Datei oder Verzeichnis unter Cursor an die Warteliste (``4``) anfügen
    * - ``E``
      - Datei oder Verzeichnis unter Cursor an den Anfang der Warteliste (``4``) setzen
    * - ``a``
      - Datei oder Verzeichnis unter Cursor in die Bibliothek (``1`` bzw. ``2``) aufnehmen
    * - ``-``
      - Lautstärke um 10% herabsetzen
    * - ``+``
      - Lautstärke um 10% erhöhen
    * - ``,``
      - Aktuell abgespielte Datei 1 Minute zurückspulen
    * - ``.``
      - Aktuell abgespielte Datei 1 Minute vorspulen
    * - :math:`\leftarrow`
      - Aktuell abgespielte Datei 5 Sekunden zurückspulen
    * - :math:`\rightarrow`
      - Aktuell abgespielte Datei 5 Sekunden vorspulen

In der Infozeile (vorletzte Zeile auf dem Bildschirm) werden auf der rechten
Seite Infos über die aktuellen Wiedergabeoptionen (Zufallswiedergabe,
Wiederholung usw.) eingeblendet. Diese können folgendermaßen verändert
werden: [#]_

.. list-table::
    :name: tab-cmus-wiedergabe
    :widths: 10 50

    * - ``s``
      - Zufallswiedergabe aktivieren oder deaktivieren
    * - ``r``
      - Wiedergabe-Modus (der ganzen Playliste bzw. des aktuellen Albums)
        aktivieren oder deaktivieren
    * - ``Ctrl r``
      - Wiederholung des aktuellen Lieds aktivieren oder deaktivieren


Um Dateien innerhalb der Wiedergabeliste oder Warteliste nach oben oder unten zu
verschieben, können die Tasten ``p`` und ``P``  ("push") genutzt werden:

.. list-table::
    :name: tab-cmus-p-tasten
    :widths: 10 50

    * - ``p``
      - Datei unter Cursor in der Ansicht ``3`` oder ``4`` nach unten
        verschieben
    * - ``P``
      - Datei unter Cursor in der Ansicht ``3`` oder ``4`` nach oben
        verschieben

Markiert man hierbei zunächst mehrere Dateien mittels der ``Space``-Taste, so
können diese anschließend mittels ``p`` oder ``P`` hinter beziehungsweise vor
die Datei unter dem Cursor verschoben werden. Mit ``D`` oder ``Del`` können
Dateien wieder aus der Wiedergabe- oder Warteliste entfernt werden.

.. Titel von vorne abpsielen: ``v c``.

..  Um die in der Bibliotheks-Ansicht ``1`` jeweiligen Alben angezeigt zu
..  bekommen, muss man ``Leertaste`` drücken.

Mehr Infos gibt es unter `CMUS im Ubuntuuser-Wiki
<http://manpages.ubuntu.com/manpages/natty/man1/cmus.1.html>`_.


.. index:: fdupes
.. _fdupes:

``fdupes``
----------

Mit ``fdupes`` kann man ein Verzeichnis nach doppelten Dateien durchsuchen und
diese gegebenenfalls auflisten.

Das Programm kann mittels ``apt`` über das gleichnamige Paket installiert
werden:

.. code-block:: bash

    sudo aptitude install fdupes

Aufgerufen wird ``fdupes`` mit folgender Syntax:

.. code-block:: bash

    fdupes verzeichnis

Verglichen werden die Dateien des Verzeichnisses dabei zunächst anhand ihrer
Größe, anschließend anhand eines Byte-für-Byte-Vergleichs; ``fdupes`` erkennt
damit auch identische, aber unterschiedlich benannte Dateien (unabhängig vom
Dateiformat). Mit ``fdupes -r verzeichnis`` werden auch die Unterverzeichnisse
rekursiv mit durchsucht, mit der Option ``-s`` können zusätzlich auch Symlinks
zu Verzeichnissen berücksichtigt werden.


.. index:: feh
.. _feh:

``feh``
-------

Feh ist ein kleines, aber feines Bildbetrachtungs-Programm. Es kann über das
gleichnamige Paket mittels der Paketverwaltung installiert werden:

.. code-block:: bash

    sudo aptitude install feh

``feh`` setzt eine aktive graphische Oberfläche voraus, kann also nicht als
"reines" Shell-Programm (ohne X-Server) verwendet werden. (Für derartige
Anwendungen kann jedoch auf das Framebuffer-Image-Programm ``fbi``
zurückgegriffen werden.)

Der grundlegende Aufruf von ``feh`` sieht folgendermaßen aus:

.. code-block:: bash

    feh image-file

Um alle Bilder des aktuellen Verzeichnisses anzusehen, genügt folgender Aufruf:

.. code-block:: bash

    feh *

``feh`` kann auf einfache Weise über die Tastatur gesteuert werden:

* Mittels der Pfeiltasten :math:`\leftarrow` und :math:`\rightarrow` kann,
  sofern mehrere Bilder geöffnet werden, zum vorherigen bzw. nächsten Bild
  gewechselt werden.
* Mittels der Pfeiltasten :math:`\uparrow` und :math:`\downarrow` wird in das
  Bild hinein- bzw. herausgezoomt.
* Mittels ``v`` kann zwischen einer Vollbild- und einer normalen Anzeige
  gewechselt werden.
* Mittels ``<`` und ``>`` kann ein Bild gegen bzw. mit dem Uhrzeigersinn um 90°
  gedreht werden.
* Mittels ``q`` ("quit") wird ``feh`` beendet.

``feh`` kann mit einer Vielzahl an Parametern aufgerufen werden, um
beispielsweise die geöffneten Bilder als Slideshow wiederzugeben. Hilfreich sind
insbesondere die beiden Parameter ``-d`` und ``-F``, mittels derer ``feh``
automatisch im Vollbild-Modus startet (``feh -F``) und den aktuellen Datei-Namen
anzeigt (``feh -d``). Um beide Optionen als Standard zu definieren, bietet sich
in der Konfigurationsdatei ``~/.bashrc`` folgendes Alias an:

.. code-block:: bash

    alias feh='feh -d -F'

Nach einem neuen Laden der Konfigurationsdatei (``source ~/.bashrc``) bzw. in
jedem neu geöffneten Shell-Fenster wird ``feh`` anschließend automatisch mit den
beiden obigen Parametern gestartet.

Weitere Infos finden sich in den ``man``-Pages und unter `Feh im Ubuntu-Wiki
<http://wiki.ubuntuusers.de/Feh>`_.


.. _gpg:

``gpg``
-------

GPG (GNU Privacy Guard) ist ein freies Verschlüsselungssystem, welches
hauptsächlich für die Verschlüsselung von Emails benutzt wird. GPG gehört zu
allen Standard-Linux-Distributionen und ist auch auf einer Vielzahl anderer
Systeme lauffähig.

Bei erstmaliger Verwendung von GPG werden zwei Schlüssel erzeugt: Ein
öffentlicher Schlüssel ("Public Key"), der beliebig verschickt werden kann, und
ein privater Schlüssel ("Private Key"), den nur der Besitzer kennt. Das
Verschlüsseln einer Nachricht oder Datei erfolgt dann mittels des öffentlichen
Schlüssels des Empfängers; entschlüsselt werden kann die Nachricht wiederum nur
mit dem privaten Schlüssel des Empfängers.

Umfangreiche Infos zu ``gpg`` gibt es im `GPG-Tutorial
<http://www.online-tutorials.net/security/gnupg-gpg-tutorial/tutorials-t-69-124.html>`_
und in der `ausführlichen GPG-Anleitung
<http://wiki.kairaven.de/open/krypto/gpg/gpganleitung>`_.

.. index:: Imagemagick
.. _imagemagick:

``imagemagick``
---------------

Bei Imagemagick handelt es sich um eine Sammlung von mehreren kleinen
Bildbearbeitungs-Programmen, mit deren Hilfe einfache Anpassungen von
Graphiken -- z.B. Formatumwandlungen, Erzeugung von kleinen Vorschaubildern,
Fotomontagen u.ä. -- stapelweise als Shell-Skript auf eine Vielzahl von
Dateien anwenden lassen.

Sollte ``imagemagick`` nicht bereits installiert sein, lässt es sich einfach
mittels ``aptitute`` nachinstallieren:

.. code-block:: bash

    sudo aptitute install imagemagick

.. index:: convert

Die Imagemagick-Suite umfasst folgende Bildbearbeitungs-Programme:

.. hlist::
    :columns: 2

    * ``import``
    * ``convert``
    * ``montage``
    * ``display``

Diese kleinen Hilfsprogramme sind nützlich, um automatisiert bestimmte
Bildbearbeitungen als Skript auszuführen.

*Beispiele:*

* Umwandeln eines transparenten in einen weißen Hintergrund:

  .. code-block:: bash

      convert image-old.png -background white -flatten -alpha off image-new.png

  ..  http://stackoverflow.com/questions/5280118/convert-png-to-jpg-and-set-transparent-background-to-white-with-imagemagick-and

* Zusammenfügen mehrere Bilder vertikal zu einem "Filmstreifen":

  .. code-block:: bash

      montage -mode concatenate -tile 1x in-*.jpg out.jpg

  ..  http://superuser.com/questions/290656/combine-multiple-images-using-imagemagick

* Verkleinern von Digitalkamera-Fotos auf kleine Formate, beispielsweise Fotos
  von Rezepten für's `Vegan-Kochbuch
  <http://www.grund-wissen.de/veganes-leben/rezepte/index.html>`_:

  .. only:: html

      .. code-block:: bash

        for i in *.jpg ; do convert $i -resize '1200x800' -quality 80 $(basename $i .jpg).png ; done

  .. only:: latex

      .. code-block:: bash

        for i in *.jpg ; \
        do convert $i -resize 600 -quality 80 $(basename $i .jpg).png ; \
        done

..  **


  Das obige Mini-Skript wandelt alle ``.jpg``-Dateien des aktuellen
  Verzeichnisses in ``600 px`` breite png-Dateien gleichen Namens um. Die
  Dateien können anschließend mit :ref:`pngnq <pngnq>` weiter komprimiert
  werden.

..  **

..  ``for i in *.jpg ; do convert $i -resize 600 -quality 80 $i-small.png ; done ;``

Mehr Infos zu ``imagemagick`` gibt es unter `Imagemagick im Ubuntu-Wiki
<http://wiki.ubuntuusers.de/ImageMagick>`_.

..  Vegan-Rezept-Bilder komprimieren:


..
..  convert -flatten -background white file.png file.jpg

..  To quantize and compress an image, for example image.png, with the compressed output as smallimage.png, I do this:

..  pngnq -n 256 image.png && pngcrush image-nq8.png smallimage.png

..  This usually results in a greater than 50% compression with a small loss of detail.

.. split pdf in png-images: convert image.pdf +adjoin image.png


.. index:: Midnight Commander, mc
.. _mc:

``mc``
------

Der "Midnight Commander" ``mc`` gilt als einer der praktischsten Dateimanager
überhaupt. Er bietet eine klar strukturierte Bedienoberfläche und ermöglicht es,
Dateien mit nur wenigen Tastendrücken schnell und elegant zu verwalten.

``mc`` ist über die Paketverwaltung mittels des gleichnamigen Pakets
installierbar:

.. code-block:: bash

    sudo aptitude install mc

..  https://www.midnight-commander.org/wiki/doc/filePanels/hotkeys

In der Grundeinstellung sind im Midnight-Commander zwei Ordner-Panele
nebeneinander angeordnet. Zwischen den beiden Panelen (und damit zwischen den
beiden angezeigten Verzeichnissen) kann mittels der ``Tab``-Taste hin- und
hergewechselt werden. In einem Panel lassen sich Dateien folgendermaßen
auswählen:

* Mit den Cursor-Tasten :math:`\uparrow` und :math:`\downarrow` kann in
  Einzelschritten zwischen den Dateien des Panel-Ordners navigiert werden.
* Mit den ``PageUP``- bzw. ``PageDown``-Tasten können umfangreiche Ordner
  seitenweise "durchblättert" werden.
* Mit der ``Home``-Taste gelangt man zum ersten Eintrag eines Verzeichnisses.
  Dieser ist stets ``..`` und ermöglicht durch Bestätigung mit der
  ``Enter``-Taste einen Wechsel in das übergeordnete Verzeichnis.
* Mit der ``End``-Taste gelangt man zum letzten Eintrag eines Verzeichnisses.
* Mit der ``Insert``-Taste können mehrere Dateien ausgewählt oder wieder
  demarkiert werden. Durch einen Wechsel in ein anderes Verzeichnis wird die
  aktuelle Auswahl ebenfalls aufgehoben.

Viele häufig auftretende Aktionen lassen sich mittels der folgenden
Funktionstasten bewerkstelligen:

.. list-table::
    :name: tab-mc-funktionstasten
    :widths: 20 50

    * - ``F3``
      - Ausgewählte Datei(en) mit dem internen Betrachter ("Pager") öffnen.
    * - ``F4``
      - Ausgewählte Datei(en) mit einem Editor öffnen.
    * - ``F5``
      - Ausgewählte Datei(en) vom aktuellen Panel in das gegenüberliegende
        kopieren.
    * - ``F6``
      - Ausgewählte Datei(en) vom aktuellen Panel in das gegenüberliegende
        verschieben.
    * - ``F7``
      - Einen neuen Ordner im Verzeichnis des aktuellen Panels erstellen
    * - ``F8``
      - Ausgewählte Datei(en) und/oder Ordner im aktuellen Panel löschen.
    * - ``F9``
      - Menüzeile anwählen

Über den Bereich "Optionen" der Menüzeile lässt sich der Midnight-Commander
bzgl. Aussehen und Verhalten etwas anpassen. Persönlich halte ich folgende
Anpassungen für sinnvoll:

* Im Bereich "Konfiguration" die Option "Sicheres Löschen" (mittels der
  Leertaste) aktivieren, um nicht eine Datei versehentlich durch Drücken der
  ``Del``-Taste, sondern nur mittels :math:`F8` löschen zu können.
* Im Bereich "Layout" die Menüleiste, Tastenleiste und Informationsleiste
  (mittels der Leertaste) deaktivieren.
* Im Bereich "Paneloptionen" (ebenfalls mittels der Leertaste) "Lynx-artige
  Bewegungen erlauben" aktivieren. Dies erlaubt es, mittels der rechten
  Cursortaste in das ausgewählte Verzeichnis zu wechseln bzw. mit der linken
  Cursortaste das übergeordnete Verzeichnis anzuwählen. Dies funktioniert
  übrigens auch auch mit (komprimierten) Archiv-Dateien!

Weitere nützliche Tastenkombinationen für die Bedienung des ``mc`` sind:

.. list-table::
    :name: tab-mc-tastenkombinationen
    :widths: 25 50

    * - ``Ins``
      - Datei unter Cursor markieren bzw. demarkieren
    * - ``*``
      - Alle Dateien des aktuellen Verzeichnisses markieren bzw. demarkieren
    * - ``+``
      - Dateien nach bestimmten Kriterien markieren
    * - ``\``
      - Dateien nach bestimmten Kriterien demarkieren
    * - ``Ctrl Leertaste``
      - Größe des ausgewählten Verzeichnisses anzeigen
    * - ``Ctrl s Text``
      - Im Aktuellen Verzeichnis zu einer Datei springen, die mit ``Text``
        beginnt. Funktioniert auch mit Verzeichnisnamen. Groß-/Kleinschreibung
        beachten!
    * - ``Esc ?``
      - Im aktuellen Verzeichnis nach Dateien und/oder Inhalten suchen
    * - ``Esc Tab``
      -  Auto-Vervollständigung der Eingabezeile (wie ``Tab`` in einer Shell)
    * - ``Esc t``
      - Zwischen verschiedenen Dateilisten-Layouts wechseln
    * - ``Esc ,``
      - Zwischen horizontaler und vertikaler Fensterteilung wechseln
    * - ``Esc .``
      - Mit ``.`` beginnende Konfigurationsdateien und -verzeichnisse ein- und
        ausblenden
    * - ``Esc Enter``
      - Name der Datei unter dem Cursor in die Eingabezeile kopieren
    * - ``Ctrl x t``
      - Die Namen aller markierten Dateien in die Eingabezeile kopieren
    * - ``Ctrl x Ctrl t``
      - Die Namen aller markierten Dateien der anderen Fensterhälfte in die
        Eingabezeile kopieren
    * - ``Ctrl x p``
      - Den aktuellen Pfadnamen in die Eingabezeile kopieren
    * - ``Ctrl x Ctrl p``
      - Den Pfadnamen der anderen Fensterhälfte in die Eingabezeile kopieren
    * - ``Ctrl a Ctrl k``
      - Die Eingabezeile säubern (an den Anfang gehen und alles bis zum Ende
        löschen).
    * - ``Ctrl O``
      -  Wechsel zwischen Mitnight-Commander und Shell (mit ``mc`` als Background-Job)
    * - ``Ctrl U``
      -  Beide Fensterhälften vertauschen
    * - ``Ctrl \``
      - Verzeichnis-"Hotlist" anzeigen. Hier lassen sich neben lokalen Pfaden
        auch FTP- bzw. SSH-Zugangsadressen speichern bzw. aufrufen
    * - ``Ctrl x Ctrl s``
      - Einen Symlink der ausgewählten Datei (bzw. des ausgewählten Ordners) im
        Pfad der anderen Fensterhälfte erzeugen (anstelle die Datei dorthin zu
        kopieren)
    * - ``Ctrl H``
      - Liste der zuletzt besuchten Verzeichnisse anzeigen. Auswahl mit Pfeiltasten,
        Bestätigen mit ``Enter``
    * - ``Ctrl h``
      - Liste der letzten Eingabezeilen-Befehle anzeigen. Auswahl mit Pfeiltasten,
        Bestätigen mit ``Enter``


.. index:: mencoder
.. _mencoder:

``mencoder``
------------

Das Programm ``mencoder`` kann für vielerlei Arten von Video-Format-Umwandlungen
genutzt werden. Beispielsweise lassen sich damit mehrere Teil-Videos
(beispielsweise ``.flv``- oder ``.mp4``-Dateien von Youtube) folgendermaßen zu
einer einzigen Datei zusammenfügen:

.. code-block:: bash

    mencoder -ovc copy -oac copy -o complete-movie.mp4 part1.mp4 part2.mp4

Mehr Infos gibt es unter `Mencoder im Ubuntuusers-Wiki
<http://wiki.ubuntuusers.de/MEncoder>`_.


.. .. index:: moc
.. .. _moc:

.. ``moc``
.. -------

.. Der "Music on Console Player" ``moc`` bietet eine schlichte und übersichtliche
.. Bedienoberfläche, um alle gängigen Audio-Formate (``ogg``, ``mp3``, ``wave``,
.. ``flac``, ``aac``) sowie Playlisten (``m3u`` und ``pls``) innerhalb eines
.. Shell-Fensters abzuspielen.

.. ``moc`` ist über die Paketverwaltung mittels des Pakets ``moc`` installierbar:

.. .. code-block:: bash

.. sudo aptitude install moc

.. Anschließend kann der Player durch den Aufruf von ``mocp`` (mit ``p``) gestartet
.. werden. Mehr Infos gibt es unter `MOC im Ubuntuuser-Wiki
.. <http://wiki.ubuntuusers.de/MOC_-_music_on_console>`_.

.. Inzwischen verwende ich zum Abspielen von Musik bevorzugt ``cmus``.

.. `MOC-Kurzbeschreibung <http://ikhaya.ubuntuusers.de/2009/06/01/projektvorstellung-moc-music-on-console/>`_

.. index:: ncdu
.. _ncdu:

``ncdu``
--------

Das Programm ``ncdu`` ("ncurses-disk-usage") ermöglicht es zu sehen, welche
Ordner bzw. Dateien am meisten Platz auf der Festplatte benötigen. Ausgehend von
dem Pfad, aus dem heraus ``ncdu`` aufgerufen wird, analysiert es den
Speicherbedarf und gibt eine sortierte, navigierbare Verzeichnisliste zurück.

``ncdu`` ist über die Paketverwaltung mittels des gleichnamigen Pakets
installierbar:

.. code-block:: bash

    sudo aptitude install ncdu

Gibt man nach der Installation ``ncdu`` ein, so wird vom aktuellen Verzeichnis
aus die Größe aller sich darin befindenden Dateien bestimmt; die Größe von
Unterverzeichnissen wird schrittweise anhand der darin enthaltenen Dateien bzw.
Verzeichnisse bestimmt. Als Ergebnis wird der Inhalt des aktuellen
Verzeichnisses nach absteigender Größe sortiert aufgelistet.

Eine Navigation innerhalb dieser Übersicht ist mittels den Pfeiltasten oder, wie
bei :ref:`Vim <Vim>`, mittels ``hjkl`` möglich. Drückt man ``?``, so wird eine
Kurzübersicht der möglichen Eingabetasten eingeblendet, mit ``d`` kann die Datei
unter dem Cursor (nach einer manuellen Bestätigung) gelöscht werden.
Mit ``q`` wird ``ncdu`` wieder beendet.


.. index:: nmap
.. _nmap:

``nmap``
--------

Mit ``nmap`` können unter anderem anderem die Rechner innerhalb des lokalen
Netzwerks mitsamt lokaler Netzwerkadresse aufgelistet werden. Die Syntax hierzu
lautet:

.. code-block:: sh

    nmap -sP 192.168.1.0/24

In diesem Fall wird davon ausgegangen, dass die zu durchsuchenden
Netzwerkadressen die Form ``192.168.1.xxx`` haben, wobei ``xxx`` eine laufende
Nummer zwischen ``1`` und ``255`` sein kann. Ebenfalls möglich sind andere
Namensräume, beispielsweise ``192.168.2.xxx``. Welcher bei den lokalen Rechnern
vorliegt, hängt von den Einstellungen des Routers ab; man kann den lokalen
Namensraum mittels Eingabe ``ip r`` abfragen.

Noch schneller lassen sich die lokalen Rechner samt Netzwerkadressen mittels
Eingabe von ``arp-scan -l`` auflisten; dazu muss lediglich das Programm
``arp-scan`` mittels ``aptitude`` installiert werden.



.. index:: pdfimages
.. _pdfimages:

``pdfimages``
-------------

Das ``pdfimages``-Programm ermöglicht es, alle in einer PDF-Datei enthaltenen
Graphiken bzw. Bilder auf einmal zu "extrahieren", d.h. als einzelne Bilddateien
zu speichern.

``pdfimages`` ist Teil des ``poppler-utils``-Pakets, das sich folgendermaßen
installieren lässt:

.. code-block:: bash

    aptitude install poppler-utils

Um alle Bilder zu extrahieren, gibt man im Ordner der PDF-Datei folgendes ein:

.. code-block:: bash

    pdfimages dateiname.pdf dateiname

Die Bilder werden dann als ``dateiname-001.ppm`` usw. gespeichert; mit
``pdfimages -f n`` bzw. ``pdfimages -l n`` können jeweils die erste und/oder die
letzte zu scannende Seitennummer (``n``) festgelegt werden. Die extrahierten
Bilder lassen sich mittels folgendem Skript beispielsweise in PNG-Dateien
umwandeln:

.. code-block:: bash

    for i in *.ppm; do convert $i $(basename $i .ppm).png ; done


.. index:: pdftk
.. _pdftk:

``pdftk``
---------

Das ``pdftk``-Toolkit ermöglicht eine vielseitige Nachbearbeitung von
``pdf``-Dateien. In den ``man pdftk``-Hilfeseiten finden sich zahlreiche
Beispiele, wie man mittels ``pdftk`` mehrere ``pdf``-Dokumente zusammenfügen,
einzelne Seiten entfernen, rotieren, oder vertauschen kann.

``pdftk`` lässt sich wie üblich aus den Paketquellen installieren:

.. code-block:: bash

    sudo aptitude install pdfk

Der grundsätzliche Aufruf erfolgt dann in folgender Form:

.. code-block:: bash

    pdftk inputdatei(en) cat [seitenzahlen] output outputdatei.pdf

* Um mehrere ``pdf``-Dokumente zu einer Datei zusammenzufügen, genügt folgender
  Aufruf:

.. code-block:: bash

    pdftk datei1.pdf datei2.pdf cat output neue-datei.pdf

* Um einzelne Seiten aus einer ``pdf``-Datei heraus zu kopieren, kann ``pdftk``
  folgendermaßen aufgerufen werden:

.. code-block:: bash

    pdftk datei.pdf cat 5 7 9-13 output ausschnitt.pdf

Mehr Infos zu ``pdftk`` gibt es unter `pdftk im Ubuntu-Wiki
<http://wiki.ubuntuusers.de/pdftk>`_.


.. index:: pngnq
.. _pngnq:

``pngnq``
---------

Das Programm ``pngnq`` kann verwendet werden, um die Dateigröße von Bildern im
PNG-Format durch Komprimierung erheblich (teilweise > 50%) zu reduzieren. Dabei
werden von ``pngnq`` Qualitätsverluste in Kauf genommen, die jedoch mit bloßem
Auge (meist) nicht zu erkennen sind -- beispielsweise reicht in vielen Fällen
zur Darstellung eines Bildes eine Farbtiefe von 256 Farben völlig aus. [#]_

Persönlich verwende ich ``pngnq`` beispielsweise, um mit Inkscape erstellte und
als ``png`` exportierte Graphiken zu verkleinern, damit die Webseiten, in denen
die Graphiken vorkommen, schneller und mit weniger Serverlast geladen werden
können. Dazu nutze ich hintereinander folgende zwei Mini-Skripte:

.. only:: html

    .. code-block:: bash

        for f in $(find ./ -name '*.png' | grep -v nq8);  do pngnq -n 256 $f && rm $f ; done

        for f in $(find ./ -name '*.png');  do mv $f $(dirname $f)/$(basename $f | sed 's/-nq8//') ; done

.. only:: latex

    .. code-block:: bash

        for f in $(find ./ -name '*.png' | grep -v nq8); \
            do pngnq -n 256 $f && rm $f ; done

        for f in $(find ./ -name '*.png'); \
            do mv $f $(dirname $f)/$(basename $f | sed 's/-nq8//') ; done

..  for f in $(find ./ -name '*.png' | grep -v nq8); do pngnq -n 256 $f && rm $f ; done
..  for f in $(find ./ -name '*.png'); do mv $f $(dirname $f)/$(basename $f | sed 's/-nq8//') ; done

Mit der ersten Zeile wird ``pngnq`` auf alle ``png``-Dateien angewendet; die
neuen Dateien erhalten automatisch die Endung ``-nq8`` angehängt, die Originale
werden gelöscht. Im zweiten Schritt werden die neuen Dateien umbenannt, so dass
sie wieder mit den ursprünglichen identisch sind (aber im Vergleich zu den
Originalen oft nur noch halb so viel Speicherplatz benötigen).

.. index:: screen
.. _screen:

``screen``
----------

Das Programm ``screen`` ermöglicht es, parallel auf mehreren virtuellen
Terminals zu arbeiten, obwohl man in Wirklichkeit nur eines verwendet. Dies kann
hilfreich sein, um sich beispielsweise über ssh auf einem externen Rechner
einzuloggen und innerhalb des gleichen Fensters mehrere Prozesse ablaufen zu
lassen.

``screen`` lässt sich wie üblich aus den Paketquellen installieren:

.. code-block:: bash

    sudo aptitude install screen

Nach der Installation kann ``screen`` ohne weitere Der Aufruf von
Screen-Funktionen werden allgemein durch Drücken von ``Ctrl a`` eingeleitet,
wobei der Eingabe der darauffolgenden Taste bestimmt, welche screen-Funktion
gewählt wird.

Screen legt beim Start ein erstes virtuelles Terminal an. Drückt man
hintereinander ``Ctrl a`` und ``c`` ("create"), so erzeugt screen ein weiteres
virutelles Fenster; die ersten 10 Fenster werden mit Nummer und Bezeichnung in
einer Infoleiste am unteren Ende des Screen-Fensters aufgelistet. Die Fenster
können über ``Ctrl a`` und eine Zahl zwischen ``0`` und ``9`` ausgewählt werden,
weitere können mittels ``Ctrl a`` und ``'`` angewählt werden. Mit ``Ctrl a`` und
``"`` wird eine Übersicht aller Fenster eingeblendet, die auch zur gezielten
Auswahl genutzt werden kann. Eine Änderung des Namens eines Fensters kann mit
``Ctrl a`` und ``a`` erreicht werden. Um ein Fenster zu schließen, kann man wie
gewohnt ``exit`` eingeben oder ``Ctrl a`` und ``k`` ("kill") drücken.


.. index:: tesseract, Texterkennung (OCR)
.. _tesseract:

``tesseract``
-------------

Mit ``tesseract`` als Texterkennungs-Software lassen sich im ``.tif``-Format
eingescannte oder abphotographierte Texte zurück in Textdateien verwandeln. Im
Gegensatz zu den eingescannten Bilddateien sind diese dann durchsuch- und
wiederverwertbar.

*Installation:*

``tesseract`` ist über die Paketverwaltung mittels der Pakete ``tesseract-ocr``
bzw. ``tesseract-ocr-deu`` und ``tesseract-ocr-eng`` für deutsche und englische
Sprachunterstützung installierbar.

.. code-block:: bash

    sudo aptitude install tesseract-ocr tesseract-ocr-deu tesseract-ocr-eng

Auch zahlreiche weitere Sprachen sind verfügbar, die entsprechenden Pakete
können mit ``aptitude search tesseract`` angezeigt werden.

*Benutzung:*

``tesseract`` benötigt als Eingabe-Format ``.tif``-Dateien mit maximal acht
Graustufen. Der Aufruf von ``tesseract`` zur Text-Erkennung erfolgt dann für
einen deutschsprachigen Text folgendermaßen:

.. code-block:: bash

    tesseract input-file.tif output-file  -l deu

Für englischsprachige Dateien wird entsprechend ``-l eng`` angegeben. An die
Ausgabe-Datei wird automatisch die Endung ``.txt`` angefügt.


*Tip: Screenshots nutzen*

Neben der Limitierung auf acht Graustufen hat tesseract den Nachteil, dass der
Original-Text einspaltig sein sollte -- eine Trennlinie oder Tabulatur zwischen
mehreren Spalten wird schlichtweg ignoriert. Wenn eine mehrspaltiger oder
mehrfarbig gescannte bzw. photographierte Originaldatei vorliegt -- womöglich
noch dazu in einem anderen Dateiformat --, so kann man sich, falls man sich
ohnehin nur für bestimmte Ausschnitte interessiert, mit einem entsprechenden
Screenshot-Alias in der ``~/.bashrc`` helfen:

.. code-block:: bash

    alias it='import -depth 8 txt_$(date +%Y%m%d_%H%M%S).tif'

Persönlich verwende ich das obige Beispiel zur Aufnahme von Screenshots mittels
des ``import``-Befehls aus dem Imagemagick-Paket. Die Angabe ``-depth 8`` legt
die Anzahl der Graustufen des Screenshots auf acht fest. Die Namen der einzelnen
Screenshots sollen dann einem einheitlichen Namensmuster und schließlich
chronologisch sortiert vorliegen; dies wird durch die Nutzung des
``date``-Befehls erreicht.

Wird die obige Code-Zeile in die Konfigurationsdatei ``~/.bashrc`` kopiert (und
diese im gleichen Shell-Fenster gegebenenfalls mit ``source ~/.bashrc`` neu
geladen), so kann mittels Eingabe von ``it`` stets ein neuer Screenshot im
aktuellen Verzeichnis gespeichert werden -- es muss nur noch mit dem
erscheinenden Fadenkreuz ein Bidschirm-Bereich für den Screenshot festgelegt und
durch einen Mausklick bestätigt werden.

*Tip: Stapelverarbeitung mehrerer .tif-Dateien:*

Mag man mehrere ``.tif``-Dateien auf einmal der Texterkennung zuführen, so kann
dies mit folgendem Einzeiler-Skript erreicht werden:

.. code-block:: bash

    for i in *.tif; do tesseract $i $i -l deu; done;

Die Ausgabedateien werden in diesem Fall nach den Eingabe-Dateien benannt,
gefolgt von der automatischen Endung ``.txt``.

Um auf diese Weise zusammengehörige Screenshots eines Buchs der Texterkennung
zuzuführen und die erzeugten Dateien wieder zu vereinen, sollten die Screenshots
zum einen in einem separaten Ordner aufgenommen bzw. dorthin kopiert werden. Zum
anderen sollten die Screenshots entlang eines Buches stets "von vorne nach
hinten" aufgenommen werden, da auch die resultierenden Bild- bzw. Textdateien
chronologisch sortiert sind.

Das Zusammenführen aller Textdateien eines Ordners zu einer neuen Zieldatei
gelingt schließlich folgendermaßen:

.. code-block:: bash

    for in in *.txt; do cat $i >> new-file.rst ; done

Für die Zieldatei nutze ich gerne die Endung ``.rst``, einerseits, um bei
möglichen späteren Erweiterungen Namenskonflikte zu vermeiden (hierbei würde
eine Zieldatei ``new-file.txt`` bei einem erneuten Aufruf des obigen Befehls mit
auf sich selbst abgebildet werden), andererseits, um den Text gleich für eine
"Informationsverwaltung" oder spätere Publikationen mittels Sphinx bereit zu
halten.

Der letztliche "Workflow" sieht möglicherweise so aus: Farbig gescannte
PDF-Datei mit ``evince`` oder einem anderen Dokumentenbetrachter öffnen; in
einem Shell-Fenster (z.B. ``guake``) zu einem gewünschten Zielordner wechseln;
mittels Eingabe von ``it`` und Textauswahl mit der Maus wiederholt Screenshots
(beliebig viele) erzeugen; die obigen beiden Einzeiler ausführen und fertig!

Bei einigermaßen guten Scans und einer brauchbaren Auflösung des Bildschirms
beim Erzeugen der Screenshots -- hierbei genügt eine Vollbild-Darstellung des
Dokuments auf einem 17-Zoll-Monitoren in den allermeisten Fällen, bei kleinen
Schriftgrößen oder kleineren Monitoren notfalls etwas "hineinzoomen" und lieber
mehrere kleinere Bildausschnitte wählen -- sollte das Ergebnis von ``tesseract``
durchaus zufriedenstellend sein.

*Tip: Tiff-Dateien nachbearbeiten*

Möchte man mehrere ``.tif``-Dateien zu einer Multipage-Tiff-Datei zusammenfügen
oder einzelne Seiten einer Multipage-Tiff-Datei entfernen, bieten sich die
Hilfsprogramme ``tiffcp``, ``tiffsplit`` und ``tiffcrop`` an.

Diese können mittels des ``libtiff-tools``-Paketes installiert werden:

.. code-block:: bash

    sudo aptitude install libtiff-tools

Das gleiche Paket stellt auch den Befehl ``tiff2pdf`` zur Umwandlung einer
Multipage-Tiff-Datei in ein PDF-Dokument bereit.

Schließlich kann auch das Programm ``unpaper`` zur Aufbesserung von Scans
genutzt werden. Infos hierzu gibt es unter `unpaper im Ubuntuuser-Wiki
<http://wiki.ubuntuusers.de/unpaper?highlight=tiffcp>`_.


.. index:: whois
.. _whois:

``whois``
---------

Mit ``whois`` können Informationen über den Betreiber, den Standort und das
System des Servers angezeigt werden, der zu einer bestimmten IP-Adresse gehört;
letztere kann zuvor mittels ``host`` ermittelt werden:

.. code-block:: bash

   host grund-wissen.de
   # grund-wissen.de has address 188.40.57.88
   # grund-wissen.de mail is handled by 10 mail.grund-wissen.de.

   whois 188.40.57.88
   # ... viele Infos ...

Üblicherweise befindet sich unter den angezeigten Informationen auch eine
Email-Adresse des Server-Administrators.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] ``cmus`` speichert alle Angaben zu den eingelesenen Dateien in der Datei
    ``~/.cmus/cache``. Um das Programm schlank und schnell zu halten, wird diese
    Datei nicht kontinuierlich aktualisiert. Dies hat zur Folge, dass ``cmus``
    nicht erkennt, wenn die Metadaten eines Stücks von einem anderen Programm
    (wie beispielsweise ``EasyTAG``) verändert wurden. Damit die Änderungen in
    ``cmus`` angezeigt werden, muss zunächst die Bibliothek mit ``:clear -l``
    gelöscht und die Cache-Datei mit ``u`` aktualisiert werden. Anschließend
    kann man die Bibliothek neu einlesen.

.. [#] Zudem kann mit ``M`` festgelegt werden, ob nach dem Abspielen aller Titel
    der Warteliste weitere Titel der Bibliothek wiedergegeben werden sollen.
    Persönlich habe ich diese Option grundsätzlich abgeschaltet, so dass in
    der Infozeile rechts nicht "album from library", sondern "playlist" steht.

.. [#] Möchte man keinerlei Qualitätsverlust hinnehmen, so kann das Programm
    ``optipng`` genutzt werden, das via ``apt`` als gleichnamiges Paket
    installierbar ist. Um beispielsweise alle ``png``-Dateien eines
    Verzeichnisses mit ``optipng`` zu optimieren, kann folgender Aufruf genutzt
    werden:

    ``for file in *.png ; do optipng -o9 $file ; done``

    Der Kompressionsgrad von ``optipng`` ist allerdings erheblich geringer als
    von ``pngnq``. Speziell für Webseiten sollte daher vergleichsweise auch
    ``pngnq`` getestet werden, wobei es ratsam ist, von den Originaldateien
    zunächst eine Backup-Kopie anzufertigen.


