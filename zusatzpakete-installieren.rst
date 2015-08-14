.. _Zusatzpakete installieren:

Zusatzpakete installieren
=========================

Nach einer erfolgreichen Basis-Installation werden üblicherweise noch weitere
Anpassungen vorgenommen. Im Wesentlichen gibt es dafür zwei Gründe:

* Einerseits mag man als Nutzer zusätzliche Software gemäß den eigenen Vorlieben
  installieren. Die Menge an verfügbarer Software passt allerdings nicht
  unbedingt auf eine CD, eine DVD, oder einen USB-Stick. Die Programme werden
  darüber hinaus beständig weiter entwickelt und sind möglicherweise in der
  Zwischenzeit aktualisiert worden.

* Andererseits werden je nach Linux-Distribution nur Software-Pakete
  mitgeliefert, die bestimmten Kriterien genügen (beispielsweise gewisse
  Lizenzbedingungen aufweisen). Manche wichtigen Pakete müssen daher, selbst
  wenn sie frei verfügbar sind, manuell installiert werden.


.. index:: Paketverwaltung
.. _Paketverwaltung:

.. rubric:: Paketverwaltung

Die Systeme Linux Mint, Ubuntu und Debian nutzen `apt ("Advanced Packaging
Tool") <http://wiki.ubuntuusers.de/Paketverwaltung>`_  zur Verwaltung und
Aktualisierung der installierten Programme und Code-Bibliotheken.

Je nach Desktop-Umgebung gibt es darauf aufbauende graphische
Verwaltungsprogramme (beispielsweise `Synaptic
<http://wiki.ubuntuusers.de/Synaptic>`_), die intuitiv mit der Maus bedienbar
sind. Von einer Shell aus kann :ref:`apt <apt>` auch direkt auf einfache Weise
genutzt werden.  Man kann

* mit ``apt-get update`` die Liste an verfügbaren Paketen aktualisieren,
* mit ``apt-cache search suchbegriff`` ein in Frage kommenden Paket suchen,
* mit ``apt-get install paketname`` ein verfügbares Paket installieren.

