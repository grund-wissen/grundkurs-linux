.. _Standard-Programme:

Standard-Programme
==================

Die folgenden Programme sind auf den meisten Debian-Systemen (und vielen anderen
Linux-Distributionen) standardmäßig installiert. Die Liste beinhaltet eine
Auswahl von Programmen, die einem mit großer Wahrscheinlichkeit früher oder
später in Shell-Scripten begegnen und die ohne Superuser-Rechte genutzt werden
können: 

.. index:: alias
.. _alias:

``alias``
---------

Mit ``alias kurzname='langer befehl'`` lassen sich Abkürzungen für längere
und/oder öfter gebrauchte Befehle definieren. Meist werden solche Aliase in der
Konfigurationsdatei ``~/.bashrc`` definiert. Steht dort in einer Zeile
beispielsweise ``alias q='exit'``, so lässt sich das aktuelle Shellfenster
wahlweise mit ``q`` oder mit ``exit`` schließen. Ist ein ``alias ll='ls -lh'``
definiert, so lässt sich eine ausführliche Liste des aktuellen Verzeichnisses
mit ``ll`` aufrufen.

.. _aptitude:

``apt``, ``aptitude``
---------------------

Mit ``apt-cache search suchbegriff`` bzw. ``aptitude search suchbegriff`` kann
das System nach Paketen durchsucht werden, deren Name oder Beschreibung dem
Suchbegriff entspricht. Die Ausgabe von ``aptitude`` gibt zusätzlich an, ob die
entsprechenden Pakete installiert sind (``i`` für "installed") oder nicht
(``p`` für "purged").

Zum (De-)Installieren von Paketen sind Superuser-Rechte erforderlich.


.. index:: basename
.. _basename:

``basename``
------------

Mit ``basename dateiname`` wird der Dateiname (ohne den Verzeichnispfad)
angezeigt. Mit ``basename dateiname endung`` wird zusätzlich zum Verzeichnispfad
auch die angegebene Endung der Datei "abgeschnitten" (nützlich für
Konvertierungs-Skripte, automatische Umbenennungen, etc.).

Im umgekehrten Fall kann das Verzeichnis einer Datei mittels ``dirname
dateiname`` bestimmt werden.


.. index:: bc
.. _bc:

``bc``
------

Mit ``bc`` steht ein simpler Taschenrechner auf der Kommandozeile zur Verfügung.
Zahlen und Rechenzeichen können nach dem Aufruf direkt eingegeben werden; bei
Bedarf können auch Klammern gesetzt werden. Nach Bestätigung mit der
``Enter``-Taste wird das Ergebnis berechnet und angezeigt. Frühere Berechnungen
können mit der :math:`\uparrow`-Taste wieder angezeigt bzw. bearbeitet werden. 

Ruft man ``bc`` mit der Option ``-l`` auf, so wird automatisch eine
Standard-Bibliothek mit einigen wichtigen mathematischen Funktionen geladen.
Beispielsweise kann so mittels ``s(num)`` der :ref:`Sinus <gwm:Winkelfunktionen
am Einheitskreis>` der Zahl ``num`` ausgegeben werden, mittels ``c(num)`` der
Cosinus und mit ``a(num)`` der :ref:`Arcus-Tangens <gwm:Arcus-Funktionen>`; die
übergebenen Werte ``num`` müssen dabei in :ref:`Radiant <gwm:Gradmaß und Bogenmaß>`
angegeben werden. Mit ``l(num)`` kann der :ref:`natürliche Logarithmus
<gwm:Logarithmusfunktionen>` der Zahl ``num`` berechnet werden, mit ``e(num)``
wird der Wert der :ref:`natürlichen Exponentialfunktion <Exponentialfunktionen>`
von ``num`` ausgegeben.

Man kann ``bc`` auch innerhalb von :ref:`Shell-Skripten <Shell-Scripting>`
verwenden, um numerische Berechnungen auszuführen und die Ergebnisse
gegebenenfalls in :ref:`Variablen <Zuweisung von Variablen>` zu speichern. Dazu
wird der auszuwertende Ausdruck mittels ``echo`` und einem :ref:`Pipe-Zeichen
<Pipelines>` an ``bc`` übergeben:

.. code-block:: bash

    echo '8/3' | bc 
    # Ergebnis: 2.66666666666666666666

    pi=$( echo 'a(1)*4' | bc -l )
    echo $pi
    # Ergebnis: 3.14159265358979323844

Beim letzten Beispiel als Trick genutzt, dass der Arcus-Tangens von :math:`1`
den Wert :math:`\frac{\pi}{4}` liefert. Die Auswertung von ``a(1)*4`` mittels
der ``bc``-Mathe-Bibliothek liefert somit die Kreiszahl :math:`\pi` als
Ergebnis.


.. index:: bzip2
.. _bzip2 und bunzip2:

``bzip2``, ``bunzip2``
----------------------

Mit ``bzip2 dateiname`` kann eine Datei zu einer gleichnamigen Datei im
``bz2``-Format im komprimiert werden. Mit ``bunzip2 dateiname.bz2`` kann die
Datei wieder dekomprimiert werden. 

