.. _Visueller Modus:

Visueller Modus
---------------

Im visuellen Modus kann Text mittels :ref:`Bewegungsanweisungen
<Bewegungsanweisungen>` markiert werden, um ihn zu kopieren oder zu bearbeiten.

Aus dem Normal-Modus gelangt man wie folgt in den visuellen Modus:

.. list-table::
    :name: tab-visueller-modus
    :widths: 10 30 20

    * - ``v``
      - "normaler" visueller Modus
      -
    * - ``V``
      - zeilenweise visueller Modus
      - (*Visual Line*)
    * - ``Ctrl v``
      - spaltenweise visueller Modus
      - (*Visual Block*)

Im normalen visuellen Modus wird der gesamte Textbereich von der aktuellen
Position aus bis zu der Stelle, zu der man sich hinbewegt, markiert. Mit ``o``
("other") kann man an das andere Ende des visuell markierten Bereichs gelangen.

Im zeilenweise-visuellen Modus können mit den Navigationsanweisungen ``{`` und
``}`` oder mit Hilfe von Markierungen leicht ganze Paragraphen oder
Textabschnitte kopiert, verschoben oder anderweitig bearbeitet werden. Der
blockweise-visuelle Modus bietet speziell mit dem Vim-Plugin Align eine elegante
Möglichkeit zur Bearbeitung von Spalten einer Tabelle.

**Tipp:** Um Zeilen mit verschieden langen Inhalten am Ende mit Leerzeichen
aufzufüllen, um beispielsweise dahinter weiteren Text als eine neue Spalte
einfügen zu können, können jeweils die ersten Zeichen der Zeilen im visuellen
Blockmodus markiert werden und anschließend ``$`` gedrückt werden. Es wird
dadurch der gesamte Text markiert. Gibt man dann ``A <Leertaste>`` ein, so wird
am Ende der längsten Zeile ein Leerzeichen angefügt und alle kürzeren Zeilen bis
zur gleichen Breite mit Leerzeichen aufgefüllt.

Weiterhin gibt es im visuellen Modus Mappings für folgende Auswahl-Kriterien,
die wahlweise mit ``i`` ("inner") ohne umgebende Whitespaces oder mit ``a``
("outer") mitsamt umgebenden Whitespaces eingeleitet werden können:

.. list-table::
    :name: tab-auswahl-kriterien
    :widths: 15 60

    * - ``w``
      - Ein einzelnes Wort (siehe Option ``iskeyword``)
    * - ``s``
      - Ein einzelner Satz
    * - ``p``
      - Ein einzelner Paragraph (Absatz)
    * - ``t``
      - Ein HTML/XML-Tag
    * - ``"``, ``'``, `````
      - Durch Anführungszeichen begrenzter Text
    * - ``{``, ``[``, ``(``, ``<``
      - Durch Klammern begrenzter Text

Gibt man also beispielsweise im visuellen Modus ``ip`` ein, so wird der aktuelle
Absatz (ohne vorangehende und darauf folgende Leerzeile) ausgewählt; ebenso kann
Text innerhalb zwei runder Klammern mit ``a(`` inklusive der Klammern ausgewählt
werden, wenn sich der Cursor innerhalb der Klammern befindet.

**Tip**: Jede Bearbeitungsanweisung, die für gewöhnlich eine darauffolgende
Bewegungs- oder Auswahlanweisung erwartet, kann auch direkt einen markierten
Bereich angewandt werden.


