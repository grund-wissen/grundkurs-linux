.. meta::
    :description: Ein Tutorial zu RestructuredText
    :keywords:  RestructuredText, Tutorial, Einführung, Sphinx, Wiki

.. _RestructuredText:

ReStructuredText-Elemente
=========================

`RestructuredText (RST) <http://de.wikipedia.org/wiki/ReStructuredText>`_ ist
eine vereinfachte Auszeichnungssprache ("markup language"), mit deren Hilfe
Textdokumente aus einfachen Strukturmerkmalen erzeugt werden können. Diese
lassen sich dann mittels eines geeigneten Converters, z.B. Sphinx, automatisiert
in LaTeX- oder HTML-Code übersetzen.

Um eine Datei mit RestructuredText-Inhalten zu erstellen, genügt es eine neue
Textdatei mit einem Editor zu öffnen. Üblicherweise werden
RestructuredText-Dateien mit der Endung ``.rst`` versehen.


.. _Überschriften und Hervorhebungen:

Überschriften und Hervorhebungen
--------------------------------

Überschriften sind zur Untergliederung eines Dokuments hilfreich und ermöglichen
eine automatische Erzeugung von Inhaltsverzeichnissen. RestructuredText kennt
dabei folgende Unterteilungen.

*Beispiel:*

