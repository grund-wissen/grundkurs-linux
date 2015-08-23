.. _Konfigurationsdatei:

Konfigurationsdatei
===================

In der Konfigurationsdatei *~/.vimrc* können zahlreiche Optionen wie
z.B. Zeilennummerierungen, Markierungen von Suchergebnissen, automatische
Backups etc. an- oder ausgeschaltet werden. Gleichzeitig können
individuelle Tastenkombinationen für beliebige Funktionen oder
Funktionsketten festgelegt werden.

Meine persönliche Konfigurationsdatei sieht etwa so aus:

:download:`Beispieldatei ~/.vimrc <vimrc.txt>`


.. .. _Einstellungen:
.. .. _Settings:

.. Einstellungen (Settings)
.. ------------------------

.. TODO set optionsname, set nooptionsname

.. Da mir persönlich die ``Esc``-Taste zu weit entfernt liegt, habe ich mir in
.. der :ref:`Konfigurationsdatei` die in normalem Text selten
.. vorkommende Tastenkombination ``jk`` mit der gleichen Funktion belegt.. :-]
.. Drückt man die Tastenkombination im Normalmodus, so ändert sich dadurch
.. die Position des Cursors nicht.

.. gute vorlage: http://dougblack.io/words/a-good-vimrc.html

.. Anzeigen, wo Option gesetzt wurde:

.. :verbose set iskeyword?

.. _Mappings:

Mappings
--------

Mappings ermöglichen es, für beliebige Befehlskombinationen selbst gewählte
Tastenkombinationen zu vergeben.

Je nach Modus, in welchem die Mappings gelten sollen, wird zwischen ``map,
imap,`` und ``vmap`` unterschieden:

.. list-table::
    :widths: 30 40
    :header-rows: 0

    * - ``nmap Kürzel Befehl``
      - Kürzel für den Normal-Modus
    * - ``cmap Kürzel Befehl``
      - Kürzel für den Kommando-Modus
    * - ``imap Kürzel Befehl``
      - Kürzel für den Einfüge-Modus
    * - ``vmap Kürzel Befehl``
      - Kürzel für den Visuell-Modus

Mappings können auch über den Kommandozeilen-Modus gesetzt werden, bleiben so
allerdings nur bis zum Beenden von Vim gespeichert. Für häufig genutzte
Tastenkombinationen empfiehlt es sich daher, diese in der Konfigurationsdatei
festzuhalten.

**Tipp**: Eine Übersicht darüber, welche Mappings vergeben sind, kann man mit
``:map`` bekommen. Um die Auswahl einzuschränken, kann dahinter der Beginn eines
Mappings stehen - z.B. listet ``:map \b`` alle Mappings auf, die mit ``\b``
beginnen. In entsprechender Weise zeit ``:imap \b`` alle Mappings im
Einfügemodus an, die mit ``\b`` beginnen.

Folgende Sonderzeichen werden in Mappings häufig verwendet, wobei die Groß- und
Kleinschreibung keine Rolle spielt:

.. list-table::
    :widths: 35 50
    :header-rows: 0

    * - ``<Leader>``
      - ``\`` (Backslash)
    * - ``<Return>`` oder ``<CR>``
      - ``Enter``-Taste (Carriage Return)
    * - ``<Esc>``
      - ``Escape``-Taste
    * - ``<Bar>``
      - ``|`` (Pipe-Symbol)
    * - ``<Space>``
      - Leerzeichen bzw. Leertaste
    * - ``<Tab>``
      - Tabulator
    * - ``<C-A>``
      - ``Ctrl A``

.. _Rechtschreibprüfung:

Rechtschreibprüfung
-------------------

Seit der Version 7.0 bietet Vim von sich aus eine integrierte
Rechtschreibprüfung. Sie wird allgemein durch ein Eingabe folgender Art in der
Vim-Kommandozeile aktiviert:

.. code-block:: vim

	:set spell spelllang=en_us

