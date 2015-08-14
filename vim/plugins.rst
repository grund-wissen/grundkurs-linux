.. _Vim-Plugins:

Plugins
=======

Vim kann durch so genannte "Plugins" erweitert werden. Diese können von der
`Projektseite <http://www.vim.org>`_ oder von `Github <https://github.com>`_
heruntergeladen werden.

Unterschieden wird zwischen allgemeinen Plugins, die nach ihrer Installation
automatisch geladen werden, und "Filetype"-Plugins, die nur geladen werden, wenn
eine Datei des entsprechenden Typs geladen wird. Gewöhnlich erkennt Vim den
Dateityp anhand der Endung, z.B. ``datei.py`` als eine
``Python``-Quellcode-Datei. Der Dateityp einer geöffneten Datei kann allerdings
auch manuell mittels ``set filetype Typ`` geändert werden, wobei die
entsprechenden Filetype-Plugins nachgeladen werden.

.. index:: Vundle (Vim-Plugin)
.. _Vundle:
.. _Vim-Plugins installieren:

Vundle: Plugins installieren und verwalten
------------------------------------------

Das `Vundle-Plugin <http://www.vim.org/scripts/script.php?script_id=3458>`_
bietet eine sehr empfehlenswerte Methode, eine individuelle Auswahl an Plugins
zu installieren und zu verwalten. Um dieses Plugin zu verwenden, wird zunächst
im Ordner ``~/.vim`` ein neues Unterverzeichnis namens ``bundle`` angelegt:

.. code-block:: bash

    mkdir ~/.vim/bundle/

Anschließend gibt man folgende Zeile ein:

.. code-block:: bash

    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Damit ist das Vundle-Plugin installiert. Die Benutzung des Plugins funktioniert
mittels der Konfigurationsdatei ``~/.vimrc``. Hier wird an beliebiger Stelle
folgendes eingegeben:

.. code-block:: vim

    set nocompatible

    " Set the runtime path and initialize Vundle:
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()

    " Let Vundle manage itself (required)
    Plugin 'gmarik/Vundle.vim'

    " Install and use the following Plugins:
    Plugin 'vim-scripts/sudo.vim'
    Plugin 'scrooloose/nerdcommenter'
    Plugin 'SirVer/ultisnips'

    " ...

    filetype on                         " Filetype-Erkennung aktivieren
    filetype indent on                  " Syntax-Einrückungen je nach Filetype
    filetype plugin on                  " Filetype-Plugins erlauben

Hierbei muss lediglich beachtet werden, dass die ``filetype on``-Anweisungen
erst **nach** den für Vundle relevanten Zeilen eingegeben werden.

Um ein Plugin mittels Vundle zu installieren, genügt es den GitHub-Namen des
Plugins mittels ``Plugin 'repository/plugin-name'`` in die Vundle-Liste
aufzunehmen. Anschließend wird Vim gestartet und ``:PluginInstall`` eingegeben.
Alle noch nicht installierten Plugins werden damit automatisch als eigene
Verzeichnisse in das ``~/.vim/bundle``-Verzeichnis installiert.

Mit Vundle ist auch eine weitere Verwaltung der Plugins möglich:

* Um ein Plugin zu deaktivieren, genügt es die entsprechende ``Plugin``-Zeile in
  der ``~/.vimrc`` auszukommentieren und Vim neu zu starten; es werden nämlich
  bei Verwendung von Vundle nur diejenigen Plugins von Vim geladen, die in der
  Plugin-Liste enthalten sind.

* Soll ein Plugin entfernt werden, so wird es ebenfalls zunächst auskommentiert,
  Vim anschließend neu gestartet und ``:PluginClean`` eingegeben.

.. _vundle-pinned:

* Um alle Plugins auf einmal zu aktualisieren, kann man ``:PluginInstall!``
  eingeben. Vundle prüft damit automatisch, ob auf GitHub eine neuere Version
  des Plugins existiert und installiert diese gegebenenfalls nach.

  Soll ein Plugin bei einer Aktualisierung mittels ``:PluginInstall!`` **nicht**
  berücksichtigt werden, so kann bei diesem als zusätzliche Option ``{"pinned, 1}``
  angegeben werden, beispielsweise:

  .. code-block:: vim

      Plugin 'honza/vim-snippets', {'pinned': 1}

  Wird ein Plugin auf diese Weise eingebunden, so werden beispielsweise eigene
  Änderungen durch einen Update nicht überschrieben.

Nahezu jedes Vim-Plugin wird inzwischen entweder vom jeweiligen Entwickler oder
innerhalb des ``vim-scripts``-Repository auf GitHub gelistet. Bei den folgenden
Beschreibungen der einzelnen Plugins sind daher neben den Beschreibungen auf der
Vim-Projektseite stets auch die entsprechenden GitHub-Repositories verlinkt.


.. _Hilfreiche Erweiterungen:

Hilfreiche Erweiterungen
------------------------

.. TODO a.vim
.. TODO abolish
.. TODO ag

.. https://github.com/rking/ag.vim
.. https://github.com/ggreer/the_silver_searcher

.. index:: Align (Vim-Plugin)
.. _Align:

Align
^^^^^

Das `Align-Plugin <http://www.vim.org/scripts/script.php?script_id=294>`_ stellt
eine gleichnamige Funktion bereit, mittels derer man visuell markierte Bereiche
zu einer übersichtlichen Tabelle ausrichten kann.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/jezcope/vim-align

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
      Repository installiert werden:
    | https://github.com/jezcope/vim-align

Als Anwendungsbeispiel sei in einer Textdatei folgende Tabelle enthalten::

    # Vorher:
    a ; b ; c ; d ; e;
    ab; bc; cd; de; ef;
    abcd ; bcde ; cdef ; defg ; efgh;

Nach einer visuellen Markierung des Textes und Eingabe von ``:Align ;`` sieht
die Datei so aus::

    # Nachher:
    a    ; b    ; c    ; d    ; e    ;
    ab   ; bc   ; cd   ; de   ; ef   ;
    abcd ; bcde ; cdef ; defg ; efgh ;

Die ``:Align``-Funktion akzeptiert jedes beliebige Trennzeichen und kann
entweder global oder mittels ``:'<,'>Align`` auf den aktuell markierten Bereich
angewendet werden. Die Bearbeitung von tabellarischem Text wird so wesentlich
erleichtert. :-)