.. code-block:: rst

    Name eines Kapitels
    ===================

    Name eines Abschnitts
    ---------------------

    Name eines Unterabschnitts
    ^^^^^^^^^^^^^^^^^^^^^^^^^^

    Name eines Paragraphen
    ''''''''''''''''''''''

*Ergebnis:*

.. raw:: html

    <div class="highlight-rst"><pre>
    <div class="section" id="name-eines-kapitels">
    <h1>Name eines Kapitels<a class="headerlink" href="#name-eines-kapitels" title="Permalink zu dieser Überschrift">¶</a></h1>
    <div class="section" id="name-eines-abschnitts">
    <h2>Name eines Abschnitts<a class="headerlink" href="#name-eines-abschnitts" title="Permalink zu dieser Überschrift">¶</a></h2>
    <div class="section" id="name-eines-unterabschnitts">
    <h3>Name eines Unterabschnitts<a class="headerlink" href="#name-eines-unterabschnitts" title="Permalink zu dieser Überschrift">¶</a></h3>
    <div class="section" id="name-eines-paragraphen">
    <h4>Name eines Paragraphen<a class="headerlink" href="#name-eines-paragraphen" title="Permalink zu dieser Überschrift">¶</a></h3>
    </pre></div>


Zur Hervorhebung einer Überschrift muss somit nur die jeweilige Zeile durch
eine zweite, ebenso lange Zeile mit entsprechenden Zeichen markiert werden;
anschließend muss eine leere Zeile folgen.

Die Überschriften werden -- je nach Converter und entsprechenden Einstellungen
-- in den erzeugten HTML- bzw. PDF-Dateien mit unterschiedlicher Schriftgröße
und/oder nummeriert dargestellt. In PDF-Dateien wird automatisch ein
Inhaltsverzeichnis zu Beginn des Dokuments erzeugt, in HTML-Dateien wird das
Inhaltsverzeichnis üblicherweise in der Seitenleiste angezeigt.

Zusätzlich ist es möglich, kleine Überschriften ohne Nummerierung und Auflistung
im Inhaltsverzeichnis einzufügen. Hierfür wird eine so genannte "Direktive"
namens ``.. rubric::`` verwendet. [#DIR]_

*Beispiel:*

.. code-block:: rst

    Kapitelname
    ===========

    Text.


    .. rubric:: Bezeichnung

    Mehr Text..


Eine weitere Aufgliederung eines Kapitels ist durch ein Aufspalten in mehrere
Dateien möglich.


.. _Das Inhaltsverzeichnis:

Das Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^^^^^

Üblicherweise werden für die einzelnen Kapitel einer Dokumentation eigene
Dateien angelegt, deren Namen in etwa den jeweiligen Kapitelüberschriften
entsprechen sollten (auf Umlaute im Dateinamen sollte dabei verzichtet werden,
Leerzeichen durch Binde- oder Unterstriche ersetzt werden). Jede dieser Dateien
muss unmittelbar mit einer Kapitelüberschrift beginnen und kann weitere
Überschriften beinhalten.

In der Hauptdatei ``index.rst`` der Dokumentation, die im Hauptverzeichnis zu
finden ist, wird auf die einzelnen Kapitel über ein Inhaltsverzeichnus
verwiesen. Um ein Inhaltsverzeichnis zu erzeugen, wird die so genannte
"toctree"-Umgebung verwendet ("Table-of-Contents"). Die Syntax dabei ist
folgende:

.. code-block:: rst


    .. toctree::
        :maxdepth: 2

        kapitelname-1.rst
        kapitelname-2.rst
        kapitelname-3.rst

Durch die Option ``:maxdepth:`` wird festgelegt, bis zu welcher Hierarchie-Stufe
das Inhaltsverzeichnis aufgegliedert werden soll. Mit ``:maxdepth: 2`` werden
beispielsweise alle Kapitel- und Abschnittsnamen eingeblendet, die in den
angegebenen Dateien zu finden sind. In der HTML-Version wird für jede
``toctree`` angegebene Datei eine neue Seite inklusive Rahmen und
Navigationshilfen erzeugt. In der LaTeX-Version werden die im ``toctree``
angegeben Dateien der Reihe nach eingebunden, als ob sich ihre Inhalte
hintereinander in einer einzigen Datei befänden.

Ein besonderer Vorteil dieser Methode liegt darin, dass umfangreichere Kapitel
beliebig in weitere Unterkapitel aufgeteilt werden können:

* Als erstes wird ein neuer Ordner angelegt, der den gleichen Namen wie die
  zugehörige RestructuredText-Datei erhält, beispielsweise ``kapitelname-2``.
* Anschließend wird die Kapitel-Datei in den neuen Ordner verschoben und dort
  in ``index.rst`` umbenannt.
* Für jedes Unterkapitel wird in dem neuen Ordner eine neue Textdatei angelegt,
  deren Namen wiederum in etwa den Überschriften der einzelnen Abschnitte
  entsprechen sollten. Jeder Abschnitt wird dann aus der ``index.rst``
  ausgeschnitten und in die entsprechende Datei eingefügt.
* In die ``index.rst`` wird schließlich ein ``toctree`` angelegt, der die Namen
  aller Dateien, aus denen das Kapitel besteht, beinhaltet.

Von welcher Hierarchie-Ebene die Überschriften in den einzelnen Dateien
ausgehen, ist nicht von Bedeutung: Beim Konvertieren der Quelltexte nach HTML
oder PDF werden alle Hierarchie-Ebenen bei Bedarf automatisch angepasst. Es muss
lediglich innerhalb jeder Datei darauf geachtet werden, dass unmittelbar mit der
"höchste" Überschrifts-Ebene begonnen wird. Eine Empfehlung hierfür ist, jede
Datei mit einer Kapitelüberschrift zu beginnen und bei Bedarf weitere
Überschriften einzufügen.


.. _Kommentare:

Kommentare
^^^^^^^^^^

RestructuredText-Dateien können um Kommentare ergänzt werden, die bei der
Übersetzung in PDF- bzw. HTML-Dateien ignoriert werden und somit lediglich als
"private" Notizen für den Autor dienen.

Jede Zeile einer RST-Datei kann, indem zu Beginn zwei Punkte und (mindestens)
ein Leerzeichen eingefügt werden, zu einem Kommentar gemacht werden.

*Beispiel:*

.. code-block:: rst

    ..  Dies hier ist ein Kommentar.

Um einen längeren, aus mehreren Zeilen bestehenden Kommentar zu erzeugen, kann
einerseits jede Zeile einzeln durch zwei Punkte und ein Leerzeichen am Anfang
der Zeile auskommentiert werden. Einfacher ist es, einen "langen Kommentar"
durch eine separate Zeile einzuleiten, die nur aus zwei Punkten und zwei
Leerzeichen besteht:

*Beispiel:*

.. code-block:: rst

    ..
        Dies hier ist ein langer Kommentar.
        Er besteht aus mehreren Zeilen.

Auf diese Weise können auch mehrere Absätze auskommentiert werden. Hierbei
muss jedoch in den Leerzeilen zwischen den Kommentar-Absätzen Leerzeichen oder
Tabulatoren eingefügt werden, da lange Kommentare stets durch eine einzelne,
komplett leere Zeile abgeschlossen werden.


.. _Hervorhebung von Textstellen:

Hervorhebung von Textstellen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um eine einzelne Textstelle innerhalb eines Absatzes hervorzuheben, kann eine
so genannte "Role" verwendet werden. [#ROL]_ Die wohl am häufigsten
auftretenden Roles sind:

* ``*Kursiver Text*``:
        Eine Textstelle, die unmittelbar (ohne Leerzeichen) durch je ein
        Sternchen begrenzt ist, wird *kursiv* dargestellt.
* ``**Fetter Text**``:
        Eine Textstelle, die unmittelbar (ohne Leerzeichen) durch je zwei
        Sternchen begrenzt ist, wird **fettgedruckt** dargestellt.
* ````Maschinenschrift````:
        Eine Textstelle, die unmittelbar (ohne Leerzeichen) durch je zwei
        schräge Apostrophen ("Backticks") begrenzt ist, wird in
        ``Maschinenschrift`` dargestellt. Diese Art der Hervorhebung kann
        insbesondere für kurze Codebeispiele genutzt werden.
* ``:sub:`Text```:
        Eine Textstelle, die unmittelbar (ohne Leerzeichen) durch je einen
        schrägen Apostrophen ("Backtick") begrenzt ist und durch das einleitende
        Schlüsselwort ``:sub:`` oder ``:subscript:`` markiert ist, wird als
        tiefgestellter Text dargestellt.
* ``:sup:`Text```:
        Eine Textstelle, die unmittelbar (ohne Leerzeichen) durch je einen
        schrägen Apostrophen ("Backtick") begrenzt ist und durch das einleitende
        Schlüsselwort ``:sub:`` markiert ist, wird als tiefgestellter Text
        dargestellt.

*Beispiel:*

.. code-block:: rst

    Etwas *kursiv dargestellter*,
    etwas **fettgedruckter** Text,
    und etwas Text in ``Maschinenschrift``;

    Tief gestellter Text: :sub:`123` und
    hoch gestellter Text: :sup:`456`

.. only:: html

    *Ergebnis:*

.. raw:: html

    <div class="highlight-rst"><div class="highlight"><pre>
    <p>Etwas <em>kursiv dargestellter</em>, etwas <strong>fettgedruckter</strong> Text, und etwas Text in <tt class="docutils literal"><span class="pre">Maschinenschrift</span></tt>.</p>
    <p>Tief gestellter Text: <sub>123</sub> und hoch gestellter Text: <sup>456</sup></p>
    </pre></div>

Mittels der ``:math:``-Role können zusätzlich mathematische Formeln, geschrieben
als :ref:`LaTeX-Code <gwil:Mathematischer Formelsatz>`, innerhalb einer Zeile
eingefügt werden. Beispielsweise liefert ``:math:`a^2 + b^2 = c^2``` als
Ergebnis die Formel :math:`a^2 + b^2 = c^2`.


.. _Hervorhebung von Absätzen:

Hervorhebung von Absätzen
^^^^^^^^^^^^^^^^^^^^^^^^^

Um einen Absatz bzw. mehrere Absätze hervorzuheben, kann eine der folgenden
Direktiven genutzt werden:

* ``.. epigraph::``

  Innerhalb einer ``epigraph``-Umgebung werden gewöhnlich Zitate in das
  Dokument eingefügt. Am Ende wird dabei üblicherweise der Name des Autors der
  zitierten Textstelle angegeben.

  *Beispiel:*

  .. code-block:: rst

      .. epigraph::

          "Phantasie ist wichtiger als Wissen, denn Wissen ist begrenzt."

          -- Albert Einstein

  *Ergebnis:*

  .. epigraph::

      "Phantasie ist wichtiger als Wissen, denn Wissen ist begrenzt."

      -- Albert Einstein

  Innerhalb einer ``epigraph``-Umgebung sind sowohl mehre Absätze als auch
  Inline-Markup (Roles) erlaubt. Die Ausgabe erfolgt eingerückt und mit reduzierter
  Zeilenlänge, um das Zitat gut erkennbar vom übrigen Text abzuheben;
  Zeilenumbrüche erfolgen automatisch.

.. ``pull-quote`` mit ``epigraph`` komplett identisch?

* ``.. line-block::``

  Die ``line-block``-Umgebung ist der ``epigraph``-Umgebung ähnlich, jedoch
  finden im Ergebnis keine automatischen Zeilenumbrüche statt. Die Zeilen
  werden stattdessen in gleicher Form ausgegeben, wie sie innerhalb der
  ``line-block``-Umgebung gesetzt werden. Dies ist insbesondere beim Zitieren
  von Gedichten und Versen nützlich:

  *Beispiel:*

  .. code-block:: rst

      .. line-block::

          "Jede Blüte will zur Frucht
          Jeder Morgen Abend werden
          Ewiges ist nicht auf Erden
          Als der Wandel, als die Flucht."

          -- Hermann Hesse (Ausschnitt aus dem Gedicht "Welkes Blatt")

  *Ergebnis:*

      .. line-block::

          "Jede Blüte will zur Frucht
          Jeder Morgen Abend werden
          Ewiges ist nicht auf Erden
          Als der Wandel, als die Flucht."

          -- Hermann Hesse (Ausschnitt aus dem Gedicht "Welkes Blatt")

  Absätze, die innerhalb einer ``line-block``-Umgebung stehen, werden nicht
  automatisch eingerückt. Ist dies gewünscht, so kann man eine Einrückung
  entweder über entsprechende CSS-Einstellungen oder über eine manuelle
  Einrückung der jeweiligen Umgebung (Leerzeichen bzw. Tabulatoren im
  Quellcode) erreichen.


* ``note``, ``hint``, ``tip``, ``warning``, ``error``, ``important``

  Mit den obigen Direktiven lassen sich Infoboxen erzeugen. Der Titel der
  Infobox leitet sich dabei aus dem Direktivennamen ab (Bemerkung, Hinweis, Tip,
  Warnung, Fehler, Wichtig).

  *Beispiel:*

  .. code-block:: rst

      .. hint::

          Hier wird ein Hinweis ausgegeben.

  *Ergebnis:*

      .. hint::

          Hier wird ein Hinweis ausgegeben.

  Neben den oben genannten Direktiven kann auch eine ``topic``-Umgebung
  genutzt werden, um eine beliebig benannte Infobox erzeugen. Dabei wird in
  der gleichen Zeile de im Anschluss an ``.. topic::`` der Name der Box
  geschrieben.

* ``math``

  Mit der ``math``-Direktive können mathematische Formeln, geschrieben als
  :ref:`LaTeX-Code <gwil:Mathematischer Formelsatz>`, als eigenständige
  zentrierte Zeilen in das Dokument eingebunden werden.

  *Beispiel:*

  .. code-block:: rst

      .. math::

          a^2 + b^2 = c^2

  *Ergebnis:*

      .. math::

          a^2 + b^2 = c^2

  Die ``math``-Direktive bietet zusätzlich die Option, der angegebenen Formel
  eine Sprungmarke ("Label") und eine automatisch vergebene Nummer zu
  vergeben. Hierzu wird eine eigene Zeile der Form ``:label: Name-des-Labels``
  unmittelbar als erste Zeile der ``math``-Direktive eingefügt (mit gleicher
  Einrückung wie die eigentliche Formel).

  *Beispiel:*

    .. code-block:: rst

      .. math::
          :label: einstein-und-pythagoras

          E \underset{Einstein}{=} m \cdot c^2
          \underset{Pythagoras}{=} m \cdot (a^2 + b^2)


  *Ergebnis:*

      .. math::
          :label: einstein-und-pythagoras

          E \underset{Einstein}{=} m \cdot c^2
          \underset{Pythagoras}{=} m \cdot (a^2 + b^2)

  Auf die Formel kann dann mittels der Referenz ``eqr:`Name-des-Labels``` an
  einer beliebigen anderen Stelle des Dokuments (derzeit jedoch nur innerhalb
  einer einzelnen Quellcode-Datei) verwiesen werden.

* ``code-block``

  Die ``code-block``-Direktive ermöglicht es, wie der Name bereits andeutet,
  Quellcode-Beispiele in das Dokument einzufügen. Dabei kann in der gleichen
  Zeile im Anschluss an ``.. code-block::`` eine Codesprache aus `dieser Liste
  <http://pygments.org/languages/>`_ ausgewählt werden, um ein
  Syntax-Highlighting zu aktivieren.

  *Beispiel:*

  .. code-block:: rst

      .. code-block:: bash
          number-lines:

          # Show the local network address
          # Result: Something like 192.168.1.105
          hostname -I | cut -d' ' -f1

  *Ergebnis:*

  .. code-block:: bash

      # Show the local network address
      # Result: Something like 192.168.1.105
      hostname -I | cut -d' ' -f1

.. :emphasize-lines: 3,5
.. :emphasize-lines: 12,15-18
.. :linenos:
.. http://sphinx-doc.org/markup/code.html

..  Alternativ zum direkten Einfügen kann mittels der Option ``:source-file:
..  Pfad`` auch der Name einer separaten Quellcode-Datei angegeben werden, deren
..  Inhalt in das Dokument eingebunden werden soll.

..
    .. literalinclude:: example.py
       .. :pyobject: Timer.start

    .. literalinclude:: example.py
       :diff: example.py.orig

Quellcode  wird üblicherweise in Maschinenschrift ausgegeben; jegliches
Inline-Markup wird dabei ignoriert. Möchte man Inline-Markup (Roles)
dennoch interpretiert haben, um beispielsweise Verlinkungen innerhalb des
Quellcodes zu setzen, kann anstelle von ``code-block`` die
``parsed-literal``-Direktive verwendet werden, die ansonsten die gleiche
Syntax aufweist.


Weitere Gestaltungsmöglichkeiten von Absätzen sind in der `Liste aller
RST-Direktiven (en.)
<http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_ aufgeführt.

.. _Aufzählungen und Beschreibungen:

Aufzählungen und Beschreibungen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In RestructuredText sind sowohl nummerierte wie auch nicht nummerierte
Aufzählungen möglich. Die Syntax hierfür ist sehr simpel:

.. code-block:: rst

    *Beispiel einer nummerierten Liste:*

    1. Dies hier ist ein Blindtext zum Testen von Textausgaben. Wer diesen Text
       liest, ist selbst schuld. Der Text gibt lediglich den Grauwert der
       Schrift an.
    2. | Dies hier ist ein Blindtext zum Testen von Textausgaben.
       | Wer diesen Text liest, ist selbst schuld.
       | Der Text gibt lediglich den Grauwert der Schrift an.

    *Beispiel einer nicht nummerierten Liste:*

    * Dies hier ist ein Blindtext zum Testen von Textausgaben. Wer diesen Text
      liest, ist selbst schuld. Der Text gibt lediglich den Grauwert der
      Schrift an.
    * | Dies hier ist ein Blindtext zum Testen von Textausgaben.
      | Wer diesen Text liest, ist selbst schuld.
      | Der Text gibt lediglich den Grauwert der Schrift an.

*Ergebnis:*

    *Beispiel einer nummerierten Liste:*

    1. Dies hier ist ein Blindtext zum Testen von Textausgaben. Wer diesen Text
       liest, ist selbst schuld. Der Text gibt lediglich den Grauwert der
       Schrift an.
    2. | Dies hier ist ein Blindtext zum Testen von Textausgaben.
       | Wer diesen Text liest, ist selbst schuld.
       | Der Text gibt lediglich den Grauwert der Schrift an.

    *Beispiel einer nicht nummerierten Liste:*

    * Dies hier ist ein Blindtext zum Testen von Textausgaben. Wer diesen Text
      liest, ist selbst schuld. Der Text gibt lediglich den Grauwert der
      Schrift an.
    * | Dies hier ist ein Blindtext zum Testen von Textausgaben.
      | Wer diesen Text liest, ist selbst schuld.
      | Der Text gibt lediglich den Grauwert der Schrift an.

Für nicht nummerierte Aufzählungen können anstelle des Zeichens ``*`` auch die
Zeichen ``-`` oder ``+`` verwendet werden; in der Ausgabe werden die
Aufzählungszeichen unabhängig davon anhand der Aufzählungstiefe ausgewählt
(innerhalb einer Aufzählung sind auch weitere Aufzählungen möglich).

Beim Erstellen von Aufzählungen muss lediglich darauf geachtet werden, dass vor
und nach der Aufzählung im Quellcode eine leere Zeile steht und die einzelnen
Einträge gleich weit eingerückt sind. Die einzelnen Einträge werden, sofern sie
nicht in eine Zeile passen, automatisch am Seitenrand umgebrochen; manuelle
Umbrücke können erzwungen werden, indem zu Beginn jeder neu zu erstellenden
Zeile ein ``|``-Zeichen eingegeben wird. Auch hierbei muss auf eine gleiche
Einrückungstiefe der Textzeilen geachtet werden.

Automatisch nummerierte Aufzählungen können mittels ``#.`` als
Aufzählungszeichen erstellt werden; in diesem Fall sind zwischen den einzelnen
Einträgen allerdings keine RestructuredText-Elemente erlaubt, die ohne
Einrückung zu Beginn der Zeile eingegeben werden müssen (beispielsweise
Sprungmarken); in diesem Fall fängt die folgende Aufzählung nämlich wieder mit
``1.`` an.

Bei Beschreibungen verwendet man das zu beschreibende Wort als
"Aufzählungszeichen". Die Syntax hierzu ist folgende:

::

    **Wort1:**
        Beschreibung zu Wort1.

    **Wort2:**
        Beschreibung zu Wort2.

*Ergebnis:*

    **Wort1:**
        Beschreibung zu Wort1.

    **Wort2:**
        Beschreibung zu Wort2.

Auch bei den Beschreibungen muss nur auf die einheitliche Einrückung des
Beschreibungs-Textes geachtet werden; der Text kann dann auch aus mehreren
Absätzen bestehen.


.. _Sprungmarken und Referenzen:

Sprungmarken und Referenzen
---------------------------

Ein sehr nützliche von Wiki-Seiten besteht darin, mittels eines klickbaren Links
auf eine andere Stelle in der Dokumentation oder auf eine externe Seite
verweisen zu können. RestructuredText bietet dazu folgende Möglichkeiten:

* Mittels ```Link-Bezeichnung <Adresse>`_`` kann ein mit einer bestimmten
  Bezeichnung versehener Link auf eine externe Seite gesetzt werden. Soll eine
  Adresse ohne eigene Bezeichnung verlinkt werden, so genügt es die Adresse ohne
  weitere Syntax anzugeben, beispielsweise ``http://www.grund-wissen.de`` für http://www.grund-wissen.de ; ein Link
  wird dabei automatisch erzeugt.

* Mittels einer eigenen Zeile der Form ``.. _Name der Sprungmarke:`` und einer
  darauf folgenden Leerzeile kann an einer beliebigen Stelle innerhalb der
  Dokumentation eine Sprungmarke (auch "Label" oder "Anker" genannt) festgelegt
  werden. Auf diese Sprungmarke kann dann von einer beliebigen anderen Stelle im
  Dokument aus mittels ``:ref:`Link-Bezeichnung <Name der Sprungmarke>```
  verwiesen werden.

  Diese Methode funktioniert auch, wenn sich die Sprungmarke und die Referenz
  in verschiedenen Dateien des Quelltextes einer Dokumentation befinden.

* Mittels der "Intersphinx"-Erweiterung, die beim Sphinx-Quickstart ausgewählt
  werden kann [#]_, ist es möglich, auch auf Sprungmarken anderer
  Sphinx-Projekte zu verweisen. Hierzu muss die Konfigurationsdatei ``conf.py``
  um einen oder mehrere Einträge mit folgender Form ergänzt werden:

  .. code-block:: python

        intersphinx_mapping = {
            'sphinx': ('http://sphinx-doc.org', None),
            'gw': ('http://grund-wissen.de', None)
        }

  Damit kann beispielsweise mittels ``:ref:`Inhaltsverzeichnis der
  Sphinx-Dokumentation <sphinx:contents>``` ein Link auf das
  :ref:`Inhaltsverzeichnis der Sphinx-Dokumentation <sphinx:contents>` gesetzt
  werden, das eine Sprungmarke namens ``contents`` enthält (dies zeigt ein Blick
  in den Quelltext der Seite, der üblicherweise in der Seitenleiste verlinkt
  ist). Führt man den Mauszeiger über einen solchen Link, so werden der Name und
  die Versionsnummer der jeweiligen Dokumentation eingeblendet.


.. _Fußnoten, Zitierungen und Index-Einträge:

Fußnoten, Zitierungen und Index-Einträge
----------------------------------------

In RestructuredText gibt es die Möglichkeit, ergänzende Anmerkungen als
Fußnoten aus dem normalen Text "auszulagern". Hierzu wird im Haupttext eine
Marke der Form ``[#]_`` oder ``[#Name]_`` gesetzt, d.h. ein Rautenzeichen in
eckigen Klammern, gefolgt von einem Unterstrich. [#]_ Optional kann jeder Marke einer
Fußnote im Anschluss an die Nummer oder das Rautensymbol (Autonummerierung) noch
ein Name hinzugefügt werden, um im Quelltext die Zuordnung der Fußnoten-Marke
zur Fußnote zu erleichtern.

An einer späteren Stelle innerhalb der gleichen Datei, meist am Ende, wird der
Inhalt der jeweiligen Fußnote dann absatzweise mittels ``.. [#] Inhalt``
beziehungsweise ``.. [#Name] Inhalt`` angegeben, wobei ``[#Name]`` der Marke im
Haupttext entsprechen muss.

*Beispiel:*

.. code-block:: rst

    Etwas Text. [#FN1]_

    Weiterer Text.

    ...


    .. [#FN1] Eine Anmerkung als Fußnote.

*Ergebnis:*

.. raw:: html

    <div class="highlight"><pre>
    <p>Etwas Text.<a class="footnote-reference" href="#fn1" id="id6">[1]</a></p>
    <p>Weiterer Text.</p>
    <p>...</p>
    <table class="docutils footnote" frame="void" id="fn1" rules="none">
    <colgroup><col class="label" /><col /></colgroup>
    <tbody valign="top">
    <tr><td class="label"><a class="fn-backref" href="#id6">[1]</a></td><td>Eine Anmerkung als Fußnote.</td></tr>
    </tbody>
    </table>
    </pre></div>

Erstreckt sich der Inhalt einer Fußnote über mehrere Zeilen, so muss jede Zeile
nach der ersten um mindestens ein Leerzeichen eingerückt werden (üblicherweise
werden Folgezeilen eine Tabulatorbreite weit eingerückt, um eine bessere
Lesbarkeit zu erzielen).


.. _Zitierungen und Literaturverzeichnis:

.. rubric:: Zitierungen und Literaturverzeichnis

Innerhalb einer Dokumentation sind auch Verweise auf literarische Werke anderer
Autoren möglich. Für jedes zitierte Werk wird dabei ein Kurzname vergeben,
häufig in der Form ``AutorJahr``. Im Haupttext (oder in einer Fußzeile) kann
auf diese Weise mittels ``[Kurzname]_`` auf eine genauere Umschreibung der
Literaturquelle verwiesen werden, die einmalig an einer beliebigen Stelle der
Dokumentation mittels eines Eintrags der Form ``.. [Kurzname] Informationen``
erfolgt. [#]_

In der HTML-Version werden alle Literatur-Einträge an genau der Stelle
eingefügt, an der sie gesetzt werden. Insofern empfiehlt sich eine eigene Datei
namens ``quellen.rst`` (oder ähnlich), in der die Literaturhinweise und
Quellenangaben gesammelt aufgelistet sind. In der LaTeX-Version wird am Ende des
Dokuments automatisch ein Literaturverzeichnis angelegt.


.. _Index-Einträge:

.. rubric:: Index-Einträge

Innerhalb der Dokumentation können an beliebiger Stelle mittels folgender
Syntax Einträge für ein Stichwortverzeichnis festgelegt werden:

.. code-block:: rst

    .. index:: Bezeichnung

In der HTML-Version wird ein Link auf die Index-Seite üblicherweise auf der
rechten Seite am oberen und unteren Seitenrand eingeblendet. In der
LaTeX-Version wird das Stichwortverzeichnis auf den letzten Seiten der
Dokumentation abgedruckt. Eine Verlinkung mit den entsprechenden Textstellen (in
der Druckversion mitsamt Angabe der jeweiligen Seitennummer) erfolgt
automatisch.

* Um mehrere Index-Einträge zur gleichen Textstelle zu erreichen, können die
  Bezeichnungen der gewünschten Einträge, durch Kommas voneinander getrennt, in
  einer einzigen Zeile aufgelistet werden:

  .. code-block:: rst

      .. index:: Eintrag1, Eintrag2

* Werden zwei Einträge durch einen Strichpunkt getrennt, so wird der zweite
  Eintrag als "Unterkategorie" des ersten im Stichwortverzeichnis angezeigt:

  .. code-block:: rst

      .. index:: Eintrag; Unterkategorie

Eine ausführliche Beschreibung findet sich in der `Sphinx-Dokumentaion
<http://sphinx-doc.org/markup/misc.html#index-generating-markup>`_.

..  This is a normal reST :index:`paragraph` that contains several
..  :index:`index entries <pair: index; entry>`.


.. _Bilder und Tabellen:

Bilder und Tabellen
-------------------

Bilder können in Restructured-Text entweder mittels einer ``image``- oder
mittels einer ``figure``-Direktive eingebunden werden; letztere muss verwendet
werden, wenn die Abbildung eine Bildunterschrift ("Caption") erhalten soll.

Die Syntax für den Einbau eines Bildes sieht etwa folgendermaßen aus:

.. code-block:: rst

    .. figure:: ../pics/no-littering.png
        :name: fig-beispiel-bild
        :alt:  fig-beispiel-bild
        :align: center
        :width: 20%

        Beispiel-Bild "No littering" ohne weitere Beschreibung.

        .. only:: html

            :download:`SVG: Beispiel-Bild ("No littering") <../pics/no-littering.svg>`

*Ergebnis:*

.. figure:: ../pics/no-littering.png
    :name: fig-beispiel-bild
    :alt:  fig-beispiel-bild
    :align: center
    :width: 20%

    Beispiel-Bild "No littering" ohne weitere Beschreibung.

    .. only:: html

        :download:`SVG: Beispiel-Bild ("No littering") <../pics/no-littering.svg>`

Bei Verwendung der ``figure``-Direktive wird zunächst der Pfad der
einzubindenden Graphik angegeben. Die ``:name:``-Attribut angegebene Bezeichnung
kann in Referenzen als Label aufgegriffen werden; die als ``:alt:``-Attribut
angegebene Bezeichnung wird im Webbrowser während des Ladens der Graphik oder im
Fall einer nicht auffindbaren Graphik-Datei angezeigt.

Über das Attribut ``:align:`` wird die Ausrichtung der Graphik am Text als
``left``, ``center`` oder ``right`` festgelegt. Die Angabe der Breite kann über
das ``:width:``-Attribut entweder als feste Längeneinheit (beispielsweise ``4.2
cm``) oder relativ zur Textbreite als Prozentangabe erfolgen. Als Alternative
zur Angabe einer Breite kann die Größe einer Abbildung auch mittels einer
``:height:``- oder ``scale``-Angabe (in Prozent der Original-Bildgröße)
festgelegt werden. Bei der Angabe einer Bildunterschrift innerhalb einer
``figure``-Umgebung muss wiederum auf die richtige Einrücktiefe geachtet werden.

Bei der ``image``-Direktive können, abgesehen von der Bildunterschrift,
ebenfalls die oben genannten Attribute angegeben werden; dafür kann (nur) bei
der ``image``-Direktive als zusätzliches Argument mittels ``:target:`` eine
Zieladresse angeegben werden, auf die beim Anklicken des Bildes verlinkt wird.

Zur Eingabe von Tabellen gibt es in RestructuredText ebenfalls mehrere
Möglichkeiten:

* Bei einer "Gitter-Tabelle" wird die tabellarische Anordnung bereits im
  Quellcode angedeutet:

  .. code-block:: rst

      +------------------+---------------+---------------+
      | Art der Einträge | Eigenschaft 1 | Eigenschaft 2 |
      +==================+===============+===============+
      | Gegenstand 1     | eckig         | rot           |
      +------------------+---------------+---------------+
      | Gegenstand 2     | rund          | blau          |
      +------------------+---------------+---------------+

  *Ergebnis:*

    +------------------+----------------+----------------+
    | Art der Einträge | Eigenschaft 1  | Eigenschaft 2  |
    +==================+================+================+
    | Gegenstand 1     | eckig          | rot            |
    +------------------+----------------+----------------+
    | Gegenstand 2     | rund           | blau           |
    +------------------+----------------+----------------+

  Werden beim ersten "Querstrich" in der Tabelle anstelle der ``=``-Zeichen
  ``-``-Zeichen gesetzt, so wird die erste Zeile in normaler Schrift (nicht
  fettgedruckt) ausgegeben.

  Tabellen gemäß dieser Syntax sind mühsam, sofern der Texteditor nicht ein
  geeignetes Feature dafür mitbringt (für den Editor :ref:`Vim <Vim>` gibt es
  hierfür beispielsweise das :ref:`Table-Mode <Table-Mode>`-Plugin). Der Vorteil
  solcher Tabellen liegt vor allem in der angenehmen Lesbarkeit im Quellcode.

  Nicht geeignet sind Grid-Tabellen, wenn auch Links oder mathematische Formeln
  in der Tabelle vorkommen sollen. Diese machen im Quellcode mehr Buchstaben aus
  als in der Ausgabe, so dass die Spalten dadurch breiter als nötig gedruckt
  werden. Hierfür sollte eher "List-Tables" verwendet werden.

* Bei "List Tables" werden die Einträge einer Tabelle in Form einer
  verschachtelten Aufzählung angegeben. Die Syntax hierzu sieht etwa
  folgendermaßen aus:

  .. code-block:: rst

      .. list-table::
          :name: tab-beispieltabelle
          :widths: 50 50 50
          :header-rows: 0

          * - Art der Einträge
            - Eigenschaft 1
            - Eigenschaft 2
          * - Gegenstand 1
            - eckig
            - rot
          * - Gegenstand 2
            - rund
            - blau

  *Ergebnis:*

    .. list-table::
        :name: tab-beispieltabelle
        :widths: 50 50 50
        :header-rows: 0

        * - Art der Einträge
          - Eigenschaft 1
          - Eigenschaft 2
        * - Gegenstand 1
          - eckig
          - rot
        * - Gegenstand 2
          - rund
          - blau

  Soll die erste Zeile der Tabelle fett gedruckt ausgegeben werden, muss das
  Attribut ``:header-rows`` auf ``1`` gesetzt werden.

  Der Vorteil von List-Tables liegt darin, dass in den einzelnen Einträgen
  beliebige Inline-Direktiven verwendet werden können (Links, Formeln, usw).
  Ebenso kann die "Gewichtung" der einzelnen Spaltenbreiten durch die Angabe der
  ``:widths:``-Werte manuell angepasst werden. Im obigen Beispiel werden die
  drei Spalten der Tabelle in einem Breitenverhältnis von ``50:50:50``, also
  mit gleicher Breite ausgegeben.

  Wird in der gleichen Zeile direkt hinter ``.. list-table::`` ein Titel
  angegeben, so wird dieser als Überschrift über die Tabelle gedruckt.

* Mit einer "CSV-Table" kann der Inhalt der Tabelle durch "Comma Seperated
  Values" erfolgen. Diese Einträgte können wahlweise im Block der
  Listen-Direktive oder in einer separaten ``.csv``-Datei angegeben werden.
  Das obige Beispiel kann damit etwa folgendermaßen aussehen:

  .. code-block:: rst

      .. csv-table::
          :widths: 50 50 50

          Art der Einträge , Eigenschaft 1 , Eigenschaft 2
          Gegenstand 1 , eckig , rot
          Gegenstand 2 , rund , blau


  *Ergebnis:*

      .. csv-table::
          :widths: 50 50 50

          Art der Einträge , Eigenschaft 1 , Eigenschaft 2
          Gegenstand 1 , eckig , rot
          Gegenstand 2 , rund , blau

  Soll anstelle von ``,`` ein anderes Zeichen zur Trennung der einzelnen
  Einträge verwendet werden, so kann dieses mittels des ``:delim:``-Attributs
  angegeben werden.

  Anstelle einer direkten Eingabe der Tabelle kann auch der Inhalt einer
  externen ``.csv``-Datei verwendet werden; hierzu muss entweder ein Pfad als
  ``:file:``-Attribut oder eine Web-Adresse als ``:url:``-Attribut angegeben
  werden.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#DIR] Eine "Direktive" ist ein Syntax-Element, das Auswirkung auf einen ganzen
    Absatz hat, d.h. auf einen Bereich, der durch zwei leere Zeilen begrenzt
    wird. Im kürzesten Fall, wie bei der ``.. rubric::``-Direktive, besteht der
    Absatz aus einer einzelnen Zeile, die unmittelbar hinter dem Namen der
    Direktive angegeben wird.

    Eine Direktive wird allgemein durch zwei Punkte und ein Leerzeichen zu
    Beginn einer Zeile eingeleitet, gefolgt vom Namen der Direktive, zwei
    Doppelpunkten und einem Leerzeichen: ``.. name::`` . Vor und nach einer
    Direktive muss (mindestens) eine Leerzeile eingefügt werden.

    Je nach Art der Direktive kann hinter ihrem Namen eine weitere Bezeichnung
    und/oder eine beliebige Anzahl von Absätzen folgen. Um den Wirkungsbereich
    der Direktive kenntlich zu machen, werden die Absätze dabei eine
    Tabulatorbreite weit eingerückt (üblicherweise 4 Leerzeichen).

    Siehe auch `Liste aller RST-Direktiven (en.)
    <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_.

.. [#ROL] Eine "Role" ist ein Syntax-Element, das Auswirkung auf eine Textstelle
    innerhalb eines Absatzes hat, d.h. auf einen Bereich, der durch zwei Leerzeichen
    begrenzt wird ("Inline-Markup").

    Eine Role hat im allgemeinen folgende Struktur: ``:name:`Inhalt```. Die
    einzigen Ausnahmen bilden die drei oben genannten (wohl am häufigsten
    auftretenden) Roles für kursiven und fettgedruckten Text sowie Text in
    Maschinenschrift. Sie stellen praktisch nutzbare Abkürzungen für
    ``:emphasis:`Text```, ``:strong:`Text``` sowie ``:literal:`Text``` dar, um
    Tippbarbeit zu sparen und den Quelltext lesbarer zu gestalten.

    Siehe auch `Liste aller RST-Roles (en.)
    <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`_.

.. [#] Die Intersphinx-Erweiterung lässt sich ebenso nutzen, wenn in der
    Konfigurationsdatei ``conf.py`` die ``extension``-Liste um den Eintrag
    ``'sphinx.ext.intersphinx'`` ergänzt wird.

.. [#] Optional können die Nummern der Fußnoten auch in der Art ``[01]_``,
    ``[02]_`` bzw. ``[01Name]_``, ``[02Name]_`` usw. selbst vergeben werden.
    Davon ist allerdings abzuraten, denn sollte zu einem späteren Zeitpunkt an
    einer Stelle mitten im Text eine weitere Fußnote eingefügt werden, so
    müssen die Nummern aller folgenden Fußnoten manuell angepasst werden. Durch
    automatisch nummerierte Fußnoten bleibt einem diese Arbeit sicher erspart.

    *Tip:* Durch die Option ``trim_footnote_reference_space = True`` in der
    ``conf.py`` wird ein mögliches Leerzeichen vor Fußnoten, wie in
    deutschsprachiger Literatur üblich, ignoriert.

.. [#] Die Syntax von Zitierungen ähnelt somit der Syntax von Fußnoten, mit dem
    Unterschied, dass innerhalb der eckigen Klammern keine Nummer
    beziehungsweise kein einleitendes Raute-Zeichen auftritt.

    Jede Literaturangabe sollte folgende Informationen beinhalten: Name des
    Autors bzw. der Autoren, Titel des Werks, (gegebenenfalls) Name des Verlags,
    Erscheinungsjahr.


.. Einrückungen

..  http://www.siafoo.net/help/reST


.. re 	            Revised, revisited, based on 're' module. *gg*
.. Structured 	    Structure-enhanced text, structuredtext.
.. Text 	        Well it is, isn't it?