Bei aktiver Rechtschreibprüfung werden Wörter als "falsch" angesehen, wenn es
dazu keinen Eintrag in der entsprechenden Spell-File gibt. Als Name der
Sprache wird allgemein die Form ``language_region`` verwendet, da sich
beispielsweise die in Großbritannien übliche Rechtschreibung ``en_en`` von der
amerikanischen Rechtschreibung ``en_us`` unterscheidet. Für die deutschsprachige
Rechtschreibung gibt es neben ``de_de``, ``de_at`` (Österreich) und ``de_ch``
(Schweiz) auch ``de_19`` und ``de_20`` für die alte beziehungsweise neue
deutsche Rechtschreibung.

Wird eine Sprachdatei bei Aktivierung mittels ``:set spell`` nicht gefunden, so
wird automatisch ein vorinstalliertes Plugin namens ``spellfile.vim`` gestartet,
das es dem Benutzer anbietet, die entsprechende Sprachdatei automatisch
herunterzuladen und zu aktivieren. Falsch geschriebene Wörter werden dann (je
nach Farbschema) durch eine rote Hintergrundfarbe gekennzeichnet.

Mit ``:set nospell`` kann die Rechtschreibprüfung wieder abgeschaltet werden.
Noch einfacher wird das Aktivieren und Deaktivieren der Rechtschreibung durch
die Aufnahme der folgenden Funktion (nach einer Vorlage aus dem `Vim-Wiki
<http://vim.wikia.com/wiki/Toggle_spellcheck_with_function_keys>`_) in der
Konfigurationsdatei ``~/.vimrc``:

.. code-block:: vim

    " Rechtschreibprüfung mit <F8> an- und ausschalten:
    let g:myLang = 1
    let g:myLangList = ['nospell', 'de_20,en_us']
    function! MySpellLang()
      if g:myLang == 0 | setlocal nospell | endif
      if g:myLang == 1 | let &l:spelllang = g:myLangList[g:myLang] | setlocal spell | endif
      echomsg ''
      let g:myLang = g:myLang + 1
      if g:myLang >= len(g:myLangList) | let g:myLang = 0 | endif
    endfunction
    nmap <F8> :call MySpellLang()<CR>
    imap <F8> <C-o>:call MySpellLang()<CR>"

Mit dieser Funktion kann durch Drücken von ``<F8>`` die Rechtschreibprüfung an-
und ausgeschaltet werden. Durch die Auswahl ``'de_20,en_us'`` an Sprachdateien
sind sowohl die neue deutsche als auch die US-amerikanische Rechtschreibung
aktiv; ein Wort wird somit nur dann als "falsch" durch ein Highlighting
hervorgehoben, wenn es in keiner der beiden Sprachdateien vorkommt.

Bei aktiver Rechtschreibprüfung können unter anderem die folgenden
Tastenkombinationen verwendet werden:

.. list-table::
    :widths: 10 50
    :header-rows: 0

    * - ``]s``
      - Gehe zum nächsten falschen Wort
    * - ``[s``
      - Gehe zum vorherigen falschen Wort
    * - ``zg``
      - Füge das Wort unter dem Cursor dem aktuellen Wörterbuch hinzu (Variable:
        ``spellfile``)
    * - ``zG``
      - Speichere das Wort unter dem Cursor in einer internen Wortliste; diese
        wird nach dem Schließen von Vim gelöscht
    * - ``zw``
      - Speichere das Wort unter dem Cursor als "falsch" in der aktuellen
        Wörterbuchdatei (Variable: ``spellfile``)
    * - ``zW``
      - Speichere das Wort unter dem Cursor als "falsch" in der internen Wortliste
    * - ``zug``, ``zuw``, ``zuG``, ``zuW``
      - Lösche das Wort unter dem Cursor aus der entsprechenden Liste

Eine ausführliche Hilfe erhält man mittels ``:h spell.txt``.

..
    Letzte Fehlermeldung(en) anzeigen: :messages

