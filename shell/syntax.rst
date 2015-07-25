.. _Shell-Syntax:

Syntax
======

Die Shell ist ein vielfältiger Interpreter, um (beliebige) Programme zu starten
und deren Rückgabewerte anzuzeigen bzw. weiter zu verarbeiten.

In vielen Fällen müssen einem Programm weitere Informationen übergeben werden,
damit es seine Aufgabe in gewünschter Weise erfüllen kann. Es gibt dabei zwei
Arten von Informationen, die man Programmen mitteilen kann: Optionen und
Argumente. Dabei werden die Optionen immer vor den Argumenten angegeben, so dass
die grundlegende Syntax aller Linux-Kommandos folgende Form hat:

..  Benutzer: user@linux$ 

.. code-block:: bash

    programm [-Optionen] [Argumente]

Die eckigen Klammern sollen andeuten, dass Optionen und Argumente nicht bei
jedem Programmaufruf notwendig sind. Ihre Angabe hängt vom Zweck des
Programmaufrufs und den möglichen Parametern eines Programms ab. 

.. rubric:: Optionen

Optionen können das Verhalten eines Kommandos beeinflussen. Jede Option wird
gewöhnlich durch einen einzelnen Buchstaben bezeichnet und beginnt mit einem
vorangestellten Minus (``-``). 

*Beispiel:*
    
* Das Kommando ``ls`` zeigt den Inhalt eines Verzeichnisses an, indem es die
  Namen der enthaltenen Unterverzeichnisse und Dateien auflistet. Will man
  allerdings nicht einfach nur die Namen der Dateien wissen, sondern auch
  Zusatzinformationen über Dateigröße, Erstellungsdatum oder ähnliches
  mitgeteilt bekommen, so muss der Aufruf von ``ls`` um entsprechende Optionen
  ergänzt werden: 

  .. code-block:: bash

      user@linux $ ls -l

  Die Option ``-l`` ("long") bewirkt eine ausführlichere Ausgabe, das Verhalten
  des Programms hat sich durch die Verwendung der Option verändert. 
  
Optionen können miteinander kombiniert werden, indem man weitere Zeichen einfach
hinzufügt; beispielsweise gibt ``ls -lh`` die Dateiliste in ausführlicher Form
*und* mit angenehm lesbaren Dateigrößen an. [#]_ Das Minuszeichen muss also nur
ein einziges Mal verwendet werden, um damit anzuzeigen, dass nun eine Reihe von
Optionen folgt.

Unter Linux gibt es darüber hinaus auch Optionen, die mit einem doppelten
Minuszeichen beginnen und einen langen Optionsnamen aufweisen. Solche Optionen
sind einerseits leichter lesbar als kurze, erfordern andererseits (gerade bei
häufigen Aufrufen) auch mehr Schreibarbeit. Ein Beispiel für eine weit
verbreitete lange Option ist ``--version``; viele Programme geben bei einem
Aufruf mit dieser Option die jeweilige Versionsnummer aus. 

Eine Übersicht möglicher Optionen eines Befehls gibt die  Manpage des jeweiligen
Programms (``man programm``).

.. rubric:: Argumente

Argumente dienen nicht zur Steuerung eines Kommandos, sondern liefern diesem
Informationen, die es zu bearbeiten hat. Viele Kommandos zur Manipulation von
Dateien benötigen zum Beispiel die Namen der Dateien, die sie manipulieren
sollen. Hier wird also nicht das Verhalten des Programmes geändert, sondern die
Information variiert, die dem Programm für seine Arbeit zur Verfügung steht. Im
Gegensatz zu Optionen kann es häufig eine sehr große Zahl verschiedener
Argumente geben. Optionen hingegen sind immer nur in relativ beschränkter Zahl
verfügbar -- immer gerade so viele, wie der Programmierer in sein Programm
implementiert hat. 

..  Nebenbei bemerkt ist jedoch auch die Anzahl der Argumente einer Kommandozeile
..  nicht unbeschränkt, denn die Argumentzeile eines Kommandos darf eine Größe von
..  128 Kilobyte nicht überschreiten.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Siehe :ref:`ls <ls>` für eine ausführlichere Beschreibung des
    Auflistungs-Programms.


