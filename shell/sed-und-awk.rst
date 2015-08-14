
.. _Sed und Awk:

Sed und Awk
===========

Unter den vielen Werkzeugen, die in Shell-Skripten eingesetzt werden können,
befinden sich auch die zwei Programme ``sed`` und ``awk``, die sich auf sehr
vielseitige Art einsetzen lassen daher in diesem Abschnitt gesondert beschrieben
haben.

.. index:: sed
.. _Sed:

Sed
---

Sed steht für "Stream Editor", ist also ein Werkzeug zum Verarbeiten von
Datenströmen dar. Im Wesentlichen wird ``sed`` also verwendet, um mit
minimalistischer Syntax exakt auf die jeweilige Aufgabe zugeschnittene
Textmanipulationen vorzunehmen. Im folgenden werden einige Einsatzmöglichkeiten
der auf Debian, Ubuntu und Linux Mint üblichen Version von ``sed`` (GNU sed)
kurz vorgestellt.

.. figure:: sed.png
    :name: fig-sed
    :alt:  fig-sed
    :align: center
    :width: 15%

Die allgemeine Sed-Syntax lautet:

.. code-block:: bash

    sed [-optionen] Anweisungen [Dateien]

Die einzelnen ``sed``-Anweisungen sollten in einfach Anführungszeichen gesetzt
werden, um automatische Ersetzungen durch den Shell-Interpreter zu vermeiden.
Sollen mehrere Anweisungen ausgeführt werden, so müssen diese mittels einem
Strichpunkt (``;``) getrennt werden und ``sed`` mit der Option ``-e`` aufgerufen
werden.

Wird bei einem ``sed``-Aufruf kein Dateiname angegeben, so wird automatisch Text
von der Standard-Eingabe eingelesen. Auf diese Weise kann ``sed`` in Kombination
mit einer :ref:`Pipe <Pipelines>` verwendet werden, um die Ausgabe eines anderen
Programms zu bearbeiten:

.. code-block:: bash

    # Lesen von der Standard-Eingabe mittels Pipe:
    programmname | sed [-optionen] Anweisungen

Üblicherweise gibt ``sed`` seine Ergebnisse wiederum auf der Standard-Ausgabe
aus. Mit der Angabe von ``> dateiname`` als letztes übergebenes Argument oder
auch mittels einer weiteren Pipe und dem Programm :ref:`tee <tee>` kann die
Ausgabe jedoch auch in Textdateien umgelenkt werden:

.. code-block:: bash

    # Lesen von der Standard-Eingabe, Ausgabe in Textdatei:
    programmname | sed [-optionen] Anweisungen > dateiname

Ebenso können mittels ``>> dateiname`` als letztes Argument die Ergebnisse eines
``sed``-Aufrufs auch an das Ende einer (möglicherweise bereits existierenden)
Datei angehängt werden.


.. _Optionen von sed:

.. rubric:: Optionen von ``sed``

In der folgenden Tabelle sind die wichtigsten Optionen von ``sed`` aufgelistet:

.. list-table::
    :name: tab-sed-optionen
    :widths: 20 50

    * - Option
      - Bedeutung
    * - | ``-e anweisung1``
        | ``-e anweisung2 ...``
      - Mehrere Anweisungen nacheinander ausführen. Alternativ dazu kann eine
        einzelne Anweisung formuliert werden, die mehrere durch Strichpunkte
        getrennte Teilanweisungen umfasst.
    * - ``-f skriptdatei``
      - Anweisungen aus der angegebenen Skriptdatei anstelle von der
        Standard-Eingabe lesen
    * - ``-i``
      - Änderungen direkt in angegebene Dateien schreiben ("in-place-editing")
    * - ``-n``
      - Ergebnisse nur dann ausgeben, wenn dies mit der Anweisung ``p`` explizit
        verlangt wird.

Wird mittels ``-f`` eine Skriptdatei (übliche Endung: ``.sed``) angegeben, so
wird in dieser üblicherweise eine ``sed``-Anweisung je Zeile formuliert, eine
Trennung einzelner Anweisungen durch Strichpunkte kann in diesem Fall entfallen.
Zusätzlich können in eine derartige Skriptdatei Kommentare eingefügt werden,
die aus eigenen, mittels des Zeichens ``#`` eingeleiteten Zeilen bestehen.


.. _Anweisungen von sed:

.. rubric:: Anweisungen von ``sed``

Die wohl häufigste Anwendung von ``sed`` besteht darin, einzelne Wörter oder
reguläre Ausdrücke durch andere Begriffe zu ersetzen. Die entsprechende
``sed``-Anweisung heißt ``s`` ("substitute"). Ihre Syntax lautet etwa wie
folgt:

.. code-block:: bash

    sed 's/alt/neu/g'