.. Besser: Easy Align?
.. http://www.vim.org/scripts/script.php?script_id=4520


.. index:: Buffer-Explorer (Vim-Plugin)
.. _Buffer-Explorer:

Buffer-Explorer
^^^^^^^^^^^^^^^

Das `BufferExplorer Plugin
<http://www.vim.org/scripts/script.php?script_id=42>`_ bietet -- ähnlich wie
``:ls`` -- eine Übersicht über die aktuell geöffneten Buffer. Um einen
bestimmten Buffer in dieser Ansicht auszuwählen, muss man nur mit ``j``, ``k``
oder ähnlichen Bewegungsanweisungen den Cursor über den gewünschten Dateinamen zu
bewegen und ``Enter`` zu drücken.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/jlanzarotta/bufexplorer

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/jlanzarotta/bufexplorer

Um schnell auf den Buffer Explorer zugreifen zu können, empfiehlt sich ein
entsprechendes Mapping in der Konfigurationsdatei, beispielsweise:

.. code-block:: vim

	nmap gB :BufExplorer<Return>

Auf diese Weise kann der Buffer-Explorer aus dem Normalmodus heraus schnell mit
``gB`` gestartet werden. (Der Cursor befindet sich beim Start des Buffer
Explorers über der aktuellen Datei, so dass es bei einem versehentlichen Öffnen
genügt ``Enter`` zu drücken, um zurück zur Ausgangsposition zu gelangen.)

.. TODO Calendar

.. index:: CtrlP (Vim-Plugin)
.. _CtrlP:

CtrlP
^^^^^

Das `CtrlP-Plugin <http://www.vim.org/scripts/script.php?script_id=3736>`_
ermöglicht ein sehr effizientes Auswählen von Dateien, ausgehend vom
Verzeichnis, in dem Vim aufgerufen wurde; ebenso können mit CtrlP zuletzt
verwendete Dateien wieder schnell geöffnet werden.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/kien/ctrlp.vim

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/kien/ctrlp.vim

Das CtrlP-Plugin wird im Normalmodus nach der Standard-Einstellung mittels
``Control p`` gestartet; es kann hierfür jedoch auch eine andere Tastenkombination,
beispielsweise ``Ctrl g``, gewählt werden (empfehlenswert bei Verwendung des
:ref:`Yankring <Yankring>`-Plugins). Hierzu muss folgende Zeile in der
Konfigurationsdatei ``~/.vimrc`` ergänzt werden:

.. code-block:: vim

	let g:ctrlp_map = '<c-g>'

Beim Start von CtrlP erscheint ein Eingabe-Prompt, der mit ``Esc`` wieder
beendet werden kann. Möchte man mit CtrlP eine Datei im Projektverzeichnis oder
einem Unterverzeichnis öffnen, so genügt es nach Drücken von ``Control p`` eine
beliebige Anzahl von Zeichen einzugeben, die im Dateinamen der gesuchten Datei
vorkommen; es muss also nicht ein realer Dateiname eingegeben werden, sondern es
wird vielmehr eine "Fuzzy"-Suche gestartet. CtrlP listet automatisch alle
zutreffenden Dateien in einem temporären Fenster auf, in dem mittels ``Ctrl j``
und ``Ctrl k`` navigiert werden kann. Drückt man ``Enter``, so wird die
ausgewählte Datei geöffnet.

Die Fuzzy-Find-Funktion kann durch folgende Einstellungen noch weiter optimiert
werden, wenn man mittels ``sudo aptitude install ag`` auch noch die :ref:`grep
<grep>`-Alternative ``ag`` installiert und folgende Zeilen in die
Konfigurationsdatei ``~/.vimrc`` aufnimmt:

.. code-block:: vim

    let g:ctrlp_user_command = 'ag %s -l --nocolor -g ""'
    let g:ctrlp_custom_ignore = '**/_build/'
    let g:ctrlp_clear_cache_on_exit=0

Durch die Verwendung von ``ag`` können in der Datei ``~/.agignore`` mit der
gleichen Syntax wie bei :ref:`gitignore <gitignore>` Dateimuster angegeben
werden, die von der Suche ausgeschlossen werden sollen; zusätzliche Dateimuster
können in der Variablen ``ctrlp_custom_ignore`` abgelegt werden (ein doppelter
Stern bedeutet dabei, dass der folgende Ausdruck auch in einem Unterverzeichnis
vorkommen kann). Durch das Setzen der Variable ``ctrlp_clear_cache_on_exit=0``
wird verhindert, dass das Plugin bei jedem Start von Vim die zu durchsuchenden
Projektverzeichnisse neu einlesen muss.

Arbeitet man mit mehreren verschiedenen Projektverzeichnissen, kann es nützlich
sein, auch folgendes Featur von CtrlP zu aktivieren:

.. code-block:: vim

	let g:ctrlp_extensions = ['bookmarkdir']

Damit könnnen mit ``:CtrlPBookmarkDirAdd pfad`` bestimmte Pfade für die
Fuzzy-Suche hinzugefügt werden.

Nach dem Start von CtrlP kann bei Bedarf mittels ``Control f`` (oder ``Control
b``) zwischen den möglichen Suchoptionen gewechselt werden (Dateien, Buffer,
Bookmarks, zuletzt verwendete Dateien, oder alle zusammen).

.. index:: Eregex (Vim-Plugin)

.. _Eregex:

Eregex
^^^^^^

Das `Eregex-Plugin <http://www.vim.org/scripts/script.php?script_id=3282>`_
ermöglicht es, in Vim für das Suchen und Ersetzen Perl-kompatible reguläre
Ausdrücke zu verwenden.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/othree/eregex.vim

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/othree/eregex.vim

Zusätzlich sollte die Konfigurationsdatei ``~/.vimrc`` um folgende Einträge
ergänzt werden:

.. code-block:: vim

    let g:eregex_default_enable = 1
    let g:eregex_forward_delim = '/'
    let g:eregex_backward_delim = '?'
    nmap <leader>/ :call eregex#toggle()<CR>

Gibt man anschließend in einer neuen Vim-Sitzung ``/`` oder ``?`` ein, so
erscheint in der Kommandozeile automatisch ``:1M/`` oder ``:1M?``. Die
unmittelbar dahinter eingegebenen Zeichen werden als Perl-compatible reguläre
Ausdrücke (PCRE) interpretiert. Durch Eingabe von ``\/`` im Normalmodus kann
dieses Verhalten aus- beziehungsweise wieder angeschaltet werden.

