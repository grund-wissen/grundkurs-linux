.. _Mercurial-Tool:

Mercurial
=========

`Mercurial <http://mercurial.selenic.com>`_ ist ein Versionskontrollsystem, das
leicht zu erlernen ist und die Entwicklung von Projekten an mehreren Orten
und/oder mit mehreren Entwicklern wesentlich erleichtert.

Unter Linux lässt sich Mercurial mittels des gleichnamigen Paketes installieren:

.. code-block:: bash

    sudo aptitude install mercurial

Die Bedienung erfolgt gewöhnlich aus einer Shell heraus; als graphisches
Frontend gibt es beispielsweise das Programm `TortoiseHg
<https://de.wikipedia.org/wiki/TortoiseHg>`_, das über das gleichnamige Paket
``tortoisehg`` installierbar ist.


.. rubric:: Archivierung eines Projekts

Ein Quellcode-Projekt kann, allerdings ohne Versionsgeschichte, in eine
ZIP-Datei archiviert werden, um es auch zum Download oder zum Verschicken via
Email zugänglich zu machen. 

Um beispielsweise den Quellcode (samt Ordnerstruktur) meines
Grund-Wissen-Projekts zu archivieren, wechsle ich in einem Shell-Fenster in den
Basispfad des Projekts und gebe dort folgenden Befehl ein:

.. erst hg addr, dann hg commit -m "message"

.. code-block:: bash

    hg archive -t zip -X "*_build/*" -X "*/_build/*" ../grund-wissen.zip

* Durch das Argument ``-t zip`` wird der Dateityp des Archivs festgelegt --
  anstelle ``zip`` kann auch ``tgz`` o.ä. gewählt werden. 

* Durch das Argument ``-X "kriterium"`` werden alle Ordner und Dateien aus
  dem Archiv ausgeschlossen, bei denen das gegebene Kriterium zutrifft. 

  Im obigen Beispiel werden dadurch die fertigen Ausgabe-Dateien (``html``,
  ``tex`` usw.) des aktuellen Verzeichnisses und aller Unterverzeichnisse nicht
  mitarchiviert. Dies reduziert die Größe des Archiv erheblich.

Das Archiv kann einfach mittels ``unzip grund-wissen.zip`` entpackt werden.

.. hg archive -t zip -X"Entwuerfe" -X"Vorlagen" ../grund-wissen-bilder.zip

.. rubric:: Links

* `Mercurial Einführung <http://mercurial.selenic.com/wiki/GermanTutorial>`_
* `Mercurial Quickstart (deutsche Übersetzung) <http://mercurial.selenic.com/wiki/QuickStartDe>`_
* `Mercurial by Example (PDF, eng.) <http://www.jemander.se/MercurialByExample.pdf>`_

..  hgignore
..  http://linux.die.net/man/5/hgignore
..  http://hginit.com/

..  http://mercurial.selenic.com/wiki/.hgignore
