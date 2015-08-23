.. index:: Superuser, Root,
.. _Administrator-Programme:

Administrator-Programme
=======================

Als Super-User (manchmal auch "Root" genannt) kann man neben den
:ref:`Standard-Programmen <Standard-Programme>` und möglichen zusätzlich installierten
:ref:`Zusatz-Programmen <Zusätzliche Shell-Programme>` auch Werkzeuge nutzen, die
systemweite Veränderungen bewirken können. Im Folgenden ist eine kleine Auswahl
dieser Programme aufgelistet:

.. index:: adduser, deluser
.. _adduser und deluser:

``adduser``, ``deluser``
------------------------

Mit ``adduser benutzername`` wird ein neues Benutzer-Konto erstellt und der
entsprechende Ordner im ``/home``-Verzeichnis angelegt. Mit ``deluser
benutzername`` kann entsprechend ein bestehendes Benutzer-Konto gelöscht
werden. Standardmäßig bleibt dabei das Home-Verzeichnis des Benutzers
erhalten; möchte man dieses gleich mit entfernen, kann ``deluser`` mit der
Option ``--remove-home benutzername`` aufgerufen werden.


.. index:: apt, aptitude, Paketverwaltung
.. _apt:

``apt``, ``aptitude``
---------------------

Mit ``apt-cache search ...`` (oder einfacher: ``aptitude search ...``) kann
jeder Benutzer die lokale Pakete-Liste nach dem Namen oder der Beschreibung
eines Programms oder einer Code-Bibliothek (lib) durchsuchen (und somit z.B.
nachsehen, ob ein bestimmtes Paket installierbar bzw. installiert ist).

