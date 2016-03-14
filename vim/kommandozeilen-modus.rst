.. _Kommandozeilen-Modus:

Kommandozeilen-Modus
====================

Im Kommandozeilen-Modus können sowohl Vim-Anweisungen als auch :ref:`externe
Systemanweisungen <Aufrufe von externen Programmen>` aufgerufen werden.

Ausgehend vom Normalmodus gelangt man mittels ``:`` in den Kommandozeilen-Modus,
mittels ``Esc`` wieder zurück.

.. % bedeutet: Aktuelle Datei
.. %:p bedeutet: Aktuelle Datei als ganzer Pfad
.. %:p:h bedeutet: Head dieses Pfads (Pfad ohne Dateiname)
.. mehrere Angaben von :h sind möglich!

.. _Buffer einlesen:

Buffer einlesen
---------------

Eine neue Datei kann mit ``:edit`` (oder kurz ``:e``) als neuer Buffer geöffnet
werden, wobei die bisherige Datei als eigener Buffer im Hintergrund geladen
bleibt.

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:e dateiname``
      - eine Datei  öffnen bzw. neu erstellen
    * - ``:e %``
      - die aktuelle Datei (``%``) neu laden

Das Zeichen ``%`` hat im Kommandozeilen-Modus eine eigene Bedeutung: Es steht
für den Namen der aktuell geöffneten Datei. Die Ausgabe von ``%`` lässt sich
unter anderem folgendermaßen ändern:

.. list-table::
    :name: tab-filename
    :widths: 10 50

    * - ``%``
      - Aktueller Dateiname
    * - ``%:~``
      - Aktueller Dateiname (relativ zum Home-Verzeichnis)
    * - ``%:p``
      - Aktueller Dateiname (absoluter Pfad)
    * - ``%:p:h``
      - Aktuelles Verzeichnis ("Head" des absoluten Pfads)
    * - ``%:p:h:h``
      - Übergeordnetes Verzeichnis ("Head" des aktuellen Verzeichnisses)
    * - ``%:p:r``
      - Aktueller Dateiname ohne Endung (absoluter Pfad)
    * - ``%:e``
      - Endung der aktuellen Datei

Eine vollständige Beschreibung kann mittels ``:h filename-modifiers``
aufgerufen werden.

Der Inhalt einer anderen Datei kann mittels ``:read`` (oder kurz ``:r``) hinter
der momentanen Cursor-Position eingefügt werden:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:r dateiname``
      - Inhalt einer Datei vor dem Cursor einfügen


.. _Buffer wechseln:

Buffer wechseln
---------------

Um Vim zu beenden oder einzelne Dateien bzw. Fenster zu schließen, gibt man
folgendes ein:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:q``
      - Schließe den aktuellen Buffer schließen (und beende Vim, falls nur ein
        Fenster offen ist)
    * - ``:qa``
      - Schließe alle Buffer, beende Vim
    * - ``:q!``
      - Schließe den aktuellen Buffer, verwerfe ungespeicherte Änderungen
    * - ``:w``
      - Speichere Änderungen an der aktuellen Datei
    * - ``:wq``
      - Speichere die aktuelle Datei und schließe den Buffer
    * - ``:wqa``
      - Speichere alle geöffneten Dateien und beende Vim
    * - ``:w Dateiname``
      - Speichere den aktuellen Buffer als ``Dateiname``

Auch die Schreib-Anweisung kann nur auf einen bestimmten Textbereich angewendet
werden. Beispielsweise kann man mit ``:1,25w dateiname`` die ersten ``25``
Zeilen der Datei in den angegebenen Dateinamen schreiben, oder man kann einen
Text visuell markieren und dabei ``:w`` eingeben; in der Kommandozeile wird
dabei automatisch ``'<,'>w`` angezeigt, wobei ``'<,'>`` den visuell markierten
Bereich bezeichnet.

In Vim können mehrere Dateien auf einmal geöffnet sein. Im Umgang mit
diesen Buffern sind folgende Anweisungen hilfreich:

.. list-table::
    :widths: 15 40 20
    :header-rows: 0

    * - ``:ls``
      - Zeige eine Liste an geöffneten Dateien an
      - (identisch mit ``:buffers``)
    * - ``:bn``
      - Gehe zur nächsten offenen Datei
      - (*buffer next*)
    * - ``:bp``
      - Gehe zur vorherigen offenen Datei
      - (*buffer previous*)
    * - ``:bf``
      - Gehe zur ersten geöffneten Datei
      - (*buffer first*)
    * - ``:bl``
      - Gehe zur letzten geöffneten Datei
      - (*buffer last*)
    * - ``:b#``
      - Gehe zur zuletzt verwendeten Buffer
      -
    * - ``:b 1..99``
      - Gehe zur Datei Nr. ``1..99`` der Bufferliste
      -
    * - ``:bd``
      - Lösche die aktuelle Datei aus der Buffer-Liste
      - (*buffer delete*)

.. :wn : write file and move to next (SUPER)
.. :bd : remove file from buffer list (SUPER)
.. :sp fred.txt : open fred.txt into a split