Um Ersetzungen mit PCRE-Syntax vorzunehmen, kann man im Kommandozeilen-Modus
``S`` statt ``s`` verwenden:

.. code-block:: vim

    :[Bereich]S/PCRE-Syntax/Ersetzung/[Optionen]

Ebenso kann in ``global``-Anweisungen die PCRE-Syntax verwendet werden, wenn
diese mit statt ``G`` statt mit ``g`` eingeleitet werden:

.. code-block:: vim

    :[Bereich]G/PCRE-Syntax/[Anweisung]

Für das Schreiben von Vim-Scripts bietet das Plugin auch eine Hilfe: Schreibt
man in der aktuellen Datei einen regulären Ausdruck in Perl-Syntax und markiert
ihn visuell, so kann dieser mittels ``:E2v`` in einen regulären Ausdruck mit
Vim-Syntax übersetzt werden.

*Beispiel:*

.. code-block:: vim

    # Entfernen von Tabs und Leerzeichen am Zeilenende:
    # Perl-Syntax:
    :%s/\s+$//g

    # Visuell markieren, :E2v eingeben (wird ergänzt zu :'<,'>E2v)
    # Ergebnis:
    :%s/\s\+$//g

Eine gute Übersicht über reguläre Ausdrücke in Perl-Syntax findet sich
beispielsweise `hier
<http://www.troubleshooters.com/codecorn/littperl/perlreg.htm>`_.


.. index:: Minibuf-Explorer (Vim-Plugin)
.. _Minibuf-Explorer:

Minibuf-Explorer
^^^^^^^^^^^^^^^^

Das `Minibuf-Explorer-Plugin
<http://www.vim.org/scripts/script.php?script_id=159>`_ bietet in einem eigenen
kleinen Subfenster am unteren Fensterrand eine Übersicht über die aktuell
geöffneten Buffer. Angezeigt werden standardmäßig die Nummern und eine
abgekürzte Bezeichnung der Buffer. Um einen bestimmten Buffer auszuwählen, kann
man in diesem Fenster mit ``h j k l`` den gewünschten Buffer anwählen und
``Enter`` drücken. Alternativ dazu kann beispielsweise ``:b5`` zur Auswahl des
fünften Buffers oder ``:bp`` bzw. ``:bn`` zur Auswahl des vorherigen bzw.
nächsten Buffers eingegeben werden, da die Buffer-Nummern ja stets angezeigt
werden.

Durch folgende Zeilen in der ``~/.vimrc`` kann das Plugin so konfiguriert
werden, dass die Bufferleiste stets unten am Bildschirm angezeigt wird und mit
``F4`` an- und ausgeschaltet werden kann:

.. code-block:: vim

	let g:miniBufExplSplitBelow=1
	map <F4> :MBEToggle<CR>
	hi MBEVisibleActiveNormal guifg=magenta ctermfg=magenta
	hi MBEVisibleActiveChanged guifg=magenta ctermfg=magenta

Durch die ``hi``-Angaben wird der aktive Buffer in der Liste durch die Farbe
``magenta`` hervorgehoben.

Das Plugin ist auch in Verbindung mit der Option ``swapfile`` sinnvoll, die
verhindert, dass eine Datei mehrfach geöffnet wird: Bei Verwendung des
Minibuf-Explorers sieht man an jedem Vim-Fenster sofort, welche Dateien dort
geöffnet sind.

.. index:: Nerd-Commenter (Vim-Plugin)
.. _Nerd-Commenter:

Nerd-Commenter
^^^^^^^^^^^^^^

Das `NerdCommenter-Plugin <http://www.vim.org/scripts/script.php?script_id=1218>`_
ermöglicht es einzelne Zeilen oder (in Verbindung mit visuellen Markierungen)
ganze Code-Abschnitte auszukommentieren. Dabei wird automatisch für jeden
Filetype das passende Kommentarzeichen gewählt.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/scrooloose/nerdcommenter

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/scrooloose/nerdcommenter

Für die Benutzung des NerdCommenter-Plugins gibt es unter anderem folgende
Tastenkombinationen:

.. list-table::
    :widths: 10 40 15
    :header-rows: 0

    * - ``\cc``
      - Kommentiere (visuell) markierte Zeilen aus
      - (*comment*)
    * - ``\cu``
      - Kommentiere (visuell) markierte Zeilen ein
      - (*undo-comment*)
    * - ``\c Leertaste``
      - Kommentiere wechselhaft ein oder aus (kann häufig ``\cc`` und ``\cu``
        ersetzen)
      -
    * - ``\cs``
      - "schickes" Auskommentieren von langen Abschnitten (z.B. in C)
      -

..  * - ``\c$``
..  - Kommentar von der Cursor-Position bis an das Zeilenende
..  * - ``\cA``
..  - fügt an dem Ende der Zeile Kommentarzeichen an, wechselt dort in den Einfügemodus
..  * - ``\cI``
..  - fügt an dem Anfang der Zeile Kommentarzeichen an, wechselt dort in den Einfügemodus
..  * - ``\ca``
..  - wechselt zwischen verschiedenen möglichen Kommentarzeichen (z.B. in C)
..  * - ``\cy``
..  - Zeilen werden vor dem Auskommentieren zu einer einzigen verbunden
..  * - ``\cn``
..  - kommentiert visuell markierte Zeilen mittels 'nesting' aus

In der Datei ``~/.vim/bundle/nerdcommenter/plugin/NERD_commenter.vim`` können
Kommentarzeichen für die verschiedenen Dateitypen einfach angepasst und/oder
ergänzt werden. Dazu sucht man mit der Vim-Suche nach der gewünschten Endung,
beispielsweise ``tex``, und gibt wie bei den übrigen Einträgen das gewünschte
Kommentarzeichen an.

.. .. index:: Nerd-Tree (Vim-Plugin)


.. index:: Renamer (Vim-Plugin)
.. _Renamer:

Renamer
^^^^^^^

Das `Renamer Plugin <http://www.vim.org/scripts/script.php?script_id=1721>`_
ermöglicht ein gleichzeitiges, fein steuerbares Umbenennen mehrerer Dateien
mittels Vim.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/qpkorr/vim-renamer

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/qpkorr/vim-renamer