Als Super-User kann man zusätzlich weitere Funktionen von ``apt`` bzw.
``aptitude`` nutzen: [#]_

* Mit ``apt-get update`` (oder einfacher: ``aptitude update``) wird die lokale
  Pakete-Liste aktualisiert; damit verbunden wird auch die Liste der Server, von
  denen die Pakete heruntergeladen werden können, auf den aktuellen Stand
  gebracht. Ein solcher Update sollte in regelmäßigen Abständen bzw. vor
  Paket-Installationen und System-Upgrades vorgenommen werden.

* Mit ``apt-get install paketname`` (oder einfacher: ``aptitude install
  paketname``) lässt sich ein Programm oder eine Bibliothek aus der Paketliste
  installieren; es können auch mehrere Paketnamen auf einmal angegeben werden:
  ``aptitude install paket1 paket2 ...``.

  Führt eine Installation zu Versions-Konflikten, sucht ``apt`` bzw.
  ``aptitude`` automatisch nach einer Lösung, welche die verletzten
  Abhängigkeiten nach Möglichkeit auflöst; es erscheint eine entsprechende
  Programm-Rückmeldung, wobei es dem Benutzer überlassen wird, ob die Lösung
  akzeptiert wird oder ob weiter nach einer anderen Lösung gesucht werden soll.

* Mit ``aptitude reinstall paket`` kann ein einzelnes Paket (Programm oder
  Bibliothek) neu installiert werden. Dabei wird gegebenenfalls automatisch ein
  Update vorgenommen. Mögliche Konfigurationsdateien bleiben dabei unberührt.

* Mit ``apt-get remove paket`` (oder einfacher: ``aptitude remove paket`` kann
  ein installiertes Paket wieder deinstalliert werden. Die Konfigurationsdateien
  bleiben dabei erhalten; um auch diese zu entfernen, kann der Aufruf ``apt-get
  purge paket`` bzw. ``aptitude purge paket`` genutzt werden.

* Mit ``apt-get source paket`` kann der Quellcode eines Pakets (Programm oder
  Bibliothek) herunter geladen werden. Somit kann man das Programm selbst
  compilieren bzw. bei entsprechenden Programmier-Kenntnissen einen Blick in die
  eigentliche Funktionalität des Programms werfen und/oder Teile des Quellcodes
  für eigene Projekte weiter verwenden.

* Mit ``apt-get upgrade`` bzw. ``aptitude safe-upgrade`` werden alle möglichst
  alle Pakete auf den neuesten Stand gebracht; ein Installieren zusätzlicher
  Pakete und/oder ein Entfernen bestehender Pakete soll dabei bei verletzten
  Abhängigkeiten (möglichst) ausbleiben. Es erscheint eine Rückmeldung über die
  anstehenden Aktualisierungs-Maßnahmen, wobei sich der Benutzer entscheiden
  kann, ob die angebotene Lösung akzeptabel ist oder nach einer anderen Lösung
  gesucht werden soll.

  Vor einem Upgrade sollte die lokale Paket-Liste stets mit ``apt-cach upgrade``
  bzw. ``aptitude update`` aktualisiert werden.

  Mit ``aptitude full-upgrade`` besteht darüber hinaus bei Versions-Konflikten
  die Möglichkeit, die Aktualisierung der installierten Pakete durch eine
  Installation weiterer Pakete und/oder ein Entfernen bestehender Pakete zu
  "erleichtern". Hier muss von Fall zu Fall geprüft werden, ob ein solcher
  Upgrade den eigenen Wünschen/Erwartungen entspricht.

* Mit ``apt-get dist-upgrade`` bzw. ``aptitude dist-upgrade`` werden nicht nur
  einzelne Pakete, sondern gegebenenfalls die gesamte Distribution aktualisiert
  (z.B. ein Wechsel von Ubuntu Version 12.04 auf Version 12.10). Da ein solcher
  System-Upgrade zahlreiche Veränderungen mit sich bringen kann, sollte man sich
  den Einsatz dieser Aktualisierungs-Variante vorher gut überlegen. [#]_

``aptitude`` kann auch ohne zusätzliche Kommandozeilen-Argumente aufgerufen
werden. In diesem Fall erscheint eine text-basierte Benutzeroberfläche. In der
oberen Hälfte werden Paketnamen (nach verschienenen Rubriken sortiert)
aufgelistet, in der unteren Hälfte erscheint zum jeweiligen Paket eine passende
Beschreibung. Mit den Cursor-Tasten kann man sich in der oberen Bildschirmhälfte
durch die Paketzweige navigieren, mit der ``Enter``-Taste werden Unterkategorien
ein- bzw. ausgeblendet. Wie in den obersten Zeilen kurz beschrieben, kann mit
``q`` das Programm beendet werden; mit ``u`` werden die Paketquellen
aktualisiert (entspricht ``aptitude update``). Mit ``+`` kann das Paket unter
dem Cursor zur (Neu-)Installation, mit ``-`` zum Entfernen und mit ``_`` zum
vollständigen Löschen vorgemerkt werden; mit ``g`` werden die vorgemerkten
Änderungswünsche ausgeführt.

``chmod``
---------

Mit ``chmod`` kann festgelegt werden, welche Dateirechte (Lesen, Schreiben,
Ausführen) für den Eigentümer, für die Benutzer-Gruppe und für alle Anderen
gelten.

.. TODO Link auf Standard-Programme

.. index:: chown, chgrp
.. _chown und chgrp:

``chown``, ``chgrp``
--------------------

Mit ``chown benutzername dateien`` kann der Eigentümer einer oder mehrerer
Dateien festgelegt werden; entsprechend können mit ``chgrp gruppenname dateien``
eine oder mehrere Datei(en) einer Benutzer-Gruppe zugewiesen werden. Mit der
Option ``-R`` lassen sich beide Werkzeuge auch rekursiv auf Verzeichnisse
mitsamt Unterverzeichnissen anwenden.

..  Beispiel: ``chgrp audio soundfile.mp3`` -> Datei wird der Gruppe "audio"
..  zugewiesen.


.. index:: chroot
.. _chroot:

``chroot``
----------

Mit ``chroot pfad`` kann der angegebene Pfad als Basispfad ``/`` des
Betriebsystems festgelegt werden. Dies ist insbesondere praktisch, um ein
"Live-System" von einem USB-Stick zu booten und von diesem System aus Wartungen
am eigentlich installierten Betriebsystem vorzunehmen (falls dieses aus
irgendwelchen Gründen nicht mehr booten sollte). Nützlich ist dabei folgende
Routine: [#]_

.. code-block:: bash

    # Vorab: Die System-Partition eingebinden:
    # -- falls unbekannt: fdisk -l eingeben! --
    # mount /dev/[systempartition] pfad

    cd pfad mount --bind /sys ./sys mount --bind /dev ./dev mount --bind /proc
    ./proc chroot .

Hierbei werden (nach einem Wechsel in den Pfad der Systempaftition) zunächst die
Systemdaten (abgelegt in ``/sys``), die Daten der angeschlossenen Geräte
(abgelegt in ``/dev``) und der laufenden Prozesse (abgelegt in ``/proc``) in das
zu wartende System eingebunden. Anschließend kann man mit ``chroot .`` das
entsprechende Verzeichnis als Basispfad nutzen und somit innerhalb des
Shell-Fensters Programme direkt auf dem zu wartenden System ausführen. Mit
``exit`` kann man in das eigentlich laufende (Live-)System zurück gelangen.


.. index:: dpkg
.. _dpkg:

``dpkg``
--------

Der Debian Package Manager (``dpkg``) ist die Basis-Anwendung zum Installieren
und Deinstallieren von Debian-Paketen; auch ``apt`` macht intern von ``dpkg``
Gebrauch. Auch wenn ein Programm nicht in den Paket-Quellen enthalten ist, kann
es von einer entsprechenden Webseite (z.B. von `Sourceforge
<http://www.sourceforge.net>`_) heruntergeladen und Download-Ordner mit ``sudo
dpkg -i paket.deb`` installiert werden. Entsprechend kann es mit ``sudo dpkg -r
paketname`` wieder (unter Beibehaltung der Konfigurationsdateien) deinstalliert
oder mit ``dpkg -P paketname`` restlos entfernt werden.

Mit ``dpkt -l suchbegriff`` lassen sich alle Pakete auflisten, die auf einen
Suchbegriff zutreffen -- reguläre Ausdrücke können ebenfalls eingesetzt werden.
Mit ``dpkg -S paketname`` wird angezeigt, welche Datei(en) durch das
entsprechende Paket installiert wurden.


.. index:: eject
.. _eject:

``eject``
---------

Mit ``eject devicename``, z.B. ``eject /dev/cdrom0``, kann das CD/DVD-Laufwerk
geöffnet werden.


.. index:: fdisk
.. _fdisk:

``fdisk``
---------

Mit ``fdisk`` können Informationen über interne und externe Festplatten bzw.
Speichermedien angezeigt werden. Ebenso ist es möglich, mit ``fdisk``
Partitionen zu verwalten.

Nützlich ist der Aufruf von ``fdisk -l``, um Disk-Informationen angeschlossener
Speichermedien anzuzeigen.


.. index:: halt, reboot
.. _halt:
.. _reboot:

``halt``, ``reboot``
--------------------

* Mit ``halt`` kann das System herunter gefahren und der Computer ausgeschaltet
  werden.

* Mit ``reboot`` kann das System neu gestartet werden.


.. index:: lshw
.. _lshw:

``lshw``
--------

Mit ``lshw`` werden die Hardware-Informationen des Computers aufgelistet; mit
``lshw -short`` wird eine Kurzform dieser Informationen ausgegeben.


.. index:: mount, umount
.. _mount:
.. _umount:

``mount``, ``umount``
---------------------

Mit ``mount device pfad`` kann ein Datenträger (Speichermedium, Partition oder
Ordner) in den angegebenen Pfad einbinden ("mounten"); entsprechend wird mit
``umount pfad`` die Einbindung gelöst, falls kein Programm aktuell auf das im
angegebenen Pfad eingebundene Medium zugreift.


.. index:: nast
.. _nast:

``nast``
--------

Das Programm ``nast`` ist nicht standardmäßig auf jedem Linux-System
installiert, kann aber einfach nachinstalliert werden:

.. code-block:: bash

    sudo aptitude install nast

Mit ``nast -m`` können dann die IP-Adressen aller Rechner und Router, die sich
im lokelen Netzwerk befinden, aufgelistet werden.


.. index:: su
.. _su:

``su``
------

Mit ``su benutzername`` kann sich ein Superuser als beliebiger anderer Benutzer
anmelden. Mit ``sudo su root`` kann sich ein beliebiger Benutzer, der dazu
berechtigt ist, sich in einer Shell dauerhaft Superuser-Rechte verschaffen; dazu
muss ein entsprechender Eintrag folgender Form in der Datei ``/etc/sudoers``
existieren:

.. code-block:: bash

    # User privilege specification
    benutzername	ALL=(ALL:ALL) ALL

Der Benutzerwechsel kann mit ``exit`` wieder beendet werden.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] In der Datei ``/etc/apt/sources.list`` ist festgelegt, auf welchen
    Servern ``apt`` nach verfügbarer Software suchen bzw. diese installieren
    soll. Je nach Vorlieben können stets die aktuellsten Entwicklungen oder nur
    ältere, bereits bewährte Pakete abgefragt werden.

    Durch Aufruf von ``apt-get update`` wird die Liste an verfügbaren Paketen
    aktualisiert. Zusätzlich zu jeder Quelle, die durch einen ``deb``-Eintrag
    festgelegt wird, kann ein ``deb-src``-Eintrag stehen, wenn von dort auch
    Quellcode heruntergeladen werden soll (interessant für Entwickler bzw. um
    Programme selbst zu kompilieren).

.. [#] Tip für private Desktop-PCs: Zwei lauffähige Linux-Varianten parallel
    installieren! So kann das weniger genutzte System als
    "Experimentier-Umgebung" genutzt werden.


.. [#]  Mit ``.`` wird der Pfad des aktuellen Verzeichnisses bezeichnet.