Gibt man mehrere Dateinamen an, so wird jede Datei in ein eigenes Archiv
komprimiert. Um eine einzelne ``bz2``-komprimierte Datei zu erhalten, die
mehrere Dateien enthält, so werden diese zunächst mittels ``tar`` zu einem
Archiv gepackt. [#TARBZ]_ 

.. cal: Kalender

.. index:: cat, head, tail
.. _cat:

``cat``
-------

Mit ``cat file`` wird der Inhalt einer Datei auf dem Bildschirm ausgegeben. Bei
der Ausgabe von langen Dateien kann mit ``Shift PageUp`` und ``Shift PageDown``
auf- und abgeblättert werden.

``cat`` kann ebenso verwendet werden, um zwei Textdateien zu einer einzelnen zu
verbinden ("concatenate"). Um beispielsweise eine Textdatei an eine andere
anzuhängen, lautet die Syntax ``cat datei1 >> datei2``. Um aus zwei Dateien
eine neue Datei zu erstellen, lautet die Syntax ``cat datei1 datei2 >
datei-neu.txt``.

Der Anfang oder das Ende einer Datei kann mit ``head file`` bzw. ``tail file``
angezeigt werden.


.. index:: cd 
.. _cd:

``cd``
------

Mit ``cd pfad`` wechselt man zu einem bestimmten Verzeichnis. Die
``pfad``-Angabe kann dabei absolut (ausgehende vom Basis-Verzeichnis ``/``) oder
relativ (ausgehend vom aktuellen Verzeichnis) sein. 

* Mit ``cd ..`` gelangt man ins übergeordnete Verzeichnis, mit ``cd ../..`` in
  das nächst höhere usw. 
* Mit ``cd`` gelangt man ebenso wie mit ``cd ~`` ins Home-Verzeichnis. Mit ``cd
  ~benutzername`` gelangt man (als Superuser) in das Home-Verzeichnis des
  angegebenen Benutzers.


.. index:: chmod 

``chmod``
---------

Mit ``chmod`` lassen sich die Zugriffsrechte einer Datei festlegen. Eine Datei
kann lesbar (``r`` für "read"), schreibbar (``w`` für "write") und/oder
ausführbar (``x`` für "executeable") sein.

* Mit ``chmod +x file`` wird eine Datei (z.B. ein Skript) im aktuellen Ordner
  ausführbar gemacht. Sie kann anschließend mit ``./file`` aufgerufen werden.
* Mit ``chmod -w file`` werden der Datei die Schreibrechte entzogen.

..  u Eigentümer (user)
..  g Gruppe (group)
..  o alle anderen (others)
..  a alle drei Benutzergruppen (all)
..  + hinzufügen
..  - wegnehmen
..  = gleich nachfolgendem Muster setzen
..  r Leserecht (read); Bit-Wert 4
..  w Schreibrecht (write); Bit-Wert 2
..  x Ausführrecht (execute); Bit-Wert 1

..  Ausführrecht für Eigentümer von Datei script hinzufügen:
..  chmod u+x script

..  Datei script: alle Rechte für Eigentümer; Lese- und Ausführrechte für
..  Gruppe; für alle anderen nur Ausführrechte. Gleichgültige Varianten:
..  chmod 751 script
..  chmod u=rwx,g=rx,o=r script

.. index:: clear
.. _clear:

``clear``
---------

Mit ``clear`` wird der Bildschirm "geleert" bzw. "aufgeräumt" -- lediglich der
aktuelle Eingabe-Prompt bleibt bestehen. Die Shell-History (mit :math:`\uparrow`
bzw. :math:`\downarrow` abrufbar) bleibt unverändert.


.. index:: cp
.. _cp:

``cp``
------

Mit ``cp datei neuer-pfad`` wird eine Datei (oder ein Verzeichnis) an eine
andere Stelle kopiert. Es können mehrere Dateien auf einmal angeben werden; der
zuletzt angegebene Pfad stellt dann den Zielpfad dar, in den alle zuvor
angegebenen Dateien kopiert werden.  

* Mit ``cp -r`` werden auch Unterverzeichnisse rekursiv kopiert (andernfalls
  werden sie weggelassen). * Mit ``cp -s`` wird anstelle des Kopierens ein
  symbolischer Link am Zielpfad erstellt.


.. index:: date
.. _date:

``date``
--------

Mit ``date`` wird das aktuelle Datum und die aktuelle Uhrzeit angezeigt.

Die Ausgabe von ``date`` kann mittels verschiedener Aufrufparameter beliebig
angepasst werden. Dies kann u.a. in Skripten hilfreich sein, um "Zeitstempel" in
Dateinamen aufzunehmen. Der Aufruf von ``date +%Y%m%d_%H%M%S`` gibt
beispielsweise eine Zeitangabe im Format ``YYYYMMDD_hhmmss`` aus. Beispielsweise
entspricht dem Datum "30.08.2012, 9:21:03 Uhr" damit die Zeichenfolge
"20120830_092103". 

..  dd [option=wert]
..  Vewendung: Kopieren von Dateien (auch Geräte)
..  dd if=/dev/cdrom of=/tmp/cd.iso
..  Es wird immer die ganze CD-ROM kopiert, egal wie voll die CD-ROM ist 

.. index:: df
.. _df:

``df``
------

Mit ``df`` wird angezeigt, wie viel Speicherplatz im Augenblick auf den
eingehängten Laufwerken verfügbar ist ("disk free").

* Mit ``df -h`` wird die Ausgabe "human readable" gestaltet, d.h. die Größen
  werden in KB, MB oder GB anstelle von Bytes angegeben.


.. index:: dirname
.. _dirname:

``dirname``
-----------

Mit ``dirname dateiname`` wird der Verzeichnisname einer Datei (ohne den
eigentlichen Dateinamen) angezeigt.


.. index:: du
.. _du:

``du``
------

Mit ``du`` wird angezeigt, wie viel Festplattenspeicher durch das aktuelle
Verzeichnis und seiner Unterverzeichnisse belegt wird. 

* Mit ``du -h`` wird die Ausgabe "human readable" gestaltet, d.h. die Größen
  werden in KB, MB oder GB anstelle von Bytes angegeben. * Mit ``du -c`` wird
  die Gesamtgröße jedes Unterverzeichnisses sowie des aktuellen Verzeichnisses
  ausgegeben. ``du -S`` bewirkt im Prinzip das gleiche, allerdings wird hierbei
  die Größe der Unterverzeichnisse nicht zur Berechnung einer Verzeichnisgröße
  einbezogen. * Mit ``du -s`` wird nur die Gesamtsumme der Dateigrößen
  ausgegeben. * Mit ``du -L`` wird statt der Größe von Symlinks die Größe der
  verlinkten Dateien berücksichtigt.


.. index:: echo
.. _echo:

``echo`` 
---------

Mit ``echo variable`` kann der Inhalt einer Variablen angezeigt werden.
Beispielsweise liefert ``echo $PATH`` die Namen aller Verzeichnisse, in denen
nach ausführbaren Shell-Programmen gesucht wird.

Möchte man ``echo`` verwenden, um einen Text mittels einer :ref:`Pipe
<Pipelines>` an ein anderes Programm zu übergeben, so muss beachtet werden, dass
dabei beispielsweise das Newline-Zeichen ``\n`` nicht ausgewertet wird. Um dies
zu erreichen, muss ``echo`` mit der Option ``-e`` aufgerufen werden.


.. index:: exit
.. _exit:

``exit``
--------

Mit ``exit`` wird der aktuelle Benutzer abgemeldet die aktuelle Sitzung (z.B.
``ssh``) beendet. Ist nur eine Sitzung geöffnet, wird das Shell-Fenster
geschlossen.


.. index:: file
.. _file:

``file``
--------

Mit ``file dateiname`` werden ausführliche Datei-Informationen (Dateityp,
Version, Kodierung) der angegebenen Datei angezeigt.


.. index:: find
.. _find:

``find``
--------

Mit ``find`` können Verzeichnisse nach Dateien durchsucht werden. Angezeigt
werden jeweils (nur) die Dateien, die dem vorgegebenen Suchmuster
entsprechen. Die allgemeine Syntax lautet:

.. code-block:: bash

    find basisordner kriterium [weitere kriterien]

Häufig genutzte Kriterien sind beispielsweise:

* ``-name suchmuster``: Zeigt alle Dateien an, die dem Suchmuster entsprechen --
  einem "normalen" Namen, oder einem regulären Ausdruck.
* ``-iname suchmuster``: Zeigt alle Daten an, die dem Suchmuster entsprechen --
  Groß- und Kleinschreibung wird dabei ignoriert.
* ``-mtime -n``: Zeigt alle Dateien an, die im Laufe der letzten :math:`n` Tage
  (``n * 24h``) modifiziert wurden. Um Dateien anzuzeigen, deren letzte Änderung
  *mindestens* ``n * 24h`` zurückliegt, wird das ``-``-Zeichen weggelassen.
* ``-executeable``: Zeigt nur ausführbare Dateien an.
* ``-size n [kMG]``: Zeigt nur Dateien an, deren Dateigröße über ``n``
  Kilo-/Mega-/Giga-Bytes liegt.
* ``-user name``: Zeigt nur Dateien an, die dem angegebenen Benutzer gehören.
* ``-type [fdl]``: Zeigt Dateien an, die dem angegebenen Dateityp entsprechen
  (``f``: Normale Datei ("file"), ``d``: Verzeichnis ("directory"), ``l``:
  Symbolischer Link).

Mit ``!-kriterium`` können die obigen und weitere Kriterien (siehe ``man find``)
"umgekehrt" werden, so dass sie die genau gegenteiligen Ergebnisse liefern.

``find`` kann auch in Verbindung mit :ref:`grep <grep>` genutzt werden, um
zunächst bestimmte Dateien zu finden, und diese dann nach bestimmten Inhalten
zu durchsuchen. Um beispielsweise die Namen aller Python-Dateien (Endung
``.py``) eines Verzeichnisses und aller Unterverzeichnisse auszugeben, welche
die Zeichenkette ``import sympy`` beinhalten, kann man folgendes eingeben:

.. code-block:: bash

    find ./ -name "*.py" -exec grep -l "import sympy" {} \;

Hierbei werden von ``find``, ausgehend vom aktuellen Verzeichnis ``./``, alle
Dateien mit der Endung ``.py`` gesucht. Mit der Option ``-exec`` werden diese
Dateien an das darauf folgende Programm übergeben, wobei die einzelnen Dateien
an der Stelle eingefügt werden, wo die geschweiften Klammern ``{}`` stehen. Die
``exec``-Anweisung muss am Ende mit ``\;`` abgeschlossen werden.

Noch einfacher ist die Verwendung von :ref:`xargs <xargs>`, um die von ``find``
gefundenen Dateinamen an ``grep`` zu übergeben. Sollen beispielsweise alle
Dateien mit der Endung ``.rst`` nach einem angegebenen Text durchsucht
werden, kann folgendes eingegeben werden:

.. code-block:: bash

    find ./ -name "*.rst" | xargs grep "Suchbegriff"

Nutzt man diese Kombination häufiger, so kann dafür in der Konfigurationsdatei
``~/.bashrc`` ein :ref:`alias <alias>` definiert werden:

.. code-block:: bash

    alias rstgrep='find ./ -name "*.rst" | xargs grep'

Damit kann künftig ``rstgrep`` ebenso wie ``grep`` mit allen dort zur Verfügung
stehenden Optionen aufgerufen werden.


..  find / -user benutzername -print 2>/dev/null

..  Findet alle Dateien eines Benutzers, gibt keine Fehlermeldungen aus, da
..  Fehlerausgaben (Kanal 2) nach /dev/null umgeleitet werden und somit nicht
..  auf dem Bildschirm erscheinen.

..  Damit uns im Beispiel hier nicht die Standardausgabe (Kanal 1) auf dem
..  Bildschirm stört, leiten wir diese auch beim Start des Scripts nach /dev/null um 
..  (``1>/dev/null``). Und damit uns die Shell für weitere Eingaben zur Verfügung
..  steht, stellen wir die Ausführung des Scripts in den Hintergrund (``&``).

.. index:: grep
.. _grep:

``grep``
--------

Mit ``grep`` ("get regular expression") können Eingabedaten, Textdateien oder
Verzeichnisse nach beliebigen Suchbegriffen und regulären Ausdrücken durchsucht
werden. Der allgemeine ``grep``-Befehl hat folgende Syntax:

.. code-block:: bash

    grep [optionen] suchmuster suchpfad

Möchte man beispielsweise das aktuelle Verzeichnis und alle Unterverzeichnisse
rekursiv nach einem Suchbegriff durchsuchen, wobei die Groß- und Kleinschreibung
ignoriert werden soll, so gibt man folgendes ein:

.. code-block:: bash

    grep -lir "suchbegriff" ./

Mittels der Option ``-l`` werden nur die Dateinamen anstelle der zutreffenden
Textzeilen ausgegeben, mit ``-i`` ("ignore-case") die Groß-und Kleinschreibung
ignoriert, und mit ``-r`` ("recursive") die Durchsuchung der Unterverzeichnisse
aktiviert. Mittels der Option ``-c`` wird die Anzahl an Treffern angezeigt, mit
der Option ``-v`` werden diejenigen Zeilen als Ergebnis ausgegeben, auf die das
Suchmuster *nicht* zutrifft.

Möchte man alle Ergebnisse anzeigen, die auf (mindestens) eines von mehreren
angegebenen Suchmustern zutreffen, so können die einzelnen Suchmuster jeweils
mit der Option ``-e`` angegeben werden.

Als :ref:`Exit-Status <Rückgabewerte und Verkettung von Programmen>` liefert
``grep`` den Wert ``0``, wenn die Suche erfolgreich war, ``1``, wenn das
Suchmuster nicht gefunden wurde, und ``2``, wenn bei der Suche ein Fehler
aufgetreten ist (beispielsweise eine Datei nicht lesbar war). 

..   
    Todo: Links auf reguläre Ausdrücke
    

.. index:: gzip
.. _gzip:

``gzip``, ``gunzip``
--------------------

Mit ``gzip dateiname`` kann eine Datei komprimiert, mit ``gunzip dateiname.gz``
wieder dekomprimiert werden. Mittels ``zcat dateiname.gz`` kann eine
komprimierte Datei auf dem Bildschirm ausgegeben werden, ohne dass sie dazu auf
der Festplatte entpackt wird (dies wird beispielsweise für Hilfeseiten genutzt,
die in komprimierter Form auf der Festplatte abgelegt sind).


.. index:: host
.. _host:

``host``
--------

Mit ``host URL`` kann die IP-Adresse einer Webseite angezeigt werden. Beispiel:

.. code-block:: bash

    host www.grund-wissen.de
    # www.grund-wissen.de has address 188.40.57.88


.. index:: ip
.. _ip:

``ip``
------

Mit ``ip r`` kann die lokale Netzwerkadresse (``192.168.xxx.xxx``) angezeigt
werden.


.. index:: kill, killall
.. _kill und killall:

``kill``, ``killall``
---------------------

Mit ``kill prozessID`` bzw. mit ``killall programmname`` lässt sich ein (evtl.
außer Kontrolle geratenes) Programm beenden. Die ID eines Prozesses lässt sich
beispielsweise mit ``ps -aux programm``, ``pgrep programmname`` oder mittels des
Systemmonitors :ref:`top <top>` anzeigen. Innerhalb von ``top`` lässt sich der
``kill``-Befehl mittels ``k`` starten.

* Mit ``kill -9 prozessID`` bzw. mit ``killall -9 programmname`` wird ein
  Prozess unterbrochen, egal welchen Signalwert er gerade ausgibt. Dies ist die
  stärkste Form, einen unerwünschten Prozess zum erliegen zu bringen.

.. index:: less
.. _less:

``less``
--------

Mit ``less dateiname`` kann der Inhalt einer Textdatei angezeigt werden. Die
Anzeige beginnt am Anfang der Datei, mit der :math:`\downarrow` bzw.
:math:`\uparrow` kann innerhalb der Datei nach unten bzw. oben gescrollt werden.
Mit ``/`` kann die Datei nach einem Begriff durchsucht werden, mit ``n`` kann
man zum nächsten Suchergebnis springen. Mit ``q`` wird less wieder beendet.

.. index:: ln
.. _ln:

``ln``
------

Mittels ``ln`` bzw. ``ln -s`` lassen sich die zwei unter Linux möglichen Arten
von Verknüpfungen erzeugen:

.. index:: Hardlink

* Mit ``ln datei1 datei2`` wird zu einer existierenden Datei ``datei1`` die
  Datei ``datai2`` als so genannter "Hardlink" erzeugt. Dabei handelt es sich im
  Grunde um eine zusätzliche Bezeichnung für die selbe Speicherstelle auf der
  Festplatte. Um beispielsweise eine mit Hardlinks versehene Datei zu löschen,
  müssen ebenfalls sämtliche Hardlink entfernt werden, um die Speicherstelle
  freizugeben. 
  
  Da sich Hardlinks stets auf der gleichen Partition befinden müssen wie die
  Original-Dateien und sich nur auf "normale" Dateien, jedoch nicht auf
  Verzeichnisse anwenden lassen, werden sie unter Linux nur selten verwendet.

.. index:: Symlink

* Mit ``ln -s datei1 datei2`` wird zu einer existierenden Datei ``datei1`` die
  Datei ``datai2`` als so genannter "Symbolischer Link" erzeugt (auch "Symlink"
  oder "Softlink" genannt). Dabei handelt es sich um eine neue Datei, deren
  einziger Inhalt ein Verweis auf die bestehende Datei ist (Symlinks sind daher
  stets nur wenige Bytes groß).

  Wird ein Symlink zu einer Textdatei mit einem Editor geöffnet, verändert und
  gespeichert, so wird auch die Originaldatei entsprechend verändert. Wird
  allerdings der Symlink einer Datei gelöscht, so bleibt die Originaldatei
  bestehen. Wird im umgekehrten Fall die Original-Datei gelöscht oder umbenannt,
  so bleibt der Symlink als Datei bestehen, zeigt aber ins Leere ("gebrochener
  Link"). Der Symlink muss in diesem Fall entfernt und neu erzeugt werden.
  [#MCS]_
  
  Wird ein Symlink zu einer ausführbaren Datei erzeugt, so kann diese auch über
  den Symlink aufgerufen werden. Wird ein Symlink zu einem Ordner erstellt, so
  lassen sich dessen Inhalte auch über den Symlink anzeigen und verändern. Da
  Symlinks auch anders benannt sein können als die Originaldateien, können sie
  beispielsweise dazu genutzt werden, um aus einer vorhandenen Musiksammlung
  individuelle Playlisten in separaten Ordnern anzulegen. 
  
  Mit Symlinks verknüpfte Ordner bzw. Dateien müssen nicht zwingend auf dem
  gleichen Datenträger bzw. der gleichen Partition liegen. So ist es
  beispielsweise möglich auf einen (automatisch ins ``/media``-Verzeichnis
  eingebundene) USB-Stick oder eine verschlüsselte Festplattenpartition über
  einen entsprechenden Symlink im Home-Verzeichnis zuzugreifen. 


.. index:: locate
.. _locate:

``locate``
----------

Mit ``locate suchbegriff`` werden alle Dateinamen des Systems nach einem
Suchbegriff durchsucht und die Ergebnisse angezeigt. Mit ``locate -i
suchbegriff`` wird dabei die Groß- und Kleinschreibung ignoriert.

Um auch neueste Änderungen, die sich seit dem letzten Systemstart ergeben haben,
anzuzeigen, kann die Datei-Datenbank mittels ``updatedb`` aktualisiert werden.

.. index:: ls
.. _ls:

``ls``
------

Mit ``ls`` wird der Inhalt des aktuellen Verzeichnisses ausgegeben. Mit weiteren
Parametern lässt sich die Ausgabe den eigenen Wünschen anpassen:

* ``ls -a`` zeigt auch Konfigurationsdateien und -verzeichnisse an, d.h.
  Dateien, deren Name mit einem ``.`` beginnt ("list all").
* ``ls -lh`` liefert eine ausführliche Liste, die auch Informationen über
  Dateityp, Dateirechte, Modifikationszeit und Dateigröße beinhaltet ("long
  list"). Der Zusatz ``h`` bewirkt, dass die Dateigröße "human readable", d.h.
  in KB, MB oder GB anstelle von Bytes angeben wird.
* ``ls -r`` listet rekursiv die Inhalte des aktuellen Verzeichnisses und der
  darin enthaltenen Unterverzeichnisse auf.

..  * ls -lt: Sortiert nach Modifikationszeit
..  * ls -lS: Sortiert nach Dateigröße

.. - normale Datei
.. d Verzeichnis ( d = directory)
.. p Named Pipe; steht für eine Art Pufferungsdatei, eine Pipe-Datei.
.. c ( c = character oriented) steht für eine zeichenorientierte Gerätedatei.
.. b ( b = block oriented) steht für eine blockorientierte Gerätedatei.
.. s ( s = socket) steht für ein Socket (genauer einen UNIX-Domain-Socket).
.. l symbolische Links

..  ( rwx ) von links nach rechts: Eigentümer, Gruppe und allen anderen.


Mit ``ls pfad`` kann ebenfalls der Inhalt eines anderen Verzeichnisses
ausgegeben werden, ohne dass das aktuelle Verzeichnis verlassen wird.

Eine vollständige Beschreibung aller Optionen findet sich in den Manpages (``man
ls``).

.. index:: man
.. _man:

``man``
-------

Mit ``man programm`` werden die Hilfeseiten ("Manual-Pages", "Manpages") eines
Programms angezeigt. Hier werden sämtliche Programm-Aufruf-Optionen sowie meist
einige nützliche Beispielfälle beschrieben.

*Beispiel:* Mit ``man less`` werden die Hilfe-Seiten zum Pager-Programm "less"
angezeigt.

Um alle Hilfeseiten nach einem bestimmten Begriff zu durchsuchen, kann ``man``
mit der Option ``-k`` ("keyword") aufgerufen werden:

*Beispiel:* Mit ``man -k find`` werden alle Programmnamen und Funktionen
aufgelistet, die den Suchbegriff "find" in ihrer Hilfeseite enthalten. 


.. index:: mkdir
.. _mkdir:

``mkdir``
---------

Mit ``mkdir verzeichnisname`` wird ein neues Verzeichnis angelegt.
``verzeichnisname`` kann auch ein absoluter Pfad sein, dann wird das Verzeichnis
an entsprechender Stelle angelegt.


.. index:: mv
.. _mv:

``mv``
------

Mit ``mv datei neuer-pfad`` wird eine Datei (oder ein Verzeichnis) an eine
andere Stelle verschoben. Es können mehrere Dateien auf einmal angeben werden;
der zuletzt angegebene Pfad stellt dann den Zielpfad dar, in den alle zuvor
angegebenen Dateien verschoben werden.  

Mit ``mv alter-dateiname neuer-dateiname`` lässt sich eine Datei umbenennen.

.. index:: pdftotext
.. _pdftotext:

``pdftotext``
-------------

Mit ``pdftotext pdf-datei`` lässt sich der gesamte Text einer PDF-Datei in eine
Textdatei extrahieren. Der Text lässt sich dann meist recht einfach mittels ein
paar Vim-Tricks und Einfügen von Restructured-Text-Syntax via Sphinx in ein
druckbares Latex-Dokument oder eine leicht durchsuchbare HTML-Seite umwandeln.
Sehr nützlich!

.. ps

.. ps -f Aktuelle Prozessliste. PID: Prozess-ID, PPID: Parent Prozess ID

.. index:: pwd
.. _pwd:

``pwd``
-------

Mit ``pwd`` ("print working directory") wird der volle Pfad des aktuellen
Verzeichnisses ausgegeben.


.. index:: rm
.. _rm:

``rm``
------

Mit ``rm datei(en)`` lässt sich eine oder mehrere Datei(en) unwiderruflich
löschen.

* Mit ``rm -r verzeichnis/*`` werden rekursiv alle Inhalte, ausgehend von
  ``verzeichnis`` gelöscht. 

*Achtung:* Die Shell kennt keinen "Papierkorb", Löschvorgänge sind somit
endgültig. Vor dem Löschen sollte man sich daher stets vergewissern, ob man die
entsprechenden Dateien auch wirklich löschen möchte.

Mit regulären Suchmustern wie ``*`` ist beim Löschen stets besondere Vorsicht
geboten: Während ``rm -r *~`` ausgehend vom aktuellen Verzeichnis alle (von
manchen Editoren angelegten) temporären Dateien löscht, würde ``rm -r ~*``
sämtliche Inhalte des Home-Verzeichnisses unwiderruflich löschen!


.. index:: rmdir
.. _rmdir:

``rmdir``
---------

Mit ``rmdir verzeichnisname`` wird ein Verzeichnis gelöscht, sofern es leer ist.
Möchte man ein nicht-leeres Verzeichnis löschen, so empfiehlt sich das einfach
zu tippende ``rm -r  verzeichnisname*`` (es werden rekursiv alle Dateien, deren
Pfadname mit ``verzeichnisname`` beginnt, gelöscht). 


.. index:: rsync
.. _rsync:

``rsync``
---------

Mit ``rsync quelldatei backupdatei`` kann man eine Datei oder ein Verzeichnis
gegenüber einer Backup-Kopie der Datei bzw. des Verzeichnisses aktualisiert
("synchronisiert") halten. Der Backup findet dabei nur in eine Richtung statt,
d.h. ``rsync`` prüft anhand der letzten Bearbeitungszeit (``MTIME``) einer
Datei, ob sich in der Quelle gegenüber dem Backup eine Veränderung ergeben hat.
Falls ja, werden diese Änderungen übernommen.

Möchte man einen Backup von einem ganzen Verzeichnispfad mitsamt allen
Unterverzeichnissen anlegen oder aktuell halten, so empfiehlt sich folgender
Aufruf von ``rsync``: 

.. code-block:: bash

    rsync -vahz quellverzeichnis/* zielverzeichnis

Das Zielverzeichnis muss dabei ein bestehender Ordner sein, kann sich allerdings
auch auf einer anderen Partition, einem externen Datenträger, oder -- bei
Verwendung von ``ssh`` -- sogar auf einem anderen Rechner befinden.

..  use rsync with -l to preserve links!  (copy symlinks as symlinks)
..  and -L or --copy-links to copy what the symlink actually points to.

.. index:: Unison

Möchte man eine Synchronisierung zweier Verzeichnisse nicht nur in eine Richtung
(ist der Backup "neuer" als die Quelle, so nimmt ``rsync`` keine Veränderungen
vor), so ist das Tool `Unison <http://wiki.ubuntuusers.de/Unison>`_ bzw. das
gleiche Programm mit graphischer Oberfläche ``unison-gtk`` zu empfehlen. Es
lässt sich über die gleichnamigen Pakete via ``apt`` installieren:

.. code-block:: bash

    sudo apt-get install unison-gtk

Nach der Installation kann Unison mittels ``unison-gtk`` aufgerufen werden. Es
verwendet intern ebenfalls ``rsync``. Um es zu benutzen, erstellt man ein
"Profil", in welchem man zwei zu synchronisierende Verzeichnisse auswählt.
Öffnet man dieses im Auswahlmenü, so scannt Unison die Verzeichnisse automatisch
nach Veränderungen und zeigt diese mitsamt der Richtung und der Art der
Veränderung graphisch an. Mit einem Klick auf "Go" (Hotkey ``g``) werden die
Änderungen übernommen.

``rsync`` und ``unison`` eignen sich sehr gut zur Verwaltung von
Sicherheitskopien oder zum "Mitnehmen" eines Projektes von einem stationären PC
auf einen USB-Stick. Veränderungen sind dabei erlaubt, denn sie können wiederum
in umgekehrter Richtung synchronisiert werden. 

Persönlich verwende ich zur Synchronisierung von Dateien zwischen meinem Rechner
und einem (mit LUKS verschlüsselten) USB-Stick folgende Methode: In einem
eigenen Verzeichnis namens ``shared`` lege ich für jede zu synchronisierende
Datei oder jeden zu synchronisierenden Ordner einen gleichnamigen Symlink ab,
der allerdings am Namen die (zusätzliche) Endung ``.sync`` erhält. Dieses
Verzeichnis mit den entsprechenden Symlinks muss sowohl auf der Festplatte wie
auch auf dem USB-Stick vorhanden sein, die Ziele der Symlinks sind allerdings
logischerweise unterschiedlich, beispielsweise::

    /home/user/shared
        code.sync       # ---> /home/user/data/code
        configs.sync    # ---> /home/user/data/configs
        homepage.sync   # ---> /home/user/data/homepage

    /media/user/usb0/shared
        code.sync       # ---> /media/user/usb0/code
        configs.sync    # ---> /media/user/usb0/configs
        homepage.sync   # ---> /media/user/usb0/homepage

Falls noch nicht vorhanden, so wird anschließend das Verzeichnis ``~/.unison``
angelegt. In diesem Verzeichnis lassen sich beliebig viele
Synchronisations-Profile als Textdateien mit der Endung ``.prf`` anlegen. Für
die Synchronisation mit dem USB-Stick sieht ein solches Profil bei mir
folgendermaßen aus::

    # Datei: ~/.unison/usb-sync.prf

    # Quell- und Zielverzeichnis:
    root = /home/user/shared
    root = /media/user/usb0/shared

    # Angabe der zu synchronisierenden Dateien:
    follow = Name *.sync

    # Folgende Dateien dennoch ignorieren: 
    ignore = Regex .*/.backupdir/*
    ignore = Regex .*/.git/*
    ignore = Regex .*/.hg/*

    # Bei Unterschieden zwischen Dateien nur das Nötigste ausgeben:
    diff = diff -y -W 79 --suppress-common-lines

Diese Variante setzt voraus, dass der USB-Stick immer an der gleichen Stelle
eingebunden wird (im obigen Beispiel ``/media/user/usb0``). Anschließend muss
nur noch ``unison usb-sync`` aufgerufen werden, um eine Synchronisation der
angegebenen Inhalte zu erreichen.

Im Shell-Modus wird die von Unison vorgeschlagene Synchronisationsrichtung mit
``<----`` oder ``---->`` angezeigt. Drückt man ``f`` ("follow"), so wird diese
Empfehlung übernommen. Wurden sowohl im Quell- wie auch im Zielverzeichnis
Änderungen vorgenommen, so zeigt Unison ``<-?->`` an. Der Benutzer muss in
diesem Fall die Unterschiede zwischen den Dateiversionen gegebenenfalls selbst
überprüfen (beispielsweise mittels :ref:`vimdiff <vimdiff>`) und kann
anschließend entweder mittels ``>`` oder ``<`` eine Synchronisationsrichtung
manuell angeben. 

.. Dies kann auch, beispielsweise mit dem Skript `watcher.py
.. <https://github.com/gregghz/Watcher>`_, automatisiert erfolgen.


Synchronisierungen mit ``rsync`` bzw. ``unison`` lassen sich nicht rückgängig
machen. Zu solch einem Zweck oder für Mehrbenutzer-Systeme, wenn es zu
konkurrierenden Entwicklungen kommen kann (wenn beispielsweise die gleiche Datei
in zwei Verzeichnissen auf unterschiedliche Weise verändert wird), sollte eine
Versionskontroll-Programm wie ``git`` oder ``mercurial`` genutzt werden.

.. sort

.. index:: ssh
.. _ssh:

``ssh``
-------

Mit ``ssh benutzername@rechneradresse`` kann man sich auf einem anderen
Linux-Rechner im lokalen Netzwerk oder im Internet anmelden. Ist die
Rechneradresse erreichbar, erscheint ein Dialogfeld zur Passworteingabe. Alle
auf dem Fremdrechner verfügbaren Shell-Befehle und -Programme lassen sich somit
"ferngesteuert" ausführen.

Zu einer Verwendung von ``ssh`` im lokalen Netzwerk sollten die folgenden beiden
Pakete installiert werden:

.. code-block:: bash

    sudo aptitude install openssh-client openssh-server

Ein Kopieren von Dateien zwischen Rechnern im Netzwerk ist (kompliziert) mit
``scp`` oder (einfach) mit Hilfe des Midnight-Commanders :ref:`mc <mc>` möglich.


..  stat: Ausführliche Dateiinformationen.. relevant? -> Scripting.. ?


.. index:: tar
.. _tar:

``tar``
-------

Mit ``tar`` können mehrere Dateien zu einem Archiv zusammengefasst werden.
Beispiel:

.. code-block:: bash

    tar -cf archiv.tar datei1 datei2 ...

Mit der Option ``z`` wird das Archiv zusätzlich mit ``gzip`` komprimiert. Mit
der Option ``v`` wird der Fortschritt der Archivierung angezeigt ("verbose" =
redselig).

.. code-block:: bash

    tar -czvf archiv.tar.gz datei1 datei2 ...

Der Inhalt eines ``tar``-Archivs kann mittels ``tar tf archiv.tar`` angezeigt
werden. Mittels der Option ``x`` (extract) kann der Inhalt des Archivs wieder
entpackt werden:

.. code-block:: bash

    tar -xvf archiv.tar          # für  "normale"   Archive 
    tar -xvzf archiv.tar.gz      # für komprimierte Archive

Anstelle der Option ``-z`` kann auch ``-j`` eingegeben werden, um anstelle der
``gz``-Komprimierung das stärker komprimierende ``bz2``-Format zu nutzen.

.. index:: tee
.. _tee:

``tee``
-------

Das Programm ``tee`` liest Text von der Standardeingabe ein und schreibt diesen
sowohl auf die Standardausgabe als auch in eine Datei. Dies kann beispielsweise
genutzt werden, um eine Fehlermeldung einerseits auf dem Bildschirm auszugeben,
andererseits gleichzeitig aber auch einen Eintrag in einer Logdatei zu
erstellen. Meistens wird dazu ein Text mittels ``echo`` ausgegeben und mittels
des :ref:`Pipe-Operators <Pipelines>` ``|`` an ``tee`` weitergereicht,
beispielsweise ``echo "Hallo!" | tee dateiname``.

.. index:: top
.. _top:

``top``
-------

Mit ``top`` werden aktuell laufende Prozesse, geordnet nach CPU-Auslastung,
angezeigt. Auf diese Weise kann die Prozess-ID (PID) eines außer Kontrolle
geratenen Programms oder "Speicherfressers" schnell ausfindig gemacht und der
entsprechende Prozess abgebrochen werden.

* Mit ``P`` werden die Prozesse nach CPU-Auslastung sortiert, mit ``M`` nach
  Memory-Auslastung, mit ``N`` nach Prozess-ID.
* Mit ``k`` wird nach Eingabe einer PID-Nummer der entsprechende Prozess
  abgebrochen. Die Nachfrage, mit welchem Signal der Prozess unterbrochen werden
  soll (Vorgabewert: ``15``), kann meist mit ``Enter`` bestätigt werden. Bei
  hartnäckigen Prozessen kann ``9`` angegeben werden, um den Prozess unabhängig
  von dessen Signalwert abzubrechen. 
* Mit ``q`` wird ``top`` wieder beendet.

.. index:: touch
.. _touch:

``touch``
---------

Mit ``touch dateiname`` lässt sich eine neue, leere Datei (beispielsweise eine
neue Log-Datei) anlegen.

.. tree Verzeichnis-Visualisierung

.. unique

.. index:: wc
.. _wc:

``wc``
------

Mit ``wc dateiname`` wird die Anzahl der Zeilen, Worte und Zeichen ausgegeben,
die in der angegebenen Datei vorkommen ("word count"). 

Oftmals wird ``wc`` in Kombination mit ``find`` oder ``grep`` verwendet, um
die Anzahl von Treffern bei einer bestimmten Suche anzuzeigen; 
um beispielsweise die Anzahl aller regulären Dateien des aktuellen
Verzeichnisses mitsamt aller Unterverzeichnisse (ohne die Verzeichnisnamen
selbst) anzuzeigen, kann man ``find ./ -type f | wc`` eingeben. 


.. index:: wget
.. _wget:

``wget``
--------

Mit ``wget`` lassen sich mit wenig Aufwand Downloads von der Shell aus starten.
Dabei können ganze Verzeichnisse (falls gewünscht auch mitsamt
Unterverzeichnissen), bestimmte Dateitypen, Dateigrößen usw. als
Auswahlkriterien festgelegt werden.

Um beispielsweise alle Beispiel-Dateien (1000 Stück!) des
Computer-Algebra-Systems Maxima von der Seite http://www.lungau-academy.at/wx1/
herunterzuladen, genügt folgender Befehl:

.. code-block:: bash

    wget -r -l1 -np -A wxmx http://www.lungau-academy.at/wxmax1001/

Hierbei steht ``-r`` für ein rekursives Herunterladen, ``-l1`` beschränkt die
Anzahl der durchsuchten Unterverzeichnisse auf 1. Die Option ``-np`` bzw.
``--no-parent`` ist wichtig, um zu verhindern, dass auch übergeordente
Verzeichnisse durchsucht werden -- dies könnte im Zweifelsfall die Downloadmenge
erheblich vergrößern. Die Option ``-A filetype`` legt anhand der angegebenen
Dateiendung(en) fest, welche Datentypen akzeptiert werden (im umgekehrten Fall
können mit ``-R filetype`` bestimmte Datentypen zurückgewiesen werden).

Ein gutes Tutorial (en.) findet sich `hier
<http://www.thegeekstuff.com/2009/09/the-ultimate-wget-download-guide-with-15-awesome-examples/>`_.

..  https://www.gnu.org/software/wget/manual/wget.html
..  http://www.delorie.com/gnu/docs/wget/wget.html

.. index:: which
.. _which:

``which``
---------

Mit ``which programm`` wird angezeigt, unter welchem Systempfad die
auszuführende Datei des angegebenen Programms zu finden ist. 


.. index:: xargs
.. _xargs:

``xargs``
---------

Mit ``xargs`` können die Ergebnisse eines Shell-Programms als Argumente eines
anderen Shell-Programms verwendet werden. Dies ist beispielsweise bei der
Kombination von :ref:`find <find>` und :ref:`grep <grep>` nützlich, um die von
``find`` gefundenen Dateinamen nicht unmittelbar als (Eingabe-)Text, sondern als
Zieldateien nach bestimmten Mustern zu durchsuchen.

Sollen beispielsweise alle ``.tex``-Dateien nach einem bestimmten Begriff
durchsucht werden, kann man folgendes eingeben:

.. code-block:: bash

    find ./ -name "*.tex" | xargs grep

Ohne die Verwendung von ``xargs`` würden hier nur die Namen der Dateien, jedoch
nicht deren Inhalt durchsucht.


.. index:: zip, unzip
.. _zip und unzip:

``zip``, ``unzip``
------------------

Mit ``zip`` können mehrere Dateien zu einem Datei-Archiv gebündelt, mit
``unzip`` wieder entpackt werden. Die grundlegenden Befehle sehen etwa so aus
(weitere Informationen erhält man mittels ``man zip`` bzw. ``man unzip``):

* Mit ``zip archivname.zip datei1 datei2 ...`` werden mehrere Dateien zu einem
  (komprimierten) ``zip``-Archiv gebündelt. Mit ``zip -r`` können Dateien
  und/oder Verzeichnisse rekursiv (samt Unterverzeichnissen) gepackt, mit ``zip
  -g`` zu einem bestehenden Archiv hinzugefügt werden.
* Mit ``unzip archivname`` wird ein ``zip``-Archiv wieder entpackt.

.. raw:: html

    <hr />
    
.. only:: html

    .. rubric:: Anmerkungen:

.. [#TARBZ] Mittels ``tar -cjvf archivname datei1 datei2`` können zwei oder mehrere
    Dateien direkt zu einem komprimierten ``tar``-Archiv zusammgefasst werden.

.. [#MCS] Beispielsweise bietet der Dateimanager :ref:`Midnight Commander <mc>`
    die Tastenkombination ``Ctrl x Ctrl s`` zur schnellen Erzeugung von Symlinks
    an. Mit dem Midnight Commander oder mittels ``cp -L`` kann man darüber
    hinaus beim Kopieren von Symlinks optional wieder auf die Originaldateien
    zurückgreifen und deren Inhalte kopieren. 
      
    Wird ein Symlink kopiert, so zeigt auch die Kopie auf den gleichen
    (absoluten) Pfad wie der ursprüngliche Symlink.

