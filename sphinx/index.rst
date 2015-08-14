.. index:: Sphinx
.. _Sphinx:

Das Dokumentations-System Sphinx
================================

Sphinx ist ein in Python geschriebenes Shell-Programm, das aus einer bzw.
mehreren Textdateien mit RestructuredText-Syntax auf dem lokalen Rechner
wahlweise eine PDF-Datei oder eine bzw. mehrere HTML-Dateien erzeugen kann. [#]_

Da die Syntax von RestructuredText leicht erlernbar ist, erspart man sich dank
Sphinx (mindestens) die Hälfte an Arbeit, die gewöhnlich nötig ist, wenn man
Dokumente sowohl als Textform (beispielsweise zum einfachen Versenden via Email)
vorliegen haben als auch im Internet und/oder in druckbarer Form publizieren
möchte.

Da es sich bei den Quelldateien um reine Textdateien mit der Endung ``.rst``
handelt, können diese auch sehr leicht nach Inhalten durchsucht werden.
Persönlich habe ich mir dazu folgende Abkürzung in der Konfigurationsdatei
``~/.bashrc`` definiert:

.. code-block:: bash

    alias rstgrep='find ./ -name "*.rst" | xargs grep'

In einer Shell kann damit mittels ``rstgrep Suchbegriff`` nach einem Begriff
oder einem regulären Ausdruck in allen ``rst``-Dateien eines Projekts (inklusive
aller Unterverzeichnisse) gesucht werden. Dabei können selbstverständlich auch
die üblichen Optionen von :ref:`grep <grep>` genutzt werden.


.. _Installation von Sphinx:

.. rubric:: Installation von Sphinx

.. code-block:: bash

    sudo aptitude install python3-setuptools python3-numpy python3-matplotlib dvipng

    sudo easy_install3 Sphinx

Mit ``sudo easy_install3 -U Sphinx`` (Update) kann Sphinx jederzeit auf den
aktuellsten Stand gebracht werden.

Zur Erzeugung von PDF-Druckversionen genügt bereits ein minimales LaTeX-System,
wie es nach Installation der oben genannten Pakete automatisch vorhanden ist. Um
beispielsweise in naturwissenschaftlichen Publikationen einen umfangreichen
mathematischen Formelsatz nutzen zu können, sollte bei Bedarf ein :ref:`volles
LaTeX-System <gwil:LaTeX>` installiert werden.


.. toctree::
    :maxdepth: 2

    quickstart.rst
    rst-tutorial.rst
    anpassungen.rst
    tinkerer.rst
    links.rst

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#]  Um die erzeugten HTML-Dateien im Internet zu publizieren, müssen sie
    lediglich in einen gemeinsamen Ordner auf einem Webserver kopiert werden.
    Weist man diesem Ordner anschließend über einen Domain-Anbieter eine feste
    Webadresse (URL) zu, so ist die Seite bereits fertig!

..  `Filezilla <http://wiki.ubuntuusers.de/FileZilla>`_ oder Midnight Commander

