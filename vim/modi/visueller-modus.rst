.. _Visueller Modus:

Visueller Modus
---------------

Im visuellen Modus kann Text mittels :ref:`Bewegungsbefehlen <Bewegungsbefehle>`
markiert werden, um ihn zu kopieren oder zu bearbeiten. 

Aus dem Normal-Modus gelangt man wie folgt in den visuellen Modus:

.. list-table:: 
    :widths: 10 30 20
    :header-rows: 0

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

Im zeilenweise-visuellen Modus können mit den Navigationsbefehlen ``{`` und
``}`` oder mit Hilfe von Markierungen leicht ganze Paragraphen oder
Textabschnitte kopiert, verschoben oder anderweitig bearbeitet werden. Der
blockweise-visuelle Modus bietet speziell mit dem Vim-Plugin Align eine elegante
Möglichkeit zur Bearbeitung von Spalten einer Tabelle.

**Tip**: Jeder Bearbeitungsbefehl, der für gewöhnlich ein darauffolgendes
Bewegungs- oder Auswahlkommando erwartet, kann auch direkt einen markierten
Bereich angewandt werden.

