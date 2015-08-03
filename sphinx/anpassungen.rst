.. _Gestalterische Anpassungen:

Gestalterische Anpassungen
==========================

Für die Grundwissen-Webseite nutze ich das Sphinx-Standard-Theme mit einigen
Anpassungen. Diese habe ich als Super-User direkt am zentralen Installationspfad
``/usr/local/lib/python2.7/dist-packages/Sphinx-1.2b1-py2.7.egg/sphinx/``
vorgenommen, so dass sie global für alle Dokumentations-Projekte gleichermaßen
gelten.

.. Mit der Basis-Installation und den folgenden Anpassungen kann die
.. Grund-Wissen-Homepage aus dem `Quelltext-Archiv <../../grund-wissen.zip>`_ und
.. dem `Graphik-Archiv <../grund-wissen-bilder.zip>`_ durch den Aufruf ``make
.. html`` bzw. ``make latexpdf`` nachgebaut werden. [#]_


.. _Suchfeld-Kommentar löschen:

.. rubric:: Suchfeld-Kommentar löschen

Da sich die Dokumentation nicht auf Software-Quellcode bezieht, mag ich
unter dem Suchfeld in der Seitenleiste ("sidebar") keinen Hinweis abgedruckt
haben, dass man einen Modul-, Klassen- oder Funktionsnamen eingeben könne.
Entsprechend habe ich die entsprechende Zeile in der Datei
``themes/basic/searchbox.html`` auskommentiert:

.. code-block:: html

    VORHER:

    <p class="searchtip" style="font-size: 90%">
    {{ _('Enter search terms or a module, class or function name.') }}
    </p>

    NACHHER:

    <!--<p class="searchtip" style="font-size: 90%">-->
    <!--{{ _('Enter search terms or a module, class or function name.') }}-->
    <!--</p>-->


.. _Kontakt-Link auf jeder HTML-Seite hinzufügen:

.. rubric:: Kontakt-Link auf jeder HTML-Seite hinzufügen

In der Fußnotenzeile sollte ein Link auf Kontakt/Impressum eingefügt werden. Das
geschieht in ``themes/basic/layout.html``:

.. code-block:: html

    VORHER:

    {%- if last_updated %}
      {% trans last_updated=last_updated|e %}Last updated on {{ last_updated }}.
      {% endtrans %}
    {%- endif %}

    NACHHER:

    {%- if last_updated %}
      {% trans last_updated=last_updated|e %}
      Zuletzt aktualisiert am {{ last_updated }}.
      <a href='http://grund-wissen.de/impressum.html'>Kontakt/Impressum</a>
      {% endtrans %}
    {%- endif %}


.. rubric:: Kopfzeile der Druckversion entfernen

Normalerweise erscheint in der erzeugten PDF-Datei in der Kopfzeile jeder
Seite ein Versionshinweis. Um dies zu deaktivieren, muss die Datei
``texinputs/sphinx.sty`` an zwei Stellen abgeändert werden. Zum einen muss
die ``\fancyhead``-Zeile, die den Versions-Eintrag erzeugt, mit einem
``%``-Zeichen auskommentiert werden. Zum anderen kann der Strich zwischen
Kopfzeile und erster Textzeile entfernt werden, indem ihr Wert auf ``0.0``
gesetzt wird: 

.. code-block:: tex

    VORHER:

    \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \py@release}}

    ...

    \renewcommand{\headrulewidth}{0.4pt}


    NACHHER:

    % \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \py@release}}

    ...

    \renewcommand{\headrulewidth}{0.0pt}


.. rubric:: Tabellen zentrieren

Normalerweise werden Tabellen im Latex-Output linksbündig dargestellt.
Persönlich sind mir zentrierte Tabellen lieber. Daher habe ich die
(umfangreiche) Datei ``writers/latex.py``, speziell die Funktion
``depart_table(self, node)``, etwas abgeändert:

.. code-block:: python
    
    VORHER:

    if not self.table.longtable and self.table.caption is not None:
        self.body.append(u'\n\\begin{threeparttable}\n'
                         u'\\capstart\\caption{%s}\n' % self.table.caption)
    elif self.table.has_verbatim:
        self.body.append('\n\\begin{tabular}')
        endmacro = '\\end{tabular}\n'
    elif self.table.has_problematic and not self.table.colspec:
        # if the user has given us tabularcolumns, accept them and use
        # tabulary nevertheless
        self.body.append('\n\\begin{tabular}')
        endmacro = '\\end{tabular}\n'
    else:
        self.body.append('\n\\begin{tabulary}{\\linewidth}')
        endmacro = '\\end{tabulary}\n'

    [...]

    if not self.table.longtable and self.table.caption is not None:
        self.body.append('\\end{threeparttable}\n')


    NACHHER:

    if not self.table.longtable and self.table.caption is not None:
        self.body.append(u'\n\n\\begin{table}\\centering\n'
                         u'\\capstart\\caption{%s}\n' % self.table.caption)
    if self.table.longtable:
        self.body.append('\n\\begin{longtable}')
        endmacro = '\\end{longtable}\n\n'
    elif self.table.has_verbatim:
        self.body.append('\n\\begin{center}\\begin{tabular}')
        endmacro = '\\end{tabular}\\end{center}\n\n'
    elif self.table.has_problematic and not self.table.colspec:
        self.body.append('\n\\begin{center}\\begin{tabular}')
        endmacro = '\\end{tabular}\\end{center}\n\n'
    else:
        self.body.append('\n\\begin{center}\\begin{tabulary}{\\linewidth}')
        endmacro = '\\end{tabulary}\\end{center}\n\n'

    [...]

    if not self.table.longtable and self.table.caption is not None:
        self.body.append('\\end{table}\n\n')


