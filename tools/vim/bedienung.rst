Bedienung
=========

Traditionell -- den Vorgänger `Vi <http://de.wikipedia.org/wiki/Vi>`_ gibt es
schon seit 35 Jahren! -- kann Vim komplett über die Tastatur gesteuert
werden.

Damit es bei einer begrenzten Anzahl an Tasten möglich ist schnell durch Dateien
zu navigieren, Text einzugeben sowie Editierbefehle auszuführen, wurden
verschiedene Ebenen ("Modi") eingeführt. Je nach aktivem Modus haben die Tasten
verschiedene Bedeutungen.

* Beim Start von Vim befindet man sich im Normalmodus. 
* In einen anderen Modus gelangt man durch Drücken einer entsprechenden Taste. 
* Durch Drücken von ``ESC`` gelangt man in den Normalmodus zurück.

Um Vim zu beenden, kann man im Normalmodus ``ZQ`` (schließen, Änderungen
verwerfen) bzw. ``ZZ`` (schließen, Änderungen speichern) eingeben. 

.. toctree::
    :maxdepth: 2

    modi/einfuege-modus.rst
    modi/normal-modus.rst
    modi/kommandozeilen-modus.rst
    modi/visueller-modus.rst


