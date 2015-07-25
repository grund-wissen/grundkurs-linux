.. _Linux installieren:

Linux installieren
==================

Linux ist komfortabel geworden. Das gilt nicht nur für die Vielfalt und
Anwenderfreundlichkeit der Programme, sondern auch für die
Installationsroutinen. Dank gut ausgearbeiteter Dokumentationen (z.B. das
`Ubuntu-Wiki <http://wiki.ubuntuusers.de/Startseite>`_) lässt sich heute in
kurzer Zeit und ohne Grundkenntnisse ein gut funktionierendes Linux-System
einrichten.

.. index:: Distribution
.. _Auswahl einer Linux-Distribution :

.. rubric:: Auswahl einer Linux-Distribution 

Als Distribution wird im Software-Bereich eine Zusammenstellung von Software zu
einem gut nutzbaren Gesamtpaket bezeichnet. Die Vielzahl an Linux-Distributionen
[#LD]_ unterscheidet sich im Wesentlichen dadurch, welche Programme
grundsätzlich installiert sind, wie häufig Updates erfolgen und wie viel
Konfigurationen der Benutzer gewöhnlich manuell vornehmen möchte. 

In Deutschland laufen die meisten Server mit der Distribution `Debian
<http://de.wikipedia.org/wiki/Debian>`_; bei den Privat-PCs zählen die auf
Debian basierenden Distributionen `Ubuntu
<http://de.wikipedia.org/wiki/Ubuntu>`_ und `Linux Mint <http://linuxmint.com>`_
zu den beliebtesten Systemen. Alle Tips dieser Notizen-Sammlung beziehen sich
auf diese einander weitgehend ähnlichen Systeme. 

Wie Linux letztendlich "aussieht", hängt nur bedingt von der Distribution ab.
Die graphische Bedienoberfläche und das eigentliche Betriebsystem sind -- anders
als bei Windows -- zweierlei Dinge. Das Betriebsystem Linux unterstützt eine
Vielzahl an Bedienoberflächen ("Desktop-Umgebungen"), die sich auch nach der
Installation jederzeit austauschen lassen. Die wohl bekanntesten
Bedienoberflächen sind `GNOME <http://de.wikipedia.org/wiki/Gnome>`_ und `KDE
<http://de.wikipedia.org/wiki/Kde>`_. Persönlich nutze ich derzeit am liebsten
die unter Linux Mint übliche (auf GNOME basierende) Oberfläche `Mate
<https://de.wikipedia.org/wiki/MATE_Desktop_Environment>`_.

.. _Die Basis-Installation:

Die Basis-Installation
----------------------

Ein Linux-System zu installieren ist heute dank moderner Hardware-Erkennung und
graphischer Installations-Assistenten denkbar einfach. Das Installations-Schema
ist bei fast allen Distributionen gleich: 

#.  Man lädt sich von der jeweiligen Homepage eine ISO-Image-Datei herunter.
    Persönlich bevorzuge ich derzeit `Linux Mint Ubuntu Edition
    <http://www.linuxmint.com/download.php>`_ mit Mate-Desktop. Je nach Hardware
    muss die 32- oder 64-Bit-Variante gewählt werden. [#MC32]_ 
#.  Man erstellt aus diesem Image mit einem beliebigen Brennprogramm eine
    bootbare CD bzw. mit `UNetBootin <http://wiki.ubuntuusers.de/UNetbootin>`_
    einen bootbaren USB-Stick. Eine gute Anleitung zur Erstellung eines
    Ubuntu-USB-Sticks, die mit Linux Mint genauso funktioniert, findet sich
    `hier <http://wiki.ubuntuusers.de/Live-USB>`_.

#.  Man bootet den Rechner mit eingelegter Boot-CD bzw. angestecktem
    Boot-USB-Stick neu.

Die Boot-Reihenfolge wird vom BIOS des Rechners festgelegt. Entsprechende
Einstellungen werden im BIOS-Menü vorgenommen, das sich bei einem Neustart des
Rechners meist mit ``F2`` (manchmal auch mit ``F8``) öffnen lässt. Je nach
ausgewählter Distribution erscheint automatisch ein Installations-Assistent
(Debian), oder es wird ein Live-System gebootet (Ubuntu bzw. Linux Mint), in dem
der Installations-Assistent als Icon auf dem Desktop zu finden ist. 

Zu Beginn der Installationsroutine legt man den Benutzernamen mit dazugehörigem
Passwort und bevorzugte Einstellungen (Tastaturlayout, Zeitzone, etc.) fest.
Nachträgliche Änderungen dieser Einstellungen sind auch später ohne Aufwand
möglich.

Der wichtigste Schritt der Installation besteht anschließend in der Festlegung
der zu nutzenden Festplattenpartitionen. Diese lassen sich wahlweise automatisch
oder von Hand mittels eines integrierten Partitionsprogramms einrichten. 
Der Installations-Assistent führt die Grundinstallation daraufhin
vollautomatisch durch.


.. _Partitionen einrichten:

.. rubric:: Optional: Partitionen manuell einrichten

Bei einer nicht-automatischen Festlegung der Partitionen empfehlen sich, sofern
genügend Festplattenspeicher vorhanden ist, folgende Partitionsgrößen:

* Eine mittelgroße Partition (min. 10 GB, max. 30 GB) mit Einhängepunkt ``/``
  für das Basis-System.
* Eine beliebig große Partition (min. 10 GB) mit Einhängepunkt ``/home`` für
  eigene Dokumente, Konfigurationsdateien, etc.
* Optional: Eine kleine Partition (2 bis 5 GB) als ``swap``, d.h. als
  Erweiterung des Arbeitsspeichers
* Optional: Eine beliebig große Partition (ohne festen Einhängepunkt) für
  gemeinsam genutzte und/oder verschlüsselte Dateien. 
* Optional: Nicht verwendeter Speicherplatz für ein weiteres, parallel
  installierbares oder bereits installiertes Betriebsystem. [#WI]_

Eine separate ``/home``-Partition  bietet den Vorteil, dass das System jederzeit
neu installiert werden kann, ohne dass eigene Daten und Einstellungen davon
berührt werden. Das gilt ebenso für Systeme mit mehreren Benutzern.

Für die ``/`` bzw. ``/home``-Partition empfiehlt sich als Dateisystem ``EXT-4``,
da es sehr schnell, sehr stabil und quasi wartungsfrei ist. Für
Daten-Partitionen empfiehlt sich ebenfalls ``EXT-4`` als Dateisystem, solange
man nur mit Linux darauf zugreifen möchte. Falls man die Daten auch unter
Windows oder MacOS nutzen mag, muss ``FAT32`` als Dateisystem verwendet werden.
``FAT32`` verfügt allerdings über keine Unterstützung von nützlichen Symlinks
und bietet keine Unterscheidung von Groß- und Kleinschreibung.  


.. _Passwortgeschützte Bereiche schaffen:

Optional: Passwortgeschützte Bereiche schaffen
----------------------------------------------

Linux ist als Betriebsystem verhältnismäßig sicher. Lässt man jedoch
beispielsweise ein Notebook unbeaufsichtigt liegen, so helfen die besten
Konfigurationen nichts, um vertrauliche Daten vor unbefugtem Fremdzugriff zu
schützen. Eine Festplatte kann einfach ausgebaut und extern an einen anderen PC
angeschlossen werden, und schon sind alle Daten (Passwörter, evtl.
Onlinebanking-Daten, Emails, etc.) frei abrufbar...

Wer private Daten in einem passwortgeschützten ("verschlüsselten") Bereich
ablegen möchte, kann sich unter Linux für eine der folgende Möglichkeiten
entscheiden: 

* :ref:`Partition-Verschlüsselung <Die Partitions-Verschlüsselung>`: Die
  Partition kann bereits während der Installation -- ohne Festlegung eines
  Einhängepunktes -- auf einem freien (unformatierten) Bereich eines
  Datenträgers angelegt werden. [#E1]_

* :ref:`System-Verschlüsselung <Die System-Verschlüsselung>`: Beim Start erscheint
  eine Passwort-Abfrage. Erst wenn das Passwort richtig eingegeben wurde, wird
  die Systempartition entschlüsselt, und der Rechner bootet. [#E2]_

.. index:: truecrypt

Darüber hinaus ist es möglich, mittels `Truecrypt
<http://wiki.ubuntuusers.de/TrueCrypt>`_ passwortgeschützte Daten-"Container" zu
erstellen. Diese können nach der Installation auf einer beliebigen Partition
eingerichtet werden und sind auch auf anderen Betriebsystemen nutzbar. [#E3]_

.. raw:: html

    <hr />
    
.. only:: html

    .. rubric:: Anmerkungen:

.. [#LD] Je nach Vorliebe und Anwendungszweck bietet sich ein weites Spektrum an
    Distributionen:

    * "Live-Disks" (z.B. `Knoppix <http://de.wikipedia.org/wiki/Knoppix>`_):

      Einige Linux-Varianten sind darauf ausgelegt von einem externen
      Datenträger (CD, USB-Stick) geladen und ohne Installation von diesem aus
      genutzt zu werden. 

    * Extrem konfigurierbare Distributionen (z.B. `Gentoo
      <http://de.wikipedia.org/wiki/Gentoo_Linux>`_, `Arch
      <http://de.wikipedia.org/wiki/Arch_Linux>`_):

      In manchen Distributionen ist es normal, den Linux-Kernel und die
      Programme stets selbst aus dem Quellcode zu compilieren, d.h. in
      ausführbaren Maschinencode zu übersetzen. Dies bietet eine maximale
      Kontrolle über die laufenden Programme und kann erhebliche
      Geschwindigkeitsvorteile im laufenden System mit sich bringen. Um das
      Potential derartiger Distributionen auch ausschöpfen zu können, sollte man
      allerdings ausreichend mit Linux- und Hardware-Grundlagen vertraut sein.

    * Distributionen von kommerziellen Anbietern (z.B. `Red Hat Enterprise
      <http://de.wikipedia.org/wiki/Red_Hat_Enterprise_Linux>`_,  `Fedora
      <http://de.wikipedia.org/wiki/Fedora_(Linux-Distribution)>`_, `Mandrivia
      <http://de.wikipedia.org/wiki/Mandriva>`_):

      Diese Distributionen werden von Firmen entwickelt und gepflegt und sind
      insbesondere für Geschäftskunden interessant, die darauf angewiesen sind,
      jederzeit einen kommerziellen technischen Support in Anspruch nehmen zu
      können.

.. [#MC32] Ältere Rechner mit einem einzelnen Prozessor (z.B. Intel Celeron,
    Intel Atom) benötigen ein 32-Bit-System, neuere Multi-Core-Prozessoren
    hingegen ein 64-Bit-System. 
    
    Ist man sich nicht sicher, welcher Systemtyp der passende ist
    (beispielsweise weil man nicht weiß, was für ein Prozessor eingebaut ist),
    so kann eine entsprechende Suchmaschinen-Anfrage weiterhelfen. Darüber
    hinaus kann auch ein (versehentlicher) Versuch, einen Rechner mit einem
    nicht passenden System zu booten, keinerlei Schaden anrichten, denn er wird
    unmittelbar unterbrochen und eine entsprechende Fehlermeldung ausgegeben.

.. [#WI] Linux lässt sich auch parallel zu einem bestehenden Windows-System
    installieren. Hierzu nutzt man am besten eine eigene Festplatte oder legt
    mit dem Installations-Assistenten eine neue EXT-4-Partition an (min. 15 GB)
    und installiert Linux in diesen Bereich; auch zwei neue Partitionen mit den
    Einhängepunkten  ``/`` für das Grundsystem und ``/home`` für persönliche
    Dateien sind als Variante möglich. Nach einer ueblichen Installation lässt
    sich anschließend bei jedem Rechnerstart in einem Menü auswählen, welches
    Betriebsystem gestartet werden soll.

    *Achtung:* Bei einer Veränderung einer bestehenden Partition --
    beispielsweise einer Verkleinerung, um Platz für eine neute Partition zu
    schaffen -- lässt sich ein Datenverlust niemals völlig ausschließen. Eine
    Sicherheitskopie bestehender Daten ist daher auf alle Fälle empfehlenswert!

    Linux kann lesend und schreibend auf alle Windows-Dateien und zugreifen. Windows
    kann jedoch nicht mit Linux-Dateisystemen umgehen, da es beispielsweise nicht
    zwischen Groß- und Kleinschreibung in Dateinamen unterscheidet. Möchte man auf
    bestimmte Daten mit beiden Systemen zugreifen, so müssen diese folglich auf
    einer Windows-Partition liegen.



.. [#E1] Der Vorteil dieser Methode liegt darin, dass sie verhältnismäßig einfach
    einzurichten und die verschlüsselte Partition unabhängig vom System ist.
    Somit kann der geschützte Bereich auch auf einem laufenden Rechner
    verschlossen bleiben. 

    Nachteilig bei dieser Methode ist, dass jeder Unbefugte mit Hardware-Zugriff
    das Betriebsystem ohne Hindernis verändern kann, beispielsweise um Trojaner
    oder Datenlogger zu installieren.

.. [#E2] Der Vorteil dieser Methode liegt darin, dass kein Unbefugter Zugriff
    auf Teile des Systems oder der persönlichen Dateien hat -- sofern er den
    Rechner ausgeschaltet vorfindet. 

    Nachteilig bei dieser Methode ist, dass sie einem Rechner im laufenden
    Betrieb -- die Systempartition ist wohl immer geöffnet -- keinerlei Schutz
    bietet. Darüber hinaus setzt diese Methode setzt einige Linux-Kenntnisse
    voraus und ist für Anfänger ungeeignet.

.. [#E3] Der Vorteil dieser Methode liegt darin, dass -- im Gegensatz zu den
    obigen Methoden -- auch Windows- und MacOS-Systeme auf den
    passwortgeschützten Bereich zugreifen können.

    Als Nachteil ist zu nennen, dass das Erstellen eines Containers -- je nach
    Größe und Rechnerleistung -- mehrere Stunden dauern kann. 