Mittels ``:bufdo`` kann man eine (oder mehrere mittels ``|`` ("Pipe")
verknüpfte) Anweisung(en) auf alle geöffneten Dateien anwenden:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:bufdo Anweisung``
      - Führe eine ``Anweisung`` in allen geöffneten Buffern aus

Das Gleiche kann man allerdings auch (meist sicherer) mittels einer
:ref:`Makro-Aufzeichnung <Makros>` erreichen.

.. _Aufrufe von externen Programmen:

Aufrufe von externen Programmen
-------------------------------

Externe Programme können im Kommandozeilen-Modus integriert werden, indem dem
jeweiligen Aufruf ein ``!`` vorangesetzt wird, wie zum Beispiel:

.. list-table::
    :widths: 10 60
    :header-rows: 0

    * - ``:ls``
      - Zeige eine Liste der geoffneten Buffer an (Vim-interne Funktion!)
    * - ``:!ls``
      - Gebe den Inhalt des Arbeitsverzeichnisses aus (gewöhnliche
        Linux-Anweisung)
    * - ``:.!sh``
      - Ersetze die momentane Zeile (``.``) durch die Rückgabe der Shell

Wird ein beliebiger Bereich vor dem Ausrufezeichen angegeben (z.B. ``%`` für die
aktuelle Datei oder ``.`` für die aktuelle Zeile), so wird die Rückgabe der
aufgerufenen Anweisung an entsprechender Stelle in die Datei geschrieben.

Die Ausgabe eines externen Programms kann wiederum mittels ``:r`` unmittelbar
hinter der aktuellen Cursorposition eingelesen werden. Um beispielsweise die
Ausgabe von ``!ls`` in den Buffer aufzunehmen, kann man folgendes eingeben:

.. code-block:: vim

    :r !ls

Im Normalmodus kann auch ``!!`` anstelle von ``:!`` eingegeben werden, um
externe Programme aufzurufen.

..  % !!tr -d abcd     # Delete a,b,c,d from the current line

Externe Programme können unter anderem eingesetzt werden, um die aktuelle Datei
zu compilieren. Um beispielsweise eine aktuell geöffnete LaTeX-Datei in ein
``.pdf``-Dokument umzuwandeln, kann man folgendes eingeben:

.. code-block:: vim

    :!pdflatex %

Für längere derartige Aufrufe können natürlich wiederum in der
:ref:`Konfigurationsdatei` entsprechende :ref:`Mappings` vergeben werden. Danach
genügt im Normal- oder Einfügemodus ein individuelles Tastenkürzel, und der
dadurch definierte Prozess wird ausgeführt.

Ebenso ist es möglich, externe Programme nur auf einen bestimmten Bereich (z.B.
im :ref:`visuellen Modus <Visueller Modus>`) anzuwenden:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``'<,'> !sort``
      - Sortiere den visuell markierten Bereich (``'<`` bis ``'>``)
    * - ``'a,'b !grep Wort``
      - Lösche alle Zeilen zwischen den Markern ``a`` und ``b``, die nicht
        ``Wort`` enthalten
    * - ``:r !grep "Test" Datei``
      - Lese die Ausgabe von ``grep`` ein und füge sie nach der aktuellen Stelle
        in die ``Datei`` ein

Das externe Programm muss also nicht an erster Stelle in der Kommandozeile
erscheinen.

.. _Text ersetzen:

Text ersetzen
-------------

Gezieltes Ersetzen von Text erfolgt in Vim nach folgendem Schema:

.. code-block:: vim

    :Bereich s/Suchbegriff/Ersetzung/Optionen

Als Optionen stehen dabei zur Verfügung:

.. list-table::
    :widths: 5 55 10
    :header-rows: 0

    * - ``c``
      - Frage bei jedem Treffer nach
      - (*confirmation*)
    * - ``g``
      - Beachte alle Vorkommen des Suchbegriffs (nicht nur den ersten Treffer in
        jeder Zeile)
      - (*global*)
    * - ``i``
      - Ignoriere Groß- / Kleinschreibung
      - (*ignore case*)

Wird eine dieser Anweisungen auf einen visuell markierten Bereich angewandt, so
werden dessen Grenzen ``'<``, ``'>`` als Bereich angenommen. Ansonsten kann
jeder beliebige Zeilenbereich, mit Komma getrennt, angegeben werden. Möchte man
Ersetzungen in der ganzen Datei vornehmen, so steht dafür ``%`` als
Auswahlbereich zur Verfügung.

Beispiel:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:% s/alt/neu/g``
      - Ersetze ``alt`` durch ``neu`` in der ganzen Datei
    * - ``:1,20 s/alt/neu/g``
      - Ersetze ``alt`` durch ``neu`` in den ersten 20 Zeilen