In einem neuen Vim-Buffer kann mittels ``:Ren`` der Inhalt des aktuellen
Verzeichnisses eingelesen werden. In der so erstellten Liste ist das Suchen und
Ersetzen von Text (inklusive regulärer Ausdrücke) wie üblich möglich; mit
``Enter`` kann zudem in das Verzeichnis unter dem Cursor gewechselt werden.

Um die Dateien eines Verzeichnisses unmittelbar aus der Shell heraus mit Vim
umzubenennen, kann ``vim -c Ren`` aufgerufen werden; hierfür kann wiederum in
der ``~/.bashrc`` ein alias definiert werden, beispielsweise ``alias vren='vim
-c Ren'``.

Beim Umbenennen ist lediglich zu beachten, dass die Reihenfolge der Dateien
nicht geändert werden darf und die Liste nach dem Umbenennen genauso viel Zeilen
beinhalten muss wie zu Beginn (da jede Zeile genau einen Dateinamen beinhaltet).

Ist man mit dem Umbenennen fertig, gibt man nochmals ``:Ren`` ein, und die
Dateien im jeweiligen Verzeichnis werden entsprechend umbenannt. :-)

.. TODO https://github.com/tpope/vim-repeat


.. index:: Sudo (Vim-Plugin)
.. _Sudo:

Sudo
^^^^

Das `Sudo Plugin <http://www.vim.org/scripts/script.php?script_id=729>`_ ermöglicht
es, sich auch nachträglich mit SuperUser-Rechten ausstatten. Nützlich ist das,
wenn man Systemdateien verändert, und es einem erst beim Speichern
auffällt, dass man eigentlich gar keine Schreibrechte besitzt.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/vim-scripts/sudo.vim

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/vim-scripts/sudo.vim

Zur Verwendung des Sudo-Plugins gibt es folgende Funktionen für die
Vim-Kommandozeile:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:SudoWrite Datei``
      - Speichere ``Datei`` mit Root-Rechten (``:SudoWrite %`` speichert so die
        aktuelle Datei ab)
    * - ``:SudoRead Datei``
      - Lese ``Datei`` mit Root-Rechten
    * - ``:e sudo:/path/Datei``
      - Öffne ``Datei`` mit Root-Rechten

Praktisch ist auch eine Abkürzung in der Konfigurationsdatei ``~/.vimrc``:

.. code-block:: vim

    cabbrev sw SudoWrite%            " Aktuellen Buffer mit Sudo-Rechten schreiben


.. index:: SuperTab (Vim-Plugin)
.. _SuperTab:

SuperTab
^^^^^^^^

Das `SuperTab-Plugin <http://www.vim.org/scripts/script.php?script_id=1643>`_
bietet eine einfach Möglichkeit, im Einfüge-Modus mittels ``Tab`` das bis zum
Cursor reichende Wort zu vervollständigen (ähnlich wie durch Verwendung von
``Control x``).

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/ervandew/supertab

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/ervandew/supertab

SuperTab bietet eine Möglichkeit, die Vervollständigung auf den Kontext bezogen
durchzuführen. Gibt man beispielsweise einen Pfadnamen ein, so versucht SuperTab
diesen zu vervollständigen; schlägt dies fehl, so wird versucht eine
Vervollständigung anhand des bisher in dem aktuell geöffneten (oder weiteren)
geöffneten Buffern zu bewirken. Hierzu muss folgender Eintrag in die
``~/.vimrc`` aufgenommen werden:

.. code-block:: vim

    let g:SuperTabDefaultCompletionType = "context"

Gibt es mehrere Möglichkeiten zur Vervollständigung, so wird ein kleines
Popup-Fenster, wobei die einzelnen Möglichkeiten mit ``Control n``, ``Control
p`` oder wiederum mit ``Tab`` durchlaufen werden können. Der aktuelle
Vervollständigungsvorschlag wird von SuperTab automatisch eingeblendet; drückt
man die Leertaste oder fährt man fort zu schreiben, so wird der Vorschlag
übernommen.

Hinweis: Bei Verwendung von SuperTab bewirkt die Tab-Taste nur noch ein
Einfügen eines Tabulator-Zeichens als Abstandmarker, wenn dieses am
Zeilenanfang steht oder wenn ein vor dem Cursor (mindestens) ein Leerzeichen
steht; andernfalls wird durch die SuperTab-Funktion das Wort vor der aktuellen
Position ergänzt.


.. * `Super Tab <http://www.vim.org/scripts/script.php?script_id=1643>`_:
  .. Mit ``Tab`` wird das aktuelle Wort gemäß in der Datei bereits vorkommenden
  .. Worten, falls eindeutig, ergänzt, ansonsten eine Auswahlsliste angeboten.

.. * `Word Complete <http://www.vim.org/scripts/script.php?script_id=73>`_:
  .. Ähnlich wie SuperTab, nur werden Ergänzungsvorschläge bereits während des
  .. Tippens automatisch, sobald eindeutig, unter dem Cursor eingeblendet und
  .. können mit ``Enter`` oder ``Tab`` bestätigt werden. Das Plugin kann
  .. wahlweise per Tastenkürzel oder durch Eintrag in der
  .. :ref:`Konfigurationsdatei` automatisiert geladen werden. Beim Editieren von
  .. Tex-Dateien deaktiviert das Plugin bei mir allerdings die `````-Mappings
  .. der Latex-Suite im Einfüge-Modus.

.. * `Autocomplete <http://www.vim.org/scripts/script.php?script_id=1879>`_:
  .. Während des Tippens wird automatisch ein Fenster mit
  .. Vervollständigungsmöglichkeiten eingeblendet. Bei mir führt(e) das
  .. allerdings oft zu fehlerhaften Vervollständigungen beim Zeilenumbruch.


.. index:: Tagbar (Vim-Plugin)
.. _Tagbar:

Tagbar
^^^^^^

Das `Tagbar-Plugin <http://www.vim.org/scripts/script.php?script_id=3465>`_
bietet eine Art Inhaltsverzeichnis für Quellcode. Es nutzt das externe Programm
``exuberant ctags``, um aus den aktuell geöffneten Dateien eine Übersicht an
Funktionsnamen, Makros, Variablen, Klassen, usw. zu erstellen. In
Latex-Dokumenten wird eine Kapitel-, Tabellen- und Labelübersicht angezeigt.
Faltungen und Suchanweisungen funktionieren wie gewohnt.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/majutsushi/tagbar

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/majutsushi/tagbar

