.. index:: Texteditor, Vim
.. _Der Texteditor Vim:
.. _Texteditor Vim:

Der Texteditor Vim
==================

`Vim <http://www.vim.org>`_ ist einer der vielseitigsten Text-Editoren aller
Zeiten. Man kann damit auf sehr effiziente Weise nicht nur Programme schreiben,
sondern auch Webseiten, Bücher, Briefe, Emails, kurz: Textdateien aller Art
bearbeiten.

Durch Tastenkombinationen (insbesondere durch :ref:`Snippets <Snippets>`) kann
die die zum Schreiben von Texten nötige Tipparbeit ist erheblich reduziert
werden; nach einer gewissen Einarbeitungszeit wird das Arbeitstempo so spürbar
erhöht. Bei häufiger Benutzung laufen einzelne Editierungsschritte mitunter so
schnell und "automatisch" ab, dass man nur noch unterbewusst darüber nachdenkt
und die Konzentration der eigentlichen Arbeit widmen kann.. ;-)

.. _Vim-Installation:

.. rubric:: Installation

Auf fast allen Linux-System ist ``vi``, der "kleine Bruder" von Vim, bereits in
der Grundversion enthalten. Für eine komfortablere Bedienung ist es allerdings
empfehlenswert, eine umfangreichere Version des Vim zu installieren: [#]_


.. code-block:: bash

    sudo aptitude install vim-common vim-gnome vim-scripts ncurses-term

Mit den obigen Paketen wird die Basis-Version von Vim installiert, die in einer
Shell mittels ``vim`` gestartet werden kann. Zudem wird eine graphische
Bedienoberfläche namens ``gvim`` installiert, die als eigenständiges Programm
ohne Shell-Fenster aufgerufen werden kann.

.. rubric:: Vim-Schnellstart

Bei der im letzten Abschnitt beschriebenen Installation wird automatisch das
Vim-Lern-Programm ``vimtutor`` mit installiert, das in einer Shell gestartet
werden kann:

.. code-block:: bash

    vimtutor

Hierbei wird Vim in einer Basis-Version gestartet und eine Tutorial-Datei
aufgerufen, in der interaktiv in mehreren Lektionen die wichtigsten Vim-Tasten
erlernt werden können. Für das Durchlaufen dieses Tutorials sollte man etwa 30
Minuten einplanen.

.. only:: html

    Die folgende Vim-Anleitung umfasst folgende Themen:

.. toctree::
    :maxdepth: 2

    bedienung.rst
    konfiguration.rst
    plugins.rst
    links.rst

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Vim läuft auch unter Windows- und Apple-Systemen. Hierfür finden sich auf
    der `Vim-Projektseite <http://www.vim.org>`_ unter der Rubrik "Downloads"
    entsprechende Pakete bzw. selbst entpackende Installationsdateien.


