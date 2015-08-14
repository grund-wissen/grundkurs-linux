
.. index:: make, Makefile
.. _Makefiles:

Makefiles
=========

Mit dem Programm ``make`` lassen sich Übersetzungs-Routinen einfach
organisieren. Hierzu wird im Ordner des zu übersetzenden Quellcodes eine Datei
namens ``Makefile`` angelegt. Darin werden Anweisungen nach folgender Regel
festgelegt:

.. code-block:: bash

    Ziel : Abhängigkeiten
        Anweisung(en) zur Generierung

* Die erste Zeile gibt jeweils an, welche (Ziel-)Dateien von welchen
  (Quell-)Dateien abhängen.
* Nach jeder so festgelegten Abhängigkeitsregel wird in einer oder mehreren
  Zeilen festgelegt, auf welche Weise die Quelldateien zu übersetzen sind. In
  jeder Zeile wird üblicherweise eine Anweisung angegeben, mehrere Anweisungen
  in einer Zeile müssen gegebenenfalls mit einem Strichpunkt getrennt werden.
  [#]_ Die Anweisungsliste wird durch eine Leerzeile beendet.

Eine Makedatei enthält üblicherweise mehrere Ziele und zugehörige
Übersetzungsregeln.

Der Einsatzbereich von ``make`` ist wegen dem allgemein gehaltenen Aufbau sehr
weitreichend; so findet ``make`` beispielsweise Einsatz beim Compilieren von
eigenem Quellcode, bei Installationsroutinen oder sogar beim Übersetzen von
RestructuredText-Dateien in PDF- oder Html-Dateien mittels :ref:`Sphinx
<Sphinx-Tool>`.

*Beispiel:*

* Eine Makefile zum Übersetzen eines C-Programms namens ``hallo-welt.c`` in ein
  ausführbares Programm ``hallo-welt`` sieht im einfachsten Fall folgendermaßen
  aus:

  .. code-block:: sh

      # Makefile-Beispiel 1:

      hallo: hallo-welt.c
          gcc -o hallo hallo-welt.c

  Speichert man das obige Beispiel als ``Makefile`` im gleichen Ordner, in dem
  sich auch ``hallo-welt.c`` befindet, so kann diese aus dem gleichen Ordner
  heraus in einer Shell mittels ``make hallo`` compiliert werden. [#]_

Mittels des Hash-Zeichens ``#`` können Makefiles an beliebigen Stellen mit
Kommentaren versehen werden, die jeweils bis zum Zeilenende reichen.

Makefiles werden vor allem dann eingesetzt, wenn mehrere Abhängigkeiten
existieren oder wenn mehrere Anweisungen zum Übersetzen notwendig sind: Diese
müssen bei Verwendung einer Makefile nur einmal eingegeben werden, was den
Schreibaufwand meist erheblich reduziert.

Ein weiterer Vorteil von ``make`` liegt darin, dass nur die Dateien übersetzt
werden, die seit dem letzten Übersetzen verändert wurden. Dabei liest ``make``
nicht den Inhalt der Datei aus, sondern orientiert sich am Änderungsdatum. Dies
spart Zeit und bewirkt, dass keine Datei unnötigerweise übersetzt wird. Falls
sich jedoch, beispielsweise in einer C-Quellcode-Datei, Abhängigkeiten von
anderen Dateien ergeben können, so muss diese C-Datei ebenfalls erneut
gespeichert werden, damit die Änderungen wirksam werden.


.. _Make-Makros:

.. rubric:: Makros

Innerhalb eines Makefiles können so genannte Makros definiert werden, die dazu
dienen, eine beliebig lange Zeichenkette durch einen Makro-Namen als
Kurzbezeichnung zu ersetzen. Üblicherweise werden die Makro-Namen dabei zur
besseren Lesbarkeit in Großbuchstaben geschrieben.

Ein Makro kann anschließend an beliebiger Stelle wieder durch den gespeicherten
Text ersetzt werden, indem man den Makro-Namen in runde Klammern setzt und das
Dollar-Zeichen ``$`` davor schreibt. So lässt sich das obige Makefile-Beispiel
auch folgendermaßen schreiben:

.. code-block:: bash

    # Makefile-Beispiel 2:

    DEST = hallo
    SOURCE = hallo-welt.c
    CC = gcc
    CFLAGS = -o

    $(DEST): $(SOURCE)
        $(CC) $(CFLAGS) $(DEST) $(SOURCE)

Die Verwendung von Makros kann einerseits die Lesbarkeit eines Makefiles
erhöhen, andererseits auch die Portierbarkeit auf andere Systeme erleichtern,
indem beispielsweise nur der Name des Compilers bei der Makro-Definition
ausgetauscht werden muss, aber nicht bei jedem einzelnen Ziel-Anweisungs-Block.


.. _Standard-Makros:

.. rubric:: Standard-Makros, Suffix- und Muster-Regeln

Neben eigenen Makros können in Makefiles die vier folgenden vordefinierten Makros verwendet
werden:

.. list-table::
    :name: tab-make-standard-makros
    :widths: 15 50

    * - Makro
      - Bedeutung
    * - $@
      - Der Name des Ziels
    * - $?
      - Alle angegebenen Quelldateien, die jünger als das Ziel sind
    * - $<
      - Der Name der Quelldatei, welcher die Anweisung ausgelöst hat
    * - $*
      - Analog, aber ohne Dateiendung

* Die beiden Makros ``$@`` und ``$?`` können immer dann eingesetzt werden, wenn
  wie in den obigen beiden Beispielen ein Ziel explizit angegeben wird.

* Die beiden Makros ``$<`` und ``$*`` hingegen werden ausschließlich für so
  genannte Suffix- oder Muster-Regeln verwendet.

Eine Suffix-Regel kann wiederum immer dann definiert werden, wenn ein bestimmter
Dateityp von einem anderen Dateityp abhängt; beispielsweise hängen
C-Objekt-Dateien mit der Endung ``.o`` stets von gleichnamigen C-Quelldateien
mit der Endung ``.c`` ab. Eine Suffix-Regel gibt dann allgemein an, wie man aus
einer beliebigen Ausgangsdatei die entsprechende Zieldatei erzeugt.
Beispielsweise kann eine einfache Suffix-Regel zur Erzeugung von ``.o``-Dateien
aus ``.c``-Dateien mittels des ``gcc``-Compilers folgendermaßen aussehen:

.. code-block:: bash

    .c.o:
        gcc $<

Möchte man beispielsweise eine Datei ``hallo-welt.c`` compilieren, so ist dies
bei Verwendung der obigen Makefile mittels ``make hallo-welt.o`` möglich. Bei
diesem Aufruf wird automatisch nach der zur Objekt-Datei ``.o`` passenden
Quelldatei ``.c`` gesucht, anschließend wird der Compiler mit dem Namen dieser
Datei aufgerufen.

Anstelle von Suffix-Regeln können (meist leichter lesbar!) auch Muster-Regeln
mittels des ``%``-Zeichens definiert werden. Das ``%``-Zeichen steht dabei für
eine beliebige Zeichenkette. Eine zur obigen Suffix-Regel äquivalente
Muster-Regel lautet damit:

.. code-block:: bash

    %.o: %.c
        gcc $<

.. Erweiterte Abhängigkeiten möglich!

Mittels solcher Regeln lässt sich das Übersetzen von Dateien erheblich
vereinfachen, wenn beispielsweise alle Dateien in einem Ordner mit den gleichen
Optionen compiliert werden sollen; so muss nicht für jedes Ziel eine extra
Regel definiert werden.


.. _Standard-Ziele:

.. rubric:: Standard-Ziele

In einer Makefile muss nicht jedes Ziel einer Datei entsprechen. Es gibt auch so
genannte Standard-Ziele, bei denen bestimmte Aktionen ausgeführt werden sollen,
die sich aus dem Namen des Ziels ergeben. Einige solcher Ziele, die häufig in
Makefiles auftreten, sind folgende:

.. list-table::
    :name: tab-make-standard-ziele
    :widths: 20 50

    * - Ziel
      - Bedeutung
    * - ``all``
      - Ziel zum Erzeugen aller anderen Regeln
    * - ``clean``
      - Löschen aller Zwischen- und Zieldateien
    * - ``new``
      - Neuerstellen aller Zieldateien (entspricht ``clean`` plus ``all``)
    * - ``usage``
      - Bedienungs-Text ausgeben

Das Ziel ``all`` wird zudem standardmäßig von ``make`` verwendet, wenn kein
anderes Ziel angegeben wird. Somit kann jederzeit anstelle von ``make all`` auch
nur ``make`` eingegeben werden.

..  * - ``depend``
..  - Generieren und Eintragen der Abhängigkeiten der C-Quellcodedateien von den Headerdateien im Makefile
..  * - ``install``
..  - Installation der erzeugten Programme und Dateien
..  * - ``uninstall``
..  - Deinstallation der erzeugten Programme und Dateien
..  * - ``backup``
..  - Sichern der seit der letzten Sicherung geänderten Quelldateien
..  * - ``save``
..  - Sichern aller Quelldateien
..  * - ``dist``
..  - Ein Quelltextpaket erzeugen (Distribution)
..  * - ``test``
..  - Testen aller Zieldateien



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Mehrere Anweisungen werden beispielsweise dann in einzelne Zeile
    geschrieben, wenn ein Pfadwechsel mittels :ref:`cd <cd>` stattfindet; dieser
    bezieht sich nur auf die jeweilige Zeile, bei der nächsten Zeile entspricht
    der Pfad wieder dem Verzeichnis der Makefile.

    Zu lange Zeilen (Faustregel: Über 80 Zeichen) können, wenn sie mit dem
    Backslash-Zeichen ``\`` abgeschlossen werden, in der nächsten Zeile
    fortgeführt werden. Dabei sollten die Original-Zeile und die
    Fortsetzungs-Zeile gleich weit eingerückt werden.

.. [#] Wird der Inhalt einer Makefile unter einem anderen Dateinamen
    gespeichert, so muss ``make`` mit der Option ``-f dateiname`` aufgerufen
    werden.
