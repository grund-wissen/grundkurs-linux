.. _Linux-Dateisystem:

Das Linux-Dateisystem
=====================

Zur Organisation der Dateien eines Linux-Systems halten sich die meisten
Distributionen an einen bestimmten Standard (" Filesystem Hierarchie Standard").
Die Bezeichnungen für die grundlegenden Verzeichnisse sind somit
auf allen Linux-Systemen (nahezu) identisch:

.. _/:

* ``/``
  Das Verzeichnis ``/`` (auch "Wurzelverzeichnis" genannt) stellt den Basispfad
  des Systems dar.

.. _/bin:

* ``/bin``
    In diesem Verzeichnis befinden sich wichtige Programme für Anwender, die
    immer verfügbar sein müssen, beispielsweise die Shell ``bash`` oder das
    Programm ``ls`` zur Anzeige von Ordnerinhalten.

.. _/boot:

* ``/boot``
    In diesem Verzeichnis befinden sich die zum Hochfahren des Systems unbedingt
    erforderlichen Dateien. Am wichtigsten ist dabei der Kernel, üblicherweise
    eine Datei mit dem Namen ``vmlinuz-versionsname`` (andere Namen sind
    ebenfalls möglich).

.. _/dev:

* ``/dev``
    In diesem Verzeichnis befinden sich ausschließlich Gerätedateien. Diese
    speziellen Dateien stellen eine einfach nutzbare Schnittstelle zur Hardware
    dar.

    Für jede Festplatte und ihre Partitionen existiert im ``/dev/``-Verzeichnis
    ein eigener Eintrag. Beispielsweise bezeichnet, sofern vorhanden,
    ``/dev/hda`` ist die erste IDE-Festplatte, ``/dev/sda`` die erste
    SCSI-Festplatte im System. Höhere Buchstaben (``sdb``, ``sdc``) stellen
    weitere Festplatten oder externe Speichermedien dar, Zahlen am Ende
    (``sda1``, ``sda2``) benennen die Partitionen der Festplatten. [#PAR]_

.. _/etc:

* ``/etc``
    In diesem Verzeichnis befinden sich zahlreiche Konfigurationsdateien, die
    Einstellungen zu den installierten Programmen sowie grundlegende
    Systeminformationen enthalten. Viele dieser Dateien haben eigene
    Manpage.

.. _/home:

* ``/home``
    In diesem Verzeichnis befinden sich die persönlichen Verzeichnisse der
    einzelnen Benutzer.

.. _/lib:

* ``/lib``
    In diesem Verzeichnis befinden sich die wichtigsten Funktionsbibliotheken
    des Systems; diese Dateien sollten nicht manuell verändert werden.

.. _/media:

* ``/media``
     In diesem Verzeichnis werden externe Datenträger als Unterverzeichnisse
     eingebunden. Bei aktuellen Ubuntu- und LinuxMint-Versionen werden
     automatisch erkannte USB-Sticks, Speicherkarten, externe Festplatten usw.
     in ein Verzeichnis der Art ``/media/benutzername/name-des-datentraegers``
     eingebunden.

.. _/proc:

* ``/proc``
    Dies ist kein normales Verzeichnis, sondern stellt eine Schnittstelle zum
    Kernel dar. Jedes laufende Programm wird hier in einem Unterverzeichnis
    geführt, dessen Dateien viele Informationen beispielsweise über den
    aktuellen Programmstatus enthalten.

..  Zudem gibt es eine umfangreiche Verzeichnisstruktur mit Daten über den
..  Kernel und die Hardware des Systems.

.. _/root:

* ``/root``
    In diesem Verzeichnis befinden sich die (persönlichen) Dateien des
    Systemverwalters ("Root" bzw. "Superuser"). Das Verzeichnis liegt im
    Wurzelverzeichnis, damit der Systemverwalter auch dann auf seine
    (Konfigurations-)Dateien zugreifen kann, wenn durch einen Fehler der Zugriff
    auf andere Partitionen nicht mehr möglich ist. [#]_

.. _/sbin:

*   ``/sbin``
    In diesem Verzeichnis befinden sich ebenfalls -- ähnlich wie im
    ``/bin``-Verzeichnis -- wichtige Programme, die allerdings für den
    Systemverwalter gedacht sind. Sie erfüllen Funktionen, auf die ein normaler
    Benutzer keinen Zugriff hat.

.. _/tmp:

* ``/tmp``
    Dieses Verzeichnis kann von jedem Benutzer und jedem Programm als temporäre
    Ablage für Dateien verwendet werden.

..  Damit sich Benutzer nicht gegenseitig ihre Dateien löschen, ist das
..  sogenannte Sticky-Bit dieses Verzeichnisses gesetzt.

.. _/usr:

* ``/usr``
    In diesem Verzeichnis ("Unix System Ressources") befinden sich der größte
    Teil der installierten Software. Auf vielen Systemen befinden sich innerhalb
    von ``/usr`` mehr Daten als in allen anderen Dateien zusammen. Die
    ausführbaren Programmdateien sind meist in ``/usr/bin``,
    Programmbibliotheken in ``/usr/lib`` abgelegt.

    In Netzwerken, an die viele gleichartige Systeme angeschlossen sind, wird
    dieses Verzeichnis häufig auf einem zentralen Server gespeichert, und alle
    anderen Computer greifen über das Netzwerk darauf zu.

..  Die umfangreichste Verzeichnisstruktur des Systems.

.. _/var:

* ``/var``
    In diesem Verzeichnis ("Variable Dateien") befinden sich hauptsächlich
    Dateien, die sich ständig verändern. Beispielsweise werden hier Log-Dateien
    gespeichert.

.. _/opt:

* ``/opt``
    In diesem Verzeichnis ("Optionale Software") werden bei Bedarf sehr große
    Programme gespeichert, die nicht unmittelbar zum System gehören. Bei knappem
    Festplattenspeicher kann dieses Verzeichnis -- wie das ``/home``-Verzeichnis
    -- auf einer externen Festplatte oder einer anderen Partition abgelegt
    werden.

.. _~:

Als Abkürzungen ist ``~`` für das persönliche Home-Verzeichnis (also
``/home/benutzername``) üblich. Zudem bezeichnet ``.`` den Namen des aktuellen
Verzeichnisses, und ``..`` den Namen des übergeordneten Verzeichnisses.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#PAR] Da auf einer Festplatte nur vier primäre Partitionen möglich sind,
    wird häufig eine erweiterte Partition angelegt, die den größten Teil der
    Festplatte umfasst. In der erweiterten Partition können dann "logische
    Laufwerke" angelegt werden. Diese erhalten grundsätzlich die
    Partitionsnummern ab 5. Enthält eine Festplatte also eine primäre und eine
    erweiterte Partition, in der sich wiederum zwei logische Laufwerke befinden,
    gibt es auf dieser Platte die Partitionen 1, 2, 5 und 6. Die primäre
    Partition ist 1, die erweiterte ist 2, und die beiden logischen Laufwerke
    sind 5 und 6.

.. [#] Häufig wird bei der Installation eines Linux-Systems für das
    ``/home``-Verzeichnis eine eigene Festplatte verwendet oder eine eigene
    Partition angelegt, um bei einer möglichen Neuinstallation des Systems die
    persönlichen Daten unverändert übernehmen zu können.