..  
    *   Zusätzlich nach folgendem suchen:
    
    .. code-block:: python
    
        if not self.table.longtable and self.table.caption is not None:
        self.body.append(u'\n\n\\begin{threeparttable}\\centering\n'
    
    und durch folgendes ersetzen:
    
    .. code-block:: python
    
        if not self.table.longtable and self.table.caption is not None:
            self.body.append(u'\n\n\\begin{table}\\centering\n'
                 u'\\caption{%s}\n' % self.table.caption)
    
    und entsprechend (einfach nach threeparttable suchen)
    
    .. code-block:: python
    
        if not self.table.longtable and self.table.caption is not None:
            self.body.append('\\end{table}\n\n')


Auch in der HTML-Ausgabe möchte ich Tabellen gerne zentriert haben;
gleichzeitig sollen die Fußnoten, die von Sphinx ebenfalls in Tabellen-Form
dargestellt werden, linksbündig bleiben. Um dies zu erreichen, habe ich in
der Datei ``themes/basis/static/basic.css_t`` den Eintrag ``table.docutils`` 
folgendermaßen ergänzt:

.. code-block:: css

    table.docutils {
        border: 1px solid gray;
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto;
    }

    table.docutils.footnote, table.docutils.citation {
        border: 0px;
        border-collapse: collapse;
        margin-left: 0;
    }

    table.docutils.footnote td, table.docutils.citation td {
        border: 0px;
    }


.. layout.html: 

..  {% trans last_updated=last_updated|e %}Zuletzt aktualisiert am {{ last_updated }}.
..  <a href='http://grund-wissen.de/impressum.html'>Kontakt/Impressum</a>


.. rubric:: Zeilenumbruch bei langen Navigationszeilen ermöglichen

In der obersten Zeile einer jeden mit Sphinx erstellten HTML-Seite wird eine
Navigations-Leiste angezeigt. Bei einer umfangreichen Dokumentation mit vielen
Unterabschnitten kann es vorkommen, dass auf kleinen Bildschirmen hierbei ein
Zeilenumbruch nötig ist -- der letzte Listeneintrag wird also in eine neue
Zeile geschrieben. In der Grundversion wird hierbei die Seitenüberschrift
verschoben. Um dies zu vermeiden, muss folgender Eintrag in der Datei
``themes/basis/static/basic.css_t`` ergänzt werden:

.. code-block:: css

    VORHER:
    
    div.related ul {
        margin: 0;
        padding: 0 0 0 10px;
        list-style: none;
        }


    NACHHER:
    
    div.related ul {
        margin: 0;
        padding: 0 0 0 10px;
        list-style: none;
        min-height: 2em;
        height: auto;
        overflow: hidden;
        }

Durch den Eintrag ``height: auto`` wird die Höhe der Navigations-Leiste
automatisch angepasst. Der Eintrag ``overflow: hidden;`` fügt anschließend bei
Bedarf automatisch eine (wieder ganz von links beginnende) neue Zeile ein.


.. rubric:: Mehrspaltige Aufzählungen (hlist) in LaTeX

Mit der ``hlist``-Umgebung kann man mit Sphinx mehrspaltige Tabellen erstellen.
Der Code dafür sieht etwa so aus:

.. code-block:: rst

    .. hlist::
        :columns: 2

        * Item 1
        * Item 2
        * ...

Während die HTML-Ausgabe ausgezeichnet funktioniert, werden ``hlist``-Umgebungen
vom LaTeX-Übersetzer wie "normale" Listen behandelt. Persönlich verwende ich
in den allermeisten Fällen zweispaltige ``hlists``, so dass ich mir in der Datei
``writers/latex.py`` mit folgendem Trick Abhilfe für den erstellten LaTeX-Code
geschaffen habe:

.. code-block:: python

    VORHER:

    \usepackage{sphinx}

    [...]

    def visit_hlist(self, node):
        self.compact_list += 1
        self.body.append('\\begin{itemize}\\setlength{\\itemsep}{0pt}'
                         '\\setlength{\\parskip}{0pt}\n')
    
    [...]

    def depart_hlist(self, node):
        self.compact_list -= 1
        self.body.append('\\end{itemize}\n')


    NACHHER:

    \usepackage{sphinx}
    \usepackage{multicol}

    def visit_hlist(self, node):
        self.compact_list += 1
        self.body.append('\\begin{multicols}{2}')
        self.body.append('\\begin{itemize}\\setlength{\\itemsep}{0pt}'
                         '\\setlength{\\parskip}{0pt}\n')

    [...]

    def depart_hlist(self, node):
        self.compact_list -= 1
        self.body.append('\\end{itemize}\n')
        self.body.append('\\end{multicols}')
    
Damit werden alle ``hlists`` in der Druckversion als zweispaltige Aufzählungen
dargestellt. [#Muc]_



.. rubric:: Darstellung von Subparagraphen und Rubriken anpassen

Bei umfangreichen Dokumentationen mit vielen ineinander geschachtelten
Abschnitten können auch Sub-Paragraphen als Überschriften vorkommen. [#]_ Damit
diese -- wie andere Überschriften auch -- in Latex ebenfalls in blauer
Schriftfarbe gedruckt werden, ist die Datei ``texinputs/sphinx.sty`` hinter um
folgenden Eintrag zu ergänzen:

  
.. code-block:: tex

    VORHER:

    \titleformat{\section}{\Large\py@HeaderFamily}%
        {\py@TitleColor\thesection}{0.5em}{\py@TitleColor}{\py@NormalColor}
    \titleformat{\subsection}{\large\py@HeaderFamily}%
        {\py@TitleColor\thesubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
    \titleformat{\subsubsection}{\py@HeaderFamily}%
        {\py@TitleColor\thesubsubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
    \titleformat{\paragraph}{\small\py@HeaderFamily}%
        {\py@TitleColor}{0em}{\py@TitleColor}{\py@NormalColor}


    NACHHER:

    \titleformat{\section}{\Large\py@HeaderFamily}%
        {\py@TitleColor\thesection}{0.5em}{\py@TitleColor}{\py@NormalColor}
    \titleformat{\subsection}{\large\py@HeaderFamily}%
        {\py@TitleColor\thesubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
    \titleformat{\subsubsection}{\py@HeaderFamily}%
        {\py@TitleColor\thesubsubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
    \titleformat{\paragraph}{\small\py@HeaderFamily}%
        {\py@TitleColor}{0em}{\py@TitleColor}{\py@NormalColor}
    \titleformat{\subparagraph}{\small\py@HeaderFamily}%
        {\py@TitleColor}{0em}{\py@TitleColor}{\py@NormalColor}


.. rubric:: Darstellung von Verbatim-Boxen anpassen

Um Code-Beispiele in LaTeX besser hervorzuheben, habe ich in der Datei
``texinputs/sphinx.sty`` die Farben für die Verbatim-Umgebung und ihre
Umrandung etwas angepasst:

.. code-block:: tex

    VORHER:

    \definecolor{VerbatimColor}{rgb}{1,1,1}
    \definecolor{VerbatimBorderColor}{rgb}{1,1,1}

    NACHHER:

    \definecolor{VerbatimColor}{rgb}{0.97,0.97,1}
    \definecolor{VerbatimBorderColor}{rgb}{0.75,0.75,1}

Die Boxen werden so in einem schwachen Blau mit einem ebenfalls leicht blauen
Rahmen gedruckt.


.. rubric:: Titelseite gestalten

Nach persönlichem Geschmack habe ich die Titelseite etwas abgewandelt --
insbesondere wollte ich dort einen Link auf die URL der Homepage einfügen.
Hierbei habe ich die Datei ``texinputs/sphinxmanual.cls`` etwas angepasst:

.. code-block:: tex

    VORHER:

    \begin{flushright}
        \sphinxlogo
        {\rm\Huge\py@HeaderFamily \@title \par}
        {\em\LARGE\py@HeaderFamily \py@release\releaseinfo \par}
        \vfill
        {\LARGE\py@HeaderFamily
            \begin{tabular}[t]{c}
            \@author
            \end{tabular}
        \par
        }
        \vfill\vfill
        {\large
            \@date \par
            \vfill
            \py@authoraddress 
            \par
        }
    \end{flushright}
    \par

    NACHHER:

    \begin{flushright}
        \sphinxlogo
        {\rm\Huge\py@HeaderFamily \@title \par}
        \vfill
        {\em\large\py@HeaderFamily \py@release\releaseinfo \par}
        {\em\py@HeaderFamily Aktualisiert am \@date \par}
        \vfill
        {\rm\Large\py@HeaderFamily
            \begin{tabular}[t]{c}
                \@author
            \end{tabular}
        \par
        }
        \vfill\vfill
        {\Large
            \url{http://www.grund-wissen.de}
        }
    \end{flushright}
    \par

Zusätzlich habe ich in der Datei ``writers/latex.py`` beide Vorkommnisse der
Bezeichnung "Release" durch "Version" ersetzt.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:
    
.. .. [#]  Der Graphik-Pfad muss gegebenenfalls noch so angepasst werden, dass das
        .. .. Hauptverzeichnis der Bilder als ``pics``-Ordner im Hauptpfad der
        .. .. Dokumentation abgelegt ist. 

.. [#Muc] Hierbei muss das LaTeX-Paket ``multicol`` installiert sein. Sollte dies
        nicht der Fall sein, kann es von der `CTAN-Projektseite
        <http://www.ctan.org/tex-archive/macros/latex/required/tools>`_ herunter
        geladen werden und gemäß dem üblichen :ref:`Installations-Schema
        <CTAN-Zusatzpakete installieren>` nachinstalliert werden.

.. [#]  Das gilt insbesondere auch für mit ``.. rubric:: Titel`` erzeugte
        Rubriken. Diese werden ohne die obigen Anpassungen in schwarzer Farbe
        und größer als die Paragraphen-Überschriften dargestellt.