Kommt der Schrägstrich selbst im Suchbegriff vor, kann auch jedes andere
Zeichen zur Trennung von Suchbegriff, Ersetzungen und Optionen gewählt
werden. Das erste Zeichen nach dem ``s`` wird dann als Trennzeichen
verwendet (z.B. ``:%s #/pfad/#irgendwas#`` ).

Bisweilen ist es auch hilfreich, "seltsame" Zeichen in einer Textdatei zu
ersetzen, beispielsweise wenn Text aus einer ``.pdf``-Datei mittels
``pdftotext`` in eine Textdatei extrahiert wird. Die zu löschenden Zeichen
können dann visuell markiert und mittels ``y`` in die Vim-interne Zwischenablage
kopiert werden. In der Kommandozeile kann der so kopierte Inhalt dann mittels
``<c-r> *`` wieder eingefügt werden.


.. _Reguläre Ausdrücke:

Reguläre Ausdrücke
------------------

Das Suchen und Ersetzen von Textstücken lässt sich durch so genannte reguläre
Ausdrücke oft wesentlich erleichtern bzw. beschleunigen. Hierzu können
spezielle Zeichen verwendet werden, die jeweils einem bestimmten Suchmuster
entsprechen.

Werden die folgenden Zeichen in einer Such- oder Ersetzungsanweisung verwendet,
so werden sie als reguläre Ausdrücke interpretiert. Möchte man das jeweilige
Zeichen in seiner Grundbedeutung interpretiert haben, so muss ein ``\``
(Backslash) davor platziert werden:

.. list-table::
    :widths: 10 50
    :header-rows: 0

    * - ``\``
      - Sonderbedeutung des nächsten Zeichens aufheben ("\\" entspricht einem Backslash)
    * - ``^``
      - Zeilenanfang
    * - ``$``
      - Zeilenende
    * - ``\r``
      - Zeilenende (carriage return)
    * - ``\t``
      - Tabulator
    * - ``.``
      - Ein beliebiges Zeichen
    * - ``*``
      - Multiplexer: Das vorhergehende Zeichen null mal oder beliebig oft
    * - ``[ ]``
      - Selektierer: Eines der Zeichen innerhalb der eckigen Klammern
    * - ``[^  ]``
      - Selektierer mit Negation: Ein Zeichen, das *nicht* in der eckigen Klammer vorkommt
    * - ``&``
      - Nur im Ersetzungsbereich: Textstelle, auf die das Suchmuster zutrifft.

..  ~ 	Matches last given substitute string.

Ebenso gibt es Zeichen, die in einer Such- oder Ersetzungsanweisung als
"normale" Zeichen interpretiert werden, jedoch durch Voranstellen eines ``\``
eine Sonderbedeutung bekommen:

.. list-table::
    :widths: 10 50
    :header-rows: 0

    * - ``\<``
      - Wortanfang
    * - ``\>``
      - Wortende
    * - ``\(   \)``
      - UND-Verknüpfung: Gruppierung mehrer Suchmuster zu einem Ausdruck
    * - ``\|``
      - ODER-Verknüpfung: Der links oder der rechts von ``\|`` stehende Ausdruck
    * - ``\_.``
      - Ein beliebigs Zeichen, auch Zeilenende-Zeichen (Suche über Zeilenumbrüche hinweg)
    * - ``\+``
      - Multiplexer: Das vorhergehende Zeichen einmal oder beliebig oft.
    * - ``\?``
      - Multiplexer: Das vorhergehende Zeichen null oder ein mal.

Teile eines regulären Ausdrucks, die beim Suchen mittels ``\(`` und ``\)``
gruppiert werden, können im neuen Ausdruck mittels ``\1``, ``\2``, ``\3`` usw.
wieder aufgegriffen werden, wobei beispielsweise ``\1`` den ersten gruppierten
Ausdruck bezeichnet. Die Textstelle, die beim Suchen auf den *gesamten*
regulären Ausdruck zutrifft, kann beim Ersetzen mittels ``\0`` referenziert
werden.

.. definition greedy, beispiel

..  \{ 	Multi-item count match specification (greedy).
..  \{n,m} 	n to m occurrences of the preceding atom (as many as possible).
..  \{n} 	Exactly n occurrences of the preceding atom.
..  \{n,} 	At least n occurrences of the preceding atom (as many as possible).
..  \{,m} 	0 to n occurrences of the preceding atom (as many as possible).
..  \{} 	0 or more occurrences of the preceding atom (as many as possible).

..  \{- 	Multi-item count match specification (non-greedy).
..  \{-n,m} 	n to m occurrences of the preceding atom (as few as possible).
..  \{-n} 	Exactly n occurrences of the preceding atom.
..  \{-n,} 	At least n occurrences of the preceding atom (as few as possible).
..  \{-,m} 	0 to n occurrences of the preceding atom (as few as possible).
..  \{-} 	0 or more occurrences of the preceding atom (as few as possible).

.. Alle Leerzeilen am Ende von Zeilen löschen:
.. :%s/\s\+$//

.. http://vimregex.com/
.. http://vim.wikia.com/wiki/Search_patterns
.. http://www.softpanorama.org/Editors/Vimorama/vim_regular_expressions.shtml
.. http://www.jeetworks.org/node/86



