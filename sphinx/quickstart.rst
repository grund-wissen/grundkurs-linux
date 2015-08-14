Sphinx-Quickstart
=================

Um ein neues Sphinx-Projekt von Grund auf zu starten, gibt man in einem neuen
Ordner ``sphinx-quickstart`` ein. Nach einigen Abfragen, mit denen einige
Angaben zum Dokument gemacht und einige Optionen festgelegt werden, Hilfe die in
jedem Projekt vorhandene Konfigurationsdatei ``conf.py`` automatisch angelegt
bzw. angepasst werden kann:

::

    $ sphinx-quickstart

    Welcome to the Sphinx 1.1.3 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Enter the root path for documentation.
    > Root path for the documentation [.]:

Gewöhnlich mag man die Sphinx-Dokumentation in genau dem Ordner erstellen, von
dem aus man ``sphinx-quickstart`` aufgerufen hat. Es genügt somit die
Bestätigung der Vorgabe ``[.]`` (aktuelles Verzeichnis) mit der Enter-Taste.

In der nächsten Abfrage geht es darum, ob für die Quelldateien ein eigener
Ordner angelegt werden soll. Auch hier ist die Vorgabe ``[n]`` empfehlenswert,
es genügt somit eine Bestätigung mit der ``Enter``-Taste. Der Quelltext befindet
sich dann im aktuellen Verzeichnis bzw. in Unterverzeichnissen für
umfangreichere Kapitel. Der von Sphinx erzeugte HTML- bzw. LaTeX-Code wird in
separaten Unterverzeichnissen ``_build/html`` bzw. ``_build/latex`` abgelegt.
[#]_

::

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/N) [n]:

Die nächste Abfrage kann ebenfalls kurzerhand mit ``Enter``-Taste bestätigt
werden. Gemäß der Vorgabe werden dann Sphinx-Unterordner, die Erweiterungen oder
Templates beinhalten, mit einem beginnenden Underline-Zeichen gekennzeichnet.

::

    Inside the root directory, two more directories will be created; "_templates"
    for custom HTML templates and "_static" for custom stylesheets and other static
    files. You can enter another prefix (such as ".") to replace the underscore.
    > Name prefix for templates and static dir [_]:

Bei der nächsten Abfrage werden der Projekt- und der Autorname der Dokumentation
sowie eine (beliebig wählbare) Versions- und Releasenummer angegeben. Die
Release-Nummer kann üblicherweise gleich der Versionsnummer gewählt
werden. [#]_

::

    The project name will occur in several places in the built documentation.
    > Project name:
    > Author name(s):

    Sphinx has the notion of a "version" and a "release" for the
    software. Each version can have multiple releases. For example, for
    Python the version is something like 2.5 or 3.0, while the release is
    something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
    just set both to the same value.
    > Project version:
    > Project release:

Bei der nächsten Abfrage kann der Benutzer eine beliebige Datei-Endung für den
RestructuredText-Quellcode festlegen. Auch hier ist es empfehlenswert die
Vorgabe ``[rst]`` mit der ``Enter``-Taste zu bestätigen, da man gewöhnlich
Texteditoren wie :ref:`Vim <Vim-Tool>` zum Bearbeiten der Textdateien nutzt, die
anhand der Datei-Endung beispielsweise ein entsprechendes Syntax-Highlighting
aktivieren.

::

    The file name suffix for source files. Commonly, this is either ".txt"
    or ".rst".  Only files with this suffix are considered documents.
    > Source file suffix [.rst]:

Bei der nächsten Abfrage geht es darum, ob eine Hauptdatei ``index.rst`` im
Basispfad der Dokumentation angelegt werden soll. Auch hier ist eine Bestätigung
der Vorgabe der ``Enter``-Taste sinnvoll. In der Datei ``index.rst`` befindet
sich üblicherweise ein Inhaltsverzeichnis ("toctree"), der auf weitere
Quelltext-Dateien verlinkt.

::

    One document is special in that it is considered the top node of the
    "contents tree", that is, it is the root of the hierarchical structure
    of the documents. Normally, this is "index", but if your "index"
    document is a custom template, you can also set this to another filename.
    > Name of your master document (without suffix) [index]:

Bei der nächsten Abfrage wird festgelegt, ob ein Epub-Builder gewünscht ist
oder nicht. Gewöhnlich kann hier die Vorgabe ``[n]`` mit der ``Enter``-Taste
bestätigt werden.

::

    Sphinx can also add configuration for epub output:
    > Do you want to use the epub builder (y/N) [n]: n

Mit der Abfrage, welche Erweiterungen genutzt werden sollen, ist man (fast) am
Ende angekommen. Je nach Art des Dokumentationsprojekts kann die Wahl
beispielsweise folgendermaßen ausfallen (sie kann jederzeit in der
Konfigurationsdatei ``conf.py`` angepasst werden):

::

    Please indicate if you want to use one of the following Sphinx extensions:
    > autodoc:
        automatically insert docstrings from modules (y/N) [n]: y
    > doctest:
        automatically test code snippets in doctest blocks (y/N) [n]: n
    > intersphinx:
        link between Sphinx documentation of different projects (y/N) [n]: y
    > todo:
        write "todo" entries that can be shown or hidden on build (y/N) [n]: y
    > coverage:
        checks for documentation coverage (y/N) [n]: n
    > pngmath:
        include math, rendered as PNG images (y/N) [n]: y
    > mathjax:
        include math, rendered in the browser by MathJax (y/N) [n]: n
    > ifconfig:
        conditional inclusion of content based on config values (y/N) [n]: n
    > viewcode:
        include links to the source code of documented Python objects (y/N) [n]: y

Zu guter Letzt wird abgefragt, ob eine :ref:`Makefile <Makefiles>` (für
Linux-Systeme) und/oder eine ``Commandfile`` (für Windows-Systeme) angelegt
werden soll:

::

    A Makefile and a Windows command file can be generated for you so that you
    only have to run e.g. `make html' instead of invoking sphinx-build
    directly.
    > Create Makefile? (Y/n) [y]: y
    > Create Windows command file? (Y/n) [y]: n

Damit ist das Projekt fertig angelegt und kann beliebig angepasst und mit
Inhalten gefüllt werden. Aus dem Quellcode der Dokumentation können jederzeit,
sofern man sich in einem Shellfenster im Hauptverzeichnis des Projekts befindet,
mit ``make html`` HTML-Dateien und mittels ``make latexpdf`` LaTeX-Code sowie
eine gleichnamige PDF-Datei erzeugt werden (die fertigen Dateien befinden sich
dann im ``_build``-Verzeichnis).

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#]  Ein Vorteil dieser Methode liegt beispielsweise darin, dass komplexere
    Unterverzeichnisse selbst mit einer ``Makefile``- und ``conf.py``-Datei
    ausgestattet und eigenständig nach HTML bzw. LaTeX übersetzt werden können.

.. [#] Die Angaben können zu jedem späteren Zeitpunkt in der
    Konfigurationsdatei ``conf.py`` geändert werden.

    Durch die Vergabe von Versionsnummern kann beispielsweise bei der
    Dokumentation von Software-Quellcode sichergestellt werden, dass eine
    Anleitung auch zur jeweiligen Software-Version passt. Auch bei allgemeinen
    Dokumentationsprojekten ist eine Versionsnummer sinnvoll, um den jeweiligen
    Entwicklungsstand aufzuzeigen; mit einem Versions-Upgrade können außerdem
    eine Rundmail über einen Verteiler, ein neuer Commit eines
    Versionsverwaltungs-Programms, ein Weblog-Eintrag o.ä. verbunden werden.


