Grundwissen Linux
=================

In dieser Dokumentation aus der `Grund-Wissen <http://www.grund-wissen.de>`_
-Reihe geht es um Linux, Open Source, Shell-Anweisungen, Shell-Scripting, den
Text-Editor Vim, und weitere damit zusammen hängende Themen.

Das Projekt verwendet `Sphinx <http://sphinx-doc.org/>`_ als Programm zum
Erstellen der HTML- bzw. PDF-Dokumente. Die Dokumentation wird kontinuierlich
ausgebaut, Unterstützung bei der Weiterentwicklung ist gerne willkommen.

Eine HTML-Version dieser Seite ist unter folgender Adresse abrufbar: 

http://www.grund-wissen.de/linux


Lokale Kopien und Mitarbeit
---------------------------

Um lokale Kopien der Dokumentation zu erstellen, müssen einige Pakete
installiert sein. Unter Debian, Ubuntu oder Linux Mint können diese
folgendermaßen installiert werden:

.. code-block:: bash

    aptitude install python3-setuptools
	easy_install3 -U Sphinx
	
Anschließend kann das Repository mittels `git clone
https://github.com//grund-wissen/grundwissen-linux.git` heruntergeladen werden.
Im Projektverzeichnis können aus den Quelldateien dann folgendermaßen wahlweise
HTML-Seiten oder ein PDF-Dokument erstellt werden:

.. code-block:: bash

    make html

    # oder:

	make latexpdf

Die fertigen Dokumente befinden sich dann im Verzeichnis ``_build/html``
beziehungsweise ``_build/latex``.

Sollen lokale Änderungen in das Projekt übernommen werden, so bittet der
Maintainer um einen Pull-Request. 


Herzlichen Dank an alle Mitwirkenden!



