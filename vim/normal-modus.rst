.. _Normalmodus:

Normalmodus
===========

Der Normalmodus dient der Navigation durch die geöffnete(n) Datei(en) und der
Bearbeitung von deren Inhalt. Jede Taste besitzt hier ihre eigene Funktion. (Ein
`Spickzettel <http://tnerual.eriogerg.free.fr/vimqrc-ge.pdf>`_ kann in der
Lernphase hilfreich sein!)

Eigene Zuweisungen von beliebigen Funktionen auf Tasten(kombinationen) lassen
sich mittels :ref:`Mappings <Mappings>` definieren.


.. _Bewegungsanweisungen:

Bewegungsanweisungen
--------------------

Die folgenden Tasten(kombinationen) bewirken im Normalmodus eine Bewegung des
Cursors.

``hjkl`` kann alternativ zu den Pfeiltasten genutzt werden:

.. list-table::
    :widths: 20 20 60
    :header-rows: 0

    * - ``j``
      - :math:`\downarrow`
      - Gehe eine Zeile nach unten
    * - ``k``
      - :math:`\uparrow`
      - Gehe eine Zeile nach oben
    * - ``h``
      - :math:`\leftarrow`
      - Gehe eine Stelle nach links
    * - ``l``
      - :math:`\rightarrow`
      - Gehe eine Stelle nach rechts

``Ctrl f`` und ``Ctrl b`` entsprechen ``PageDOWN`` und ``PageUp``:

.. todo: move in long lines!

.. list-table::
    :widths: 40 60
    :header-rows: 0

    * - ``Ctrl f`` oder ``PageDOWN``
      - Gehe eine Seite nach unten
    * - ``Ctrl b`` oder ``PageUP``
      - Gehe eine Seite nach oben

Um zu einer bestimmten Zeile zu gelangen, gibt es folgende Tastenkürzel:

.. list-table::
    :widths: 40 60
    :header-rows: 0

    * - ``gg``
      - Gehe zum Anfang der Datei
    * - ``G``
      - Gehe ans Ende der Datei

Mit der Eingabe von ``nG`` oder ``ngg`` springt man zur ``n``-ten Zeile.
Beispielsweise gelangt man durch die Eingabe von ``3gg`` bzw. ``3G`` zur dritten
Zeile.

.. _Navigation innerhalb einer Zeile:

.. rubric:: Navigation innerhalb einer Zeile

Mit ``0`` und ``$`` gelangt man schnell an den Anfang oder das Ende der
aktuellen Zeile. Einzelne Buchstaben lassen sich gezielt mit ``f`` und ``t``
ansteuern:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``^`` oder ``0``
      - Gehe an den Anfang der Zeile
    * - ``$``
      - Gehe an das Ende der Zeile
    * - ``f`` ``Buchstabe``
      - Gehe zu dem nächsten Vorkommen von ``Buchstabe`` (exakt)
    * - ``F`` ``Buchstabe``
      - Gehe zu dem vorherigen Vorkommen von ``Buchstabe`` (exakt)
    * - ``t`` ``Buchstabe``
      - Gehe zu dem nächsten Vorkommen von ``Buchstabe`` (eine Stelle vorher)
    * - ``T`` ``Buchstabe``
      - Gehe zu dem vorherigen Vorkommen von ``Buchstabe`` (eine Stelle vorher)
    * - ``;`` (Strichpunkt)
      - Wiederhole die letzte Buchstabensuche in gleicher Richtung
    * - ``,`` (Komma)
      - Wiederhole die letzte Buchstabensuche in umgekehrter Richtung

Um von einem Wort zum nächsten zu gelangen, gibt es folgende Tastenkürzel:

.. list-table::
    :widths: 5 45 5 45
    :header-rows: 0

    * - ``w``
      - Gehe an den Anfang des nächsten Wortes
      - ``W``
      - wie ``w``, jedoch ohne Rücksicht auf Satzzeichen
    * - ``e``
      - Gehe an das Ende des aktuellen Wortes
      - ``E``
      - wie ``e``, jedoch ohne Rücksicht auf Satzzeichen
    * - ``b``
      - Gehe an den Anfang des vorherigen Wortes
      - ``B``
      - wie ``b``, jedoch ohne Rücksicht auf Satzzeichen
    * - ``ge``
      - Gehe an das Ende des vorherigen Wortes
      -
      -

