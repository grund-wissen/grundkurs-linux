.. _Vim-Plugins:

Plugins
=======

Vim kann durch so genannte "Plugins" erweitert werden. Diese können von der
`Projektseite <http://www.vim.org>`_ oder von `Github <https://github.com>`_
heruntergeladen werden. 

..  Beispiele:

..  * Dynamische Inhaltsverzeichnisse (:ref:`Voom`), 
..  * Projektverwaltung (:ref:`Project`), 
..  * Auto-Vervollständigung (:ref:`Supertab`), 
..  * Code-Schnipsel (:ref:`Snipmate`), 


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

.. "pinned" option: Plugin 'localplugin', {"pinned", 1}: Keine GitHub-Upgrades!

.. Um Vim mit Zusatzpaketen zu erweitern, wird, so er nicht schon existiert, ein
.. Ordner ``.vim`` im Home-Verzeichnis angelegt. Pakete, wie sie z.B. von der
.. `Projektseite <http://www.vim.org>`_  bekommen werden können, werden dorthin
.. gespeichert. Meistens genügt es schon, die jeweilige ``.tar.gz``-Datei dorthin
.. zu kopieren und zu entpacken - benötigte Ordner werden (falls nicht vorhanden)
.. automatisch angelegt. 

.. Besteht ein Plugin nur aus einer ``.vim``-Datei, so wird diese in den meisten
.. Fällen in den ``~/.vim/plugin``-Ordner kopiert. Auf Sonderfälle wird
.. auf der Vim-Homepage ausdrücklich hingewiesen.

.. Zunehmende Verbreitung findet das Vimball-Format ``.vba``: Ist das
.. `Vimball`_-Plugin einmal installiert, können (entzippte) ``.vba``-Dateien wie
.. folgt aufgerufen bzw. installiert werden::

.. vim Pluginname.vba
.. :so %


Hilfreiche Erweiterungen
------------------------

.. ag 
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
oder ähnlichen Bewegungsbefehlen den Cursor über den gewünschten Dateinamen zu
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

.. index:: CtrlP (Vim-Plugin)
.. _CtrlP:

CtrlP
^^^^^

Das `CtrlP-Plugin <http://www.vim.org/scripts/script.php?script_id=3736>`_
ermöglicht ein sehr effizientes Auswählen von Dateien, ausgehend vom
Verzeichnis, in dem Vim aufgerufen wurde; ebenso können mit ``CtrlP`` zuletzt
verwendete Dateien wieder schnell geöffnet werden. 

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/kien/ctrlp.vim

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden: 
    | https://github.com/kien/ctrlp.vim

Das CtrlP-Plugin wird vom Normalmodus aus mittels ``Control p`` gestartet. Es
erscheint ein Eingabe-Prompt, der mit ``Esc`` wieder beendet werden kann.
Möchte man mit CtrlP eine Datei im Projektverzeichnis oder einem
Unterverzeichnis öffnen, so genügt es nach Drücken von ``Control p`` eine
beliebige Anzahl von Zeichen einzugeben, die im Dateinamen der gesuchten Datei
vorkommen; es muss also nicht ein realer Dateiname eingegeben werden, sondern es
wird vielmehr eine "Fuzzy"-Suche gestartet. CtrlP listet automatisch alle
zutreffenden Dateien in einem temporären Fenster auf, in dem mittels ``Ctrl j``
und ``Ctrl k`` navigiert werden kann. Drückt man ``Enter``, so wird die
ausgewählte Datei geöffnet.

Nach Drücken von ``Control p`` kann bei Bedarf mittels ``Control f`` (oder
``Control b``) zwischen den möglichen Suchoptionen gewechselt werden (Dateien,
Buffer, zuletzt verwendete Dateien, oder alle zusammen). 

Eregex
^^^^^^

Das `Eregex-Plugin <http://www.vim.org/scripts/script.php?script_id=3282>`
ermöglicht es, in Vim für das Suchen und Ersetzen Perl-kompatible reguläre
Ausdrücke zu verwenden.

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/othree/eregex.vim

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden: 
    | https://github.com/othree/eregex.vim

Eine gute Übersicht über reguläre Ausdrücke in Perl-Syntax findet sich
beispielsweise `hier
<http://www.troubleshooters.com/codecorn/littperl/perlreg.htm>`_.

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

Für die Benutzung des NerdCommenter-Plugins gibt es folgende
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

..  Weitere Funktionen:

..  .. list-table:: 
    ..  :widths: 15 60
    ..  :header-rows: 0

    ..  * - ``\c$`` 
      ..  - Kommentar von der Cursor-Position bis an das Zeilenende                            
    ..  * - ``\cA`` 
      ..  - fügt an dem Ende der Zeile Kommentarzeichen an, wechselt dort in den Einfügemodus  
    ..  * - ``\cI`` 
      ..  - fügt an dem Anfang der Zeile Kommentarzeichen an, wechselt dort in den Einfügemodus
    ..  * - ``\ca`` 
      ..  - wechselt zwischen verschiedenen möglichen Kommentarzeichen (z.B. in C)             
    ..  * - ``\cs`` 
      ..  - "schickes" Auskommentieren von langen Abschnitten (z.B. in C)                      
    ..  * - ``\cy`` 
      ..  - Zeilen werden vor dem Auskommentieren zu einer einzigen verbunden                  
    ..  * - ``\cn`` 
      ..  - kommentiert visuell markierte Zeilen mittels 'nesting' aus                         

.. Bei der Original-Variante des NERD-Commenter ist das Komma-Zeichen als
.. einleitendes Symbol vorgesehen. Es empfiehlt sich allerdings, dieses in der Datei
.. ``NERD_comments.vim`` im :ref:`Plugin-Ordner <Vim-Plugins installieren>` in
.. einen Backslash umzuwandeln. Dazu sucht man in obiger Datei nach
.. ``NERDMapleader`` und ersetzt ``,c`` durch ``\c``. 

.. (Ansonsten wird die :ref:`Standard-Funktion der Komma-Taste <Navigation
.. innerhalb einer Zeile>` behindert.)

In der Datei ``~/.vim/bundle/nerdcommenter/plugin/NERD_commenter.vim`` können
Kommentarzeichen für die verschiedenen Dateitypen einfach angepasst und/oder
ergänzt werden. Dazu sucht man mit der Vim-Suche nach der gewünschten Endung,
beispielsweise ``tex``, und gibt wie bei den übrigen Einträgen das gewünschte
Kommentarzeichen an.

.. .. index:: Nerd-Tree (Vim-Plugin)

.. .. _Project:

.. Project
.. ^^^^^^^

.. Das `Project Plugin <http://www.vim.org/scripts/script.php?script_id=69>`_ bietet eine
.. übersichtliche Projektverwaltung von zusammengehörigen Dateien, z.B. Quellcode,
.. Notizen oder Forschungsarbeiten. 

.. Auf Knopfdruck öffnet bzw. schließt sich dabei am linken Fensterrand eine
.. Projekt-Leiste. Zwischen dieser und der aktuell geöffneten Datei kann
.. wie zwischen gesplitteten Fenstern mittels ``Ctrl W h`` bzw. ``Ctrl W l``
.. gewechselt werden.

.. Nach der regulären Installation wird ein Mapping in der
.. :ref:`Konfigurationsdatei` definiert, welches das Ein- und Ausschalten der
.. Projektleiste festlegt, beispielsweise::

    .. map gP	<Plug>ToggleProject

.. Im Normalmodus stehen stehen im Projektfenster folgende Funktionen zur
.. Verfügung:

.. .. list-table:: 
    .. :widths: 15 50 10
    .. :header-rows: 0

    .. * - ``\C``             
      .. - Erstelle ein neues Projekt
      .. - (*Create*)  
    .. * - ``\R``             
      .. - Lade den aktuellen Projekt-Ordner neu
      .. - (*Refresh*)  
    .. * - ``\G``             
      .. - Suche nach einem regulären Ausdruck im momentanen Projekt 
      .. - (*Grep*)     
    .. * - ``\L``             
      .. - Öffne alle Dateien im Projekt
      .. - (*Load*)     
    .. * - ``\I`` bzw. ``\i`` 
      .. - Zeige Infos über Projekt-Parameter bzw. absolute Pfadnamen an
      .. - (*Info*)     
    .. * - ``\E``             
      .. - Starte den Datei-Browser im aktuellen Verzeichnis 
      .. - (*Explorer*) 

.. Alle Befehle können auch in Kleinbuchstaben-Variante ausgeführt werden.
.. Der Unterschied besteht darin, dass dann nur das aktuelle Projekt, und
.. nicht rekursiv alle Unterprojekte berücksichtigt werden (bzw. beim
.. Erstellen keine Unterordner mit eingebunden werden).

.. Ein neues Projekt wird mittels ``\C`` erstellt:

.. * Der Projektname dient nur als Notiz, um bei mehreren Projekten die
  .. Übersicht zu bewahren (Faltungen funktionieren wie gewohnt).
.. * Die ``CD=``-Option ermöglicht es, ein anderes Arbeitsverzeichnis als das
  .. Projektverzeichnis (für spezielle Make-Files) zu benennen. In den meisten
  .. Fällen kann hier ``.`` (Punkt) für den aktuellen Ordner gesetzt werden.