Mittels ``:TagbarToggle`` oder einem entsprechenden Mapping in der
:ref:`Konfigurationsdatei` wird rechts ein Fenster mit der Tagliste
eingeblendet. Drückt man im Taglisten-Fenster über einem Schlagwort ``Enter``,
so wird im Hauptfenster das entsprechende Dokument an der jeweiligen Position
geöffnet. Möchte man das Tag-Fenster auf der linken statt auf der rechten Seite
platziert haben, so kann man die ``~/.vimrc`` um folgende Zeile ergänzen:

.. code-block:: vim

    let g:tagbar_left = 1

    "Optional: Tagbar mit gT aufrufen:
    nmap gT :TagbarToggle<CR>


.. Da ich im Normal-Modus gerne ``Space`` als Falt-Taste (``za``) verwende, habe
.. ich in der Datei ``taglist.vim`` an allen Stellen ``<space>`` durch ``i``
.. ersetzt und am Ende ``map <space> za`` angefügt. So funktioniert das Auf- und
.. Zufalten wie gewohnt, und mit ``i`` bekommt man die Definition bzw.
.. Variableninfos angezeigt.

.. Achtung: Bei großen Dateien wird das Plugin rechenintensiv, die Liste
.. braucht dann lange zum Laden!


.. index:: Ultisnips (Vim-Plugin)
.. _Ultisnips:
.. _Snippets:

Ultisnips
^^^^^^^^^

Das `Ultisnips-Plugin <http://www.vim.org/scripts/script.php?script_id=2715>`_
ist eine Weiterentwicklung des `Snipmate-Plugins
<http://www.vim.org/scripts/script.php?script_id=2540>`_ mit erheblich größerem
Funtkionsumfang. Das Plugin ermöglicht es durch Eingabe kurzer, selbst
definierter Textstücke ("Snippets") und Drücken der Tab-Taste diese durch
entsprechende Templates zu ersetzen.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/sirver/ultisnips

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden:
    | https://github.com/sirver/ultisnips

Vordefinierte Beispielsnippets finden sich im Paket `vim-snippets
<https://github.com/honza/vim-snippets>`_, das zusätzlich installiert werden
sollte. Bei der Verwendung von Vundle empfiehlt sich dabei die :ref:`pinned
<vundle-pinned>`-Option zu verwenden, damit eigene Änderungen in den
Snippets-Dateien nicht durch Aktualisierungen überschrieben werden. Es sollten
also folgende beiden Zeilen im Plugins-Abschnitt der Konfigurationsdatei
``~/.vimrc`` stehen::

    Plugin 'sirver/ultisnips'
    Plugin 'honza/vim-snippets', {'pinned': 1}

Nach der Installation der beiden Plugins befinden sich die zu den einzelnen
Filetypes gehörenden Snippets im Verzeichnis
``~/.vim/bundle/vim-snippets/UltiSnips/``; beispielsweise beinhaltet die Datei
``python.snippets`` in diesem Verzeichnis alle Snippets, die für Python-Dateien
relevant sind. Die Snippets in der Datei ``all.snippets`` gelten für alle
Dateitypen gleichermaßen.

Zur Verwendung des Ultisnips-Plugin habe ich zudem folgende Zeilen in die
Konfigurationsdatei ``~/.vimrc`` aufgenommen:

.. code-block:: vim

    " Snippets mit Tab vervollständigen, mit S-Tab mögliche Snippets anzeigen:
    let g:UltiSnipsExpandTrigger="<tab>"
    let g:UltiSnipsListSnippets="<s-tab>"

    " Mit C-h und C-l zur vorherigen bzw. nächsten Snippet-Position springen:
    let g:UltiSnipsJumpForwardTrigger="<c-l>"
    let g:UltiSnipsJumpBackwardTrigger="<c-h>"

    " Weitere Einstellungen:
    let g:UltiSnipsSnippetsDir="~/.vim/bundle/vim-snippets/UltiSnips"
    let g:UltiSnipsEditSplit="horizontal"
    let g:UltiSnipsEnableSnipMate=0

Einzelne Snippets haben folgende Syntax:

.. code-block:: vim

    snippet shortkey "Beschreibung" optionen
    ... template ...
    endsnippet


*Beispiel:* (Definiert in ``~/.vim/bundle/vim-snippets/UltiSnips/tex.snippets``)

.. code-block:: vim

    snippet / "Math Fraction" w
    \frac{$1}{$2}$0
    endsnippet

Wird mit dieser Snippet-Definition in einer ``.tex``-Datei im Einfügemodus das
Zeichen ``/`` eingegeben und ``Tab`` gedrückt, so wird dieses Zeichen durch
``\frac{}{}`` ersetzt und der Cursor an die mit ``$1`` bezeichnete Stelle
bewegt. Durch ein Drücken der Jump-Forward-Taste, die bei der obigen
Konfiguration mit ``<C-l>`` definiert ist, gelangt man zur zweiten Sprungmarke
``$2``; durch Drücken der Jump-Backwards-Taste, die mit ``<C-h>`` definiert ist,
kann man umgekehrt wieder zur vorherigen Sprungmarke zurückkehren. Erreicht man
schließlich, gegebenenfalls durch mehrmaliges Drücken der Jump-Forward-Taste,
die Position ``$0``, so wird das Ergänzen des Snippets abgeschlossen; die
vorherigen Sprungmarken können dann nicht mehr angesteuert werden.

.. _Vorgabewerte und Snippets für visuell markierte Bereiche:

.. rubric:: Vorgabewerte und Snippets für visuell markierte Bereiche

Bei der Definition von Snippets können die Sprungmarken auch als ``${1}``,
``${2}`` usw. angegeben werden. Dies nutzt man insbesondere dann, wenn man an
den Sprungstellen mittels ``${1:Vorgabe}`` einen Standard-Text einfügen mag, der
bei der Ergänzung des Snippets an dieser Stelle eingefügt wird. Gelangt der
Cursor durch Drücken der Jump-Forward-Taste zu so einer Position mit
Textvorgabe, so kann diese durch ein erneutes Drücken der Jump-Forward-Taste
bestätigt werden; gibt man hingegen einen beliebigen anderen Text ein, so wird
die Textvorgabe durch diesen ersetzt. Beispielsweise wird mittels ``${2:$1}``
der bei ``$1`` eingegebene Text automatisch als Vorgabewert an der Stelle ``$2``
eingefügt.