Zur Vereinfachung ist das Programm ``aptitude`` empfehlenswert. [#apt1]_  So
lassen sich die beiden Aufruf-Varianten ``apt-get`` und ``"apt-cache"`` durch
den entsprechenden ``aptitude``-Befehl ersetzen:

* ``aptitude search suchbegriff`` entspricht ``apt-cache search suchbegriff``
* ``aptitude install paketname`` entspricht ``apt-get install paketname``

.. _Wichtige Zusatzpakete:

.. rubric:: Wichtige Zusatzpakete

Folgende Programm-Pakete, die als Superuser mittels ``apt`` hinzugefügt werden
können, halte ich persönlich als Ergänzungen zum Basissystem für sehr nützlich:
[#Ding1]_ [#Red]_ [#VLC1]_ [#XPDF1]_

.. list-table:: Programme mit graphischer Bedienoberfläche (GUI)
    :name: tab-zusatzprogramme-graphisch
    :widths: 30 70

    * - Programmname
      - Beschreibung
    * - `abiword <http://wiki.ubuntuusers.de/Abiword>`_
      - ein alternatives Textverarbeitungs-Programm
    * - `alarm-clock-applet <http://community.linuxmint.com/software/view/alarm-clock-applet>`_
      - ein Weck- und Erinnerungsdienst-Programm für die Symbolleiste
    * - `blender <http://wiki.ubuntuusers.de/Blender_3D>`_
      - ein Programm zur Modellierung und Animation von 3D-Modellen
    * - `ding <http://wiki.ubuntuusers.de/Wörterbücher#Ding>`_
      - ein Deutsch-Englisches Wörterbuch
        (zusätzlich muss auch das Paket ``trans-de-en`` installiert werden)
    * - `easytag <http://wiki.ubuntuusers.de/Easytag>`_
      - ein Programm zur schnellen und einfachen Bearbeitung von Audio-Metadaten
        ("ID3-Tags")
    * - `evince <http://wiki.ubuntuusers.de/Evince>`_
      - ein ausgereifter Dokument-Betrachter (PDF, PS, TIF, u.a.)
    * - `gimp <http://wiki.ubuntuusers.de/Gimp>`_
      - ein Programm zur Bild-Bearbeitung (JPG, PNG, TIF, u.a.)
    * - `gnumeric <http://wiki.ubuntuusers.de/Gnumeric>`_
      - ein alternativer Tabellen-Editor
    * - `gparted <https://wiki.ubuntuusers.de/gparted>`_
      - ein Partitions-Manager, mit dem Partitionen beispielsweise auf lokalen
        Festplatten oder USB-Sticks erstellt und verwaltet werden können.
    * - `gtk-redshift <http://wiki.ubuntuusers.de/Redshift>`_
      - ein Programm, das den Bildschirm je nach Tageszeit und geographischer
        Lage rötlich einfärbt (wirkt entspannend auf das menschliche Auge).
    * - `guake <http://wiki.ubuntuusers.de/Guake>`_
      - eine Shell, die auf Tastendruck am oberen Bildschirmrand ein- und
        ausgeblendet werden kann
    * - `inkscape <http://wiki.ubuntuusers.de/Inkscape>`_
      - ein Programm zur Erstellung von Vektor-Graphiken (SVG)
    * - `keepassx <http://wiki.ubuntuusers.de/Keepassx>`_
      - ein Programm zur sicheren Verwaltung von Passwörtern
    * - `musescore <http://wiki.ubuntuusers.de/MuseScore>`_
      - ein umfangreiches Notensatz-Programm
    * - `pidgin <http://wiki.ubuntuusers.de/Pidgin>`_
      - ein Chat-Programm, das mehrere Protokolle unterstützt (u.a. Jabber und
        IRC)
    * - `transmission <http://wiki.ubuntuusers.de/Transmission>`_
      - ein einfach bedienbares BitTorrent-Programm
    * - `xpdf <http://www.foolabs.com/xpdf/>`_
      - ein schlanker, schneller PDF-Betrachter
    * - `unetbootin <https://wiki.ubuntuusers.de/UNetbootin>`_
      - ein Programm zum erstellen von bootfähigen Live-USB-Sticks
    * - `vlc <http://wiki.ubuntuusers.de/VLC>`_
      - ein Audio- und Videoplayer, der alle gängigen Formate unterstützt (MPG,
        AVI, FLV, MP3, OGG, u.a.)

Je nach Distribution und Desktop-Umgebung können einige der genannten Programme
bereits installiert sein. In diesem Fall bleibt ein Aufruf von ``sudo aptitude
install paketname`` ohne Wirkung.

Zusätzlich empfiehlt es sich auch einige Shell-Programme und Code-Bibliotheken zu
installieren. Im Abschnitt :ref:`Zusätzliche Shell-Programme` ist die Installation
und der Nutzen einiger Pakete näher beschrieben.


.. _Emulieren von Windows-Programmen:

.. rubric:: Emulieren von Windows-Programmen

Auch wenn es unter Linux für die meisten Zwecke eigene, auf dem
Open-Source-Prinzip basierende Programme gibt, lassen sich bei Bedarf --
allerdings ohne Garantie -- kommerzielle Windows-Programme auch mittels des
Windows-Emulators `Wine <http://wiki.ubuntuusers.de/Wine>`_ installieren bzw.
bedienen. [#W1]_ Um Wine unter Ubuntu 12.04 oder neuer beziehungsweise Linux
Mint 13 (oder neuer) zu installieren, sollte man folgendermaßen vorgehen:

..  [#W2]_

.. code-block:: bash

    sudo add-apt-repository ppa:ubuntu-wine/ppa
    sudo apt-get update
    sudo apt-get install wine1.7

Nach der Installation können Windows-Programme (auch Installations-Programme)
mittels ``wine programm.exe`` gestartet werden. Mittels ``winecfg`` bzw. des
entsprechenden Startmenü-Eintrags kann eine graphische Konfigurations-Oberfläche
gestartet werden.

Da das Emulieren von Programmen in vielen Fällen zu einer erheblichen Prozessor-
und Speicherlast führt und nur bedingt auf Linux-Systeme abgestimmt ist
(insbesondere stets eine Sicherheitslücke darstellt), sollte es nur dann
genutzt werden, wenn es unbedingt erforderlich ist und noch kein entsprechendes
Linux-Programm existiert.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#Apt1] Unter LinuxMint und Ubuntu ist ``aptitude`` bereits vorinstalliert.
    Unter Debian kann es mittels ``sudo apt-get install aptitude``
    nachinstalliert werden.

.. [#Ding1] Unter Linux Mint 17 bzw. Ubuntu 14.04 startet ``ding`` nach der
    Installation nicht, sondern gibt stattdessen die Fehlermeldung ``wish not
    found`` aus. Um dieses Problem zu beheben, öffnet man die Datei
    ``/usr/bin/ding`` mit Superuser-Rechten und ersetzt in der dritten Zeile
    ``exec wish "$0" "$@"`` durch ``exec wish8.4 "$0" "$@"``; danach startet
    ``ding`` wie gewohnt.

.. [#Red] Redshift kann nach der Installation im Kontrollzentrum als
    Startprogramm mit folgendem Aufruf festgelegt werden: ``gtk-redshift -l
    breitengrad:längengrad``, z.B. ``gtk-redshift -l 50:-10`` für den Standort
    Augsburg.

.. [#VLC1] VLC lässt sich auch zum Abspielen von DVDs und CDs nutzen. Während
    unter neueren Versionen von Linux Mint und Ubuntu bereits alle dafür nötigen
    Codecs vorinstalliert sind, müssen auf Debian-Systemen folgende Pakete
    manuell nachinstalliert werden:

    ``sudo aptitude install libc6 w32codecs libdvdcss2``

.. [#XPDF1] Damit ``xpdf`` beim Öffnen einer PDF-Datei keine Fehlermeldung der
    Art ``Warning: Cannot convert string
    "-*-courier-medium-r-normal--12-*-*-*-*-*-iso8859-1" to type FontStruct``
    anzeigt, muss zusätzlich das Paket ``gsfonts-x11`` mittels :ref:`apt <apt>`
    installiert werden. Die Änderung wird erst mit einem Neustart des X-Servers
    oder des ganzen Rechners wirksam.

.. [#W1] Eine andere Möglichkeit besteht darin, Windows unter linux
    beispielsweise mittels `KVM
    <http://wiki.ubuntuusers.de/Virtualisierung?#KVM>`_, `QEMU
    <http://wiki.ubuntuusers.de/Virtualisierung?highlight=vmware#QEMU>`_ oder
    `VirtualBox
    <http://wiki.ubuntuusers.de/Virtualisierung?highlight=vmware#VirtualBox>`_
    als "Virtuelles Betriebsystem" zu installieren. Windows-Programme können
    innerhalb dieser Umgebung wie unter Windows üblich installiert und benutzt
    werden.

    Der Vorteil dieser Methode liegt darin, dass auf diese Weise können *alle*
    Windows-Programme benutzt werden, da es sich quasi um ein gesamtes
    Windows-System handelt. Zusätzlich ist es teilweise möglich, den aktuellen
    Stand des virtuellen Systems zu speichern und bei Bedarf wiederherzustellen
    -- dies kann unter Windows nötige Firewalls und Virenscanner überflüssig
    machen.

    Nachteilig ist bei dieser Methode, dass virtuelle Betriebsysteme oft mit
    erheblichen Geschwindigkeits-Einbußen verbunden sind und viel
    Arbeitsspeicher erfordern.

..  .. [#W2] Siehe `Original-Anleitung
    ..  <http://www.upubuntu.com/2012/06/how-to-install-wine-157-on-ubuntu.html>`_