.. * Durch Filterregeln lässt sich einschränken, welche Dateitypen in dem
  .. Projekt eine Rolle spielen. 

.. *Beispiel:* Der Filter ``"*.vim"`` berücksichtigt alle Vim-Dateien im
.. Arbeitsverzeichnis (und ignoriert alle anderen Dateien), mit dem Filter
.. ``*.c *.h`` werden ausschließlich C-Dateien mitsamt Headern angezeigt.

.. Hat man beispielsweise für eine bestimmte Programmiersprache oder ein
.. separates Themengebiet einen eigenen Ordner angelegt, so funktioniert das 
.. Project-Plugin wie ein besseres Lesezeichen mit nützlicher Suchfunktion.


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

.. index:: Snipmate (Vim-Plugin)
.. _Snipmate:

Snipmate
^^^^^^^^

Das `Snipmate Plugin <http://www.vim.org/scripts/script.php?script_id=2540>`_
erlaubt es auf einfache Weise für verschiedene Dateitypen Schlüsselwörter zu
definieren, die, wenn sie im Insert-Modus eingegeben werden, mittels Drücken
einer Auslöse-Taste ("Trigger", normalerweise ``Tab``) durch ein vorgegebenes
Template ersetzt werden. 

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
    installiert werden: https://github.com/garbas/vim-snipmate

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes Repository
      installiert werden: 
    | https://github.com/garbas/vim-snipmate

Die einzelnen Snippets werden im Ordner ``~/.vim/snippets`` in verschiedenen,
nach dem Filetype benannten Dateien definiert, beispielsweise ``rst.snippets``
für RestructuredText-Snippets.

Die Definition von Snippets erfolgt nach folgender Syntax:

.. code-block:: vim

    snippet kürzel
        template
        

*Beispiel:* (Ausschnitt aus der Datei ``~/.vim/snippets/rst.snippets``)

.. code-block:: vim

    snippet toc

        .. toctree::
            :maxdepth: 2

            ${1}