Ein besonderer Vorgabewert ist ``${VISUAL}``: Diese Variable enthält den visuell
markierten Textbereich, wenn (vom visuellen Modus ausgehend ``Tab`` gedrückt
wird. Man kann sich damit Snippets definieren, die wahlweise auf visuell
markierte Textbereiche angewendet werden können oder andernfalls ein leeres
Template erzeugen:

.. code-block:: vim

    snippet cen "Centered Text" b
    \begin{center}
        ${1:${VISUAL:}}
    \end{center}
    $0
    endsnippet

Das obige Snippet kann auf zweierlei Arten verwendet werden:

* Im Einfügemodus wird durch Eingabe von ``cen<Tab>`` eine ``center``-Umgebung
  erzeugt und der Cursor an die Stelle ``${1}`` gesetzt; da ``${VISUAL}``
  hierbei leer ist, wird an ``${1}`` kein Text eingefügt (es könnte auch
  ``${VISUAL:Standard}`` angegeben werden, um einen Vorgabewert zu setzen, wenn
  ``${VISUAL}`` leer ist).

* Im visuellen Modus kann ein Textbereich markiert und ``<Tab>cen<Tab>``
  eingegeben werden. Dabei verschwindet während der Eingabe von ``cen`` der
  visuell markierte Bereich; drückt man wieder ``<Tab>``, so wird er als
  Vorgabewert für ``${1}`` wieder eingeblendet. Drückt man die
  Jump-Forward-Taste, so wird dieser Vorgabewert übernommen und man gelangt an
  das Ende des Snippets (``$0``).

Derartige Snippets können, ähnlich wie das Surround-Plugin, Textbereiche in
gewünschte Umgebungen setzen.

.. _Snippet-Optionen und reguläre Ausdrücke:

.. rubric:: Snippet-Optionen und reguläre Ausdrücke

Durch die Angabe von Optionen kann gezielter festgelegt werden, wann ein Snippet
durch Drücken von ``<Tab>`` ausgelöst werden soll:

* Die Option ``w`` ("word") besagt, dass das Snippet nur dann ausgelöst wird,
  wenn das Kürzel ein eigenständiges Wort bildet, also unmittelbar vor dem
  Kürzel ein Whitespace-Zeichen (Leerzeichen, Tab, usw.) steht. Wird keine
  Option angegeben, wird automatisch ``w`` als Standard-Kriterium verwendet.

  *Beispiel:*

  Folgendes Snippet für ``.rst``-Dateien fügt durch Drücken von ``mi<Tab>`` eine
  Math-Inline-Umgebung ein:

  .. code-block:: vim

      snippet mi "Math Inline" w
      :math:\`$1\` $0

  Die Bedeutung der Backticks (``````) als Begrenzungszeichen für :ref:`Scripte
  innerhalb eines Snippets <Ausführen von Scripten>` muss
  im obigen Beispiel mit je einem Backslash (``\``) aufgehoben werden, um eine
  Interpretation des Inhalts zwischen den Backticks als Shell-Skript zu
  verhindern.

  Das Snippet soll nur ausgelöst werden, wenn ``mi`` nicht Teil eines Wortes
  ist; beispielsweise soll eine Expansion vermieden werden, wenn ``vermi<Tab>``
  eingegeben wird (um beispielsweise dieses Wort mittels des
  :ref:`SuperTab-Plugins <SuperTab>` zu "vermieden" o.ä. zu ergänzen.)

* Die Option ``b`` ("begin of line") bewirkt, dass das Snippet nur dann
  ausgelöst wird, wenn das Kürzel am Anfang einer Zeile steht.
  Whitespace-Zeichen (Leerzeichen, Tab, usw.) am Beginn der Zeile werden dabei
  ignoriert.

  *Beispiel:*

  Folgendes Snippet für ``.rst``-Dateien fügt durch Drücken von ``ma<Tab>`` eine
  Math-Paragraph-Umgebung ein:

  .. code-block:: vim

      snippet ma "Math Paragraph" b
      .. math::

          ${1}

      $0
      endsnippet

  Das Snippet soll allerdings nicht ausgelöst werden, wenn ``ma`` Teil eines
  Wortes ist oder mitten in der Zeile vorkommt.

* Die Option ``i`` ("inner word") bewirkt, dass das Snippet auch dann ausgelöst
  wird, wenn es innerhalb eines Wortes vorkommt.

  Persönlich verwende ich derartige Snippets, um beispielsweise durch Eingabe
  von ``a<Tab>`` oder ``ae<Tab>`` den deutschsprachigen Umlaut ``ä`` zu
  erzeugen. Damit ist es ohne Mehraufwand möglich, auch bei Verwendung eines
  englischen Tastaturlayouts deutschsprachigen Text zu schreiben.

* Die Option ``r`` kann in Verbindung mit den Optionen ``i``, ``w``, und ``b``
  angegeben werden, um zu bewirken, dass das Snippet-Kürzel als regulärer
  Ausdruck mit Python-Syntax interpretiert wird; Das Kürzel muss dabei in
  Anführungszeichen gesetzt werden.

  *Beispiel*:

  Die folgenden Snippets ermöglichen als Inner-Word-Snippets die Umwandlung von
  ``a<Tab>``, ``ae<Tab>`` usw. in deutschsprachige Umlaute:

  .. code-block:: vim

      snippet "ae?" "ä" ri
      ä$0
      endsnippet
      snippet "Ae?" "Ä" ri
      Ä$0
      endsnippet
      snippet "oe?" "ö" ri
      ö$0
      endsnippet
      snippet "Oe?" "Ö" ri
      Ö$0
      endsnippet
      snippet "ue?" "ü" ri
      ü$0
      endsnippet
      snippet "Ue?" "ü" ri
      Ü$0
      endsnippet
      snippet "ss?" "ß" ri
      ß$0
      endsnippet

  Das Zeichen ``?`` in der Snippet-Definition steht dabei für ``0`` oder ``1``
  Vorkommen des vorherigen Zeichens.

.. _Prioritäten:

.. rubric:: Prioritäten