.. _Navigation zwischen Sätzen und Abschnitten:

.. rubric:: Navigation zwischen Sätzen und Abschnitten

Für Sprünge zum nächsten bzw. vorherigen Satz oder  Abschnitt  lassen  sich  die
Klammer-Symbole verwenden:

.. list-table::
    :widths: 5 45 5 45
    :header-rows: 0

    * - ``(``
      - Gehe an den Anfang des aktuellen Satzes
      - ``)``
      - Gehe an den Anfang des nächsten  Satzes
    * - ``{``
      - Gehe zu der vorherigen leeren Zeile
      - ``}``
      - Gehe zu der nächsten leeren Zeile
    * - ``[[``
      - Gehe zu der vorherigen Überschrift
      - ``]]``
      - Gehe zu der nächsten Überschrift

.. TODO Für Programmierer: Fehlen passende Gegenstücke, so können ungeschlossene Klammern leicht gefunden werden:

.. ``[(`` bzw. ``[)``   | gehe zu der vorherigen öffnenden bzw. schließenden runden Klammer
.. ``](`` bzw. ``])``   | gehe zu der nächsten öffnenden bzw. schließenden runden Klammer
.. ``[\{`` bzw. ``]\{`` | gehe zu der vorherigen öffnenden bzw. schließenden geschweiften Klammer
.. ``[\{`` bzw. ``]\}`` | gehe zu der nächsten öffnenden bzw. schließenden geschweiften Klammer

Innerhalb des aktuellen Bildschirms kann man sich wie folgt bewegen:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``H``
      - Gehe zu der obersten Zeile des Bildschirms
    * - ``M``
      - Gehe zu der mittleren Zeile des Bildschirms
    * - ``L``
      - Gehe zu der untersten Zeile des Bildschirms

Hierbei gelangt man mit z.B. ``5H`` zur fünften Zeile des aktuellen Bildschirms,
mit ``2L`` zur vorletzten.


Manchmal (z.B. beim Aufnehmen von :ref:`Makros`)  finden  auch  folgende  Tasten
Verwendung:

.. list-table::
    :widths: 15 80
    :header-rows: 0

    * - ``+``
      - Gehe zum ersten Zeichen der folgenden Zeile
    * - ``-``
      - Gehe zum ersten Zeichen der vorherigen Zeile
    * - ``n|``
      - Gehe zum ``n``-ten Zeichen der aktuellen Zeile
    * - ``gm``
      - Gehe zur Fenstermitte (horizontal)
    * - ``%``
      - Gehe zum passenden Gegenstück einer Klammer
    * - ``Ctrl d``
      - Gehe eine halbe Seite nach unten
    * - ``Ctrl u``
      - Gehe eine halbe Seite nach oben
    * - ``Ctrl e``
      - Scrolle den Bildschirm eine Zeile nach oben (der Cursor bleibt
        unverändert)
    * - ``Ctrl y``
      - Scrolle den Bildschirm eine Zeile nach unten (der Cursor bleibt
        unverändert)
    * - ``zt``
      - Scrolle den Cursor an das obere Ende des Bildschirms
    * - ``zb``
      - Scrolle den Cursor an das untere Ende des Bildschirms
    * - ``zz``
      - Scrolle den Cursor in die Mitte des Bildschirms

.. _Weitere Navigationsmöglichkeiten:

.. rubric:: Weitere Navigationsmöglichkeiten

Folgende Tastenkombinationen sind im Normalmodus ebenfalls oftmals hilfreich:

.. list-table::
    :widths: 10 90
    :header-rows: 0

    * - ``gf``
      - Öffne die Datei unter dem Cursor
    * - ``gx``
      - Öffne den Link unter dem Cursor im Standard-Webbrowser

Beide Tastenkombinationen funktionieren nur, wenn sich der Cursor aktuell über
einem existierenden Dateipfad oder einer Web-Adresse befindet.


.. _Suchanweisungen:

Suchanweisungen
---------------

Im Normalmodus kann man mit ``/`` bzw. ``?`` die aktuelle Datei vorwärts bzw.
rückwärts nach Textstellen durchsuchen:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``/`` ``Suchbegriff``
      - Gehe zu dem nächsten Vorkommen von ``Suchbegriff``
    * - ``?`` ``Suchbegriff``
      - Gehe zu dem vorherigen Vorkommen von ``Suchbegriff``
    * - ``*``
      - Gehe zu dem nächsten Vorkommen des Worts unter dem Cursor
    * - ``#``
      - Gehe zu dem vorherigen Vorkommen des Worts unter dem Cursor
    * - ``gd``
      - Gehe zu dem ersten Vorkommen des Worts unter dem Cursor (*go [to the] definition*)

Ist die Option ``hlsearch`` in der :ref:`Konfigurationsdatei` gesetzt, so werden
die Treffer farblich hervorgehoben. Mittels ``:nohl`` ("no-highlight") oder
einem entsprechenden :ref:`Mapping <Mappings>` kann die Hervorhebung wieder
aufgehoben werden.

Zu dem jeweils nächsten Treffer gelangt man mit ``n``:

.. list-table::
    :widths: 15 80
    :header-rows: 0

    * - ``n``
      - Gehe zum nächsten Treffer
    * - ``N``
      - Gehe zum nächsten Treffer (umgekehrte Richtung)

Mit ``gD`` kann auch nach einer globalen Definition (in allen geöffneten Buffern
gesucht werden.


.. _Bearbeitungsanweisungen:

Bearbeitungsanweisungen
-----------------------

Im Normalmodus gibt es folgende Anweisungen, um Text zu kopieren, löschen,
abzuändern, oder einzufügen:


.. list-table::
    :widths: 15 60 25
    :header-rows: 0

    * - ``y``
      - Kopieren
      - (*yank*)
    * - ``d``
      - Löschen bwz. Ausschneiden
      - (*delete*)
    * - ``c``
      - Ändern
      - (*change*)
    * - ``p``
      - Einfügen
      - (*paste*)

Damit lassen sich beliebige Mengen an Text bearbeiten:

.. list-table::
    :widths: 35 15 20 20
    :header-rows: 0

    * - Text
      - kopieren
      - ändern
      - löschen
    * - wortweise vorwärts
      - ``yw``
      - ``cw``
      - ``dw``
    * - wortweise rückwärts
      - ``yb``
      - ``cb``
      - ``db``
    * - bis zum Zeilenanfang
      - ``y0``
      - ``c0``
      - ``d0``
    * - bis zum Zeilenende
      - ``y$``
      - ``c$`` oder ``C``
      - ``d$`` oder ``D``
    * - die ganze Zeile
      - ``yy``
      - ``cc``
      - ``dd``

**Tip**: Mir erscheint es logisch, mit ``Y`` alles bis zum Zeilenende zu
kopieren. Da dies nicht standardmäßig der Fall ist, habe ich mir ein
eigenes Mapping in der :ref:`Konfigurationsdatei` so definiert.

Natürlich lassen sich die Anweisungen wieder beliebig multiplizieren, ``c3W``
oder ``3cW`` ändert die nächsten drei Wörter ohne Rücksicht auf
Satzzeichen, ``y3y`` oder ``3yy`` löscht die nächsten drei Zeilen. Bei
umfassenderen Textmengen empfiehlt es sich, diese zuerst im :ref:`visuellen
Modus <Visueller Modus>` zu markieren, und dann die entsprechende Taste für
die gewünschte Bearbeitungsfunktion zu drücken.

Will man nur einzelne Buchstaben oder Ziffern abändern, so kann man folgende
Funktionen nutzen:

.. list-table::
    :widths: 5 70 10
    :header-rows: 0

    * - ``x``
      - Lösche das Zeichen unter dem Cursor
      -
    * - ``~``
      - Ändere Kleinbuchstaben in Großbuchstaben und umgekehrt
      -
    * - ``gu``
      - Ändere Buchstaben in Kleinbuchstaben (auch visuell markierte Bereiche)
      -
    * - ``gU``
      - Ändere Buchstaben in Großbuchstaben (auch visuell markierte Bereiche)
      -
    * - ``r``
      - Ändere das Zeichen unter dem Cursor, danach weiter im Normal-Mode
      - (*replace*)
    * - ``R``
      - Überschreibe eine beliebige Anzahl an Zeichen ("Replace"-Mode, zurück mit ``ESC``)
      -
    * - ``s``
      - Ändere das Zeichen unter dem Cursor, weiter im Insert-Mode
      - (*substitute*)
    * - ``S``
      - Ändere die ganze Zeile
      -

Bei jeder Bearbeitungsanweisung wird der entsprechende Textteil in die
Zwischenablage kopiert. Von dort aus kann er mittels ``p`` wieder eingefügt
werden:

.. list-table::
    :widths: 10 90

    * - ``p``
      - Füge Inhalt des Zwischenspeichers *hinter* dem Cursor ein
    * - ``P``
      - Füge Inhalt des Zwischenspeichers *vor* dem Cursor ein

Im Einfügemodus kann Text aus der systemweiten Zwischenablage mittels
``Shift Insert`` (Einfüge-Taste) oder durch Klick auf die mittlere
Maustaste (gleichzeitiges Klicken von linker und rechter Taste bei
zweitastigen Mäusen und Notebooks) eingefügt werden.

Im Normalmodus kann Text aus der systemweiten Zwischenablage mittels des
:ref:`Registers <Register>` ``*`` genutzt, d.h. mittels ``"*p`` bzw. ``"*P``
eingefügt werden.

Undo und Redo
-------------

Änderungen  können  mit  ``u``  rückgängig   gemacht   bzw.   mit   ``Ctrl   r``
wiederhergestellt werden:

.. list-table::
    :widths: 20 50 40

    * - ``u``
      - Mache die letzte Änderung rückgängig
      - (*undo*)
    * - ``U``
      - Mache alle Änderungen in der aktuellen Zeile rückgängig
      -
    * - ``Ctrl r``
      - Stelle eine rückgängig gemachte Änderung wieder her
      - (*redo*)
    * - ``.``
      - Wiederhole die zuletzt getätigte Texteingabe, Textbearbeitung,
        Formatierung, etc.
      -


.. _Marker:

Marker
------

Muss man öfters innerhalb einer Datei hin- und herspringen, so schaffen
Markierungshilfen (*Marker*) Abhilfe.

Im Normalmodus kann man die Stelle, an der sich der Cursor gerade befindet,  mit
``m`` gefolgt von einem beliebigen Buchstaben markieren:

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - ``m`` ``Kleinbuchstabe``
      - Setze  eine lokale Markierung (gilt nur in der aktuellen Datei)
    * - ``m`` ``Großbuchstabe``
      - Setze eine globale Markierung

Mit Hilfe der globalen Markierungen lassen sich häufig genutzte Dokumente
schnell laden, egal wo man sich gerade befindet.

*Beispiel:* Man kann man mit ``'G`` zu genau der Stelle wechseln, die man
vorhergehend mit ``mG`` markiert hat. Liegt der Marker dabei in einer anderen
Datei, so bleibt der ursprüngliche Buffer im Hintergrund geöffnet (ein
:ref:`Wechsel zwischen den geöffneten Dateien <Buffer wechseln>` ist
beispielsweise mit dem :ref:`Buffer-Explorer <Buffer-Explorer>`- oder
:ref:`Minibuf-Explorer`-Plugin leicht möglich).

Mit ``'`` (einfaches Anführungszeichen), gefolgt von dem angegebenen
Buchstaben, gelangt man von wieder zu der entsprechenden Zeile, mittels
````` (Apostroph) sogar in die entsprechende Spalte. Mittels ``''`` bzw.
`````` gelangt man zur zuletzt bearbeiteten Zeile bzw. Position zurück.

*Tipp:* Mittels ``'.`` gelangt man zu der zuletzt editierten Stelle, mit
``'^`` zur letzten Einfüge-Stelle, und mit ``'"`` zur Position beim letzten
Beenden zurück!

Ein weiteres Springen zwischen verschiedenen Änderungen und deren Positionen
ist mittels ``Ctrl o`` bzw. ``Ctrl i`` möglich:

.. list-table::
    :widths: 15 80
    :header-rows: 0

    * - ``Ctrl o``
      - Gehe zurück zur letzten Änderung (bzw. zur zuletzt geänderten Datei)
    * - ``Ctrl i``
      - Gehe vorwärts zur letzten Änderung (umgekehrte Richtung)


.. _Register:

Register
--------

Vim besitzt nicht nur *eine* Zwischenablage, sondern kann Textelemente und
:ref:`Makros` jedem beliebigen Kleinbuchstaben zuweisen. Ein Register ist quasi eine
benannte Zwischenablage.

Im Normalmodus kann man mit ``"`` ``Buchstabe`` auf einen Register zugreifen:

.. list-table::
    :widths: 40 60
    :header-rows: 0

    * - ``"`` ``Kleinbuchstabe`` ``Bearbeitungsanweisung``
      - Kopiere in/aus das Register ``Buchstabe`` hinein/heraus
    * - ``"`` ``Großbuchstabe`` ``Bearbeitungsanweisung``
      - Füge Text oder Code hinten an das Register ``Buchstabe`` an

*Beispiel:* Mittels ``"hyy`` kann die aktuelle Zeile in die Ablage ``h``
kopiert werden. Deren Inhalt kann mit ``"hp`` wieder an anderer Stelle
eingefügt werden. So abgelegte Inhalte gehen beim Schließen von Vim nicht
verloren!

Mit ``:reg`` erhält man eine Übersicht, welcher Inhalt in welchem Register
abgelegt ist:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``:reg``
      - Zeige den Inhalt aller Register an

Ein spezielles Register ist die (systemweite) Zwischenablage ''*'', mittels
der ein Kopieren von bzw. in andere(n) Programme(n) möglich ist:

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - ``"*y`` ``Bewegung``
      - Kopiere in die Zwischenablage
    * - ``"*p`` ``Bewegung``
      - Füge aus der Zwischenabage ein

Unter Linux werden Bereiche bereits durch ein einfaches Markieren
(:ref:`Visueller Modus`) in die systemweite Zwischenablage kopiert. An
anderer Stelle können sie dann mit ``Shift Ins`` (Einfüge-Taste) oder durch
einen Klick auf die mittlere Maustaste wieder eingefügt werden.


.. _Makros:

Makros
------

Es kann nicht nur Text in einem :ref:`Register` abgelegt werden, sondern auch
jede beliebige Anweisungssequenz. Wie bei einem Kassettenrecorder können
Anweisungen mit aufgezeichnet, und als "Makro" später beliebig oft wieder
abgespielt werden:

Im Normalmodus werden Makros mit ``q`` ``Buchstabe`` aufgezeichnet und mit
``@`` ``Buchstabe`` wiedergegeben:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``q`` ``Kleinbuchstabe``
      - Nehme eine Anweisungssequenz bis zum nächsten Drücken von ``q`` auf
    * - ``q`` ``Großbuchstabe``
      - Hänge eine Anweisungssequenz an das Register ``Buchstabe`` an
    * - ``@`` ``Buchstabe``
      - Führe die im Register ``Buchstabe`` liegende Anweisungssequenz aus

Es kann durchaus nützlich sein, z.B. mittels ``10@Buchstabe`` eine
Anweisungskette 10fach auszuführen. Speziell gleichförmige Bearbeitungen
mehrerer Dateien sind so möglich, denn :ref:`Bufferwechsel <Buffer wechseln>`
können ja gleich mit "aufgenommen" werden.. :-)

*Tipp:* Der zuletzt ausgeführte Makro-Anweisung kann mit ``@@`` wiederholt werden.

..  Die unmittelbar letzte Anweisung (Eingabe von Text, usw.) kann man auch ohne Makro
..  im Normalmodus mittels ``.`` (*Punkt*) wiederholen.

.. _Faltungen:

Faltungen
---------

Werden Text-Dateien infolge ihrer Länge zu unübersichtlich, können bestimmte
Bereiche ausgeblendet werden. Das kann entweder über Schlüsselworte,
Einrückungen oder über Symbole erfolgen.

Beispielsweise wird Python-Code standardmäßig anhand von Einrückungen gefaltet.
Wird kein spezieller Faltungsmechanismus von einem Plugin geladen, so wird das
in der :ref:`Konfigurationsdatei` festgelegt Faltungsschema verwendet. Oft
werden dabei als Faltungsmarkierungen ``{{{`` und ``}}}`` genutzt, so dass alle
Textbereiche, die sich zwischen solchen Dreifach-Klammern befinden, gefaltet
werden.

Folgende Anweisungen können im Umgang mit Faltungen nützlich sein:

.. list-table::
    :widths: 10 30 10
    :header-rows: 0

    * - ``zf``
      - Erstelle eine Faltung
      -
    * - ``zo``
      - Öffne eine Faltung
      -  (*open*)
    * - ``zc``
      - Schließe eine Faltung
      - (*close*)
    * - ``zd``
      - Entferne eine Faltung
      - (*delete*)
    * - ``\rf``
      - Falte die Datei neu
      - (*refold*)

Um eine Faltung zu erstellen, wird der Bereich meist zuerst visuell
markiert, und dann mittels ``zf`` gefaltet.

Faltungen können auch ineinandergeschachtelt (*nested*) auftreten. Faltungen
unter dem Cursor können einzeln oder auf einmal mittels ``za`` bzw. ``zA``
geöffnet und geschlossen werden.

.. list-table::
    :widths: 10 40
    :header-rows: 0

    * - ``za``
      - Öffne bzw. schließe lokale Faltungen
    * - ``zA``
      - Öffne bzw. schließe lokale Faltungen (rekursiv)

Ebenfalls nützlich sind folgende Faltungsanweisungen:

.. list-table::
    :widths: 10 50 10
    :header-rows: 0

    * - ``zr``
      - Reduziere die Anzahl der Faltungsebenen um eins
      -  (*reduce*)
    * - ``zm``
      - Erhöhe die Anzahl der Faltungsebenen um eins
      - (*more*)
    * - ``zR``
      - Öffne alle Faltungen
      -
    * - ``zM``
      - Schließe alle Faltungen
      -

.. Nach Belieben können Faltungen gelegentlich auch komplett de- und reaktiviert
..  werden:

..  .. list-table::
    ..  :widths: 10 40
    ..  :header-rows: 0

    ..  * - ``zn``
      ..  - Faltung deaktivieren
    ..  * - ``zN``
      ..  - Faltung reaktivieren
    ..  * - ``zi``
      ..  - Wechsel zwischen ``zn`` und ``zN``

..   *   Mit   ''\rf''   werden   die   Faltungen   einer   Datei   aufgefrischt

.. _Fenster splitten:

Fenster splitten
----------------

Vim kann mehrere Dateien optional in verschiedenen Tabs im oder in unterteilten
Fenstern öffnen:

* Mit ``:tabedit datei`` wird eine Datei in einem neuen Tab geöffnet.
  Zwischen den Tabs kann mit ``Ctrl PageUP`` und ``Ctrl PageDOWN``
  gewechselt werden. Infos findet man z.B. unter ``:h tabpage.txt``.

* Mit ``:[v]split`` bzw. ``Ctrl W s`` oder ``Ctrl W v`` wird ein Fenster
  horizontal bzw. vertikal geteilt. Manche Plugins wie die Latex-Suite,
  :ref:`Voom` oder :ref:`Taglist` nutzen diese Funktion, um auf der linken Seite
  beispielsweise ein Inhaltsverzeichnis ein- oder auszublenden.

Anweisungen zur Handhabung von geteilten Fenstern werden gewöhnlich mit ``Ctrl W``
eingeleitet. Mit folgenden Tastenkombinationen kann man zwischen den geöffneten
Fenstern wechseln:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``Ctrl W w``
      -  Wechsle zum jeweils nächsten Fenster (im Uhrzeigersinn)
    * - ``Ctrl W h j k l``
      - Wechsle man zum nächsten Fenster auf der linken, unteren, oberen oder
        rechten Seite
    * - ``Ctrl W H J K L``
      -  Verschiebe das aktuelle Fenster in die jeweilige Richtung
    * - ``Ctrl W r`` bzw. ``Ctrl W R``
      - Verschiebe alle geöffnete Fenster der Reihenfolge nach, das letzte wird
        das erste

Mit folgenden Anweisungen lässt sich die Größe des aktuellen Fensters anpassen:

.. list-table::
    :widths: 15 50
    :header-rows: 0

    * - ``Ctrl W +``
      - Vergrößere das aktuelle Fenster um eine Zeile
    * - ``Ctrl W -``
      - Verkleinere das aktuelle Fenster um eine Zeile
    * - ``n Ctrl W |``
      - Setze die Breite des aktuellen Fensters auf ``n``
    * - ``Ctrl W _``
      - Maximiere das aktuelle Fenster
    * - ``Ctrl W =``
      - Richte alle Fenster auf die gleiche Größe aus

Zum Schließen des aktuellen bzw. der übrigen Fenster gibt es folgende
Tastenkombinationen:

.. list-table::
    :widths: 10 25 10
    :header-rows: 0

    * - ``Ctrl W c``
      - Schließe das aktuelles Fenster
      - (*close*)
    * - ``Ctrl W o``
      - Schließe alle anderen Fenster
      - (*close other*)

.. rubric:: Quickfixleiste

Nutzt man den Vim als Programmier-Umgebung bzw. compiliert aus dem Vim heraus
Quellcode, so bekommt man Fehlermeldungen in der sogenannten "Quickfix-Leiste"
angezeigt. Im Prinzip ist das ein gesplittetes Fenster, in welchem zwischen den
Fehlern navigiert werden kann. Durch Drücken von ``Enter`` gelangt man an die
entsprechende Stelle im Hauptdokument. Von dort aus gelangt man zum nächsten
bzw. vorherigen Fehler mittels ``:cn`` bzw. ``:cp``.

.. Normalerweise wird die Quickfix-Leiste mit
.. ``:copen`` geöffnet und mit ``:cclose`` geschlossen. Bei häufigerem
.. Gebrauch empfiehlt sich dafuer allerdings z.B. folgendes Makro von der
.. fuer die Konfigurationsdatei:
..
.. command -bang -nargs=? QFix call QFixToggle(<bang>0)
.. function! QFixToggle(forced)
.. if exists("g:qfix_win") && a:forced == 0
.. cclose
.. unlet g:qfix_win
.. else
.. copen 10
.. let g:qfix_win = bufnr("$")
.. endif
.. endfunction
..
.. Tastenkuerzel F6 dafuer festlegen:
.. nmap <silent> <F6> :QFix<CR>

.. index:: vimdiff
.. _vimdiff:

.. rubric:: Vimdiff

Das Linux-Programm ``vimdiff`` zeigt ebenfalls in gesplitteten Fenstern
Unterschiede zwischen zwei Dateien an. Auf diese Weise lassen sich verschiedenen
Versionen des gleichen Dokuments schnell und übersichtlich abgleichen
(abweichende Stellen werden automatisch markiert):

.. code-block:: bash

 vimdiff datei1 datei2

Bewegt man sich in einer Datei nach unten, so scrolled die Anzeige der anderen
Datei im gegenüberliegenden Fenster mit, so dass stets die entsprechenden zwei
Zeilen verglichen werden. Beide Dateien können editiert werden, der Abgleich
erfolgt automatisch.


