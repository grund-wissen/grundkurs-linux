.. _Kommandozeilen-Modus:

Kommandozeilen-Modus
====================

Im Kommando-Modus können sowohl Vim-Befehle als auch :ref:`externe Systembefehle
<Externe Befehle>` aufgerufen werden.

Ausgehend vom Normalmodus gelangt man mittels ``:`` in den Kommandozeilen-Modus,
mittels ``Esc`` wieder zurück. 

Buffer einlesen
---------------

Eine neue Datei kann mit ``:e`` geoffnet werden, wobei die bisherige Datei im
Hintergrund geladen bleibt.

.. list-table:: 
    :widths: 20 60
    :header-rows: 0

    * - ``:e dateiname`` 
      - eine Datei  öffnen bzw. neu erstellen 
    * - ``:e %``         
      - die aktuelle Datei neu laden 

Der Inhalt einer anderen Datei kann mittels ``:r`` hinter der momentanen
Cursor-Position eingefügt werden:

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
      - Schließe den aktuellen Buffer schließen (und beende Vim, falls nur ein Fenster offen ist) 
    * - ``:qa``          
      - Schließe alle Buffer, beende Vim
    * - ``:q!``          
      - Schließe den aktuellen Buffer, verwerfe ungespeicherte Änderungen
    * - ``:w``           
      - Speichere Änderungen an der aktuellen Datei
    * - ``:wq``          
      - Speichere die aktuelle Datei und schließe den Buffer
    * - ``:w Dateiname`` 
      - Speichere den aktuellen Buffer als ``Dateiname``

In Vim können mehrere Dateien auf einmal geoffnet sein. Im Umgang mit
diesen sogenannten "Buffern" sind folgende Befehle hilfreich:

.. todo umformulieren, buffer frueher definieren

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
    * - ``:b 1..99`` 
      - Gehe zur Datei Nr. ``1..99`` der Bufferliste   
      -                              
    * - ``:bd``      
      - Lösche die aktuelle Datei aus der Buffer-Liste 
      - (*buffer delete*)            

.. :wn : write file and move to next (SUPER)
.. :bd : remove file from buffer list (SUPER)
.. :sp fred.txt : open fred.txt into a split

Mittels ``:bufdo`` kann man (einen oder mehrere mittels ``|`` ("Pipe")
verknüpfte) Befehl(e) auf alle geöffneten Dateien loslassen:

.. list-table:: 
    :widths: 20 60
    :header-rows: 0

    * - ``:bufdo Kommando`` 
      - Führe ein ``Kommando`` in allen geöffneten Buffern aus 

Das Gleiche kann man allerdings auch (meist sicherer) mittels einer
:ref:`Makro-Aufzeichnung <Makros>` erreichen.

..  .. tip::
    ..  Vim besitzt einen integrierten Buffer-Explorer, welcher mit ``\be``
    ..  aufgerufen werden kann. In der übersichtlichen Liste der geöffneten Dateien
    ..  kann man sich wie gewohnt bewegen und mittels ``Enter`` den ausgewählten
    ..  Buffer öffnen.

..  mcdonnell S.64
..  :cd %:p:h
 
..  What the preceding command does is change the directory to the result of the %:p:h. We already know that %
..  gives us the file name and that the option :p converts that into a full path to the file. From there, we use the :h option
..  to then give us back the full path, but minus “head” (which is the file name), so that we end up with the following:
..  /Users/markmcdonnell/Code/ProjectA.

.. _Externe Befehle:

Externe Befehle
---------------

Externe Programme können im Kommando-Modus integriert werden, indem dem
jeweiligen Aufruf ein ``!`` vorangesetzt wird, wie zum Beispiel:

.. list-table:: 
    :widths: 10 60
    :header-rows: 0

    * - ``:ls``   
      - Zeige eine Liste der geoffneten Buffer an (Vim-interne Funktion!)   
    * - ``:!ls``  
      - Gebe den Inhalt des Arbeitsverzeichnisses aus (gewöhnlicher
        Linux-Befehl) 
    * - ``:.!sh`` 
      - Ersetze die momentane Zeile (``.``) durch die Rückgabe der Shell   

Wird ein beliebiger Bereich vor dem Ausrufezeichen angegeben (z.B. ``%`` für
die gesamte Datei oder ``.`` für die aktuelle Zeile), so wird die Rückgabe des
aufgerufenen Befehls an entsprechender Stelle in die Datei geschrieben.

..  .. tip:: 
..  Im Normalmodus ist ``!!`` ein Tastenkürzel für :.!
..  ``!!date``           ; Ersetzt den Inhalt der aktuellen Zeile durch das heutige Datum
..  % !!tr -d abcd     # Delete a,b,c,d from the current line

..  So können z.B. kleine mathematische Berechnungen mittels des
..  Konsolen-Taschenrechners ``bc`` ausgeführt werden, indem man die Rechnung
..  in eine extra Zeile eingibt und ``!!bc`` eingibt. Einzelne Zahlen unter dem
..  Cursor können im Normalmodus übrigens auch intern mit ``Ctrl a`` bzw.
..  ``Ctrl x`` stufenweise um 1 erhöht oder erniedrigt werden.

..  Persönlich verwende ich externe Kommandos z.B. gerne, um die momentan
..  bearbeitete Latex-Datei in
..  ein .pdf- bzw. html-Dokument umzuwandeln:

..  #Table cols=w.3cm,w.20cm hiCol=first sep=\; <<#---
..  ``:!pdflatex %`` ; wandelt das aktuelle Dokument (%) mittes ``pdflatex`` in ein pdf-Dokument
..  ``:!deplate %`` ; wandelt das aktuelle Dokument (%) mittes ``deplate`` in ein html-Dokument
..  #---

Für längere derartige Aufrufe können natürlich wiederum in der
:ref:`Konfigurationsdatei` entsprechende :ref:`Mappings` vergeben werden. Danach genügt
im Normal- oder Einfügemodus ein individuelles Tastenkürzel, und der dadurch
definierte Prozess wird ausgeführt. 

Ebenso ist es möglich, externe Kommandos nur auf einen bestimmten Bereich
(z.B. im :ref:`visuellen Modus <Visueller Modus>`) anzuwenden:

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

Das externe Kommando muss also nicht an erster Stelle in der Kommandozeile
erscheinen. 

.. _Text ersetzen:

Text ersetzen 
-------------

Gezieltes Ersetzen von Text erfolgt in Vim nach folgendem Schema::

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

Wird der Befehl auf einen visuell markierten Bereich angewandt, so werden 
dessen Grenzen ``'<``, ``'>`` als Bereich angenommen. Ansonsten kann jeder
beliebige Zeilenbereich, mit Komma getrennt, angegeben werden. Möchte man
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

.. todo: hier befehle mit <c-r>* und so

Reguläre Ausdrücke
------------------

Das Suchen und Ersetzen von Textstücken lässt sich durch so genannte reguläre
Ausdrücke oft wesentlich erleichtern bzw. beschleunigen. Hierzu können
spezielle Zeichen verwendet werden, die jeweils einem bestimmten Suchmuster
entsprechen.

Werden die folgenden Zeichen in einem Such- oder Ersetzungsbefehl verwendet, so
werden sie als reguläre Ausdrücke interpretiert. Möchte man das jeweilige
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

Ebenso gibt es Zeichen, die in einem Such- oder Ersetzungsbefehl als "normale"
Zeichen interpretiert werden, jedoch durch Voranstellen eines ``\`` eine
Sonderbedeutung bekommen:

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

..  http://www.jeetworks.org/node/86

..  http://www.softpanorama.org/Editors/Vimorama/vim_regular_expressions.shtml