Gibt es zu einem im Einfügemodus eingegebenen Textstück mehrere mögliche
Snippets, so werden diese beim Drücken von ``Tab`` nummeriert und unter Angabe
der jeweiligen Snippet-Datei aufgelistet und können durch Eingabe von ``1``,
``2``, usw. ausgewählt werden. Üblicherweise wird allerdings eine eindeutige und
somit schnelle Ergänzung der Snippets bevorzugt. Dies lässt sich in einer
Snippets-Datei durch die Vergabe von Prioritäten mittels ``priority num``
erreichen, wobei ``num`` einen Wert zwischen ``-50`` und ``+50`` bezeichnet.
Alle Snippets, die unterhalb einer solchen Eingabezeile stehen, bekommen diese
Priorität zugewiesen (bis zum Ende der Datei oder bis zur nächsten
``priority``-Zeile).

Die vordefinierten Snippets aus dem ``vim-snippets``-Plugin haben alle als
Priorität ``-50``; sie werden also nur dann ausgeführt, wenn kein anderes (auch
gleichnamiges) Plugin mit höherer Priorität existiert.

Beispielsweise haben bei mir die Umlaut-Snippets die Priorität ``-10``, so dass
sie nur dann ausgeführt werden, wenn kein anderes Snippet auf den eingegebenen
Text zutrifft; beispielsweise soll gemäß des obigen Beispiels ``ma<Tab>`` am
Anfang einer Zeile zu einer ``math``-Umgebung expandiert werden, innerhalb einer
Zeile soll ``ma<Tab>`` hingegen zu ``mä`` expandiert werden, wenn beispielsweise
"mäkeln" geschrieben werden soll.

Ohne die explizite Angabe einer Priorität haben Snippets (beispielsweise in
einer neuen Snippet-Datei) die Priorität Null. Man kann sich damit zusätzliche
Snippets in eigenen Dateien definieren, beispielsweise ``textemplates.snippets``
für eigene LaTeX-Dokumentvorlagen oder ``texmath.snippets`` für Mathe-Snippets.
Man kann eine Snippets-Datei mittels des Schlüsselwortes ``extends`` um weitere
"Dateitypen" erweitern::

    # Innerhalb der Datei ``tex.snippets``:
    # Zusätzlich die Snippets in folgenden Dateien (ohne Dateiendung) berücksichtigen:

    extends textemplates, texmath

Beispielsweise können so LaTeX-Mathe-Snippets zentral sowohl für ``.tex`` wie
auch für ``.rst``-Dateien definiert werden. Das spart nochmals Schreibarbeit --
don't repeat yourself!

.. _Einfache Ersetzungen:

.. rubric:: Einfache Ersetzungen

Soll der an der Stelle ``$1`` eingegebene Text auch an einer Stelle erscheinen, so
gibt man dort erneut ``$1`` oder beispielsweise ``${2:$1}`` ein, sofern ``$1``
nur ein Vorgabewert sein soll. Man kann bei der erneuten Verwendung von ``$1``
den dort gespeicherten Inhalt allerdings auch abändern, indem man
``${1/search/replace/}`` eingibt.

Beispielsweise werden in den Grund-Wissen-Tutorials oft ``.png``-Bilder
eingefügt und dabei in der Fußzeile die zugehörigen ``.svg``-Vektorgraphiken mit
als Download-Option verlinkt. Um dabei den Dateinamen nur einmal eingeben zu
müssen, kann folgendes Snippet verwendet werden:

.. code-block:: vim

    snippet figs "Figure with SVG" b
    .. figure:: ${1:path}
        :name:  fig-${2}
        :alt:   fig-${3:$2}
        :align: center
        :width: 50%

        .. only:: html

            :download:\`SVG: ${1/png/svg/}>\`

    $0
    endsnippet

Bei der Expansion dieses Snippets gelangt man zunächst an die Stelle ``$1``, an
der offensichtlich eine Pfadangabe erwartet wird. Gibt man hier einen Pfad ein,
der mit ``.png`` endet, so erscheint in der Fußzeile automatisch der gleiche
Pfad mit der Endung ``.svg``; möchte man diesen so automatisch generierten Pfad
nur als Vorgabewert haben, kann man an dieser Stelle auch ``${4:${1/png/svg/}}``
schreiben, um eine entsprechende zusätzliche Sprungmarke zu definieren.

.. _Ausführen von Scripten:

.. rubric:: Ausführen von Scripten

Weitere Möglichkeiten für Snippets bieten sich dadurch, dass innerhalb von
Snippets wahlweise Vim-, Shell- oder Python-Scripts ausgeführt werden können.
Diese können mehrere Zeilen umfassen und werden innerhalb der Snippet-Templates
folgendermaßen begrenzt:

* ```   ... ```: Shell-Script
* ```!v ... ```: Vim-Script
* ```!p ... ```: Python-Script

Verwendet man Python-Scripts, so werden automatisch die Module ``vim``, ``re``,
``os``, ``string`` und ``random`` geladen; zudem sind automatisch folgende
Variablen vordefiniert:

.. list-table::
    :name: tab-python-variablen
    :widths: 20 50

    * - ``snip``
      - Ein zum aktuellen Snippet gehörendes Snippet-Objekt
    * - ``fn``
      - aktueller Dateiname
    * - ``path``
      - Absoluter Pfad der aktuellen Datei
    * - ``t``
      - | Liste mit den Inhalten von ``$1``, ``$2``, usw.
        | (``t[1]`` entspricht dem Inhalt von ``$1`` usw.)

Ein ``snip``-Objekt hat dabei unter anderem folgende Attribute:

* In der Variable ``snip.rv`` wird der Rückgabewert des Snippets gespeichert.
* Die Variable ``snip.basename`` enthält den Namen der aktuellen Datei ohne
  Dateiendung.
* Die Variable ``snip.ft`` enthält den Namen des aktuellen Filetypes.
* Die Variable ``snip.v`` enthält Daten, die sich auf ``${VISUAL}`` beziehen:
  ``snip.v.text`` gibt den Inhalt von ``${VISUAL}`` an, ``snip.v.mode`` hat als
  Wert entweder ``v``, ``V`` oder ``^V`` je nach Art des visuellen Modus.

Durch Scripte bieten sich in Snippets nahezu unbegrenzte Möglichkeiten; man kann
sich so geradezu temporäre "Buttons" definieren, die bei der Expansion bestimmte
Funktionen auslösen; beispielsweise können reguläre Ausdrücke in der Definition
von Snippets gezielt ausgewertet werden:

.. code-block:: vim

    # Snippet zum Ergänzen von "bei<Tab>" zu "beispielsweise":

    snippet "(B|b)ei" "beispielsweise" rw
    `!p
    if match.group(1).islower():
        snip.rv = "beispielsweise"
    else:
        snip.rv = "Beispielsweise"
    ` $0
    endsnippet

Hierbei steht ``match.group(1)`` für den konkreten Wert, der sich bei der
Auswertung der ersten in der Snippet-Definition auftretenden Gruppierung
``(b|B)`` ergibt.

Weitere, auch umfangreichere Beispiele zum Einsatz von Scripten sind in den
Snippet-Dateien von des ``vim-snippets``-Plugins enthalten.



.. https://github.com/Valloric/YouCompleteMe

.. index:: Vicle (Vim-Plugin)
.. _Vicle:

Vicle
^^^^^

.. IDE für Kommandozeilen-Interpreter

Das `Vicle Plugin <http://www.vim.org/scripts/script.php?script_id=255>`_
ermöglicht es, von Vim aus mittels ``Ctrl c Ctrl c`` die aktuelle Zeile oder im
visuellen Modus ganze Codeblöcke an eine offene :ref:`Screen <screen>`- oder
``tmux``-Sitzung zu schicken. Egal ob Python, R, MySQL oder die Shell selbst als
Interpreter verwendet wird: Skript-Teile lassen sich auf diese Weise bereits
während des Erstellens "on-the-fly" testen.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
    Github-Repository installiert werden: https://github.com/vim-scripts/Vicle

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
      Github-Repository installiert werden:
    | https://github.com/vim-scripts/Vicle