Die obige Anweisung würde im gesamten an ``sed`` übergebenen Text nach dem
Begriff ``alt`` suchen und diesen durch ``neu`` ersetzen. Das Schlüsselzeichen
``g`` ("global") am Ende der Anweisung bewirkt, dass nicht nur das erste,
sondern alle Vorkommen von ``alt`` durch ``neu`` ersetzt werden sollen. [#]_

Sollen Ersetzungen in Textstellen vorgenommen werden, die selbst Schrägstriche
beinhalten (beispielsweise Pfadangaben), so kann anstelle von ``/`` auch ein
anderes Zeichen als Trennzeichen verwendet werden. Der gleiche Aufruf von Sed
sieht beispielsweise mit ``#`` als Trennzeichen so aus:

.. code-block:: bash

    sed 's#alt#neu#g'

Möchte man die Ersetzungen nur in einem bestimmten Bereich, beispielsweise
zwischen zwei Zeilennummern, vornehmen, so ist eine Bereichsangabe unmittelbar
zu Beginn der ``sed``-Anweisung möglich. Diese kann aus einer einzelnen Adresse
oder auch zwei Adressen, die einen Bereich markieren, bestehen:

.. code-block:: bash

    # In der Zeile 5 "alt" durch "neu" ersetzen:
    5s/alt/neu/g

    # In den Zeilen 10-30 "alt" durch "neu" ersetzen:
    10,30s/alt/neu/g

Bei einer Bereichsangabe kann auch eine der beiden Adressen weggelassen werden,
um eine Ersetzung vom Anfang des Textes bis zu einer beziehungsweise ab einer
gegebenen Stelle bis zum Ende des Textes zu erreichen:

.. code-block:: bash

    # Ab Zeile 10 "alt" durch "neu" ersetzen:
    10,s/alt/neu/g

    # Bis Zeile 30 "alt" durch "neu" ersetzen:
    ,30s/alt/neu/g

Bereichsangaben können durch ein angefügtes Ausrufezeichen (``!``) umgekehrt
werden. Die Anweisung bezieht sich dann auf alle Zeilen, die außerhalb der
Bereichsangabe liegen:

.. code-block:: bash

    # In allen Zeilen außer 10-30 "alt" durch "neu" ersetzen:
    10,30!s/alt/neu/g

Anstelle von Zeilenangaben können Adressen auch aus Suchmustern bestehen, die
ebenfalls zwischen zwei Schrägstrichen angegeben werden:

.. code-block:: bash

    # In allen Zeilen, die "total" enthalten, alt" durch "neu" ersetzen:
    /total/s/alt/neu/g

    # Zwischen "START" und "END" alle Vorkommnisse von alt" durch "neu" ersetzen:
    /START/,/END/s/alt/neu/g

Auch Bereichsangaben, die aus Suchmustern bestehen, können mittels einem
Ausrufezeichen negiert werden. Sowohl in den Bereichsangaben wie ich in den zu
ersetzenden Begriffen können zudem :ref:`reguläre Ausdrücke <Reguläre
Ausdrücke für Sed>` eingesetzt werden.

Weitere gebräuchliche Anweisungen von ``sed`` sind in der folgenden Tabelle
aufgelistet:

.. list-table::
    :name: tab-sed-anweisungen
    :widths: 10 70

    * - Anweisung
      - Bedeutung
    * - ``a``
      - An die angegebene(n) Stelle(n) den folgenden Text als neue Zeile anfügen
        ("append").

        Beispiel: ``/adresse/a text``
    * - ``c``
      - Die angegebene(n) Stelle(n) durch den folgenden Text als neue Zeile
        ersetzen ("change").

        Beispiel: ``/adresse/c text``
    * - ``i``
      - Vor den angegebene(n) Stelle(n) den folgenden Text als neue Zeile
        einfügen ("insert").

        Beispiel: ``/adresse/i text``
    * - ``d``
      - Die angegebene(n) Stelle(n) löschen ("delete")

        Beispiel: ``/adresse/d``
    * - ``p``
      - Gibt die angegebene(n) Stelle(n) aus ("print"); wird üblicherweise in
        Kombination mit der Option ``-n`` verwendet.
    * - ``q``
      - Sed innerhalb einer Skriptdatei beenden ("quit").
    * - ``r``
      - Vor den angegebene(n) Stelle(n) den Inhalt der folgenden Datei einfügen
        ("read").

        Beispiel: ``/adresse/r dateiname``
    * - ``y``
      - An den angegebene(n) Stelle(n) Zeichen aus einer Liste durch andere
        Zeichen ersetzen ("yank").

        Beispiel: ``/adresse/y/abc/ABC/``
    * - ``w``
      - Schreibt die angegebene(n) Stelle(n) in die folgende Datei ("write").

        Beispiel: ``/adresse/w dateiname``

Weitere Funktionen von ``sed`` sind in den Manpages beschrieben (``man sed``).


.. _Reguläre Ausdrücke für Sed:

.. rubric:: Reguläre Ausdrücke für Sed

In Bereichsangaben, Suchmustern und Ersetzungen können in ``sed`` so genannte
reguläre Ausdrücke eingesetzt werden. Dabei handelt es sich um Kombinationen von
normalen Buchstaben und Sonderzeichen, die eine besondere Bedeutung besitzen.
Die wichtigsten Sonderzeichen sind in der folgenden Tabelle aufgelistet.

.. only:: html

    .. list-table::
        :name: tab-sed-sonderzeichen
        :widths: 10 50

        * - Sonderzeichen
          - Bedeutung
        * - ``^``
          - Zeilenanfang
        * - ``$``
          - Zeilenende
        * - ``.``
          - ein beliebiges Zeichen (außer dem Newline-Zeichen ``\n``)
        * - ``[A-Z]``
          - ein Großbuchstabe
        * - ``[a-z]``
          - ein Kleinbuchstabe
        * - ``[0-9]``
          - eine Ziffer
        * - ``[abc123]``
          - ein Zeichen aus der angegebenen Menge an Buchstaben oder Ziffern
        * - ``[^abc123]``
          - ein beliebiges Zeichen außer der angegebenen Menge an Buchstaben oder
            Ziffern
        * - ``\( \)``
          - Gruppierung der zwischen den Klammern angegebenen Zeichen zu einem
            einzigen Ausdruck.

            Die Textstellen, auf welche die einzelnen Gruppierungen zutreffen,
            können bei Ersetzungen mittels ``\1``, ``\2``,
            ``\3`` usw. wieder eingesetzt werden.
        * - ``\{m,n\}``
          - mindestens  :math:`m` und höchstens :math:`n` Wiederholungen des
            vorhergehenden Zeichens oder der vorangehenden Gruppierung.

            Mit ``\{m\}`` kann die Anzahl auf genau :math:`m`, mit ``\{m,\}``
            auf mindestens :math:`m` festgelegt werden.
        * - ``*``
          - keine, eine oder beliebig viele Wiederholungen des vorhergehenden
            Zeichens oder der vorangehenden Gruppierung
        * - ``\< \>``
          - Wortanfang und Wortende
        * - ``&``
          - Bei Ersetzungen entspricht ``&`` der gesamten Textstelle, auf welche das
            angegebene Suchmuster zugetrifft.

.. raw:: latex

    \label{tab-sed-sonderzeichen}
    \vspace*{1cm}
    {\centering
    \begin{tabulary}{\linewidth}{|p{5cm}|p{10cm}|} \hline
    Sonderzeichen & Bedeutung \\ \hline
    \code{\textasciicircum{}} & Zeilenanfang \\ \hline
    \code{\$} & Zeilenende \\ \hline
    \code{.} & ein beliebiges Zeichen (außer dem Newline-Zeichen \code{\textbackslash{}n}) \\ \hline
    \code{{[}abc123{]}} & ein Zeichen aus der angegebenen Menge an Buchstaben oder Zahlen \\ \hline
    \code{{[}\textasciicircum{}abc123{]}} & ein beliebiges Zeichen außer der angegebenen Menge an Buchstaben oder Zahlen \\ \hline
    \code{\textbackslash{}( \textbackslash{})} & Gruppierung der zwischen den
    Klammern angegebenen Zeichen zu einem einzigen Ausdruck. Die Textstellen,
    auf welche die einzelnen Gruppierungen zutreffen, können bei Ersetzungen mittels \code{\textbackslash{}1},
    \code{\textbackslash{}2}, \code{\textbackslash{}3} usw. wieder eingesetzt werden. \\ \hline
    \code{\textbackslash{}\{m,n\textbackslash{}\}} & mindestens  \(m\) und höchstens \(n\) Wiederholungen des
    vorhergehenden Zeichens oder der vorangehenden Gruppierung. Mit
    \code{\textbackslash{}\{m\textbackslash{}\}} kann die Anzahl auf genau \(m\), mit
    \code{\textbackslash{}\{m,\}} auf mindestens \(m\) festgelegt werden. \\ \hline
    \code{*} & keine, eine oder beliebig viele Wiederholungen des vorhergehenden
    Zeichens oder der vorangehenden Gruppierung \\ \hline
    \code{\textbackslash{}\textless{} \textbackslash{}\textgreater{}} & Wortanfang und Wortende \\ \hline
    \code{\&} & Bei Ersetzungen entspricht \code{\&} der gesamten Textstelle, auf welche das angegebene Suchmuster zugetrifft. \\
    \hline
    \end{tabulary}
    }

In eckigen Klammern kann zur Definition einer Charakter-Klasse auch auch ein
anderer Bereich angegeben werden; beispielsweise bezeichnet ``[a-m]`` einen
Kleinbuchstaben zwischen ``a`` und ``m``. Soll ein Zeichen mit Sonderbedeutung,
beispielsweise ein Dollar-Zeichen oder ein Punkt Teil eines regulären Ausdrucks
sein, so muss davor ein Backslash-Zeichen gesetzt werden, um die Sonderbedeutung
des Zeichens aufzuheben.

..  \code{\$} & Zeilenende  \\
..  \code{.} & ein beliebiges Zeichen (außer dem Newline-Zeichen \code{\textbackslash{}n}) \\
..  \code{{[}abc123{]}} &  ein Zeichen aus der angegebenen Menge an Buchstaben oder Zahlen \\
..  * - ``[^abc123]``
..  - ein beliebiges Zeichen außer der angegebenen Menge an Buchstaben oder
..  Zahlen
..  * - ``\( \)``
..  - Gruppierung der zwischen den Klammern angegebenen Zeichen zu einem
..  einzigen Ausdruck.

..  Die Textstellen, auf welche die einzelnen Gruppierungen zutreffen,
..  können bei Ersetzungen mittels ``\1``, ``\2``,
..  ``\3`` usw. wieder eingesetzt werden.
..  * - ``\{m,n\}``
..  - mindestens  :math:`m` und höchstens :math:`n` Wiederholungen des
..  vorhergehenden Zeichens oder der vorangehenden Gruppierung.

..  Mit ``\{m\}`` kann die Anzahl auf :math:`m`, mit ``\{m,}`` auf
..  mindestens :math:`m` festgelegt werden.
..  * - ``*``
..  - keine, eine oder beliebig viele Wiederholungen des vorhergehenden
..  Zeichens oder der vorangehenden Gruppierung
..  * - ``\< \>``
..  - Wortanfang und Wortende
..  * - ``&``
..  - Bei Ersetzungen entspricht ``&`` der gesamten Textstelle, auf welche das
..  angegebene Suchmuster zugetrifft.


.. PatternSpace und Holdspace
.. Multiline

.. rubric:: Links

* `GNU Sed Reference <https://www.gnu.org/software/sed/manual/sed.html>`_
* `Sed-Einzeiler mit Kommentaren <http://sed.sourceforge.net/sed1line_de.html>`_
* `An Introduction and Tutorial to Sed <http://www.grymoire.com/Unix/Sed.html>`_

.. index:: awk
.. _Awk:

Awk
---

Awk wird bevorzugt verwendet, um tabularische Daten zeilenweise einzulesen und
dabei einzelne Zeilen, die bestimmte Muster enthalten, zu bearbeiten. Jedes
Awk-Skript, das oftmals nur wenige Zeilen umfasst, besteht also aus Mustern und
zugehörigen Aktionen.

Als Suchmuster werden, wie bei Sed, oftmals reguläre Ausdrücke genutzt. Die
Formulierung der zugehörigen Aktionen hat einige Ähnlichkeiten mit der
Programmiersprache :ref:`C <gwic:Grundkurs C>`. Awk nimmt dem Benutzer
allerdings viel Arbeit ab: Es liest den Eingabetext automatisch zeilenweise ein
und zerlegt jede Zeile anhand eines frei wählbaren Trennzeichens in einzelne
Felder (Spalten).

.. _Einfache Awk-Skripte:

.. rubric:: Einfache Awk-Skripte

Einfache Awk-Skripte sind oftmals folgendermaßen aufgebaut:

.. code-block:: bash

    awk [optionen] '/muster/ {print ...}' dateiname

Das angegebene Muster kann eine einfache Zeichenkette, aber auch ein regulärer
Ausdruck oder eine Bedingung sein. Im obigen Fall würde damit die angegebene
Datei zeilenweise eingelesen und einzelne Teile jeder auf das Muster
zutreffenden Zeile ausgegeben.

Die einzelnen Felder einer Zeile werden von Awk mit ``$1`` bis ``$9``
durchnummeriert, ``$0`` steht für den gesamten Inhalt einer Zeile. Möchte man
beispielsweise von allen Zeilen einer Datei nur die ersten drei Spalte ausgeben,
so kann das Muster auch weggelassen werden:

.. code-block:: bash

    # Awk-Print-Anweisung auf alle Zeilen einer Datei anwenden:
    awk '{print $1 $2 $3}' dateiname

Ebenso kann Awk mittels einer :ref:`Pipe <Pipelines>` Ausgabedaten eines anderen
Programms als Eingabe verwenden. In diesem Fall kann der Dateiname weggelassen
werden:

.. code-block:: bash

   # Daten vom Bildschirm anstelle von einer Datei einlesen:
   other_programm | awk '/muster/ {anweisungen}'

Üblicherweise werden von ``awk`` so genannte "Whitespace"-Zeichen, also
Leerzeichen und Tabulator-Zeichen (``\t``), als Trennzeichen zwischen den
einzelnen Feldern einer Zeile interpretiert. Möchte man beispielsweise bei der
Verarbeitung einer ``.csv``-Datei ("Comma Seperated Values") das Zeichen ``,``
oder ``;`` als Trennzeichen verwenden, so kann dies mittels der Option ``-F``
("Field Seperator") angegeben werden:

.. code-block:: bash

    # Das Zeichen ";" als Feldtrennzeichen verwenden:
    awk -F ";" '/muster/ {anweisungen}' dateiname

In einem Awk-Skript können auch mehrere Muster-Anweisungs-Paare in folgender
Form angegeben werden:

.. code-block:: bash

    # Mehrere Muster-Anweisungspaare angeben:
    awk [optionen] '/muster1/ {anweisung1} /muster2/ {anweisung2} ...' dateiname

In einer Shellskript-Datei können die einzelnen Anweisungen zur besseren
Lesbarkeit auch untereinander geschrieben werden:

.. code-block:: bash

    # Mehrere Muster-Anweisungspaare, andere Form:
    awk [optionen] '/muster1/ {anweisung1}
                    /muster2/ {anweisung2}
                    ... ' dateiname

In diesem Fall wird bei jeder eingelesenen Zeile zunächst das erste Muster
geprüft und gegebenenfalls der zugehörige Anweisungsblock ausgeführt. Wenn das
erste Muster nicht zutrifft, wird geprüft, ob das zweite Muster zutrifft, usw.
Sobald ein Muster zutrifft, werden also die entsprechenden Anweisungen
ausgeführt, und Awk fährt mit dem Einlesen der nächsten Zeile fort. Die
einzelnen Muster-Anweisungs-Paare werden somit als einander ausschließende
Entweder-Oder-Abfragen interpretiert. Das vorrangige Suchmuster muss also an
erster Stelle stehen, da es sonst gegebenenfalls nicht ausgeführt wird.

Soll ein Anweisungsblock ausgeführt werden, wenn wahlweise das eine und/oder ein
anderes Muster auftritt, so können diese in folgender Form angeben werden:

.. code-block:: bash

    # Ausführung, wenn muster1 oder muster2 oder beide zutreffen:
    awk [optionen] '/muster1/ || /muster2/ {anweisungen}' dateiname

Das Zeichen ``||`` entspricht somit, ebenso wie in der Programmiersprache C,
einem logischen ``ODER``. Soll ein Anweisungsblock hingegen nur dann ausgeführt
werden, wenn sowohl das eine als auch das andere Muster auftritt, so kann
folgende Syntax verwendet werden:

.. code-block:: bash

    # Ausführung nur, wenn sowohl muster1 und muster2 zutreffen:
    awk [optionen] '/muster1/ && /muster2/ {anweisungen}' dateiname

Das Zeichen ``&&`` entspricht, ebenso wie in C, einem logischen ``UND``. Mittels
``||`` beziehungsweise ``&&`` können auch mehr als zwei (Teil-)Muster kombiniert
werden; bei Bedarf können runde Klammern gesetzt werden, um die gewünschte
Kombination der Ausdrücke zu erreichen (siehe :ref:`Aussagenlogik
<gwm:Verknüpfungen von Aussagen>`).

.. rubric:: BEGIN- und END-Anweisungen

In Awk kann man je einen Anweisungsblock einmalig zu Beginn beziehungsweise
einmalig am Ende eines Skripts ausführen. ``BEGIN``-Anweisungen können
beispielsweise dazu genutzt werden, um Header-Zeilen in eine Ausgabe-Datei zu
schreiben, bevor die eigentlichen Daten verarbeitet werden.

.. code-block:: bash

   awk 'BEGIN {anweisungen} /muster/ {anweisungen}' dateiname

Entsprechend können mittels einer ``END``-Anweisung zusätzliche Informationen
am Ende der Datenverarbeitung ausgegeben werden:

.. code-block:: bash

   awk '/muster/ {anweisungen} END {anweisungen}' dateiname

``END``-Anweisungen sind insbesondere praktisch, wenn mehrere Werte summiert
werden und das Ergebnis am Ende ausgegeben werden soll. Dies ist, wie im
nächsten Abschnitt beschrieben, durch die Verwendung von Variablen möglich.


.. _Variablen und arithmetische Operationen:

.. rubric:: Variablen und arithmetische Operationen

In Awk lassen sich auf sehr einfache Weise einzelne Werte in Variablen
speichern. Dazu wird folgende Syntax verwendet::

    varname=wert

Die Definition einer Variablen kann an jeder beliebigen Stelle innerhalb eines
Awk-Skripts erfolgen. Mittels ``print varname`` kann der gespeicherte Wert
wieder ausgegeben werden. Die Variablen ``$0`` für den Inhalt der aktuellen
Zeile sowie die Variablen ``$1`` bis ``$9`` für die einzelnen Felder der
aktuellen Zeile sind bereits vordefiniert.

In Awk werden alle Variablen als Zeichenketten interpretiert. Dennoch können
einfache arithmetische Operationen auf Variablen angewendet werden;
beispielsweise kann mit ``awk '{prod=$1*$2 ; print $1 $2 prod}'`` eine
zweispaltige Datentabelle um eine dritte Spalte ergänzt werden, deren Werte in
jeder Zeile dem Produkt der ersten beiden Spalten entspricht. [#]_

Einer Variablen kann nicht nur mittels des üblichen Zuweisungsoperators ``=``,
sondern auch beispielsweise mittels ``+=`` ein Wert zugewiesen werden. Hierbei
wird der bisherige Wert der Variablen um den auf der rechten Seite stehenden
Ausdruck erhöht. Da jede neu definierte Variable in Awk zunächst den Wert Null
hat, können auf diese Weise beispielsweise alle in einer Spalte stehenden
Zahlenwerte aufaddiert werden. Das Ergebnis kann dann mittels eines
``END``-Blocks ausgegeben werden:

.. code-block:: bash

    # Dateigrößen des aktuellen Verzeichnisses ausgeben:
    # (Die 5. Spalte von `ls -l` gibt die Dateigröße an)
    ls -l | awk '{print $5}'

    # Alle Werte zur Gesamtgröße aufsummieren:
    ls -l | awk '{sum += $5} END {print "Gesamt:\t" sum}'

.. _Reguläre Ausdrücke für Awk:

.. rubric:: Reguläre Ausdrücke für Awk

In den angegebenen Mustern können auch in Awk reguläre Ausdrücke eingesetzt
werden; damit sind Kombinationen von normalen Buchstaben und Sonderzeichen
gemeint, wobei letztere die eine besondere Bedeutung besitzen. Die wichtigsten
Sonderzeichen sind in der folgenden Tabelle aufgelistet.

.. list-table::
    :name: tab-awk-sonderzeichen
    :widths: 10 50

    * - Sonderzeichen
      - Bedeutung
    * - ``^``
      - Zeilenanfang
    * - ``$``
      - Zeilenende
    * - ``.``
      - ein beliebiges Zeichen
    * - ``[A-Z]``
      - ein Großbuchstabe
    * - ``[a-z]``
      - ein Kleinbuchstabe
    * - ``[0-9]``
      - eine Ziffer
    * - ``[abc123]``
      - ein Zeichen aus der angegebenen Menge an Buchstaben oder Ziffern.
    * - ``[^abc123]``
      - ein beliebiges Zeichen außer der angegebenen Menge an Buchstaben oder
        Ziffern
    * - ``( )``
      - Gruppierung der zwischen den Klammern angegebenen Zeichen zu einem
        einzigen Ausdruck.
    * - ``|``
      - entweder der vor unmittelbar vor oder unmittelbar nach ``|`` stehende
        Audruck (oder die entsprechende Gruppierung)
    * - ``+``
      - eine oder beliebig viele Wiederholungen des vorhergehenden
        Zeichens oder der vorangehenden Gruppierung
    * - ``*``
      - keine, eine oder beliebig viele Wiederholungen des vorhergehenden
        Zeichens oder der vorangehenden Gruppierung
    * - ``?``
      - kein oder genau ein Vorkommen des vorhergehenden Zeichens oder der
        vorangehenden Gruppierung
    * - ``{m,n}``
      - mindestens :math:`m` und höchstens :math:`n` Wiederholungen des
        vorhergehenden Zeichens oder der vorangehenden Gruppierung.
        Mit ``{m}`` kann die Anzahl auf genau :math:`m`, mit ``{m,}`` auf
        mindestens :math:`m` festgelegt werden.


Im Gegensatz zu den :ref:`regulären Ausdrücken für Sed <Reguläre Ausdrücke für
Sed>` haben runde und geschweifte Klammern standardmäßig die oben angegebene
Sonderbedeutung; soll das jeweilige Zeichen an sich Teil eines regulären
Ausdrucks sein, so muss davor ein Backslash-Zeichen gesetzt werden.

.. rubric:: Bedingungen als Muster

Nicht nur reguläre Ausdrücke, sondern auch Bedingungen können als Muster zur
Auswahl der zu bearbeitenden Zeilen genutzt werden. Sollen beispielsweise alle
Zeilen einer Tabelle ausgegeben werden, deren Wert in der dritten Spalte
:math:`\ge 50` ist, so könnte man folgendes schreiben:

.. code-block:: bash

    # Print-Anweisung unter einer bestimmten Bedingung ausführen:
    awk '$3 >= 50 {print $0}' dateiname

Für Werte-Vergleiche können folgende Operatoren genutzt werden:

.. list-table::
    :name: tab-vergleichssoperatoren
    :widths: 20 50

    * - Operator
      - Beschreibung
    * - ``==``
      - Test auf Wertgleichheit
    * - ``!=``
      - Test auf Ungleichheit
    * - ``<``
      - Test, ob kleiner
    * - ``<=``
      - Test, ob kleiner oder gleich
    * - ``=>``
      - Test, ob größer oder gleich
    * - ``>``
      - Test, ob größer

Auch bei Werte-Vergleichen können mehrere Bedingungen mittels ``&&`` als
``UND``-Verknüpfung beziehungsweise ``||`` als ``ODER``-Verknüpfung zu einer
Gesamt-Bedingung kombiniert werden; ebenso sind Kombinationen von
Werte-Vergleichen und normalen Suchmustern oder regulären Ausdrücken möglich.
Zur Gruppierung einzelner Teilbedingungen können wiederum runde Klammern gesetzt
werden.

Der Istgleich-Operator ``==`` kann zudem verwendet werden, um eine Spalte mit
einer Zeichenkette zu vergleichen, beispielsweise ``$1 == "Hallo"``.

.. Bedingungen mittels ``if (condition)``, um auch Werte von Variablen prüfen
.. zu können.

.. xpdf:
.. Warning: Cannot convert string
.. "-*-courier-medium-r-normal--12-*-*-*-*-*-iso8859-1" to type FontStruct
..

.. ls -l | awk '/4,0K/ || /Mai/ {printf("%-20s\t %10i\n", $9, $5)}'

.. Formattierte Ausgabe     Dougherty 214

.. Ein weiterer Vorteil von Awk ist, dass auf einfache Weise
.. Variablen angelegt werden können. Mit diesen können dann beispielsweise einfache
.. arithmetische Operationen ausgeführt und die Ergebnisse ausgegeben werden.

.. Im folgenden werden einige Einsatzmöglichkeiten der auf
.. Debian, Ubuntu und Linux Mint üblichen Version von ``awk`` (GNU awk) kurz
.. vorgestellt.


..  Die allgemeine Awk-Syntax lautet:

..  .. code-block:: bash

    ..  awk [-optionen] Anweisungen [Datei]

..  Die einzelnen ``awk``-Anweisungen sollten in einfach Anführungszeichen gesetzt
..  werden, um automatische Ersetzungen durch den Shell-Interpreter zu vermeiden.
..  Sollen mehrere Anweisungen ausgeführt werden, so müssen diese in geschweifte
..  Klammern gesetzt und einem Strichpunkt (``;``) getrennt werden. Diese Variante
..  wird für kurze Awk-Skripte verwendet, die nur eine oder zwei Zeilen Code
..  umfassen. Längere Awk-Skripte werden üblicherweise in Dateien mit der Endung
..  ``.awk`` geschrieben und mittels der Option ``-f`` ohne weitere Anweisungen
..  aufgerufen.

..  Wird bei einem ``awk``-Aufruf kein Dateiname angegeben, so wird automatisch Text
..  von der Standard-Eingabe eingelesen. Auf diese Weise kann ``awk`` in Kombination
..  mit einer :ref:`Pipe <Pipelines>` verwendet werden, um die Ausgabe eines anderen
..  Programms zu bearbeiten:

..  .. code-block:: bash

    ..  # Lesen von der Standard-Eingabe mittels Pipe:
    ..  programmname | awk [-optionen] Anweisungen

..  Üblicherweise gibt ``awk`` seine Ergebnisse wiederum auf der Standard-Ausgabe
..  aus. Mit der Angabe von ``> dateiname`` als letztes übergebenes Argument oder
..  auch mittels einer weiteren Pipe und dem Programm :ref:`tee <tee>` kann die
..  Ausgabe jedoch auch in Textdateien umgelenkt werden:

..  .. code-block:: bash

    ..  # Lesen von der Standard-Eingabe, Ausgabe in Textdatei:
    ..  programmname | awk [-optionen] Anweisungen > dateiname


..  .. _Optionen von awk:

..  .. rubric:: Optionen von ``awk``

..  In der folgenden Tabelle sind die wichtigsten Optionen von ``awk`` aufgelistet:

..  .. list-table::
    ..  :name: tab-sed-optionen
    ..  :widths: 20 50

    ..  * - Option
      ..  - Bedeutung
    ..  * - ``-f skriptdatei``
      ..  - Anweisungen aus der angegebenen Skriptdatei anstelle von der
        ..  Standard-Eingabe lesen
    ..  * - ``-F symbol``
      ..  - Das angegebene Symbol als Feldtrenn-Zeichen verwenden
        ..  (Standard: Leerzeichen)
    ..  * - ``-v varname=wert``
      ..  - Eine Variable mit einem bestimmten Wert definieren

..  Zusätzlich kann mittels der Option ``-p dateiname.awk`` eine anschließend
..  angegebene ``.awk``-Skriptdatei in einer ordentlich formatierten Form als
..  ``dateiname.awk`` ausgegeben werden.

..  In Skriptdateien können zusätzlich Kommentare eingefügt werden, die aus eigenen,
..  mittels des Zeichens ``#`` eingeleiteten Zeilen bestehen und die Lesbarkeit des
..  Skripts verbessern.


..  .. _Vordefinierte Variablen:

..  .. rubric:: Vordefinierte Variablen

..  Awk verfügt als Skriptsprache über einige automatisch definierte Variablen; die
..  wichtigsten sind in der folgenden Tabelle aufgelistet.

..  .. list-table::
    ..  :name: tab-awk-variablen
    ..  :widths: 20 50

    ..  * - Variablenname
      ..  - Beschreibung
    ..  * - ``ARGC``
      ..  - Anzahl der Befehlszeilenparameter
    ..  * - ``ARGV``
      ..  - Array der Befehlszeilenparameter. Die Indizes laufen von 0 bis ARGC-1.
        ..  Durch ändern von ARGV kann man vom Script aus weitere Dateien öffnen.
    ..  * - ``CONVFMT``
      ..  - Das voreingestellte Format für Zahlen. Standardwert ist "%.6g".
    ..  * - ``ENVIRON``
      ..  - Stellt die Umgebungsvariablen als assoziatives Array zur Verfügung. Z.B.
        ..  liefert ENVIRON["HOME"] unser Homerverzeichnis.
    ..  * - ``ERRNO``
      ..  - Text zum letzten aufgetretenen Fehler bei einer Dateioperation
    ..  * - ``FIELDWIDTHS``
      ..  - Wenn man diese Variable mit einer durch Leerzeichen getrennten Liste von
        ..  Zahlen füllt, so werden die Felder nicht durch die in FS angegebenen
        ..  Trennzeichen, sondern an den entsprechenden festen Positionen getrennt.
        ..  Ich verwende das oft, um vom Host per FTP übertragene Dateien in Felder
        ..  zu zerlegen und weiterzuverarbeiten.
    ..  * - ``FNR``
      ..  - Die Nummer des aktuellen Eingabesatzes. Ein awk '{print FNR, $0}'
        ..  liefert ein Listing mit Zeilennummern.
    ..  * - ``IGNORECASE``
      ..  - Hat diese Variable einen von Null verschiedenen Wert, so werden alle
        ..  Stringvergleiche, das Trennen der Eingabe mit FS bzw. RS und die
        ..  Auswertung regulärer Ausdrücke unabhängig von Groß- bzw. Kleinschreibung
        ..  vorgenommen.
    ..  * - ``NF``
      ..  - Liefert die Anzahl Felder im aktuellen Eingabesatz.
    ..  * - ``OFMT``
      ..  - Das Standard-Ausgabeformat für Zahlen. Voreingestellt ist "%.6g"
    ..  * - ``OFS``
      ..  - Das Feldtrennzeichen für die Ausgabe. Voreingestellt ist ein
        ..  Leerzeichen.
    ..  * - ``ORS``
      ..  - Das Satztrennzeichen für die Ausgabe. Voreingestellt ist LF. Braucht man
        ..  Zeilenenden im DOS-Format (CR+LF), kann man das (unter anderem) mit dem
        ..  awk erledigen: awk -v 'ORS=\r\n' '{print $0}'

..  * - Sonderzeichen
..    - Bedeutung



..  Kennt (nur) 2 Datentypen (und Arrays davon):

..  * Gleitkommazahl: double, emuliert Integer (maximal 16 Stellen).
..  * Zeichenkette: dynamisch, beliebig lang.

..  Bietet mehrdimensionale, dynamische, assoziative Arrays
.. Die Verarbeitung von Zeichenketten ist einfach + sicher (keine
.. Speicherplatzreservierung oder -freigabe notwendig).

..  * AWKPATH legt Suchpfad fest (analog ``PATH``, d.h. eine Liste von durch ``:``
  ..  getrennten Verzeichnissen), in denen nach den per Option ``-f`` angegebenen
  ..  Awk-Dateien gesucht wird wenn sie nicht im aktuellen Verzeichnis gefunden
  ..  werden.

..  Zeichenkonstanten wie in C ('x') sind nicht verfügbar, sie sind allerdings durch
..  einbuchstabige Zeichenketten ("x") ersetzbar.

.. rubric:: Links

* `Awk Tutorial (PDF) <https://www.ostc.de/awk.pdf>`_
* `Einführung in Awk 1 <http://www.linux-schule.com/trans_html/007Awk/index.html>`_
* `Einführung in Awk 2 (PDF) <https://www.bg.bib.de/portale/bes/Scripting/AWK/awk.pdf>`_
* `Awk Wikibook <https://de.wikibooks.org/wiki/Awk>`_


..  https://www-user.tu-chemnitz.de/~hot/unix_linux_werkzeugkasten/awk.html
..  http://www.64-bit.de/dokumentationen/progr-software/a/005/awk.html

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Anstelle von ``g`` kann auch eine beliebige Zahl ``n`` angegeben werden,
    um nur das :math:`n`-te Vorkommen des angegebenen Begriffs zu ersetzen.

    Neben dem Schlüsselzeichen ``g`` gibt es nur noch ein weiteres
    Schlüsselzeichen für die Substitutions-Anweisung, und zwar ``p``. Dieses
    wird nur in Verbindung mit der Option ``-n`` verwendet, die eine Ausgabe der
    ``sed``-Ergebnisse grundsätzlich unterdrückt. Das Schlüsselzeichen ``p``
    ("print") am Ende einer ``sed``-Anweisung bewirkt, dass das Ergebnis dieser
    Anweisung dennoch ausgegeben wird.

.. [#] Möchte man die einzelnen Spalten bei der Ausgabe durch Tabulator-Zeichen
    ``"\t"`` getrennt haben, so ist dies mittels ``awk '{prod=$1*$2 ; print $1
    "\t" $2 "\t" prod}'`` möglich.