Hat man ein Snippet wie im obigen Beispiel definiert und befindet sich in einer
beliebigen ``rst``-Datei, so genügt im Insert-Modus die Eingabe von ``toc`` und
das Drücken der Trigger-Taste, und es wird anstelle von ``toc`` das entsprechend
definierte ``toctree``-Template an der aktuellen Stelle in die Datei eingefügt.
Der Cursor befindet sich  anschließend an der mit ``${1}`` festgelegten
Position. [#]_

Das Snipmate-Plugin zeichnet sich durch einen einfachen Aufbau aus, der bereits
eine große Arbeitserleichterung mit sich bringt. Möchte man allerdings einen
Schritt weiter gehen und unter anderem in Snippets reguläre Ausdrücke verwenden
oder selbst definierte Python-Funktionen auslösen können, so sollte man
unbedingt das :ref:`UltiSnips <Ultisnips>`-Plugin als gelungene
Weiterentwicklung von Snipmate verwenden. 


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
Faltungen und Suchbefehle funktionieren wie gewohnt.

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
ist eine Weiterentwicklung des :ref:`Snipmate <Snipmate>`-Plugins mit erheblich
größerem Funtkionsumfang. Das Plugin ermöglicht es, durch Eingabe kurzer, selbst
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
sollte. Bei der Verwendung von Vundle empfielt sich dabei die :ref:`pinned
<vundle-pinned>`-Option zu verwenden, damit eigene Änderungen in den
Snippets-Dateien nicht durch Aktualisierungen überschrieben werden. Nach der
Installation befinden sich die Filetype-spezifischen Snippets im Verzeichnis
``~/.vim/bundle/vim-snippets/UltiSnips/``.

Zur Verwendung des Ultisnips-Plugin habe ich zudem folgende Zeilen in die
Konfigurationsdatei ``~/.vimrc`` aufgenommen::

    let g:UltiSnipsExpandTrigger="<tab>"
    let g:UltiSnipsListSnippets="<s-tab>"

    let g:UltiSnipsJumpForwardTrigger="<c-l>"
    let g:UltiSnipsJumpBackwardTrigger="<c-h>"

    let g:UltiSnipsSnippetsDir="~/.vim/bundle/vim-snippets/UltiSnips"
    let g:UltiSnipsEditSplit="horizontal"
    let g:UltiSnipsEnableSnipMate=0

Die Definition der Snippets  im Verzeichnis
``~/.vim/bundle/vim-snippets/UltiSnips/`` erfolgt nach folgender Syntax:

.. code-block:: vim

    snippet kürzel "Beschreibung" optionen
    ... template ...
    endsnippet
        

*Beispiel:* (Definiert in ``~/.vim/bundle/vim-snippets/UltiSnips/tex.snippets``)

.. code-block:: vim

    snippet / "Math Fraction" 
    \frac{$1}{$2}$0
    endsnippet

Wird mit dieser Snippet-Definition in einer ``.tex``-Datei im Einfügemodus das
Zeichen ``/`` eingegeben und ``Tab`` gedrückt, so wird dieses Zeichen durch
``\frac{}{}`` ersetzt und der Cursor an die mit ``$1`` bezeichnete Stelle
bewegt. Durch ein Drücken der Jump-Forward-Taste, die ich mit ``<C-l>``
definiert habe, gelangt man zur zweiten Sprungmarke ``$2``; durch Drücken der
Jump-Backwards-Taste, die ich mit ``<C-h>`` definiert habe, kann man umgekehrt
wieder zur vorherigen Sprungmarke zurückkehren. Erreicht man schließlich,
gegebenenfalls durch mehrmaliges Drücken der Jump-Forward-Taste, die Position
``$0``, so wird das Ergänzen des Snippets abgeschlossen; die vorherigen
Sprungmarken können dann nicht mehr angesteuert werden.

.. rubric:: Vorgabewerte und Optionen

Sprungmarken können bei der Definition von Snippets auch als ``${1}``, ``${2}``
usw. angegeben werden. Dies nutzt man insbesondere dann, wenn man an den
Sprungstellen mittels ``${1:Vorgabe}`` einen Standard-Text einfügen mag, der bei
der Ergänzung des Snippets an dieser Stelle eingefügt wird. Gelangt der Cursor
durch Drücken der Jump-Forward-Taste zu so einer Position mit Textvorgabe, so
kann diese durch ein erneutes Drücken der Jump-Forward-Taste bestätigt werden;
gibt man hingegen einen beliebigen anderen Text ein, so wird die Textvorgabe
durch diesen ersetzt.

... to be continued ...

.. Mittels Optionen kann 

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

Damit wird innerhalb einer Python- oder RestructuredText-Datei durch Drücken von
:math:``F2`` auf der linken Fensterseite ein Inhaltsverzeichnis der aktuellen
Datei eingeblendet. Da Voom in der aktuellen Version das Inhaltsverzeichnis von
Restructured-Text-Dateien (noch) nicht automatisch aktualisiert, wenn man
zwischen diesen wechselt, kann man auf diese Weise eine solche Aktualisierung
manuell beispielsweise durch eine Tastenkombination von ``F3 F2`` erreichen.

Im Normalmodus kann man mittels ``Tab`` zwischen
diesem Fenster und dem Hauptfenster hin und her wechseln, durch Drücken von
``Enter`` kann ein Eintrag des Inhaltsverzeichnisses direkt angewählt werden.

.. https://github.com/maxbrunsfeld/vim-yankstack

.. index:: Yankstack (Vim-Plugin)
.. _Yankstack:

Yankstack
^^^^^^^^^

Das `Yankstack Plugin <http://www.vim.org/scripts/script.php?script_id=3834>`_
speichert automatisch der Reihenfolge nach die zuletzt in die Vim-interne
Zwischenablage kopierten Inhalte, so dass diese an anderer Stelle in beliebiger
Reihenfolge wieder eingefügt werden können. 

.. only:: html

    Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
    Github-Repository installiert werden:

.. only:: latex

    | Mittels :ref:`Vundle <Vundle>` kann dieses Plugin über folgendes
      Github-Repository installiert werden:
    | https://github.com/maxbrunsfeld/vim-yankstack

Zur Verwendung des Yankstack-Plugins verwende ich folgende Mappings in der
``~/.vimrc``:

.. code-block:: vim

    au BufEnter,BufNewFile * nmap gp <Plug>yankstack_substitute_older_paste
    au BufEnter,BufNewFile * nmap gn <Plug>yankstack_substitute_newer_paste

Auf diese Weise kann nach einem Einfügen mittels ``p`` oder ``P`` der eingefügte
Inhalt mittels ``gp`` bzw. ``gn`` durch einen früheren bzw. späteren Eintrag in
der Kopier-Liste ersetzt werden.

.. Das `Yankring Plugin <http://www.vim.org/scripts/script.php?script_id=1234>`_
.. speichert automatisch der Reihenfolge nach die zuletzt in die interne
.. Zwischenablage kopierten Inhalte, so dass sie gezielt an einer anderen Stelle
.. und/oder zu einem späteren Zeitpunkt wieder eingefügt werden können. 

.. Wird der Inhalt der Vim-internen Zwischenablage im Normalmodus mit ``p``
.. oder ``P`` eingefügt, kann mit ``Ctrl p`` und ``Ctrl n`` anstelle dessen
.. der rückwärts bzw. vorwärts in der Kopier-History nächstgelegene Inhalt
.. ausgewählt und eingefügt werden. 





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

