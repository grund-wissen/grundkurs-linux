
.. _Einfügemodus:

Einfügemodus
------------

Der Einfügemodus dient -- wie der Name schon sagt -- zum Einfügen von Text in
die aktuelle Datei. Hier gleicht Vim einem "normalen" Editor: Alle Buchstaben,
Zahlen, etc. erscheinen nach der Eingabe an der aktuellen Position auf dem
Bildschirm.

Ausgehend vom Normalmodus gelangt man in den Einfügemodus durch Drücken einer
der folgenden Tasten:

.. list-table::
    :widths: 10 60 30
    :header-rows: 0

    * - ``i``
      - Text einfügen vor  der momentanen Position
      - (*insert*)
    * - ``I``
      - Text einfügen zu Beginn der momentanen Zeile
      -
    * - ``a``
      - Text einfügen nach der momentanen  Position
      - (*append*)
    * - ``A``
      - Text einfügen am Ende der  momentanen Zeile
      -
    * - ``o``
      - Text einfügen unter der aktuellen Zeile
      - (*open a new line*)
    * - ``O``
      - Text einfügen über der aktuellen  Zeile
      -


Auch mit ``s, S, c, C, r, R`` gelangt man in den Einfügemodus. Hierbei wird
jedoch bestehender Text ersetzt.

Gibt man beispielsweise ``10i`` gefolgt von etwas Text ein, so wird nach Beenden
der Eingabe mit ``Esc`` das 10-fache des eigegebenen Textes eingefügt.

Der Einfügemodus bietet folgende hilfreiche Tastenkombinationen:

.. list-table::
    :widths: 20 60 20
    :header-rows: 0

    * - ``Ctrl n`` bzw. ``Ctrl p``
      - Vervollständigung des aktuellen Wortes anhand eines bereits vorkommenden
        Wortes
      - (*next* bzw. *previous word*)
    * - ``Ctrl x  Ctrl l``
      - Vervollständigung der aktuellen Zeile anhand einer bereits vorkommenden
        Zeile
      - (*line-completion*)
    * - ``Ctrl x  Ctrl f``
      - Vervollständigung der Eingabe von Dateinamen und Pfaden
      - (*file-completion*)


