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

.. Da mir persönlich die ``Esc``-Taste zu weit entfernt liegt, habe ich mir in
.. der :ref:`Konfigurationsdatei` die in normalem Text selten
.. vorkommende Tastenkombination ``jk`` mit der gleichen Funktion belegt.. :-]
.. Drückt man die Tastenkombination im Normalmodus, so ändert sich dadurch
.. die Position des Cursors nicht.

.. gute vorlage: http://dougblack.io/words/a-good-vimrc.html


.. _Mappings:

Mappings
--------

Mappings ermöglichen es, für beliebige Befehlskombinationen selbstgewählte
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
    * - ``map Kürzel Befehl``  
      - Kürzel für alle Modi

Mappings können auch über den Kommandozeilen-Modus gesetzt werden,
bleiben so allerdings nur bis zum Beenden von Vim gespeichert. Für
häufig genutzte Tastenkombinationen empfielt es sich daher, diese in der
`Konfigurationsdatei`_ festzuhalten.

**Tipp**: Eine Übersicht darüber, welche Mappings vergeben sind, kann man mit
``:map`` bekommen. Um die Auswahl einzuschränken, kann dahinter der Beginn
eines Mappings stehen - z.B. listet ``:map \b`` alle Mappings auf, welche
mit ``\b`` beginnen. Analoges gilt für ``imap`` usw.

Folgende Sonderzeichen werden dabei häufig verwendet, wobei die Groß- und
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

Herunterladen von Sprachdateien von der `Vim-Sprachenseite
<http://ftp.vim.org/vim/runtime/spell/>`_:

.. code-block:: bash

    wget -P ~/.vim/spell/ http://ftp.vim.org/vim/runtime/spell/de.utf-8.spl
    wget -P ~/.vim/spell/ http://ftp.vim.org/vim/runtime/spell/de.utf-8.sug

Folgende Zeile in die Konfigurationsdatei eintragen:: 

    map <F8>  :setlocal spell spelllang=de <return>

Ist Aspell (Apt-Paket: ``aspell-de``) installiert, können Texte aus Vim heraus
mit Aspell überprüft werden. Der Aufruf erfolgt hier ebenfalls wieder per
Tastenmakro. Das wird folgendermaßen in der .vimrc definiert::

    map <F7> :w!<CR>:!aspell check %<CR>:e! %<CR>


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

..  
    Letzte Fehlermeldung(en) anzeigen: :messages