Um ein ``tmux``-Fenster als Ziel für den übergebenen Code zu verwenden, muss man
die ``~/.vimrc`` um folgenden Eintrag ergänzen:

.. code-block:: vim

    let g:vicle_use = 'tmux'

Drückt man in einer Vim-Sitzung erstmals ``Ctrl c Ctrl c``, so wird man
aufgefordert, den Namen der ``tmux``-Session und des Zielfensters einzugeben. Im
folgenden schickt Vicle alle weiteren Zeilen von dieser Vim-Sitzung aus immer an
dieses Fenster; von mehreren verschiedenen Vim-Sitzungen aus kann allerdings
Text auch an verschiedene Interpreter geschickt werden.


.. index:: Voom (Vim-Plugin)
.. _Voom:

Voom
^^^^

Das `Voom Plugin <http://www.vim.org/scripts/script.php?script_id=2657>`_ ist
eine interaktive Python-Erweiterung [#]_, die je nach Filetype ein passendes
Inhaltsverzeichnis bietet. Voom unterstützt zahlreiche Wiki-Markups
(Restructured Text, Markdown u.a.), HTML- und Python-Quellcode.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
    Github-Repository installiert werden: https://github.com/vim-voom/VOoM

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
      Github-Repository installiert werden:
    | https://github.com/vim-voom/VOoM

Um Voom zu nutzen, sind Mappings folgender Art in der :ref:`Konfigurationsdatei`
empfehlenswert:

.. code-block:: vim

    au BufEnter,BufNewFile *.py		noremap <F2> :VoomToggle python<CR>
    au BufEnter,BufNewFile *.rst	noremap <F2> :VoomToggle rest<CR>
    au BufEnter,BufNewFile *.rst	noremap <F3> :VoomQuitAll <CR>

Damit wird innerhalb einer Python- oder ReStructuredText-Datei durch Drücken von
:math:``F2`` auf der linken Fensterseite ein Inhaltsverzeichnis der aktuellen
Datei eingeblendet. Da Voom in der aktuellen Version das Inhaltsverzeichnis von
Restructured-Text-Dateien (noch) nicht automatisch aktualisiert, wenn man
zwischen diesen wechselt, kann man auf diese Weise eine solche Aktualisierung
manuell beispielsweise durch eine Tastenkombination von ``F3 F2`` erreichen.

Im Normalmodus kann man mittels ``Tab`` zwischen
diesem Fenster und dem Hauptfenster hin und her wechseln, durch Drücken von
``Enter`` kann ein Eintrag des Inhaltsverzeichnisses direkt angewählt werden.


.. index:: Yankring (Vim-Plugin)
.. _Yankring:

Yankring
^^^^^^^^^

Das `Yankring Plugin <http://www.vim.org/scripts/script.php?script_id=1234>`_
speichert automatisch der Reihenfolge nach die zuletzt in die interne
Zwischenablage kopierten Inhalte, so dass sie gezielt an einer anderen Stelle
und/oder zu einem späteren Zeitpunkt wieder eingefügt werden können.


.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
    Github-Repository installiert werden:

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
      Github-Repository installiert werden:
    | https://github.com/vim-scripts/YankRing.vim

Wird der Inhalt der Vim-internen Zwischenablage im Normalmodus mit ``p``
oder ``P`` eingefügt, kann mit ``Ctrl p`` und ``Ctrl n`` anstelle dessen
der rückwärts bzw. vorwärts in der Kopier-History nächstgelegene Inhalt
ausgewählt und eingefügt werden.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Persönlich habe ich, bevor ich zum :ref:`Ultisnips <Ultisnips>`-Plugin
    gewechselt bin, ``Shift Tab`` als Trigger für Snipmate verwendet, da in
    meinen Einstellungen die ``Tab``-Taste bereits für das :ref:`SuperTab
    <SuperTab>`-Plugin reserviert ist. Hierzu
    muss man in der ``~/.vimrc`` folgende Änderung vornehmen:

    .. only:: html

        .. code-block:: vim

            :imap <S-Tab> <Plug>snipMateTrigger
            :smap <S-Tab> <Plug>snipMateTrigger

    .. only:: latex

        ``:imap <S-Tab> <Plug>snipMateTrigger``

        ``:smap <S-Tab> <Plug>snipMateTrigger``

    Bei Verwendung des Ultisnips-Plugin kann auch in Kombination mit SuperTab
    weiterhin die Tab-Taste als Trigger verwendet werden.

.. [#] Hierzu muss neben dem unter Linux bereits vorhandenen Python-System das
    Python-Modul ``vim_bridge`` installiert werden. Die Installation dieses
    Moduls kann in einer Shell durch Eingabe von ``sudo aptitude install
    python-setuptools`` und ``sudo easy_install vim_bridge`` erfolgen.

