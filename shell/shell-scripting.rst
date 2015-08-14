.. _Shell-Scripting:

Shell-Scripting
===============

.. todo Definition Prozess

Die Shell kann unmittelbar als Interpreter für einzelne Programmaufrufe genutzt
werden. Darüber hinaus ist es ebenso möglich, mehrere Eingabezeilen miteinander
zu kombinieren. Diese Methode, mehrere aufeinander folgende Programmaufrufe --
ähnlich wie ein Kochrezept -- in eine Textdatei zu schreiben und mittels dieser
Datei von der Shell ausführen zu lassen, wird als "Shell-Scripting" bezeichnet.

In den folgenden Abschnitten werden einige Möglichkeiten zum gezielten Scripten
der ``bash``, d.h. der unter Debian, Ubuntu und Linux Mint am weitesten
verbreiteten Shell, näher vorgestellt.


.. index:: Shebang
.. _Aufbau und Aufruf eines Shellskripts:

Aufbau und Aufruf eines Shellskripts
------------------------------------

Shell-Skripte sind Textdateien, die üblicherweise die Endung ``.sh`` oder
überhaupt keine Endung besitzen. [#]_ In beiden Fällen sollte am Anfang der
Datei festgelegt werden, welcher Shell-Interpreter beim Aufruf des Skripts
genutzt wird. Dies erfolgt über den so genannten "Shebang": [#]_

.. code-block:: bash

    #!/bin/bash

Die Zeichenkette ``#!`` bewirkt dabei, dass die nachfolgende Anweisung
(gegebenenfalls mit zusätzlichen Argumenten) beim Aufruf des Programms
ausgeführt wird. Im obigen Beispiel wird also ein ``bash``-Prozess gestartet,
der die darauf folgenden Anweisungen und Programmaufrufe Zeile für Zeile
interpretiert. [#]_ Alle anderen Zeilen, die mit ``#`` beginnen, werden als
Kommentare ignoriert.

Um das Shell-Skript aufzurufen, wird in einer Shell folgende Zeile eingegeben:

.. code-block:: bash

    sh pfad/skriptdatei

Ebenso ist es möglich, die Skriptdatei mit ``chmod +x`` ausführbar zu machen.
Dann kann sie -- wie ein binäres Programm -- direkt aufgerufen werden:

.. code-block:: bash

    # Datei ausführbar machen:
    cd pfad
    chmod +x skriptdatei

    # Skript aufrufen:
    pfad/skriptdatei

Befindet man sich im gleichen Ordner wie die Skriptdatei, so kann diese mit
``./skriptdatei`` aufgerufen werden, da ``.`` für den Namen des aktuellen
Verzeichnisses steht.

Möchte man bestimmte Skripte auch ohne explizite Angabe des Pfades aufrufen, so
empfiehlt es sich zu diesem Zweck mit ``mkdir ~/bin`` ein eigenes
Unterverzeichnis im Home-Verzeichnis anzulegen und in die Konfigurationsdatei
``~/.bashrc`` folgenden Eintrag zu schreiben:


.. code-block:: bash

    # Eigenes bin-Verzeichnis zum Systempfad PATH hinzufügen

    # Prüfen ob das Verzeichnis existiert:
    if [ -d "$HOME/bin" ] ; then
        PATH="$HOME/bin:$PATH"
        export PATH;
    fi

Durch die Zeile ``PATH="$HOME/bin:$PATH"`` wird das eigene ``bin``-Verzeichnis
an den Anfang des Systempfades gesetzt. Wird in einer Shell eine beliebige
Anweisung eingegeben, so wird zunächst der eigene ``bin``-Ordner und erst
anschließend alle anderen in der ``PATH``-Variable gespeicherten Verzeichnisse
nach einem entsprechenden Programm bzw. Skript durchsucht.

.. index:: Exit-Status
.. _Rückgabewerte und Verkettung von Programmen:

Rückgabewerte und Verkettung von Programmen
--------------------------------------------

Jedes Programm oder Shell-Skript sollte beim Beenden einen Wert liefern, der
angibt, ob das Skript fehlerfrei abgelaufen ist oder nicht. Üblicherweise wird
dazu das Programm bei einem fehlerfreien Durchlauf mit ``exit 0`` beendet. Jeder
andere "Exit-Status" zwischen ``1`` bis ``255`` deutet meistens auf einen Fehler
hin. [#]_ Der Rückgabewert wird in einem Skript an einer beliebigen Stelle
mittels ``exit num`` festgelegt; das Skript wird dadurch unmittelbar
beendet.

Bei der interaktiven Benutzung der Shell wird der Exit-Status eines Skripts oder
Programms nur selten benutzt, da mögliche Fehlermeldungen direkt vom Benutzer
abgelesen werden können. In Shell-Skripten jedoch werden bestimmte Aktionen
häufig in Abhängigkeit von anderen Aktionen ausgeführt; sollen beispielsweise
Dateien verschoben werden, so dürfen die Originale nur dann gelöscht werden,
wenn sie zuvor erfolgreich kopiert worden sind.

.. index:: &&, ||

.. rubric:: Die Operatoren ``&&`` und ``||``

Mittels der Operatoren ``&&`` und ``||`` kann man die Ausführung einer zweiten
Anweisung vom Rückgabewert der ersten Anweisung abhängig machen:

* Ein Ausdruck der Form ``anweisung1 && anweisung2`` bedeutet, dass
  ``anweisung2`` nur dann ausgeführt wird, wenn ``anweisung1`` fehlerfrei
  ausgeführt bzw. mit Exit-Status ``0`` beendet wurde.

* Ein Ausdruck der Form ``anweisung1 || anweisung2`` bedeutet, dass
  ``anweisung2`` genau dann ausgeführt wird, wenn ``anweisung1`` mit einem
  Fehler bzw. mit einem Exit-Status zwischen ``1`` und ``255`` beendet wurde.

Bedingte Anweisungen können auch mittels ``if`` und ``case`` implementiert
werden.


.. _Ausgaben in Textdateien umlenken:

.. rubric:: Ausgaben in Textdateien umlenken

Normalerweise geben Skripte und Programme Meldungen und Rückgabewerte als Text
im Shell-Fenster aus. Mit den Operatoren ``>`` und ``>>`` ist es allerdings auch
möglich, die Ausgabe in Text-Dateien umzuleiten:

.. index:: >

* Mit dem Operator ``>``  kann man die Ausgabe eines Programms in eine Datei
  umleiten, deren Name im Anschluss an das ``>``-Zeichen geschrieben wird:

  .. code-block:: bash

      # Inhalt des Verzeichnisses und aller Unterverzeichnisse
      # in Text-Datei "folder-content.txt" schreiben:
      ls -R > folder-content.txt

  Existiert die Datei noch nicht, so wird sie neu angelegt; als Eigentümer der
  Datei wird dabei der Benutzer eingetragen, der den Shell-Prozess ausführt.

  Existiert die Datei schon, so wird sie zunächst geleert und anschließend neu
  beschrieben. Der Eigentümer und die Zugriffsrechte bleiben dabei erhalten. Damit
  das Überschreiben funktioniert, muss das Schreiben der Datei erlaubt sein.

.. index:: >>

* Nach dem gleichen Prinzip kann man mit dem Operator ``>>``  die Ausgabe eines
  Programms an eine Datei anhängen. Diese Variante findet insbesondere bei der
  Protokollierung einzelner Prozesse in Log-Dateien Anwendung.

.. index:: <

Umgekehrt kann man mittels des Operators :math:`<` eine Datei angeben, aus der
gelesen werden soll. Selten wird diese Syntax von Programmen zwingend gefordert,
in den meisten Fällen kann eine einzulesende Datei auch ohne ``<`` angegeben werden.
Beispielsweise sind die Anweisungen ``cat anyfile.txt`` und ``cat <
anyfile.txt`` identisch.


.. index:: Standard-Kanal
.. _Fehlermeldungen umlenken:

.. rubric:: Fehlermeldungen umlenken

Für jeden Prozess öffnet die Shell drei Standard-Kanäle: Kanal ``0`` steht für
die Standard-Eingabe, Kanal ``1`` für die Standard-Ausgabe und ``2`` für  den
Standard-Fehlerkanal.

Man kann jedem der Umleitungskommandos ``<``, ``>`` und ``>>`` eine dieser
Nummern für den jeweiligen Kanal voranstellen. So kann beispielsweise die
Fehlerausgabe einer Anweisung mittels ``2> error-logfile.txt`` in eine
entsprechende Log-Datei umgelenkt werden.

Als eine Besonderheit ist hierbei die Datei ``/dev/null`` hervorzuheben. Diese
Datei dient als "Mülleimer", d.h. es werden alle Meldungen, die zu dieser Datei
umgelenkt werden, verworfen. So kann man beispielsweise mittels der Anweisung
``any_program 2> /dev/null`` die Ausgabe von Fehlern unterdrücken.


.. index:: Pipeline, |
.. _Pipelines:

.. rubric:: Pipelines

Die Ausgaben eines Programms können nicht nur Dateien, sondern auch an andere
Programme weitergeleitet werden. Hierzu wird in Shell-Skripts der Operator ``|``
("Pipe") in der Form ``anweisung1 | anweisung2`` verwendet:

.. code-block:: bash

    # Alle Dateien des aktuellen Verzeichnisses und aller
    # Unterverzeichnisse anzeigen, die "txt" enthalten:
    ls -R | grep txt

Bei einer solchen Verkettung von Programmen werden die Daten nicht in eine
Zwischendatei angelegt, sondern direkt an das nächste Programm übergeben.

Pipelines stellen ein vielseitiges Werkzeug dar, insbesondere in Kombination mit
folgenden Programmen:

* Mit :ref:`grep <grep>` kann die Ausgabe eines Programms hinsichtlich
  bestimmter Suchmuster gefiltert werden.

* Mit :ref:`tee <tee>` kann die Standard-Ausgabe oder Standard-Fehlerausgabe sowohl auf
  dem Bildschirm ausgegeben als auch in eine Datei geschrieben werden. Die
  Syntax hierzu könnte also ``anweisung | tee error-logfile.txt`` lauten.

.. index:: xargs

* Mit ``xargs`` werden alle empfangenen Werte als Argumente der folgenden
  Anweisung übergeben. Beispielsweise würde die Anweisung ``find ./ -name *foo*
  | xargs grep muster`` alle Dateien, die "foo" in ihrem Dateinamen enthalten,
  nach dem gegebenen Begriff oder Suchmuster durchsuchen (ohne ``xargs`` würden
  hingegen die Dateinamen nach ``muster`` durchsucht).


.. _Dateimuster und Variablen:

Dateimuster und Variablen
-------------------------

Die Shell weist als Interpreter einigen Sonderzeichen eine besondere Bedeutung
zu. Mit Hilfe solcher Zeichen (so genannten "Wildcards") können Muster für
Dateinamen einfach formuliert werden. Die Shell ersetzt dann bei der Ausführung
die Muster dann durch die entsprechenden Dateinamen.

.. list-table::
    :name: tab-wildcards
    :widths: 10 50

    * - Zeichen
      - Bedeutung
    * - ``*``
      - Eine beliebig lange Folge von Zeichen
    * - ``?``
      - Ein einzelnes beliebiges Zeichen
    * - ``[abc123]``
      - Eines der Zeichen, die in der Klammer vorkommen
    * - ``[!abc]``
      - Ein beliebiges Zeichen, das *nicht* in der Klammer vorkommt


Wohl am häufigsten wird das ``*``-Zeichen verwendet, das für eine beliebig lange
Folge von Zeichen steht; dabei ist auch die Länge Null explizit erlaubt.
Beispielsweise werden mittels ``ls *foo*`` alle Dateien ausgegeben, die "foo" in
ihrem Dateinamen beinhalten, egal welche Zeichen vorher oder nachher im
Dateinamen vorkommen. Mit ``ls *.txt`` werden alle Dateien angezeigt, deren
Dateiname auf ".txt" endet. Zu beachten ist hierbei jedoch eine Ausnahme: Der
Stern als Suchmuster ignoriert Dateien, deren Name mit einem Punkt beginnt, es
sei denn, man schreibt explizit ``.*txt``. Dadurch soll verhindert werden, dass
versehentlich Konfigurationsdateien gelöscht werden.

In den eckigen Klammern kann auch ein Buchstaben- oder Zahlenbereich in der Form
``[a-z]`` oder ``[0-9]`` angegeben werden; auch eine Kombination der Form
``[a-zA-Z0-9]`` ist möglich, um ein beliebiges alphanumerisches Zeichen
auszudrücken. Diese Syntax funktioniert ebenso für ausschließende Klammern,
beispielsweise steht ``[!a-z]`` für ein beliebiges Zeichen außer einem
Kleinbuchstaben.

.. index:: $

Eine weitere besondere Bedeutung hat das Dollar-Zeichen ``$``: Es ersetzt den
unmittelbar (ohne Leerstelle) folgenden Variablennamen durch den in der
Variablen abgespeicherten Wert.

.. index:: \

Möchte man die gewöhnliche Bedeutung eines Zeichens aufheben, so muss diesem das
Backslash-Zeichen ``\`` vorangestellt werden. Dies betrifft sowohl die oben
angegebenen Sonderzeichen wie auch das Leerzeichen, das eigentlich zur Trennung
verschiedener Argumente genutzt wird, aber auch Bestandteil von Dateinamen sein
kann. In gleicher Weise muss den Zeichen ``; & | ( )  < >`` sowie ``\n`` und
``\t`` (Zeilenende und Tabulator) ein Backslash vorangestellt werden, um die
jeweilige Sonderbedeutung aufzuheben.

Eine weitere bisweilen nützliche Ergänzung bieten geschweifte Klammern innerhalb
von Dateimustern. Diese eignen sich dazu, um an der gegebenen Stelle einen der
in den geschweiften Klammern stehenden, durch Komma-Zeichen voneinander
getrennten Namen einzusetzen. Beispielsweise gibt ``ls -R
~/data/{buecher,docs}/?*/{*.pdf,*djvu}`` alle ``pdf``- und ``djvu``-Dateien in
den Unterverzeichnissen von ``~/data/buecher`` und ``~/data/docs`` auf. Diese
Liste kann dann beispielsweise mittels ``| grep`` gezielt nach Einträgen
durchsucht werden.

.. _Zuweisung von Variablen:

.. rubric:: Zuweisung von Variablen

Ähnlich wie in Programmiersprachen, so lassen sich auch in der Shell Werte in
Variablen speichern. Allerdings sind nur Zeichenketten ("Strings") als Werte
erlaubt.

Um einer Variablen einen Wert zuzuweisen, muss folgende Syntax verwendet werden:

.. code-block:: bash

    variablenname=wert

Zwischen dem Variablennamen, dem Zuweisungsoperator ``=`` und dem zu
speichernden Wert darf dabei kein Leerzeichen stehen.

.. index:: set

Mit der Anweisung ``set`` kann in der Shell abgefragt werden, welche Variablen
aktuell gesetzt sind und welche Werte diese haben. Unter Umständen kann diese
Liste recht lang sein, so dass es nützlich ist, die Ausgabe von ``set`` mittels
einer Pipe entweder an einen Pager wie :ref:`less <less>` zu übergeben oder
mittels :ref:`grep <grep>` nach einem bestimmten Variablennamen zu filtern.

.. code-block:: bash

    # Alle Variablen und ihre Werte mit less betrachten:
    set | less

    # Wert der Variablen EDITOR prüfen:
    set | grep EDITOR

Variablen können in der Shell an jeder beliebigen Stelle genutzt werden. Trifft
der Shell-Interpreter auf ein ``$``-Zeichen, so wird der unmittelbar (ohne
Leerzeichen) folgende Variablenname durch den gespeicherten Variablenwert
ersetzt. Ist die angegebene Variable nicht definiert, so wird vom Interpreter an
dieser Stelle nichts eingesetzt.

.. index:: unset

Mittels ``unset variablenname`` kann man eine Variable wieder löschen.

.. index:: export
.. _Exportieren von Variablen:

.. rubric:: Exportieren von Variablen

Weist man in einer Shell einer Variablen einen Wert zu, so ist diese Variable
per Voreinstellung nur dem aktuellen Shell-Prozess bekannt. Möchte man eine
Variable auch in von der aktuellen Shell-Sitzung aus gestarteten Unterprozessen
nutzen, so kann sie mittels der ``export``-Anweisung zugänglich gemacht werden:

.. code-block:: bash

    # Variable definieren:
    my_var=fooo

    # Variable öffentlich machen:
    export my_var

Auch in diesem Fall kann die Variable mittels ``unset my_var`` wieder gelöscht
werden. Wird dem gleichen Variablennamen erneut ein Wert zugewiesen, so wird die
Variable wieder als lokal angesehen und muss bei Bedarf erneut exportiert
werden.


.. index:: readonly
.. _Definition von Konstanten:

.. rubric:: Definition von Konstanten

Mittels der Anweisung ``readonly variablenname`` kann eine Variable in eine
Konstante umgewandelt werden. Der Wert, den die Variable zu diesem Zeitpunkt
hat, kann später nicht mehr verändert werden, auch kann die Variable nicht mehr
mittels ``unset`` gelöscht werden -- sie ist sozusagen schreibgeschützt. Erst
mit dem Beenden der Shell wird die Konstante wieder gelöscht.

Mittels ``readonly`` (ohne Variablennamen) kann eine Liste mit allen aktuell
definierten Konstanten ausgegeben werden.

Besondere Shell-Variablen
-------------------------

Im folgenden werden einige Standard-Variablen aufgelistet, die automatisch
definiert sind und häufig in Shell-Skripten vorkommen:

.. only:: html

    .. list-table::
        :name: standard-variablen
        :widths: 10 60

        * - ``$0``
          - | Diese Variable enthält den Namen des aktuellen Prozesses, beispielsweise
              ``/bin/bash``.
            | Im Fall eines laufenden Shellskripts entspricht ``$0`` dem Namen der
              Skriptdatei.

        * - ``$1`` bis ``$9``
          - Diese Variablen enthalten die beim Aufruf des Skripts übergebenen
            Argumente ``1`` bis ``9``.

        * - ``$*``
          - | Diese Variable enthält alle beim Aufruf des Skripts übergebenen
              Argumente als eine einzelne Zeichenkette.
            | Die einzelnen Argumente sind
              dabei durch Leerzeicheen getrennt.

        * - ``$@``
          - Diese Variable enthält alle beim Aufruf des Skripts übergebenen
            Argumente als Liste.

        * - ``$#``
          - Die Variable gibt die Anzahl der beim Aufruf des Skripts übergebenen
            Argumente an.

        * - ``$-``
          - Diese Variable enthält alle im aktuellen Prozess eingeschalteten
            Optionsbuchstaben.

        * - ``$?``
          - Diese Variable enthält den :ref:`Exit-Status <Rückgabewerte und
            Verkettung von Programmen>` der zuletzt ausgeführten Anweisung.

        * - ``$$``
          - Diese Variable enthält die Prozess-Nummer der Shell, in der das Skript
            ausgeführt wird.


        * - ``$!``
          - Diese Variable enthält die Prozess-Nummer des zuletzt erzeugten
            Hintergrundprozesses.

.. only:: latex

    .. list-table::
        :name: standard-variablen-tex
        :widths: 10 60

        * - ``$0``
          - Diese Variable enthält den Namen des aktuellen Prozesses,
            beispielsweise ``/bin/bash``. Im Fall eines laufenden Shellskripts
            entspricht ``$0`` dem Namen der Skriptdatei.

        * - ``$1`` bis ``$9``
          - Diese Variablen enthalten die beim Aufruf des Skripts übergebenen
            Argumente ``1`` bis ``9``.

        * - ``$*``
          - Diese Variable enthält alle beim Aufruf des Skripts übergebenen
            Argumente als eine einzelne Zeichenkette. Die einzelnen Argumente
            sind dabei durch Leerzeicheen getrennt.

        * - ``$@``
          - Diese Variable enthält alle beim Aufruf des Skripts übergebenen
            Argumente als Liste.

        * - ``$#``
          - Diese Variable gibt die Anzahl der beim Aufruf des Skripts übergebenen
            Argumente an.

        * - ``$-``
          - Diese Variable enthält alle im aktuellen Prozess eingeschalteten
            Optionsbuchstaben.

        * - ``$?``
          - Diese Variable enthält den :ref:`Exit-Status <Rückgabewerte und
            Verkettung von Programmen>` der zuletzt ausgeführten Anweisung.

        * - ``$$``
          - Diese Variable enthält die Prozess-Nummer der Shell, in der das Skript
            ausgeführt wird.


        * - ``$!``
          - Diese Variable enthält die Prozess-Nummer des zuletzt erzeugten
            Hintergrundprozesses.

Die Variable ``$$`` ist insbesondere für die Erzeugung von temporären Dateien
von Bedeutung. Erzeugt ein Skript beispielsweise eine gleichnamige Datei
``/tmp/$0`` im ``/tmp``-Verzeichnis, so würde das Skript bei einem
gleichzeitigen Aufruf in verschiedenen Shell-Fenstern die gleiche Datei nutzen
und dabei mit großer Wahrscheinlichkeit jeweils Daten der anderen Prozesse
überschreiben. Verwendet man hingegen ``/tmp/$0.$$`` als Namen für die temporäre
Datei, so bekommt jede ausführende Instanz des Skripts eine eigene Datei
zugewiesen.

Neben den obigen, minimalistisch benannten Variablen existieren weitere vordefinierte
Variablen, die häufig in Shell-Skripten eingesetzt werden:

.. only:: html

    .. list-table::
        :name: standard-variablen-2
        :widths: 10 60

        * - ``$EDITOR``
          - Diese Variable gibt an, welches Programm bevorzugt als Texteditor
            geöffnet werden soll.
        * - ``$HOME``
          - Diese Variable enthält den Namen des Home-Verzeichnisses des aktuellen
            Benutzers.
        * - ``$PAGER``
          - Diese Variable gibt an, welches Programm als Pager, also als
            Anzeigeprogramm für Textdateien geöffnet werden soll
        * - ``$PATH``
          - Diese Variable enthält alle Verzeichnisse, in denen bei Eingabe einer
            Shell-Anweisung nach einem entsprechenden Programm gesucht wird. Die
            Namen der einzelnen Verzeichnisse sind durch Doppelpunkte getrennt und
            werden in der angegebenen Reihenfolge durchsucht.
        * - ``$PS1``
          - In dieser Variablen ("Prompt String 1") wird das Aussehen des
            Eingabe-Prompts definiert. Üblicherweise steht ``$`` für normale Benutzer
            und ``#`` für den Systemverwalter.
        * - ``$PS2``
          - In dieser Variablen ("Prompt String 2") wird definiert, wie der
            Eingabe-Prompt im Fall eines Zeilenumbruchs aussehen soll.
            Üblicherweise wird hierfür das Zeichen ``>`` verwendet.
        * - ``$TERM``
          - Diese Variable enthält den Namen des aktuellen Shell-Anzeige-Programms.
        * - ``$USER``
          - Diese Variable enthält den Namen des aktuellen Benutzers.

.. only:: latex

    .. list-table::
        :name: standard-variablen-2-tex
        :widths: 50 50

        * - ``$EDITOR``
          - Diese Variable gibt an, welches Programm bevorzugt als Texteditor
            geöffnet werden soll.
        * - ``$HOME``
          - Diese Variable enthält den Namen des Home-Verzeichnisses des aktuellen
            Benutzers.
        * - ``$PAGER``
          - Diese Variable gibt an, welches Programm als Pager, also als
            Anzeigeprogramm für Textdateien geöffnet werden soll
        * - ``$PATH``
          - Diese Variable enthält alle Verzeichnisse, in denen bei Eingabe einer
            Shell-Anweisung nach einem entsprechenden Programm gesucht wird. Die
            Namen der einzelnen Verzeichnisse sind durch Doppelpunkte getrennt und
            werden in der angegebenen Reihenfolge durchsucht.
        * - ``$PS1``
          - In dieser Variablen ("Prompt String 1") wird das Aussehen des
            Eingabe-Prompts definiert. Üblicherweise steht ``$`` für normale Benutzer
            und ``#`` für den Systemverwalter.
        * - ``$PS2``
          - In dieser Variablen ("Prompt String 2") wird definiert, wie der
            Eingabe-Prompt im Fall eines Zeilenumbruchs aussehen soll.
            Üblicherweise wird hierfür das Zeichen ``>`` verwendet.
        * - ``$TERM``
          - Diese Variable enthält den Namen des aktuellen Shell-Anzeige-Programms.
        * - ``$USER``
          - Diese Variable enthält den Namen des aktuellen Benutzers.

.. index:: printenv

Die aktuellen Werte aller Variablen können mittels der Anweisung ``printenv``
angezeigt werden; eine einzelne Variable wie ``$EDITOR`` kann mittels ``printenv
EDITOR`` ausgegeben werden.

Üblicherweise werden die ``$EDITOR`` und ``$PAGER``-Variablen in der
Konfigurationsdatei ``.bashrc`` festgelegt:

.. code-block:: bash

    # Vim als Editor festlegen:
    export EDITOR=vim

    # Less als Pager festlegen:
    export PAGER=less

Werden die Variablen nicht vom Benutzer gesetzt, so wird üblicherweise ``vi``
als Standard-Editor und ``cat`` als Pager verwendet.

Wer keine Erfahrung mit :ref:`Vim <Texteditor Vim>` hat, kann an dieser Stelle
beispielsweise ``pico``, ``nano``, ``joe`` oder ``emacs`` verwenden, wobei die
letzten beiden gegebenenfalls mittels der gleichnamigen Pakete via :ref:`apt
<apt>` installiert werden müssen.

.. todo Konfiguration von $PS1 in .bashrc


.. _Auswertung von Variablen:

Auswertung von Variablen
------------------------

.. index:: ${}

In manchen Fällen, beispielsweise beim Arbeiten mit Verzeichnis- und Dateinamen,
kann es passieren, dass der Wert einer Variable nahtlos in weiteren Text
übergehen soll. In diesem Fall muss der Name der Variablen in geschweifte
Klammern gesetzt werden:

.. code-block:: bash

    # Variable definieren:
    zwei=ZWEI

    echo eins$zweidrei
    # Ergebnis: eins

    echo eins${zwei}drei
    # Ergebnis: einsZWEIdrei

Ist der Variablenname in geschweiften Klammern nicht definiert, so wird sie wie
gewöhnlich vom Interpreter ausgelassen (durch "nichts" ersetzt). Dieses
Verhalten des Interpreters kann auf mehrere Arten beeinflusst werden:

* Schreibt man ``${variablenname-standardwert}``, so wird an der Stelle der
  Variablen der angegebene Standardwert eingesetzt, sofern der Variablenname
  nicht definiert ist; Die Variable bleibt dabei undefiniert.
* Schreibt man ``${variablenname=standardwert}``, so wird ebenfalls an der
  Stelle der Variablen der angegebene Standardwert eingesetzt, sofern der
  Variablenname nicht definiert ist; die Variable wird dabei allerdings mit
  dem angegebenen Standardwert neu definiert.
* Schreibt man ``${variablenname?fehlermeldung}``, so wird geprüft,
  ob der angegebene Variablenname definiert ist. Ist er es nicht, so wird das
  Shellskript abgebrochen und die hinter dem ``?`` angegebene Fehlermeldung
  angezeigt. Wird keine Fehlermeldung angegeben, so wird als Standard die
  Meldung "parameter null or not set" ausgegeben.

Möchte man im umgekehrten Fall einen bestimmten Wert ausgeben, wenn eine
Variable definiert ist, so kann man die Syntax ``${variablenname+wert}``
verwenden. Beispielsweise Liefert ``${one+yes}`` den Wert ``yes``, wenn die
Variable ``one`` definiert ist, andernfalls wird die angegebene Variable
ausgelassen (durch nichts ersetzt).


.. _Quotings:

.. rubric:: Quotings

In der Shell haben einfache Anführungszeichen, doppelte Anführungszeichen und so
genannte "Backticks" (`````) eine jeweils eigene Bedeutung:

* Innerhalb von doppelten Anführungszeichen kann ein beliebig langer Text als
  eine einzelne Zeichenkette eingegeben werden. Diese kann sich über mehrere
  Bildschirmzeilen erstrecken und Leerzeichen beinhalten, ohne dass diesen
  jeweils ein Backslash vorangestellt werden muss. Die Bedeutung des
  Dollar-Zeichens bleibt allerdings erhalten, so dass mittels ``$variablenname``
  innerhalb doppelter Anführungszeichen der Wert einer Variablen wie gewohnt
  ausgewertet werden kann.

  Dateinamen-Erweiterungen, beispielsweise mittels des Stern-Zeichens ``*``,
  sind hingegen innerhalb der Anführungszeichen nicht möglich.

* Innerhalb von einfachen Anführungszeichen kann ebenfalls ein beliebig langer
  Text als eine einzelne Zeichenkette eingegeben werden. Auch in diesem Fall
  kann sich der Text über mehrere Bildschirmzeilen erstrecken. Die Besonderheit
  bei der Benutzung von einfachen Anführungszeichen liegt darin, dass in diesem
  Fall sämtliche Sonderzeichen ihre Bedeutung verlieren, also auch keine
  Auswertung von Variablen mittels des Dollar-Zeichens ``$`` erfolgt.

.. index:: Backticks

* Backticks werden üblicherweise für Shell-Anweisungen genutzt, wobei die
  innerhalb der Backticks stehende(n) Anweisung(en) von der Shell durch ihren
  Rückgabewert ersetzt werden.

.. index:: $()

Soll das Ergebnis einer Shell-Anweisung wie eine Variable genutzt werden, so
kann dies alternativ zur Backticks-Notation auch mittels ``$(anweisung)``
erfolgen. Diese Schreibweise ist im Allgemeinen sogar vorzuziehen, da sie meist
übersichtlicher und somit angenehmer zu lesen ist.


.. _Kontrollstrukturen:

Kontrollstrukturen
------------------

Die folgenden Kontrollstrukturen können zur Steuerung eines Shell-Skripts
verwendet werden, wenn einzelne Code-Blöcke nur unter bestimmten Bedingungen
oder auch mehrfach ausgeführt werden sollen.


.. index:: if,then
.. _Fallunterscheidungen:

.. rubric:: Fallunterscheidungen -- ``if``, ``then``, ``else``

Mit Hilfe von ``if``-Abfragen ist es möglich, Teile eines Shell-Skripts nur
unter bestimmten Bedingungen ablaufen zu lassen. Ist die ``if``-Bedingung wahr,
so wird der anschließende, durch ``then`` gekennzeichnete Code ausgeführt, bis
das Schlüsselwort ``fi`` (ein umgedrehtes ``if``) die bedingte Anweisung
abschließt.

Die grundsätzliche Syntax lautet also:

.. code-block:: bash

    if bedingung
    then
        anweisungen
    fi

.. index:: elif, else

Optional können nach einem ``if``-Block mittels ``elif`` eine oder mehrere
zusätzliche Bedingungen formuliert werden, die jedoch nur dann untersucht
werden, wenn die erste ``if``-Bedingung falsch ist. Schließlich kann auch eine
``else``-Bedingung angegeben werden, die genau dann ausgeführt wird, wenn die
vorherige Bedingung (beziehungsweise alle vorherigen Bedingungen bei Verwendung
eines ``elif``-Blocks) nicht zutreffen.

Insgesamt kann eine Fallunterscheidung beispielsweise folgenden Aufbau haben:

.. code-block:: bash

    if bedingung1
    then
        anweisung1

    elif bedingung2
    then
        anweisung2

    else
        anweisung3

    fi

.. index:: test, []

Um die Bedingungen zu formulieren, wird häufig die Shell-Anweisung ``test``
verwendet. Mit dieser lassen sich zum einen Datei-Tests durchführen, zum
anderen auch Zahlenwerte und Zeichenketten miteinander vergleichen.

* Um die zu einem Dateinamen gehörende Datei auf eine bestimmte Eigenschaft hin
  zu überprüfen, lautet die ``test``-Syntax wie folgt:

  .. code-block:: bash

      test option dateiname

  Eine Auswahl an häufig verwendeten Prüfoptionen sind in der
  :ref:`Datei-Test-Tabelle <tab-file-tests>` aufgelistet; eine vollständige
  Liste aller Optionen findet in den ``test``-Manpages (``man test``).

.. list-table::
    :name: tab-file-tests
    :widths: 20 50

    * - ``-d``
      - wahr, wenn Datei existiert und ein Verzeichnis ist
    * - ``-e``
      - wahr, wenn Datei existiert
    * - ``-f``
      - wahr, wenn Datei existiert und regulär ist (kein Verzeichnis, kein Link)
    * - ``-h`` oder ``-L``
      - wahr, wenn Datei existiert und ein Symlink ist
    * - ``-r``
      - wahr, wenn Datei existiert und lesbar ist
    * - ``-s``
      - wahr, wenn Datei existiert und nicht leer ist
    * - ``-w``
      - wahr, wenn Datei existiert und schreibbar ist
    * - ``-x``
      - wahr, wenn Datei existiert und ausführbar ist


Anstelle von ``test option dateiname`` kann auch kürzer ``[ option dateiname ]``
geschrieben werden. In dieser Form kommen Test-Anweisungen sehr häufig bei
``if``-Bedingungen vor.

* Um ganzzahlige Werte miteinander zu vergleichen, können die Optionen
  ``-eq``, ``-ne``, ``-gt``, ``-lt``, ``-ge``, und ``-le`` verwendet werden.

  .. code-block:: bash

      test zahl1 operator zahl2

  Die möglichen Vergleichsoperatoren für Zahlen sind in der
  :ref:`Integer-Test-Tabelle <tab-integer-tests>` aufgelistet.

.. list-table::
    :name: tab-integer-tests
    :widths: 10 50

    * - ``-eq``
      - wahr, wenn beide Zahlen gleich sind ("equal")
    * - ``-ne``
      - wahr, wenn beide Zahlen nicht gleich sind ("not equal")
    * - ``-gt``
      - wahr, wenn erste Zahl größer als zweite Zahl ist ("greater than")
    * - ``-lt``
      - wahr, wenn erste Zahl kleiner als zweite Zahl ist ("less than")
    * - ``-ge``
      - wahr, wenn erste Zahl größer oder gleich der zweiten Zahl ist
        ("greater or equal")
    * - ``-le``
      - wahr,  wenn erste Zahl kleiner oder gleich der zweiten Zahl ist
        ("less or equal")

* Um eine einzelne Zeichenkette zu überprüfen, können die Optionen ``-z``
  ("zero") oder ``-n`` ("non-zero") verwendet werden. Mit ``test -z $mystring``
  wird beispielsweise getestet, ob die in der Variablen ``mystring`` gespeicherte
  Zeichenkette die Länge Null hat.

  Um zwei Zeichenketten miteinander zu vergleichen, können die Operatoren
  ``==`` zum Test auf Gleichheit und ``!=`` zum Test auf Ungleichheit verwendet
  werden. Beispielsweise kann mit ``if [ $mystring1 == $mystring2 ]`` eine
  Bedingung für die Gleichheit von ``mystring1`` und ``mystring2`` formuliert
  werden.

Möchte man mehrere Teilbedingungen zu einer einzigen Bedingung verknüpfen,
können die Optionen ``-a`` ("and") für eine UND-Bedingung und ``-o`` ("or") für
eine ODER-Bedingung eingesetzt werden. Wird einer (Teil-)Bedingung das
Negationszeichen ``!`` vorangestellt, so wird der Wahrheitswert des
Bedingungsterms umgekehrt.



.. index:: case
.. _Mehrfach-Unterscheidungen:

.. rubric:: Mehrfach-Unterscheidungen -- ``case``

Sollen Anweisungen in Abhängigkeit des konkreten Werts einer Variablen oder
einer Test-Bedingung ausgeführt werden, so kann das Schlüsselwort ``case``
genutzt werden. Dieses hat folgende Syntax:

.. code-block:: bash

    case variable in

        muster1) anweisung1 ;;

        muster2) anweisung2 ;;

        muster3) anweisung3 ;;

        *) sonstige-anweisungen ;;

    esac

Im obigen Beispiel kann anstelle ``variable`` auch ein Ausdruck stehen, der
eine Zeichenkette als Ergebnis liefert.

Trifft ein Muster auf den Wert der Variablen zu, so wird die dahinter angegebene
Anweisung ausgeführt. Die ``case``-Struktur wird unmittelbar anschließend
beendet; bei mehreren passenden Mustern werden somit nur die Anweisungen beim
ersten zutreffenden Muster ausgeführt.

Das Muster darf jedes :ref:`Suchmuster <Dateimuster und Variablen>` beinhalten,
das auch für Dateinamen erlaubt ist. Zwei oder mehrere einzelne Teilmuster
können dabei mittels ``|``-Zeichen zu einem Gesamt-Muster verbunden werden.

Das Suchmuster ``*`` trifft auf jeden beliebigen Wert zu. Es kann daher
verwendet werden, um Anweisungen festzulegen, die genau ausgeführt werden, wenn
kein anderer Fall zutrifft. Da nach dem ``*``-Muster die ``case``-Struktur mit
Sicherheit beendet wird, darf es erst am Ende der möglichen Fälle aufgelistet
werden. Anschließend wird die ``case``-Struktur mittels ``esac`` (ein
umgekehrtes ``case``) beendet.

.. _Schleifen:

.. rubric:: Schleifen -- ``for``, ``while`` und ``until``

In einer Shell stehen folgende Schleifentypen zur Verfügung:

.. index:: for

* Mittels einer ``for``-Schleife kann eine Liste von Variablen elementweise
  abgearbeitet werden. Häufig wird als Liste ein Dateimuster verwendet,
  beispielsweise würde ``for pic in *.png`` alle ``png``-Dateien des
  Verzeichnisses in eine Liste speichern und bei jedem Durchlauf der Schleife
  die jeweils nächste solche Datei in der Variablen ``pic`` ablegen. Sind alle
  Elemente der Liste abgearbeitet, wird die ``for``-Schleife automatisch
  beendet.

  Die Anweisungen, die innerhalb der Schleife abgearbeitet werden sollen, werden
  durch die Schlüsselwörter ``do`` und ``done`` begrenzt. Eine ``for``-Schleife
  hat damit insgesamt folgende Form:

  .. code-block:: bash

      for varname in var_list
      do
          echo "Doing something with $varname ..."
      done

  In Kurzform, insbesondere bei einer einzelnen Schleifenanweisung, kann eine
  ``for``-Schleife auch in eine Zeile geschrieben werden:

  .. code-block:: bash

      for varname in var_list ; do echo "Doing something with $varname ..." ; done

  Üblicherweise werden ``for``-Schleifen zum Durchlaufen einer vorgegebenen
  Anzahl an Listenelementen verwendet.

.. index:: while

* Mittels einer ``while``-Schleife kann eine beliebe Anzahl an Anweisungen,
  solange eine bestimmte Bedingung erfüllt ist, beliebig oft wiederholt werden:

  .. code-block:: bash

      while [ $count -le 10 ]
      do
          echo "Hallo"
          count=$( expr $count + 1 )
      done

  Die Bedingung wird vor jedem Schleifendurchlauf geprüft, und sofern diese nicht
  erfüllt ist, wird die Schleife beendet. Stellt sich die Bedingung schon vor dem
  ersten Schleifendurchlauf als Falsch heraus, wird die Schleife somit komplett
  übersprungen.

  Die ``expr``-Anweisung wertet dabei den gegebenen arithmetischen Ausdruck aus
  und gibt das Ergebnis als Rückgabewert zurück. Anstelle ``$(expr $count +1)``
  kann auch kürzer ``$(($count + 1))`` geschrieben werden. Für komplexere
  Berechnungen innerhalb eines Shell-Skripts sollte :ref:`bc <bc>` verwendet
  werden.


  Eine ``while``-Schleife kann beispielsweise verwendet werden, um alle dem Skript
  beim Aufruf übergebenen Parameter auszulesen:

  .. code-block:: bash

      while [ -n $1 ]
      do
          echo $1
          shift
      done

  Hierbei bewirkt die Funktion ``shift``, dass die Nummerierung der Parameter
  ``$1`` bis ``$9`` nach links verschoben wird, aus ``$3`` wird beispielsweise
  ``$2`` und aus ``$2`` wird ``$1``. Auf diese Weise können auch mehr als
  :math:`9` übergebene Parameter der Reihe nach abgearbeitet werden.

..  getopt Das Kommando getopt kann eingesetzt werden, um in einem Shellscript die
..  Kommandzeilenparameter auszuwerten.



.. index:: until

* Hat man eine Bedingung in der Form ``while not``, so kann dafür das
  Schlüsselwort ``until`` verwendet werden. Mit ``until`` wird ebenfalls eine
  Schleife eingeleitet, wobei die angegebene Bedingung -- wie bei einer
  ``while``-Schleife -- vor jedem Schleifendurchgang geprüft wird.

  .. code-block:: bash

      until [ $count -eq 10 ]
      do
          echo "Hallo"
          count=$(expr $count + 1)
      done

Mit ``while`` und ``until`` werden üblicherweise Endlos-Schleifen definiert,
die dann zu einem bestimmten Zeitpunkt mittels ``break`` abgebrochen werden.


.. index:: break, continue
.. _break und continue:

.. rubric:: break und continue

Um den gewöhnlichen Schleifenverlauf zu verändern, akzeptiert der
Shell-Interpreter zwei Schlüsselwörter: ``break`` und ``continue``:

* Mittels ``break`` wird die Schleife komplett abgebrochen.

  Beispielsweise kann somit eine Endlos-Schleife unterbrochen werden, wenn eine
  bestimmte Bedingung eintritt:

  .. code-block:: bash

      while true
      do
        echo "Doing something.."

        if given_condition
        then
            break

      done


* Mittels ``continue`` wird der aktuelle Schleifendurchlauf abgebrochen. Die
  Schleife wird dann mit dem nächsten Schleifendurchlauf fortgesetzt.

  Die ``continue``-Anweisung wird häufig in ``for``-Schleifen eingesetzt, wenn
  beispielsweise alle Dateien eines Verzeichnisses abgearbeitet werden und nur
  in Sonderfällen zur nächsten Datei gegangen werden soll.

Die Anweisung ``break`` kann bei Bedarf auch mit einer Zahl ``n`` aufgerufen
werden, um in einer verschachtelten Schleife nur die innersten :math:`n` Ebenen
der Schleife zu verlassen (beispielsweise bricht ``break 1`` nur die innerste
Schleifenebene ab). Ebenso kann die Anweisung ``continue`` mit einer Zahl ``n``
aufgerufen werden, um insgesamt :math:`n` Schleifendurchläufe zu überspringen.

Definition von Funktionen
-------------------------

In Shell-Skripten können, ähnlich wie in Programmiersprachen, Kombinationen
von mehreren Anweisungen als Funktionen definiert und somit beliebig oft an
verschiedenen Stellen eines Skripts aufgerufen werden.

Die grundlegende Syntax zur Definition eigener Funktionen ist folgende:

.. code-block:: bash

    funktionsname ()
        {
        anweisungen
        }

Funktionsdefinitionen können, ebenso wie Variablen, mit ``unset funktionsname``
gelöscht, jedoch nicht an Unterprozesse exportiert werden.

Mit ``return num`` kann eine Funktion an jeder beliebigen Stelle beendet werden;
dabei wird ``num`` als :ref:`Exit-Status <Rückgabewerte und Verkettung von
Programmen>` an die Shell zurück geliefert. Gibt es in einer Funktion keine
``return``-Anweisung, so entspricht der Exit-Status der letzten Anweisung dem
Rückgabewert der Funktion.

..  # put a function in the background
..  name &

..  Another way to add a progress bar to your script using dialog --gauge.

..  Damit das Script nicht im Hintergrund unnötig Ressourcen verbraucht,
..  wurde es mit kill $! beendet. Die Zeichenfolge ``$!`` ist eine Shell-Variable
..  einer Prozessnummer vom zuletzt gestarteten Hintergrundprozess (auch hierauf
..  wird noch eingegangen).

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die Dateinamen von Shell-Skripten sollten keine Zeichen außer Groß- und
    Kleinbuchstaben, Nummern und dem Unterstrich beinhalten; Umlaute und
    Sonderzeichen sollten, obwohl sie prinzipiell zulässig sind, vermieden
    werden.

.. [#] Auf die gleiche Weise kann man zu Beginn einer Skriptdatei auch einen
    anderen Interpreter festlegen. Beispielsweise leiten ``#!/bin/awk -f``
    ein AWK-Skript oder ``/usr/bin/python3`` ein Python3-Skript ein.

.. [#] Möchte man in eine Zeile zwei oder mehrere Anweisungen schreiben, so
    müssen diese durch ``;`` getrennt werden. (Andernfalls würde die zweite
    Anweisung als Argument der ersten Anweisung interpretiert werden.)

.. [#] Wird ein Shell-Skript nicht explizit mittels ``exit`` beendet, so
    entspricht der Exit-Status dem Rückgabewert der zuletzt ausgeführten
    Anweisung.

..  Bei einigen Programmen (beispielsweise bei ``grep``) werden unterschiedliche
..  Rückgabewerte für unterschiedliche Ereignisse benutzt.


